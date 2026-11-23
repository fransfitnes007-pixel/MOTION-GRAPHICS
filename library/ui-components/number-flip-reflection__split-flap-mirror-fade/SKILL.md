---
name: number-flip-reflection-split-flap-mirror-fade
description: "A big streak counter whose digits fold like split-flap cards on a glossy dark floor, with a faded mirror reflection flipping in sync below. Use for streaks, scores and milestone counters."
---

# Number flip with reflection

**Code name:** Split-flap flip with mirror fade.
Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
On a near-black stage a caption in tracked capitals, DAY STREAK, sits above three dark cards showing 1 2 8 in large white tabular figures, each split by a thin hinge line with side notches. The cards stand on a glossy floor: a thin highlight line at the horizon, a soft pool of light, and a mirror image of the digits below, faded to nothing over about 70% of its height and slightly blurred.
- 0 to .5s: the group fades and rises 24px into place.
- .9s, 1.7s, 2.5s, 3.3s: the value steps 128, 129, 130, 131, 132. A digit that changes flips in .62s: the top half folds down around the hinge, darkening as it goes, while the shadow deepens on the old bottom half; past halfway the new bottom half swings down from edge-on and lands with a small overshoot. 129 to 130 flips two cards at once.
- The reflection runs the same code, mirrored, so it flips in step.
- 4.4 to 4.8s: everything fades out, the value resets to 128 unseen, and the loop restarts from the fade-in.

## When to use it
A streak, score, level or milestone number that changes by one and should feel physical: habit apps, game results, countdown-to-launch videos. Wrong for numbers that change every frame, or where the digit count changes (the cards are fixed at three).

## How it works
Each digit is a card with perspective. It holds four half-height elements: a static top (new digit), a static bottom (old digit), a flap top (old digit) hinged at its bottom edge and a flap bottom (new digit) hinged at its top edge. Every half contains the full glyph, offset by half the card height, and is clipped by `overflow:hidden`.
```js
const a = seg(p, 0, .5), b = seg(p, .5, 1)
flapTop.transform    = `rotateX(${-90 * a * a}deg)`          // folds down, accelerating
flapBottom.transform = `rotateX(${90 * (1 - spring(b, 6, 9))}deg)` // swings in, small overshoot
flapTop.shade = .7 * a; staticBottom.shade = .7 * a; flapBottom.shade = .55 * (1 - eo(b))
```
The reflection is the same builder called a second time inside a wrapper with `transform: scaleY(-1)`, a `mask-image: linear-gradient(to top, ...)` fade, `opacity:.42` and `blur(1.6px)`, driven by the same `update(t)` so it cannot drift out of sync. Step times come from a `START` array, so the value is a pure function of `t`.

## Numbers that matter
| | |
|---|---|
| Steps | at .9, 1.7, 2.5, 3.3s; each flip .62s |
| Fold | top: `rotateX(0 to -90deg)` ease-in squared; bottom: `rotateX(90deg to 0)` with `spring(b,6,9)` |
| Card | 300 x 426px (270 x 383 tall), 28px gap, radius 9% of width, font 74% of card height |
| Reflection | `scaleY(-1)`, opacity .42, blur 1.6px, mask to transparent at 72% |
| Loop | 5s; fade-in 0 to .5s, fade-out 4.4 to 4.8s |

## Sound
Silent. A soft click per digit or tap, and a light chime on success, would fit.

## Adapt it
- `BASE`, `START` and `N`: starting value, step times, digit count.
- Card colours (`TOPBG`, `BOTBG`) and glyph colour for a light or branded version.
- Caption text ("Day streak") and the floor gradient.
- Reflection opacity and mask length for a glossier or subtler floor.

## Files
- `code/demo.html`
- `media/poster.jpg`
