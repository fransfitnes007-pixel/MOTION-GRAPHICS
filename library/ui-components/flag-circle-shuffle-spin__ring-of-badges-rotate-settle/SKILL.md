---
name: flag-circle-shuffle-spin-ring-of-badges-rotate-settle
description: "A ring of 12 round flag-style badges around a SPIN hub; a tap spins the ring with momentum while the badges swap places, and the one that lands on top scales up with a glow and a name label. Use for a country or region picker, a lucky-draw moment or a randomiser."
---

# Flag circle shuffle spin

**Code name:** Ring of badges rotate settle. Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
Twelve 108px round badges (two- or three-colour stripes, discs, crosses and quarters, no real flags) sit on a 350px-radius ring around a dark SPIN hub, popping in one after another from 0.05 to 1.0s. A simulated finger (translucent circle) glides to the hub, presses at 1.3s and ripples. From 1.35 to 4.1s the ring turns two full turns with fast-start momentum, leaving soft ghost trails; between 1.6 and 3.7s the badges also swap places, alternating inward and outward lanes so none collide. At 4.1s the badge that has reached the top springs up to 1.62x, gets a gold glow and a white ring, and a pill with its name pops under it. The ring fades out 5.7 to 6.3s for the loop.

## When to use it
Pickers, giveaways, "where are you from" steps, a reveal of one item out of many. Wrong when the result must look fair and the shuffle would confuse (data tables).

## How it works
Each badge i has a start slot i and an end slot `PERM[i]`. Position along the ring is a function of two eased values, the ring rotation and the shuffle:
```js
slot = i + (PERM[i] - i) * sh(t)                 // sh = eio(seg(t, 1.6, 3.7))
ang  = TOP + slot * 30deg + rot(t)              // rot = 4pi * (1 - (1-p)^3.5), p = seg(t, 1.35, 4.1)
r    = R + (i % 2 ? 1 : -1) * 46 * sin(pi * sh)   // inner/outer lanes while swapping
```
Because rot ends on a whole number of turns, slot 0 lands exactly at the top, and `WIN = PERM.indexOf(0)` is the badge that gets the highlight. Ghosts are the same badges drawn at `t - 0.026k` at low alpha while the ring is fast. Everything is a function of t, no state.

## Numbers that matter
| | |
|---|---|
| Timeline | pop-in 0.05-1.0s, tap 1.3s, spin 1.35-4.1s, shuffle 1.6-3.7s, land 4.1s, exit 5.7-6.3s |
| Ring | radius 350 (330 tall), 12 badges r 54, hub r 104 |
| Winner | 1 + 0.62 x spring(6, 12), glow radius 3.3x badge |
| Finger | 76px circle, ripple 34 to 120px over 0.6s |

## Sound
A soft tick per badge pop, a rising whoosh under the spin, a chime on the landing.

## Adapt it
- `PAL` and the six badge designs in `badge()` for your own flags or logos.
- `PERM` for a different shuffle; the landing badge follows `PERM.indexOf(0)`.
- `T0`, `T1` and the exponent 3.5 for a longer or snappier spin.
- `NAMES` for the label text.

## Files
- `code/demo.html` runs on its own and loops in 6.4s; wide 1920x1080 or `?w=1080&h=1920`.
- `media/poster.jpg`
