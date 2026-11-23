---
name: distance-wheel-drag-fill-dial-rotate-arc-progress
description: "A circular dial with tick marks that a finger drags around; the dial turns with inertia, an arc fills in proportion, the centre number counts km and a haptic-style bounce lands on every 5 km step. Use for goal, distance or amount pickers."
---

# Distance wheel drag fill

**Code name:** Dial rotate arc progress. Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
A 720px dark dial with 50 ticks (a longer one every 5, a label every 10) sits inside a thin progress ring, the pointer at the top. A translucent finger lands on the lower left of the dial at 0.9s and drags clockwise to 4.0s, covering 270 degrees. The dial lags the finger and swings slightly past on a spring, so it keeps turning after the finger lifts. The outer ring fills clockwise in cyan to violet in step with it, the big number counts from 0 to 37 km, and each time the reading crosses a multiple of 5 the pointer kicks 7px and the number pulses 6% with a quick damped wobble. At 5.9s the dial turns back to 0 for the loop.

## When to use it
Goal setting (distance, calories, minutes), volume or budget dials, fitness onboarding. Wrong for precise numeric entry.

## How it works
The finger sets a target angle `fingerRot(t)`; the dial angle is a spring following it, integrated with a fixed 1/240 s step from t = 0 on every call (still a pure function of t, and cheap):
```js
a = w*w*(target - x) - 2*z*w*v   // w 15, z 0.5
```
Kilometres are `x / 7.2 degrees`. While stepping, the times when `floor(km / 5)` changes are recorded; the bounce is `sum(exp(-11 d) * sin(42 d))` over crossings less than 0.6s old. Tick k sits at `-k * 7.2` degrees, so a clockwise turn raises the reading.

## Numbers that matter
| | |
|---|---|
| Timeline | drag 0.9-4.0s (eio), back 5.9-6.5s |
| Dial | radius 360 (340 tall), ring +46, 50 km per turn |
| Spring | w 15, z 0.5, dt 1/240 |
| Bounce | exp(-11 d) sin(42 d), 0.6s, pointer 7px, number 6% |

## Sound
A tick per kilometre that sharpens on every fifth, a low haptic thump on the 5 km marks.

## Adapt it
- `KM_MAX` and the 37.5 target in `A_END`.
- Spring `w` and `z` for more or less inertia.
- The unit text and labels.
- Conic gradient stops for the ring.

## Files
- `code/demo.html` runs on its own and loops in 7.2s; wide 1920x1080 or `?w=1080&h=1920`.
- `media/poster.jpg`
