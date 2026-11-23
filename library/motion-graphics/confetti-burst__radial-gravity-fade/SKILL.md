---
name: confetti-burst-radial-gravity-fade
description: "Twenty-six small coloured dots and squares fly outward from the centre of the frame, spin, fall under gravity and fade out in just over a second. Reach for it to celebrate a paid, won or completed moment."
---

# Confetti burst

**Code name:** Radial burst with gravity and fade.

## What you see
At the moment a confirmation card's check pops in, 26 small pieces appear at the centre of the frame and fly out in all directions. Each piece is 14px: two thirds are round and one third has a 3px corner radius, in five colours in rotation (blue, yellow, pink, cyan, green). They travel between 300 and 720px from the centre, fast at first, slowing as they go, while falling under gravity (up to 500px by the end), spinning up to two turns, and fading out toward the end. The whole burst lasts 1.15s. In the demo a green check circle sits at the centre as the thing being celebrated.

## When to use it
A celebration beat tied to a spoken result, over a card or number. It is brief enough to sit over other content. It is wrong in a calm, serious video, and the pieces are too small to read in a thumbnail.

## How it works
Each piece reads one progress value `u` (0 to 1 over 1.15s) and a pair of seeded random numbers, so frame N is always identical:

```js
const rnd = (i, s = 1) => { const x = Math.sin(i * 127.1 + s * 311.7) * 43758.5453; return x - Math.floor(x) }
const a = rnd(i, 7) * Math.PI * 2, sp = 300 + rnd(i, 8) * 420           // angle and reach
x = CX + cos(a) * sp * eo(u)                                          // radial: fast then slowing (ease-out)
y = CY + sin(a) * sp * eo(u) + 500 * u * u                            // plus gravity: a parabola
opacity = 1 - u * u; rotate = u * 720 * rnd(i, 9)
```
Because radial distance uses ease-out and gravity uses `u^2`, the pieces first fan out, then drop. They are hidden outside `0 < u < 1`.

## Numbers that matter
| | |
|---|---|
| Pieces | 26, 14px (`14 * K`), shape alternates, colours `#2f6bff #ffd23d #ff2e97 #38bdf8 #1f8f3e` |
| Duration | 1.15s from the voice word |
| Reach | 300 to 720px, angle random over 360 degrees |
| Gravity | `500 * u^2` px |
| Fade | `1 - u^2` |
| Spin | up to 720 degrees |

## Sound
A run of 16 high pops (1500 to 2400Hz, 0.11s, quiet, panned left and right) over 0.5s starting at the burst.

## Adapt it
- Count, colours and sizes.
- Reach and gravity: raise gravity for a heavier fall.
- Origin point: the centre of the card or button that triggered it.
- Duration.

## Files
- `code/demo.html` runs on its own.
