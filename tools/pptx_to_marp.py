#!/usr/bin/env python3
"""Convert a finished PowerPoint talk into a Marp web deck that looks exactly like the original.

Conference decks are designed slide by slide (custom shapes, charts, photos), so instead of
re-authoring them in Markdown this tool renders every presented slide to a full-slide image and
writes a Marp deck that shows those images, one per slide, with the PowerPoint speaker notes kept
as presenter notes.

    python3 tools/pptx_to_marp.py "path/to/deck.pptx" --inspect
    python3 tools/pptx_to_marp.py "path/to/deck.pptx" presentations/<slug> \
        --title "Talk title" --event "Meeting, place, date" \
        [--builds 13] [--width 2400]

What it does
  * Drops hidden slides (the web deck shows what you present).
  * --builds N [N ...]: slide numbers (1-based, as in PowerPoint) whose click animations reveal
    groups of shapes. Each such slide becomes several web slides: the base state, then one slide per
    click, showing only that click's shapes. Shapes targeted by the slide's animations are the
    "build" shapes; everything else is the base.
  * Renders with LibreOffice (headless) and PyMuPDF, writes JPEGs to <out>/images/.
  * Writes <out>/index.md (the Marp source). The site build turns it into <out>/index.html.
  * Speaker notes come ONLY from <out>/notes.json (reviewed, public). The raw PowerPoint notes are
    written to <out>/notes.source.json (git-ignored) for drafting it. No notes.json = no notes.
  * Sets `size: 4:3` or `size: 16:9` from the PowerPoint slide size.

Requires: python-pptx, pymupdf, Pillow, lxml, LibreOffice (soffice on PATH or /opt/homebrew/bin).
"""
import argparse
import copy
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pymupdf
from lxml import etree
from PIL import Image
from pptx import Presentation

NS = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main"}
SOFFICE = shutil.which("soffice") or "/opt/homebrew/bin/soffice"


def build_groups(slide):
    """Return a list of click groups, each a list of shape ids revealed on that click."""
    timing = slide._element.find("p:timing", NS)
    if timing is None:
        return []
    main = timing.find('.//p:cTn[@nodeType="mainSeq"]', NS)
    if main is None:
        return []
    groups = []
    for click in main.find("p:childTnLst", NS):
        ids = []
        # only entrance effects define what a click reveals; exit effects hide the previous step
        for ctn in click.iter("{%s}cTn" % NS["p"]):
            if ctn.get("presetClass") != "entr":
                continue
            for tgt in ctn.iter("{%s}spTgt" % NS["p"]):
                sid = tgt.get("spid")
                if sid and sid not in ids:
                    ids.append(sid)
        if ids:
            groups.append(ids)
    return groups


def expand_builds(prs, build_numbers):
    """Duplicate each build slide into base + one-per-click frames (in place). Returns notes map."""
    slides = list(prs.slides)
    lst = prs.slides._sldIdLst
    for num in sorted(build_numbers, reverse=True):
        src = slides[num - 1]
        groups = build_groups(src)
        if not groups:
            print(f"  slide {num}: no click animations found, left as is")
            continue
        all_build = {sid for g in groups for sid in g}
        src_sid = [s for s in lst if prs.part.related_part(s.rId) is src.part][0]
        pos = list(lst).index(src_sid)
        frames = [set()] + [set(g) for g in groups]
        for k, visible in enumerate(frames):
            new = prs.slides.add_slide(src.slide_layout)
            tree = new.shapes._spTree
            for el in list(tree)[2:]:
                tree.remove(el)
            for el in list(src.shapes._spTree)[2:]:
                sid = el.find(".//p:cNvPr", NS).get("id")
                if sid in all_build and sid not in visible:
                    continue
                el = copy.deepcopy(el)
                for node in el.iter():
                    for attr in list(node.attrib):
                        if attr.endswith("}embed") or attr.endswith("}link"):
                            rel = src.part.rels[node.get(attr)]
                            if "image" in rel.reltype:
                                import io
                                _, rid = new.part.get_or_add_image_part(io.BytesIO(rel.target_part.blob))
                                node.set(attr, rid)
                tree.append(el)
            if src.has_notes_slide:
                note = src.notes_slide.notes_text_frame.text
                new.notes_slide.notes_text_frame.text = note if k == 0 else f"[Build step {k} of {len(groups)}]"
            new_sid = list(lst)[-1]
            lst.remove(new_sid)
            lst.insert(pos + 1 + k, new_sid)
        lst.remove(src_sid)
        print(f"  slide {num}: expanded into {len(frames)} frames")


