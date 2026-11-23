---
name: photo-to-illustration-flip-3d-flip-style-swap
description: "A card showing a soft photo-style scene flips in 3D to reveal the same scene as a flat line illustration; the flip overshoots and settles and a tap flips it back. Use for before/after, style-swap and filter previews."
---

# Photo to illustration flip

**Code name:** 3D flip style swap. Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
An 860x600 card shows a "photo": a blue-to-peach sky, a blurred sun with bloom, soft clouds, three layered green hills, a dark vignette and faint scan grain. A simulated finger taps the card at 0.78s (ripple). The card flips about Y from 0.88 to 2.0s on a spring that passes 180 degrees by about 14 degrees and settles, lifting toward the viewer and tilting a few degrees mid-turn while its floor shadow narrows. The back is a cream-paper flat illustration of the same scene: a flat-yellow sun with rays, an outlined cloud and three flat-filled hills with hatching. The Photo / Illustration switch below follows the angle. A second tap at 3.95s flips it back, ending at 5.1s.

## When to use it
Before/after, photo-to-art filters, "see it as an illustration" previews, any two-state card. Wrong when the two sides are not the same composition.

## How it works
`.flip` has `transform-style: preserve-3d`; both faces use `backface-visibility: hidden` and the back is pre-rotated `rotateY(180deg)`. The angle is a difference of two springs:
```js
ang = 180 * (spring(seg(t, .88, 2.0), 8, 10) - spring(seg(t, 4.05, 5.15), 8, 10))
```
`spring(x, 8, 10)` peaks near 1.08, which is the 14 degree overshoot. Lift is `translateZ(90 * sin(pi * |ang| / 180))` and a 6% scale. Hills are ellipses in both faces from one geometry table, so the scenes line up.

## Numbers that matter
| | |
|---|---|
| Timeline | tap 0.78s, flip 0.88-2.0s, tap 3.95s, back 4.05-5.15s |
| Card | 860x600, radius 36, perspective 2000px |
| Spring | k 8, f 10 (about 8% overshoot) |
| Mid-flip | translateZ 90px, scale +6%, tilt -5 degrees |

## Sound
A soft paper whoosh at the flip and a tiny tap on each press.

## Adapt it
- `HILLS`, the colours in `HG` and the sun position for your scene, or drop your own art into each face.
- Spring `k` and `f` for more or less overshoot.
- `TAP1`, `TAP2` for pacing.
- The switch labels.

## Files
- `code/demo.html` runs on its own and loops in 6.4s; wide 1920x1080 or `?w=1080&h=1920`.
- `media/poster.jpg`
