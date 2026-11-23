---
name: dark-stage-circle-reveal-clip-path-circle-wipe
description: "Between two light scenes, a near-black purple stage opens as a circle growing from an off-centre point until it fills the frame, then closes back down to the centre. It is the light-to-dark-to-light transition behind a product moment."
---

# Dark stage circle reveal

**Code name:** Clip-path circle wipe.

## What you see
The light grey stage with soft orbs is the default. At 8.18s a black-violet stage (a vertical radial gradient with a purple glow and a faint white dot grid) is revealed through a circle that grows from (1240,470) to a 1300px radius in 0.6s. The circle's edge is hard. At 12.18s it shrinks the other way over 0.44s, but now toward the frame centre (960,540), returning to the light stage.

## When to use it
To make one scene special: a dark "inside the machine" section in an otherwise light video, such as a scan, a terminal, a result. The circle gives direction, so put the circle's origin where the previous scene's action ended.

## How it works
Two full-frame layers, the light below and the dark above. The dark layer is clipped by a CSS `clip-path: circle(r at x y)` driven by one number.

```js
const dIn = eio5(seg(t, 8.18, 8.78)), dOut = eio5(seg(t, 12.18, 12.62))
const rD = dIn * (1 - dOut) * 1300
vis(bgD, rD > 1)
bgD.style.clipPath = `circle(${rD}px at ${dOut > 0 ? 960 : 1240}px ${dOut > 0 ? 540 : 470}px)`
```
The centre point jumps from the open point to the middle the instant the close starts; because the circle is still at its full 1300px (larger than the frame) nothing visible jumps. Anything that should appear only on the dark stage must be inside the dark layer, so it is clipped by the circle too. You can also swap a logo watermark from dark to light once `rD > 900`.

## Numbers that matter
| | |
|---|---|
| Open | `eio5`, 0.6s, from (1240,470) to r=1300 |
| Close | `eio5`, 0.44s, toward (960,540) |
| Dark fill | `radial-gradient(ellipse at 50% 40%, #1a1030 0%, #0a0812 55%, #050409 100%)` |
| Glow | 1500x1100 blurred orb `rgba(124,58,237,.38)`, drifting by sin/cos 60px and 40px |
| Dots | white at 7%, 1.3px, 34px grid |

## Sound
A whoosh peaks at the open (8.5s) and a bigger one at the close (12.42s). Drop the clap and half the hi-hats in the music while dark.

## Adapt it
- `T_IN`, `T_OUT` and the circle origin.
- The dark gradient and glow colour.
- Final radius: it must be at least the distance from the origin to the farthest corner.
- Use the same trick with `inset()` or `polygon()` for other wipes.

## Files
- `code/demo.html`