def inspect(prs):
    """Print what a converter run needs to know about the deck, then exit."""
    w, h = prs.slide_width, prs.slide_height
    print(f"slide size: {w/914400:.2f} x {h/914400:.2f} in  (aspect {w/h:.3f}; "
          f"{'4:3' if abs(w/h - 4/3) < 0.02 else '16:9' if abs(w/h - 16/9) < 0.02 else 'OTHER: check renders'})")
    print(f"{'#':>3}  {'hidden':6}  {'clicks':6}  {'video':5}  {'notes':5}  title")
    for i, s in enumerate(prs.slides, 1):
        hidden = "yes" if s._element.get("show") == "0" else ""
        clicks = len(build_groups(s)) or ""
        rels = [r.reltype for r in s.part.rels.values()]
        video = "yes" if any(("video" in r or "media" in r.split("/")[-1]) for r in rels) else ""
        notes = "yes" if s.has_notes_slide and s.notes_slide.notes_text_frame.text.strip() else ""
        title = ""
        if s.shapes.title is not None and s.shapes.title.has_text_frame:
            title = s.shapes.title.text_frame.text
        if not title:
            texts = [sh.text_frame.text for sh in s.shapes if sh.has_text_frame and sh.text_frame.text.strip()]
            title = texts[0] if texts else "(no text)"
        print(f"{i:>3}  {hidden:6}  {str(clicks):6}  {video:5}  {notes:5}  {' '.join(title.split())[:70]}")
    print("\nclicks = number of click steps that reveal shapes. Pass slides whose clicks tell a story to --builds.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pptx")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--inspect", action="store_true", help="list slides (hidden, click builds, video, notes) and exit")
    ap.add_argument("--title")
    ap.add_argument("--event", default="")
    ap.add_argument("--builds", nargs="*", type=int, default=[])
    ap.add_argument("--width", type=int, default=2400)
    ap.add_argument("--quality", type=int, default=86)
    a = ap.parse_args()

    prs = Presentation(a.pptx)
    if a.inspect:
        inspect(prs)
        return
    if not a.out or not a.title:
        ap.error("out and --title are required unless --inspect is given")

    out = Path(a.out)
    img_dir = out / "images"
    if img_dir.exists():
        shutil.rmtree(img_dir)
    img_dir.mkdir(parents=True)

    aspect = prs.slide_width / prs.slide_height
    size = "4:3" if abs(aspect - 4 / 3) < 0.02 else "16:9"
    if abs(aspect - 16 / 9) >= 0.02 and size == "16:9":
        print(f"  WARNING: unusual slide aspect {aspect:.3f}; rendered as 16:9 with letterboxing")

    # --builds numbers refer to the original PowerPoint numbering, so expand before dropping hidden slides
    hidden = [i + 1 for i, s in enumerate(prs.slides) if s._element.get("show") == "0"]
    expand_builds(prs, a.builds)
    lst = prs.slides._sldIdLst
    for sid in list(lst):
        s = prs.part.related_part(sid.rId).slide
        if s._element.get("show") == "0":
            lst.remove(sid)
    print(f"  dropped hidden slides: {hidden or 'none'}")
    notes = []
    for s in prs.slides:
        s._element.attrib.pop("show", None)
        t = s._element.find("p:timing", NS)
        if t is not None:
            s._element.remove(t)
        notes.append(s.notes_slide.notes_text_frame.text.strip() if s.has_notes_slide else "")

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        deck = tmp / "deck.pptx"
        prs.save(deck)
        subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", str(tmp), str(deck)],
                       check=True, capture_output=True, timeout=900)
        pdf = pymupdf.open(tmp / "deck.pdf")
        if len(pdf) != len(notes):
            sys.exit(f"page count {len(pdf)} != slide count {len(notes)}")
        names = []
        for i, page in enumerate(pdf, 1):
            zoom = a.width / page.rect.width
            pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom))
            im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            name = f"slide-{i:02d}.jpg"
            im.save(img_dir / name, quality=a.quality, optimize=True, progressive=True)
            names.append(name)

    import json
    # Raw PowerPoint notes, numbered by WEB slide, for drafting notes.json. Git-ignored: never publish it.
    (out / "notes.source.json").write_text(json.dumps({str(i): n for i, n in enumerate(notes, 1)}, indent=1, ensure_ascii=False))
    notes_file = out / "notes.json"
    if notes_file.exists():
        public = json.loads(notes_file.read_text())
        missing = [str(i) for i in range(1, len(notes) + 1) if str(i) not in public]
        extra = [k for k in public if not k.startswith("_") and (not k.isdigit() or int(k) > len(notes))]
        if missing or extra:
            sys.exit(f"{notes_file} does not match the {len(notes)} web slides "
                     f"(missing: {', '.join(missing) or 'none'}; extra: {', '.join(extra) or 'none'}). Fix it and re-run.")
        notes = [public[str(i)] for i in range(1, len(notes) + 1)]
        print(f"  speaker notes taken from {notes_file}")
    else:
        notes = [""] * len(notes)
        print(f"  NOTE: no {notes_file}; deck written WITHOUT speaker notes. Draft one from notes.source.json.")

    def q(t):
        return t.replace('"', '\\"')

    md = ["---", "marp: true", "theme: ames", f"size: {size}", "paginate: false", f'title: "{q(a.title)}"',
          f'description: "{q(a.event)}"', "---", ""]
    for i, (name, note) in enumerate(zip(names, notes)):
        if i:
            md += ["", "---", ""]
        md.append(f"![bg contain](images/{name})")
        if note:
            md += ["", "<!--", note.replace("--", "–"), "-->"]
    (out / "index.md").write_text("\n".join(md) + "\n")
    mb = sum(f.stat().st_size for f in img_dir.iterdir()) / 1e6
    print(f"wrote {out/'index.md'}: {len(names)} slides ({size}), images {mb:.1f} MB")


if __name__ == "__main__":
    main()
