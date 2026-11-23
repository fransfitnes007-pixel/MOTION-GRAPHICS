---
name: cover-wall-glass-counter-grid-zoom-out-count
description: "A 15x9 wall of vertical video covers pulls back from a tight 3.2x crop, ripples in outward from the centre, with a frosted-glass card holding a counter that runs to \"10,000+\" members, then runs on to half a billion views while a line chart draws across the bottom."
---

# Cover wall with glass counter

**Code name:** Grid zoom-out, count.

## What you see
The wall is 135 tiles (150x266px, 170px by 286px pitch) scaled 3.2x and rotated -4 degrees, so a few tiles fill the frame. Over 1.2s it eases back to 1x and 0 degrees, then keeps pulling out slowly to 90% over three more seconds. Tiles fade in from the centre outwards, delayed by their distance (0.045s per unit). A pale veil is laid over the wall so the middle is readable, and a glass card 1060x420 springs in. Inside it a 200px counter runs from 400 to the target, shows "+" and turns violet, then blurs and swaps to a second figure of 170px which runs from 5,000,000 to the big number, ends in the short form at 230px in violet. At the bottom a purple line with a fading area fill draws left to right over 60 points. At the end the wall zooms away and fades.

## When to use it
"Scale" scenes: how many people, products or items are behind the claim. The wall is texture; the numbers are the content. It needs a lot of different covers; a repeated tile reads as a template.

## How it works
Four things in one scene:

1. The wall is one parent scaled and rotated (`scale(z)`, `rotate(-4 + 4 * e)`), with each tile's own opacity and scale driven by `p = eo5(seg(t, 22.4 + d*.045, 22.85 + d*.045))`, where `d = hypot(r * 1.6, c)`.
2. The veil fades up from 90% to 100% opacity as the figures change so the card text stays legible over busy covers.
3. The counter is a text swap, not two elements: a width-stable `tabular-nums` string and a short blur (`sw`) hides the jump from the "members" to the "views" figure.
4. The line chart is rebuilt as an SVG path each frame from a fixed 60-point array, showing `round(cp * 60)` points:
```js
const n = Math.max(2, Math.round(cp * CHART.length)), pts = CHART.slice(0, n).map((v, i) => [i * 1600 / 59, 240 - v * 220])
```

## Numbers that matter
| | |
|---|---|
| Wall | 15 columns x 9 rows, tile 150x266 radius 14px, pitch 170x286, origin the frame centre |
| Zoom | 3.2 to 1 over 22.4s to 23.6s (`eio5`), then to 0.9 until 26.4s; rotate -4 to 0 |
| Tile fade | 0.45s `eo5`, delay 0.045s x distance |
| Card | 1060x420, radius 44px, glass `rgba(255,255,255,.72)`, spring k=7 f=11 |
| Counter | `eo5`; "members" 400 to 5,000 in the demo; "views tracked" 170px, 230px at the end |
| Chart | 1600x260 at (160,790); 6px line `#6d3cff`, area gradient `#8b5cf6` .35 to 0; draws 24.42s to 25.9s |

## Sound
Impacts when each figure lands, and a whoosh into and out of the scene. Rising music energy.

## Adapt it
- Figures and their labels; real numbers need a source line.
- `CHART`: replace the 60 points with your own series.
- Wall size and pitch; `T0` and the card position.
- The veil colour, which must match the stage.

## Files
- `code/demo.html` (covers are gradient placeholders; the figures are placeholders too).
- Related: `cover-wall-tight-crop-pull-back__scale-rotatex-pull` (the same pull-back with stamps instead of a counter).
