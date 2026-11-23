---
name: confetti-burst-random-pitch-pop-scatter
description: "A bright pop followed by sixteen quiet pops at random pitches and random left-right positions, like paper flying out. A payoff: money received, goal reached, checkout done."
---

# Confetti burst

**Code name:** Random-pitch pop scatter.

## What you hear
One brighter pop as the burst fires, then a quick scatter of sixteen soft pops spread over half a second, each at a different high pitch and a different place between the speakers. It sounds like sparkle or confetti. The demo then plays a wider burst of 32 pops, 22 ms apart.

## When to use it
A payoff: money received, goal reached, checkout done. It needs a visual burst to match; sound with no visual looks like a bug. It is wrong for a quiet or serious moment, and one burst per video is plenty.

## How it works
The same `pop()` as the word-reveal recipe, but every pitch and pan comes from a seeded random generator so the burst sounds the same each time you render it.

```python
put(fx, pop(1700), 20.7, .25)
for i in range(16):
    put(fx, pop(1500 + rng.integers(0, 900)), 20.72 + i * .03, .06, pan=rng.uniform(-.6, .6))
```

The recipe uses `numpy.random.default_rng(11)`, but the sequence of random numbers depends on everything drawn before it. Fix the seed and render once if you want the same burst every time.

## Numbers that matter
| | |
|---|---|
| Lead pop | `pop(1700)`, gain 0.25, 20 ms before the scatter |
| Scatter | 16 pops, 30 ms apart, gain 0.06 |
| Pitch | random 1500 to 2399 Hz |
| Pan | random -0.6 to +0.6 |
| Length of burst | 0.48 s |

## Sound
Plays after the counter ticks, at the moment the final number lands. Add a low impact if the moment is big.

## Adapt it
- Count (16) and spacing (0.03 s): a bigger count and tighter spacing for a larger burst.
- The pitch range: `1500 + rng.integers(0, 900)`.
- The pan width, `uniform(-.6, .6)`.
- The seed, to get a different but repeatable scatter.

## Files
