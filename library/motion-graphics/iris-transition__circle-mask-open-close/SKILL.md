---
name: iris-transition-circle-mask-open-close
description: "A circle mask that opens to reveal a scene, closes onto a subject and opens again on the next scene from the same point. Reach for it as a classic scene change that points the viewer at one object, or as an opening and closing frame."
---

# Iris transition

**Code name:** Circle mask open and close. **From:** original build, neutral copy.

Original code; the move name follows the vocabulary catalogued by motionvideo.xyz.

## What you see
Black frame. At 0.25s a circle opens from the centre and reveals scene one (indigo, a glowing sphere on the right, "Scene one") with a fast-then-slow ease (`eo5`), filling the frame by 1.3s. A thin white ring with a faint outer ring rides the edge of the circle while it is a visible shape. Scene one holds until 2.5s, then the iris closes: over 0.8s the circle shrinks with an accelerating ease (`eio5`) while its centre slides from the middle to the sphere, so the last thing you see is the sphere. At 3.3s the frame is black for 0.3s, and at 3.6s the circle opens again from the sphere's position onto scene two (orange to magenta, sphere in the same place). It holds from 4.6s, and from 5.3s it closes, travelling back to the centre, ending on black at 6s so the loop restarts cleanly.

## When to use it
Between two scenes that share a subject position, to point at the thing the next scene is about; as a film-style open and close; for retro or playful tones. Closing on the subject then opening on the matching point is the key: the cut hides in the black. It is wrong for modern, fluid UI stories where a morph or push reads better.

## How it works
Each scene is full-frame and shown through `clip-path: circle(r at x y)`. The radius is a fraction of the distance from the iris centre to the farthest corner, so any centre fully covers or empties the frame.

```js
const rmax = c => Math.max(hypot(c.x, c.y), hypot(W-c.x, c.y), hypot(c.x, H-c.y), hypot(W-c.x, H-c.y)) + 4
open:  r = rmax(P) * eo5(pr(t, 3.6, 1.0))
close: c = lerp(C, P, eio((t-2.5)/.8));  r = rmax(c) * (1 - eio5(pr(t, 2.5, .8)))
scene.style.clipPath = `circle(${r}px at ${c.x}px ${c.y}px)`
```
Opening eases out (fast reveal, slow settle) and closing eases in-out so it accelerates into the subject. The ring is a separate bordered circle at the same centre and radius, faded out near full size so it never crosses the frame edge.

## Numbers that matter
| | |
|---|---|
| Open A | 0.25 to 1.3s, `eo5`, from the frame centre |
| Close A | 2.5 to 3.3s, `eio5`, centre slides to the subject with `eio` |
| Black | 3.3 to 3.6s |
| Open B | 3.6 to 4.6s, `eo5`, from the subject |
| Close B | 5.3 to 6.0s, back to the centre |
| Subject | sphere radius 270px (240px tall), at 20% right of centre (wide) |
| Ring | 3px white at 85%, glow 40px, outer hairline 22px out |

## Sound
A short rising tone or swoop on the open, a falling one on the close, and a soft click or low thud in the black. A single drum hit at the full-open frame works too.

## Adapt it
- `P` for where the iris closes and opens, and `OR` for the subject size.
- The two `mk(...)` scenes: swap in your real frames.
- The durations and the 0.3s black gap; remove the gap for a direct iris cross.
- Remove the rings for a pure mask, or soften the edge with a radial-gradient mask instead of `clip-path`.

## Files
- `code/demo.html` runs on its own and loops.
- `media/poster.jpg`
