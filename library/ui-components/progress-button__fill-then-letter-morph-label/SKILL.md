---
name: progress-button-fill-then-letter-morph-label
description: An outlined Export button grows into its own progress bar: it widens, shows a percentage, a light fill sweeps left to right under a shimmering "Exporting", then the label morphs letter by letter into "Exported" with a tick, and it shrinks back to "Export". Use for export button, download button and progress button beats in app promos.
---

# Progress button

**Code name:** Fill, then letter-morph label.

## What you see
A white page, one 40px button: download-tray icon and "Export", 1px dark border, 8px radius. At 0.6s it is pressed. Over 0.5s the button widens (101px to 165px) as the label turns into "Exporting" (the new letters rise in one after another, 35ms apart) and a "0%" slides in. From 1.65s a light grey fill grows from the left: 1% at 1.7s, 32% at 2.7s, 100% at 3.65s, the number counting with it, while a soft sheen runs along the letters. At 3.7s the icon turns into a tick and "ing" swaps to "ed" with a brief brighter flash on the fill. It holds as "Exported 100%" until 5.6s, then the fill fades, the percentage folds away, the tick turns back to the tray, "Exported" becomes "Export" and the button is back to 101px by 6.1s. 7.4s loop.

## When to use it
Export, download, save and send buttons in app promos: one small control that tells a whole story (pressed, working, done, reset). It is small, so run it large (the demo scales it 2x) or cut in close.

## How it works
Width is not animated: the button is `inline-flex` and its content changes (the percent box grows from 0 to the width of "100%" with `cubic-bezier(.22,1,.36,1)` over 0.5s; label slots change width as letters swap), so the button follows. Letters are separate slots; a swap is `p = clamp((s - ts - i * .035) / .3)`: the old letter fades out and rises 5px with a 2px blur, the new one fades in from 6px below. Progress is piecewise linear through (1.05s, 0), (1.12, 1), (2.12, 32), (3.05, 100). The fill is #0a0a0a at 10% opacity, clipped by the button; the source has a `sheen` keyframe (`mask-position` 100% to -50%) for the moving highlight, rebuilt here as a per-letter opacity wave of 1.4s.

## Numbers that matter
| | |
|---|---|
| Button | 40px high, 1px solid #34343a, radius 8, padding 0 16, gap 8, 14px / 500 |
| Widths | idle 101px, working 165px, done 170px |
| Fill | #0a0a0a at 10% |
| Letter swap | 0.3s, 35ms stagger |
| Progress | 1.05s to 3.05s after the press, 32% at 2.12s |
| Reset | fill fades and width returns over 0.5s starting 5.0s after the press |
| Press | scale to .96 and back |

## Sound
A tap on press; a rising tick while it fills; a "done" chime at the tick.

## Adapt it
- `CONFIG.idle`, `working`, `done` words (swap letters are computed for you)
- `FILLP` to change how long the work takes
- `CONFIG.size` for how big it renders
- Fill colour and border in the CSS

## Files
- `code/demo.html` self-contained, loops, `?w=1080&h=1920` for 9:16 (a 540-wide phone column), `?w=1280&h=800` for wide.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Progress Button" by joseestevez520 (https://21st.dev/@joseestevez520/components/progress-button), MIT. Recreated by eye from the public preview; this demo is original code. Full notices: `THIRD_PARTY_NOTICES.md`.
