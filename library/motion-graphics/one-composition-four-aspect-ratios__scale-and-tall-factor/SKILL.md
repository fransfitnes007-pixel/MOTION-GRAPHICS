---
name: one-composition-four-aspect-ratios-scale-and-tall-factor
description: "A way to render one hand-coded composition at 16:9, 9:16, 4:5 and 1:1 from the same file: three derived numbers (scale, vertical flag, tallness) drive every position. Use it when one video must ship to every platform."
---

# One composition, four aspect ratios

**Code name:** Scale and tall factor.

## What you see
Four frames of one scene: a house photo, a two-line headline, a card and cast chips. In 16:9 the headline is large and chips sit in a row at the lower left; in 9:16 the type is smaller and the chips become a column; 1:1 and 4:5 keep the 9:16 sizes at their own height. The demo puts the four finished layouts side by side at the same moment.

## When to use it
A video for TikTok, Reels, a YouTube cut and a feed square from one source. It works best for coded motion graphics where you control every position. It is not a re-cropping trick: the layout is recomputed, not cropped.

## How it works
One page reads `w`, `h` from the URL (`?w=1080&h=1920`) and derives:

```js
const V = H >= W                                          // vertical-ish: 9:16, 4:5, 1:1
const S = V ? W / 1080 : Math.min(W / 1920, H / 1080)     // design scale: designs live at 1920x1080 or 1080 wide
const TALL = V ? H / W : 0                                // 1.78, 1.25 or 1
const HF = (V ? 100 : 128) * S, M = (V ? 72 : 110) * S    // headline size and margin
```
Every position is a fraction of `W`/`H` or a multiple of `S`, with `V ? a : b` choosing the layout, and `TALL` picking a third branch when it matters (hero scale 0.95 / 0.8 / 0.66; chips in a column when `TALL > 1.4`). Photos are cover-fitted by `Math.max(W / iw, H / ih)`. `render.cjs` then loads the page at each size and steps `render(t)` frame by frame; `build.sh` renders one deliverable per size and cut. The demo shows four copies of the same helpers, each closed over its own `W, H, V, S, TALL`, drawn at native size and scaled down, so you can compare layouts in one frame.

## Numbers that matter
| | |
|---|---|
| Sizes rendered | 1920 by 1080, 1080 by 1920, 1080 by 1350, 1080 by 1080 |
| Design scale | wide `min(W/1920, H/1080)`, vertical `W/1080` |
| Headline | 128px wide, 100px vertical (times scale) |
| Margin | 110px wide, 72px vertical |
| Hero scale (vertical) | 0.95 if TALL > 1.5, 0.8 if > 1.15, else 0.66 |

## Sound
Each ratio can carry the same narration and effects in every ratio; the sound is not tied to layout.

## Adapt it
- The breakpoints (`TALL > 1.4` etc.) for your own layouts.
- The design widths (1920 / 1080).
- Add more ratios in the build job list.

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. Playfair Display (SIL Open Font License, from Google Fonts) is copied into `code/fonts/` because the serif headline is half the look. The demo uses the system font stack. The demo draws gradient placeholders in CSS.
- `code/fonts/` holds the fonts the demo loads.
