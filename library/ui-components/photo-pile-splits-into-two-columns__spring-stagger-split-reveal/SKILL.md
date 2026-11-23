---
name: photo-pile-splits-into-two-columns-spring-stagger-split-reveal
description: A pile of eight rounded photo tiles at the centre of a cream page flies apart into two tilted columns on click or scroll, revealing a headline and paragraph; reach for it as a hero that opens on interaction.
---

# Photo pile that splits into two columns

**Code name:** Spring stagger split reveal.

## What you see
A cream page (#f3f0e8) inside a rounded frame with a faint dot grid. In the middle sits a small loose pile of eight rounded-square photo tiles (132px, radius 30, soft shadow), each rotated a few degrees. A pointing-hand cursor rests to the right of the pile and a pill at the bottom reads "Scroll down or click to unveil" with an orange dot.

On the trigger the pile opens like a curtain: four tiles go to the left edge, four to the right, in two phases. First they slide out sideways and toward their column, then they spread vertically to rows 167, 334, 493 and 654 px. Each row starts 0.045s after the one above, and a spring overshoots a few percent before settling. The tiles end tilted (left column -13, -8, -6, -3 degrees; right column +8, +6, +4, +2). While this happens the eyebrow "MONOGRAPH NO. 04", a two-line serif headline, a short rule and a three-line paragraph fade up in the gap between the columns. The pill changes to "Scroll up or click to close curtain" and its dot turns green.

The video only shows the opening (2.9s). The demo loops it: pile for 1s, opens, holds, closes the same way at 4.2s. The closing motion is inferred from the pill text, not seen.

## When to use it
A landing hero where the first view is a calm object and the headline is revealed by the visitor. It fits editorial, architecture or portfolio sites with eight good images. It is a poor fit when the headline must be visible immediately, since it starts hidden.

## How it works
Each tile has a stacked pose (centre, small seeded nudge and tilt) and an open pose (column x, row y, set tilt). One spring value `k` blends between them, with the vertical blend lagging the horizontal by 0.12s so they slide out first and then fan down:
```js
const k  = open(i)        // x and rotation
const k2 = open(i, .12)   // y, 0.12s later
x = lerp(sx, ex, k);  y = lerp(sy, ey, k2);  r = lerp(sr, er, k)
open = spring(seg(t, tOpen + row * .045, tOpen + row * .045 + .8), 6.5, 7)
```
The text fades with the same progress (`opacity = clamp((k - .3) / .7)`). In the real component the toggle is a scroll wheel or a click; here `tOpen` and `tClose` stand in for it.

## Numbers that matter
| | |
|---|---|
| Canvas | 1256 x 856, frame inset 18px, radius 34 |
| Tiles | 132px, radius 30, 8 of them, columns at x 207 and 1049 |
| Open | 0.8s spring k=6.5 f=7, 0.045s per row, y lags x by 0.12s |
| Headline | Georgia 54px/56px, eyebrow mono 12px at .3em spacing |
| Pill | 336 x 40, 14px semibold, dot orange then green |
| Loop | open at 1.0s, close at 4.2s, 6.4s total |

## Sound
Silent.

## Adapt it
- `CONFIG.eyebrow`, `title`, `body` and the two pill texts.
- Swap the `art(i)` SVGs for `<img>` tags; keep the tile size and radius.
- `CONFIG.colX`, `rowY` and `tilt` to change where the columns land.
- `CONFIG.stagger` and `openTime` for a slower or snappier curtain; wire `tOpen` to your own click or scroll.

## Files
- `code/demo.html` runs on its own and loops. Placeholder art is CSS and SVG only.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Curtain Split Hero" by daiwiikharihar on 21st.dev (https://21st.dev/@daiwiikharihar/components/curtain-split-hero), MIT. This demo is an original recreation written from the public preview.
