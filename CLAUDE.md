# Converting a PowerPoint talk into a live web deck

This repository publishes Dr. Dan Ames' conference and invited talks as live web slides at
**https://danames.com/ames-presentations/**. This file is the procedure for adding a talk. Follow it
step by step; every talk should look and behave the same.

The stack is the same as the CCE 114 and CE 414 course sites: [Marp](https://marp.app/) decks,
built and deployed to GitHub Pages by `.github/workflows/pages.yml` on every push to `main`.
The first talk converted, `presentations/2026-ciroh-science-meeting/`, is the reference example.

## How it works (read once)

Conference decks are designed slide by slide in PowerPoint, with custom shapes, charts, and photos.
Rewriting them as Markdown loses that design, so `tools/pptx_to_marp.py` does not re-author slides.
It renders each presented slide to a full-slide JPEG with LibreOffice and writes a Marp deck
(`index.md`) that shows one image per slide. Specifically, it:

- drops hidden slides (the web deck shows what was presented);
- expands click-build slides (`--builds N`) into one web slide per click, showing only the shapes
  that click reveals, so a walkthrough still steps through on the web;
- sets the deck to 4:3 or 16:9 from the PowerPoint slide size;
- takes speaker notes **only** from a reviewed `notes.json`, never directly from PowerPoint.

The published URL for a talk is `https://danames.com/ames-presentations/presentations/<slug>/`.
The landing page, `index.html`, lists every talk and is edited by hand.

## Hard rules

1. **Speaker notes are public.** They are embedded in the page source that anyone can read. The
   PowerPoint notes are Dan's private presenter notes and must never be published as-is. Write
   audience-safe notes in `notes.json` (Step 4). The raw notes land in `notes.source.json`, which is
   git-ignored; never commit it and never copy it wholesale into `notes.json`.
2. **Never edit Dan's source `.pptx`.** Read it and render copies. If a slide itself has a problem,
   report it; don't fix the original.
3. **Never commit** the `.pptx`, `notes.source.json`, or built `.html` (all are in `.gitignore`).
4. **Pushing to `main` publishes to the public web within about a minute, and the repo is public.**
   Show Dan what you built and get his explicit OK before you push. Never force-push or rewrite
   history unless he asks.
5. **Always look at what you produced.** Render the deck and view the slides before calling it done.

## Step 1: find the deck and choose a slug

- Get the exact `.pptx` path from Dan, and confirm it is the **final** version. Conference folders
  often hold several (`v2`, `v3`, … or "final"); when in doubt, ask. His talks usually live under
  `/Users/dan/ames-sync/Work/Conferences/<year>/<meeting>/`.
- Collect for the landing card and front matter: the talk title, the meeting name, the city, and the
  date. Take them from the title slide or ask; do not guess a date.
- Choose a slug: `<yyyy>-<short-meeting-name>`, lowercase with hyphens, e.g.
  `2026-ciroh-science-meeting`, `2025-agu-fall-meeting`. If Dan gave two talks at one meeting,
  append a topic: `2025-agu-fall-meeting-rivr`.

## Step 2: set up (first time on a machine)

```bash
pip install python-pptx pymupdf pillow lxml
brew install --cask libreoffice      # provides soffice; the converter finds it on PATH or /opt/homebrew/bin
npm install -g @marp-team/marp-cli   # or use npx -y @marp-team/marp-cli@latest
```

## Step 3: inspect, then convert

```bash
python3 tools/pptx_to_marp.py "/path/to/Talk.pptx" --inspect
```

This lists every slide with its hidden flag, number of click steps, video, and whether it has notes,
plus the slide size. Decide:

- **Builds.** A slide whose clicks reveal a sequence (a walkthrough, highlights, zooms) should be
  expanded: pass its PowerPoint slide number to `--builds`. Slides where clicks only fade in bullets
  do not need it; the final state is fine. Check the rendered frames: the converter reveals only the
  shapes each click *enters* and hides the rest, matching the common "highlight one step at a time"
  pattern. If a build accumulates instead (each click adds to the last), the frames will each show
  only one step; tell Dan rather than hand-editing.
- **Hidden slides** are dropped automatically. If Dan wants a hidden slide published, he must unhide
  it in PowerPoint first.
- **Video** cannot play in a still image. The slide renders as its poster frame. Mention it to Dan
  and, if the video is online, put its link in that slide's note.

Then convert:

```bash
python3 tools/pptx_to_marp.py "/path/to/Talk.pptx" presentations/<slug> \
    --title "Talk title" --event "Meeting · City, State · Month D, YYYY" --builds 13
```

This writes `presentations/<slug>/images/slide-NN.jpg`, `index.md`, and `notes.source.json` (raw
PowerPoint notes numbered by **web** slide, i.e. after builds are expanded and hidden slides dropped).
On this first run there is no `notes.json` yet, so `index.md` has no notes. That is expected.

## Step 4: write the public speaker notes (`notes.json`)

Read `notes.source.json` alongside the slide images and write `presentations/<slug>/notes.json`:

```json
{
  "_about": "Public speaker notes for the web deck, keyed by web slide number.",
  "1": "…",
  "2": "…"
}
```

Every web slide needs an entry (use `""` for none); the converter refuses to build if one is missing
or extra. Write each note as neutral narration of what the slide says and shows, as if for a viewer
clicking through on their own.

**Keep:** the factual content, numbers, methods, results, what a figure shows and how to read it,
citations, and credit that already appears on the slide.

**Remove or rewrite:**
- presenter coaching and delivery tips ("keep it brisk", "pause here", "land the joke",
  "deliver it as a finding, not a confession"), and timings ("~1 min");
- logistics: session numbers and times, room, "first talk of the session", "backup slides follow";
- private opinions or candid remarks about people, institutions, reviewers, funders, or competing
  tools (e.g., why another tool is slow);
- personally identifiable or sensitive information about anyone other than Dan: email addresses,
  phone numbers, grades, student status beyond what the slide shows, health, family, visa or
  immigration status, and anything said about a person's performance;
- names not shown on the slides. Credit a student in a note only if the slide already credits them;
- leftovers from editing or from AI assistance ("Yes, the brief is from…", "as you asked",
  TODO comments, version notes);
- claims the slide does not support. If a note asserts something new (a result, a status, a date),
  keep it out and ask Dan.

For expanded build frames, give each frame a one-line note describing that step.

If something on a **slide image** itself looks sensitive (a personal photo, an unpublished figure
marked confidential, a document with someone's details), do not remove it silently. List it for Dan.

Re-run the Step 3 convert command. It now reports `speaker notes taken from …/notes.json`.

## Step 5: check it

```bash
marp --no-stdin --theme theme/ames.css --html --allow-local-files --images png --image-scale 0.4 \
    presentations/<slug>/index.md -o /tmp/<slug>-qa/s.png
```

`--no-stdin` stops marp from hanging on stdin; `--allow-local-files` is needed for images to render.
Make a contact sheet of the PNGs (Pillow) and look at every slide. Check:

- **Font substitution.** LibreOffice renders fonts it lacks with substitutes. Look for text that
  overflows its box, wraps differently, or overlaps; compare against the original deck if in doubt.
  Fix by telling Dan which slides and fonts; do not edit his `.pptx`.
- **Build frames** step through correctly (one highlighted step each, nothing stacked).
- **Charts, SmartArt, and equations** rendered (LibreOffice occasionally drops or misdraws them).
- **No blank or duplicate slides**, and the slide count matches the `--inspect` listing minus hidden
  slides plus extra build frames.
- **Size.** Keep a talk's `images/` under about 25 MB. If it is larger, re-run with `--width 1920`
  or `--quality 80`.

Then view the real thing in a browser. Build to a scratch folder (not inside the repo), serve it,
and click through:

```bash
mkdir -p /tmp/site/presentations/<slug> && cp index.html /tmp/site/ \
  && marp --no-stdin --theme theme/ames.css --html presentations/<slug>/index.md -o /tmp/site/presentations/<slug>/index.html \
  && cp -r presentations/<slug>/images /tmp/site/presentations/<slug>/ \
  && python3 -m http.server 8765 --directory /tmp/site
```

Confirm arrow keys advance, **F** goes full screen, and **P** opens presenter view with the notes.

## Step 6: add the talk to the landing page

Edit `index.html`. Talks are grouped under year headings, newest first. Add a year heading if needed,
then copy an existing card:

```html
<a class="talk" href="presentations/<slug>/">
  <img src="presentations/<slug>/images/slide-01.jpg" alt="">
  <div>
    <div class="title">Full talk title</div>
    <div class="meta">Meeting · City, State · Month D, YYYY</div>
  </div>
</a>
```

Also add a row to the talk table in `README.md`.

## Step 7: publish (with Dan's OK)

Report to Dan before pushing: the slug and future URL, the slide count, which slides were dropped
(hidden) or expanded (builds), any video slides, any rendering problems, anything sensitive you saw
on slides, and a summary of what you removed from the notes. Once he approves:

```bash
git add presentations/<slug> index.html README.md
git commit -m "Add <meeting> <year> web deck: <short title>"
git push
gh run watch "$(gh run list --limit 1 --json databaseId -q '.[0].databaseId')" --exit-status
```

Then open `https://danames.com/ames-presentations/` and the talk URL and confirm both load, the card
thumbnail shows, and the deck steps through. GitHub Pages can take a minute or two after the run
finishes; add `?x=1` to the URL to bypass caching.

## Updating a talk that is already published

If Dan revises the PowerPoint, re-run the Step 3 convert command into the same folder (it replaces
`images/` and `index.md`). If the slide count or order changed, `notes.json` will no longer match and
the converter will say so: update the note numbering and content, then re-run. Check (Step 5), get
his OK, commit, and push.

## Layout

| Path | What |
| --- | --- |
| `index.html` | Landing page listing every talk (hand-edited, newest first) |
| `presentations/<slug>/index.md` | Marp source for one talk (generated by the converter) |
| `presentations/<slug>/images/` | Rendered slides (generated) |
| `presentations/<slug>/notes.json` | Reviewed public speaker notes (hand-written) |
| `presentations/<slug>/notes.source.json` | Raw PowerPoint notes (generated, git-ignored, private) |
| `theme/ames.css` | Deck theme: full-bleed, 16:9 and 4:3 sizes. Do not edit for one talk |
| `tools/pptx_to_marp.py` | The converter (`--help` for options) |
| `.github/workflows/pages.yml` | Builds every `presentations/*/index.md` and deploys the site |

Dan's homepage (`danames.com`, repo `danames/danames.github.io`) already links to the landing page
under "Presentations"; adding a talk does not require touching it.

## When you finish

Say plainly what you converted, the URL, what you verified versus assumed, what you flagged for Dan,
and whether you pushed.
