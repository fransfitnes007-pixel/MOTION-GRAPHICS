---
name: readiness-meter-gauge-arc-fill-needle-spring
description: "A semicircular gauge fills from the left with a red-to-green gradient while a needle sweeps, springs past 82 and settles; a big number counts up and a Ready pill fades in, then it drains for the loop. Use for scores, readiness and health meters."
---

# Readiness meter gauge

**Code name:** Arc fill needle spring. Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
A 760px-wide half-circle track with 41 tick marks and 0, 50 and 100 labels fades in. From 1.0 to 3.2s a conic-gradient arc (red, amber, green) fills from the left while a white needle on a metal hub sweeps with it; the needle then overshoots 82 by about 5 points and settles by 4.2s. The number below counts 0 to 82 over the same fill and "Readiness score" sits under it. At 3.4s a green pill with a check and the word Ready springs in. The pill fades 5.0 to 5.5s, and from 5.3 to 6.4s needle, arc and number drain back to 0.

## When to use it
Credit or health scores, setup completeness, battery or signal readiness, an assessment result. Wrong where the number matters more than the shape (use a stat tile).

## How it works
Arc fill and number share one eased value; the needle adds a decaying sine so it springs past:
```js
needle = (0.82 * eo(seg(t, 1.0, 3.2)) + 0.05 * sin(ov * pi * 2.4) * (1 - ov)^1.5) * drain
fill   = min(needle, 0.82)
```
The fill uses `createConicGradient(pi, cx, cy)` so the colours are locked to the arc position, not to its length. `drain = 1 - eio(seg(t, 5.3, 6.4))` multiplies everything on the way out.

## Numbers that matter
| | |
|---|---|
| Timeline | appear 0.1-0.7s, fill 1.0-3.2s, label 3.4s, drain 5.3-6.4s |
| Gauge | radius 380 (360 tall), stroke 58, 41 ticks |
| Value | 82, overshoot 0.05 of full scale |
| Colours | #ff5a5f, #ffb020, #3fe08a |

## Sound
Rising synth sweep tied to the fill, a tick burst on the overshoot, a soft confirm tone on Ready.

## Adapt it
- `VAL` for your score and the label text.
- Conic stops for another colour story.
- The `.05` overshoot amount and `T0`, `T1` for pace.
- Drop the drain for a one-way reveal.

## Files
- `code/demo.html` runs on its own and loops in 6.8s; wide 1920x1080 or `?w=1080&h=1920`.
- `media/poster.jpg`
