---
name: anticipation-then-launch-pull-back-release
description: "A block pulls back against an elastic band (anticipation), holds with a tremble, then is released and flies to a target with stretch, overshoot and settle. Reach for it to make any hero move feel intentional by telling the viewer it is about to happen."
---

# Anticipation then launch

**Code name:** Pull back, hold, release. **From:** original build, neutral copy.

Original code; the move name follows the vocabulary catalogued by motionvideo.xyz.

## What you see
An indigo block sits on a line between two small posts, with a dashed target ring across the frame (left to right on wide, bottom to top on tall). From 0.05s everything springs in. At 0.95s the block drags backwards over one second (`eio`), squashing along its direction of travel to 78% and widening 12%, while an elastic band stretches into a V between the posts. At 1.95s it holds, trembling by 3px at about 15 Hz until 2.3s. At 2.3s it is released: it crosses the whole span in 0.26s, stretched up to 1.55x with up to four ghost copies trailing, hits the target ring (two shock rings expand), overshoots by about 10% and settles by 3.3s. The band snaps forward and wobbles out in half a second. Two captions swap: "Anticipation" then "Launch". At 3.95s all scales to nothing so the loop restarts clean.

## When to use it
Before any fast, big action: a card flying to its place, a number shooting up, a product launching into frame. The pull-back tells the eye where to look and makes the release feel earned. Skip it for small incidental moves, which just feel slow, and keep the hold under about 0.4s or the wait becomes the story.

## How it works
Position is one function of time along the launch axis `U` (`U = (1,0)` wide, `(0,-1)` tall), so one formula serves both layouts.

```js
// 0) pull back:  s = -D * eio(pr(t, 0.95, 1.0))   D = 22% of the span
// 1) hold:       s += 3 * sin(t*95) * pr(t, 1.95, 0.35)       // tremble
// 2) release:    s = lerp(-D, SPAN, spring((t - 2.3) / 1.2, 5.2, 7.2))
```
`spring(x,k,f)` is `1 - e^(-k x) cos(f x)`: it starts with a high speed (k) and overshoots by `e^(-k*pi/f)`, here about 10%. Stretch comes from speed, a numeric derivative of the same function: `stretch = clamp(v / 5000)`, then `scale along U = (1 - .22*pull) * (1 + .55*stretch)`. The band is a quadratic curve between the posts whose apex follows the block while pulled and then decays as `exp(-9 t) cos(34 t)`. Ghosts are the same block drawn at `t - n * .018`.

## Numbers that matter
| | |
|---|---|
| Pull | 0.95 to 1.95s, `eio`, distance 22% of span (about 236px wide) |
| Hold | 1.95 to 2.3s, 3px tremble |
| Squash while pulled | 0.78 along, 1.12 across |
| Release | `spring(x, 5.2, 7.2)` over 1.2s, first arrival at about 0.26s |
| Max stretch | 1.55 at about 5000 px/s |
| Band | 11px to 6px stroke, snap wobble `exp(-9t)cos(34t)` over 0.55s |
| Colours | block `#8b93ff` to `#3a2fb0`, band and rings `#a5b4fc` |

## Sound
A rising creak or rubber-band stretch under the pull, a short silence on the hold, a sharp whoosh at the release and a low thud with the shock rings.

## Adapt it
- `D` (pull distance) and the hold length: more pull for a bigger launch.
- The `spring` constants: raise `k` for a snappier take-off, lower `f` for a softer overshoot.
- `U` to launch at any angle; the block size `B`; the block face (the chevron is a placeholder).
- Drop the band and ghosts for a quiet version that keeps only squash, tremble and spring.

## Files
- `code/demo.html` runs on its own and loops.
- `media/poster.jpg`
