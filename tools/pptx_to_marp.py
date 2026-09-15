#!/usr/bin/env python3
"""Convert a finished PowerPoint talk into a Marp web deck that looks exactly like the original.

Conference decks are designed slide by slide (custom shapes, charts, photos), so instead of
re-authoring them in Markdown this tool renders every presented slide to a full-slide image and
writes a Marp deck that shows those images, one per slide, with the PowerPoint speaker notes kept
as presenter notes.

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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx")
    ap.add_argument("out")
    ap.add_argument("--title", required=True)
    ap.add_argument("--event", default="")
    ap.add_argument("--builds", nargs="*", type=int, default=[])
    ap.add_argument("--width", type=int, default=2400)
    ap.add_argument("--quality", type=int, default=86)
    a = ap.parse_args()

    out = Path(a.out)
    img_dir = out / "images"
    if img_dir.exists():
        shutil.rmtree(img_dir)
    img_dir.mkdir(parents=True)

    prs = Presentation(a.pptx)
    # drop hidden slides first so --builds numbers refer to the original PowerPoint numbering
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
                       check=True, capture_output=True, timeout=600)
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

    notes_file = out / "notes.json"
    if notes_file.exists():
        import json
        public = json.loads(notes_file.read_text())
        missing = [str(i) for i in range(1, len(notes) + 1) if str(i) not in public]
        if missing:
            sys.exit(f"{notes_file} has no entry for web slides {', '.join(missing)}; add them before publishing")
        notes = [public[str(i)] for i in range(1, len(notes) + 1)]
        print(f"  speaker notes taken from {notes_file}")
    else:
        print("  WARNING: using PowerPoint speaker notes as-is; they will be public. Consider a notes.json.")

    md = ["---", "marp: true", "theme: ames", "paginate: false", f"title: \"{a.title}\"",
          f"description: \"{a.event}\"", "---", ""]
    for i, (name, note) in enumerate(zip(names, notes)):
        if i:
            md += ["", "---", ""]
        md.append(f"![bg contain](images/{name})")
        if note:
            md += ["", "<!--", note.replace("--", "–"), "-->"]
    (out / "index.md").write_text("\n".join(md) + "\n")
    size = sum(f.stat().st_size for f in img_dir.iterdir()) / 1e6
    print(f"wrote {out/'index.md'}: {len(names)} slides, images {size:.1f} MB")


if __name__ == "__main__":
    main()
