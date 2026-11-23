---
name: copy-button-check-draw-label-crossfade
description: A compact outlined button that turns "Copy" plus a clipboard icon into "Copied" plus a tick that draws itself. Reach for it beside code snippets, install commands and share links.
---

# Copy button

**Code name:** Check stroke draw and label crossfade.

## What you see
A white page with one small button in the middle: white fill, 1px light grey border, 14px corners, a soft two-layer shadow. About 163 by 64 in the clip's pixel scale. Left is a clipboard icon, right is "Copy" in 22px semibold dark grey.

The clip is 4.6s. A cursor moves onto the button at about 0.8s and clicks at about 1.1s. The clipboard icon is replaced by a check mark that draws itself, and the word crossfades to "Copied" in the same spot, so the button does not change width. The cursor then drifts away, and "Copied" is still showing when the clip ends. The demo holds it for 2.3s, crossfades back to "Copy" and loops at 5.6s.

## When to use it
Anywhere a value is copied: install commands, API keys, invite links, code blocks. The check draw gives a clear "it worked" without a toast. It is a bad fit when the copy can fail often and needs an error message; the 21st.dev description says this component also has an error state with a clipboard fallback and reduced-motion handling, which the clip does not show.

## How it works
Two icons and two labels share one slot each. State drives opacity; the label also moves 5px and blurs 2px as it fades. The check is a single SVG path with `pathLength="1"` so its dash offset runs from 1 to 0.

```js
chk.style.strokeDashoffset = String(1 - draw)   // draw: 0 to 1 over 0.3s, ease-out
S(tx1, { opacity: 1 - m, transform: `translateY(${-5*m}px)`, filter: `blur(${m*2}px)` })
S(tx2, { opacity: m,     transform: `translateY(${5*(1-m)}px)`,  filter: `blur(${(1-m)*2}px)` })
```

The usage example is `<CopyButton value="npx interior add copy-button" />`, so the text to copy is the only prop shown.

## Numbers that matter
| | |
|---|---|
| Button | 164 x 64, 14px radius, 1px `#e4e4e6`, fill `#fff`, hover `#f6f6f7` |
| Label | 22px / 600 `#2b2b2e` |
| Icon | 20px, stroke 2 |
| Swap | 0.22s crossfade, label shifts 5px |
| Check draw | 0.3s ease-out |
| Press | scale 0.96 for about 0.18s |
| Hold | 2.3s in the demo before reverting |

## Sound
Silent.

## Adapt it
- `CONFIG.idleLabel` and `doneLabel`.
- `resetAfter` for how long the confirmation stays.
- `drawSec` and `swapSec` for a snappier or slower feel.
- The scale `K2` near the top if you want the button bigger or smaller on screen.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Copy Button" by ddoemonn on 21st.dev (https://21st.dev/@ddoemonn/components/copy-button), MIT. This demo is an original recreation written from the public preview.
