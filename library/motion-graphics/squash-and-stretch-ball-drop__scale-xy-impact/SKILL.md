---
name: squash-and-stretch-ball-drop-scale-xy-impact
description: "A glossy ball drops in stretched along its speed, squashes flat on the floor, bounces with decaying height and a live scale readout, then crouches and launches out the top. Reach for it to show how volume-preserving scale gives an object weight."
---

# Squash and stretch ball drop

**Code name:** Scale XY on impact. **From:** original build, neutral copy.

Original code; the move name follows the vocabulary catalogued by motionvideo.xyz.

## What you see
At 0s the frame is empty: a dark stage with a faint floor line two thirds down. The orange ball falls into view from above the top edge at 0.78s of free fall, stretched tall (scaleY about 1.42, scaleX about 0.84) because it is moving fast. At 0.78s it hits the floor, flattens to about 0.6 of its height for 0.14s while a dust ring spreads along the floor, then rebounds 381px high at the first bounce and stretches again on the way up and down. Six bounces follow, each lower and shorter (air time 0.94s, 0.56s, 0.34s, 0.20s, 0.12s). A pill under the floor shows the live scaleY and scaleX. At 3.6s the ball crouches (scaleY down to about 0.64), at 3.9s it releases and shoots up out of the frame by 4.3s, so the loop point is off screen.

## When to use it
Any object that needs weight or bounce: a dropped logo, a button landing, a ball in an explainer. It reads in one second and teaches the idea behind most good motion. It is wrong for rigid or heavy things (a safe, a phone) where you want almost no squash, and for UI where bounce feels toy-like.

## How it works
The ball is one element whose width and height are set every frame, with the bottom edge pinned to the floor so squash grows upward from the contact point. Stretch comes from speed, squash from contact, and the two are volume-preserving: when height scales by `sy`, width scales by `1/sqrt(sy)`.

```js
// flight: stretch along the direction of travel
sy = 1 + .42 * clamp(Math.abs(vy) / V0);  sx = 1 / Math.sqrt(sy)
// contact: a half sine of squash, deeper for harder hits
sq = .4 * Math.pow(v / V0, .55) * Math.sin(Math.PI * u);  sy = 1 - sq
// bounces: gravity G = 2*H0/T0^2, exit speed = 0.6 * arrival speed, air time = 2*E*v/G
```
Contact lasts `.04 + .1*sqrt(v/V0)` seconds, so hard hits stay down longer. The shadow is a radial gradient ellipse whose width and opacity follow the height. Because every number is a function of `t`, there are no timers: the bounce list is built once from the physics and `render(t)` looks up the phase.

## Numbers that matter
| | |
|---|---|
| Ball | 300px across (270px tall layout), radial gradient `#ffe2c4` to `#a31d2c` |
| Fall | 0.78s, g = 2*H0/0.78^2, start height off screen |
| Restitution | 0.6 per bounce |
| Stretch | 1 + 0.42 * speed/V0, capped at 1.42 |
| Squash | up to 0.4 at the first hit, power 0.55 of speed |
| Contact time | 0.04 to 0.14s |
| Crouch / launch | crouch 3.6 to 3.9s (to 0.64), launch 3.9 to 4.32s with `ei` |

## Sound
A soft thud on each contact, pitched down a little for the first hit and up for the small ones, plus a quick rising whoosh on the launch. Pair with the "hit on cut" sound recipe in the library.

## Adapt it
- `R` for the size, and the ball gradient for the brand colour.
- `E` (0.6) for bounciness: 0.4 is a dull thud, 0.8 is a super ball.
- The stretch (0.42) and squash (0.4) amounts; 0.2 is subtle, 0.6 is slapstick.
- Swap the ball for any element; keep the bottom pinned and the width at `1/sqrt(height)`.

## Files
- `code/demo.html` runs on its own and loops.
- `media/poster.jpg`
