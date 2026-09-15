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

Follow [`CLAUDE.md`](CLAUDE.md), the step-by-step procedure (it is also what an AI agent working in
this repo reads first). In short: inspect the deck, convert it, write reviewed public speaker notes in
`notes.json`, check the rendered slides, add a card to `index.html`, and push.

```bash
python3 tools/pptx_to_marp.py "path/to/Talk.pptx" --inspect
python3 tools/pptx_to_marp.py "path/to/Talk.pptx" presentations/2027-some-meeting \
    --title "Talk title" --event "Meeting · City · Date" --builds 13
```

## Viewing

Arrow keys or click to advance, **F** for full screen, **P** for presenter view with speaker notes.
Speaker notes are embedded in the published page source, so each talk publishes only its reviewed `notes.json`.
