---
name: line-chart-grow-point-slice-path
description: "A blue line chart draws itself left to right with a soft gradient fill under it, by redrawing the path with more points each frame. Reach for it for 'growth' behind or under a big number."
---

# Growing line chart

**Code name:** Point-slice path with gradient fill.

## What you see
Under the counting number, a thick (7px) blue line with round ends starts at the left edge of an 800 by 260 area, scaled to 1.3 times its size. Over a little over a second it draws toward the right, climbing slowly then steeply, with small waves in it. A fill under the line is the same blue at 35% opacity at the line and 0% at the bottom, so the line sits on a soft glow. It stops at the top right corner. There are no axes, labels or gridlines: it is only a shape that says "up".

## When to use it
Growth under a big number, or as a background element in a results scene. It is a decoration, not a data chart. It is wrong where the audience should read values.

## How it works
No stroke-dash trick. The path is rebuilt each frame from a list of 41 points, using only as many as the progress allows, so the line's end really moves along the curve:

```js
const chPts = Array.from({ length: 41 }, (_, i) => [i * 20, 240 - 220 * Math.pow(i / 40, 2.2) * (0.86 + 0.14 * Math.sin(i * 1.7))])
const m = Math.max(2, Math.round(eo(seg(t, t0, t1)) * 40))
line.d = 'M' + chPts.slice(0, m + 1).map((p) => p.join(' ')).join(' L')
fill.d = line.d + ` L${lastX} 260 L0 260 Z`                       // close down to the baseline and back
```
The curve is `i^2.2` (slow start, steep finish) times a wiggle of `sin(i * 1.7)` between .86 and 1, so the line is not a perfect curve. The path is built from straight segments between 20px steps and `stroke-linejoin: round` hides the corners. Because the points are added in whole steps, the line's tip advances in 20px jumps; at 30 fps over 1s that is barely visible.

## Numbers that matter
| | |
|---|---|
| Points | 41, 20px apart, `x` from 0 to 800 |
| Shape | `y = 240 - 220 * (i/40)^2.2 * (.86 + .14 * sin(1.7 i))` |
| Line | 7px, `#2f6bff`, round caps and joins |
| Fill | `#2f6bff` from 35% to 0% opacity, top to bottom |
| Timing | `eo` over 1.06s; the whole chart fades in over .4s |
| Size | 800 by 260, scaled 1.3 (1.2 on tall) |

## Sound
Shares the keypress ticks of the number count above it (28 ticks over 0.8s).

## Adapt it
- The 41 data points: use real data (`y` values from 0 to 240).
- Line colour and fill.
- Duration and ease.
- Add a dot at the tip: use `pts[pts.length - 1]`.

## Files
- `code/demo.html` runs on its own.
