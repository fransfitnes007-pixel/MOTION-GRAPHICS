---
name: easing-lanes-comparison-board-six-curve-ball-race
description: A cream board titled in italic serif shows six easing lanes, each with a tiny curve icon, and six balls racing from A to B on their own easing at the same time. Rebuilt by eye from a public motion video (see Credit); use it in app promos and launch reels.
---

# Easing lanes comparison board

**Code name:** Six-curve ball race. Rebuilt by eye from a public motion video; original code, credited below.

## What you see
Black frame with thin white HUD corner marks. A cream (#ece8df) board rises in 0.4s. Title "Easings from A to B" in italic serif. Six lanes: linear, ease in, ease out, ease in out, back out, spring; each has its name, a 36px curve drawn as an icon, a hairline track and a ball (black, blue or red-orange). At 0.5s all six balls leave A together and arrive at B by 1.9s, each on its own curve: the ease-in ball lags, the ease-out ball races ahead, the back-out ball overshoots B and returns, the spring ball wobbles. At 2.6s they all return to A on ease-in-out.

## When to use it
A showreel beat that says "I know motion", a tutorial, or a reference while choosing an easing. Also good as a hook for content about app animation. Wrong in a product promo for a non-design product.

## How it works
Six lanes, one formula each; the ball's x is `lerp(A, B, f(progress))`. The formulas are the library's own (`eo`, `ei`, `eio`, `back` with s 1.9, and a spring `1 - e^(-6x) cos(13x)`), so this doubles as a visual key to the helpers every other demo uses.
```js
['back out', (x) => { const s = 1.9, c3 = s + 1; return 1 + c3*(x-1)**3 + s*(x-1)**2 }]
const v = t < back ? f(go) : 1 - eio(backProgress)   // all six return together
```

## Numbers that matter
| | |
|---|---|
| Travel | 1.4s from .5s |
| Return | .98s ease-in-out from 2.6s |
| Board | 80% x 78% of the frame, radius 18 |
| Title | 64px italic serif |
| Balls | 15px radius, #111 / #2f5bea / #ed4938 |

## Sound
Silent in the source scene (music only). A soft tick as each ball arrives at B would expose the timing differences. The demo is silent.

## Adapt it
- `lanes`: swap in your own easing functions (e.g. a framer-motion spring) to compare them.
- `title`, colours.

## Files
- `code/demo.html` runs on its own; every value to change is in the `CONFIG` block at the top of the skill script.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "revid.ai Claude Opus 5.5 wall #1: The showreel that started it" by @stephanlivera (https://x.com/stephanlivera/status/2103315922098470926), Video belongs to its creator; not included. Recreated by eye from watching the public video; this demo is original code and contains none of the video. Full notices: `THIRD_PARTY_NOTICES.md`.
