---
name: creator-tile-grid-scatter-staggered-spring-fly
description: "Forty-eight small portrait tiles fly in from a single point above, spinning and growing at slightly different moments, and land as an offset grid that then fades. Reach for it to say 'a lot of people' or 'a crowd of creators'."
---

# Profile tile grid scatter

**Code name:** Staggered spring fly-in.

## What you see
Right after a headline sentence reaches its last word, 48 small portrait tiles appear at one point above the centre of the frame, tiny and rotated at random angles up to 45 degrees either way. Each one springs along its own line down to the bottom of the frame, growing to full size and spinning upright, between 0.1s and 1.15s after the start (each tile's delay is random, up to 0.35s). They land in a grid of rows with every other row offset by half a tile. About 12 tiles are on screen across the width of a wide frame. The grid holds, then all tiles fade over 0.3s as the next scene begins. The demo holds a static headline above them.

## When to use it
"A crowd" or "a thousand": people, customers, apps, results. The tiles can be any small images. It is wrong when each tile has to be read, since they are about 170px wide and 100px high. It needs the sentence that names the idea to be placed above it.

## How it works
Every tile uses the same pure formula, with the random numbers coming from a seeded hash so frame N is always the same:

```js
const rnd = (i, s = 1) => { const x = Math.sin(i * 127.1 + s * 311.7) * 43758.5453; return x - Math.floor(x) }
const d = rnd(i) * .35                                       // each tile starts up to .35s late
const q = spring(seg(t, T0 + d, T0 + .7 + d), 6, 9)           // lower k and f than the other springs: a loose, floaty landing
left = lerp(fx, gx, q); top = lerp(fy, gy, q)
transform = `translate(-50%,-50%) rotate(${(1 - q) * (rnd(i, 3) - .5) * 90}deg) scale(${.3 + .7 * q})`
```
The start point `(fx, fy)` is `CX + (rnd(i, 2) - .5) * 300` by `CY - 500`: a 300px-wide cloud above the frame. The landing point puts tiles on a grid with a 14px gap and a half-tile shift on every second row. Opacity ramps with `clamp(q * 2)` and ends at .96.

## Numbers that matter
| | |
|---|---|
| Tiles | 48 wide (36 tall), 170px (150 tall) wide, height `width * 16/9 * .6` |
| Spring | k6 f9 over .7s, delay `rnd(i) * .35` |
| Start | 300px cloud, 500px above centre, scale .3, up to 45 degrees off |
| Grid | 2 rows (3 tall), gap 14px, odd rows shifted half a tile |
| Fade | .3s, 1.4s after the start |

## Sound
A quick run of 48 tiny pops (1100 to 1450Hz, 0.11s each, quiet), spread over 0.55s with slight stereo spread, as if the tiles were clicking into place.

## Adapt it
- The tile images and count.
- Start point and spread (`fx`, `fy`) to change where they come from.
- Grid columns, rows and the offset.
- Spring `k` and `f`: higher `k` makes a tighter landing.

## Files
- `code/demo.html` runs on its own. Tiles are gradient placeholders.
