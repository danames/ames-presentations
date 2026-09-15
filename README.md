# Ames Presentations

Dr. Dan Ames' conference and invited talks as live web slides, published at
**https://danames.com/ames-presentations/**.

Same stack as the CCE 114 and CE 414 course sites: [Marp](https://marp.app/) decks, built and
deployed to GitHub Pages by `.github/workflows/pages.yml` on every push to `main`.

| Talk | Live deck |
| --- | --- |
| From Reach IDs to Reasoning Agents · CIROH Science Meeting 2026 | [open](https://danames.com/ames-presentations/presentations/2026-ciroh-science-meeting/) |

## Layout

| Path | What |
| --- | --- |
| `index.html` | The landing page that lists every talk (hand-edited, newest first) |
| `presentations/<yyyy-event>/index.md` | Marp source for one talk |
| `presentations/<yyyy-event>/images/` | That talk's slide images |
| `theme/ames.css` | Deck theme (full-bleed, stays out of the way) |
| `tools/pptx_to_marp.py` | PowerPoint → Marp converter |

## Adding a talk

Conference decks are designed slide by slide in PowerPoint, so the converter renders each presented
slide to an image rather than re-authoring it. Speaker notes become presenter notes, hidden slides
are dropped, and click-build slides can be expanded into one web slide per click.

```bash
pip install python-pptx pymupdf pillow lxml      # plus LibreOffice for rendering
python3 tools/pptx_to_marp.py "path/to/Talk.pptx" presentations/2027-some-meeting \
    --title "Talk title" --event "Meeting · City · Date" --builds 13
```

`--builds` takes PowerPoint slide numbers whose click animations should become separate slides.

**Speaker notes are public** (they are in the page source). PowerPoint notes often hold private
presenter coaching, so write audience-safe notes in `presentations/<slug>/notes.json`, keyed by web
slide number; the converter uses that file whenever it exists and refuses to build if a slide is missing.

Then add a card for the talk to `index.html`, check it locally, and push:

```bash
marp --no-stdin --theme theme/ames.css --html --allow-local-files \
    presentations/2027-some-meeting/index.md -o /tmp/check.html && open /tmp/check.html
```

Do not commit built `.html` decks or the source `.pptx`.

## Viewing

Arrow keys or click to advance, **F** for full screen, **P** for presenter view with speaker notes.
Speaker notes are embedded in the published page source, which is why each talk keeps a reviewed `notes.json`.
