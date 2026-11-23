---
name: card-burn-particle-dissolve-noise-edge-ember-sparks
description: "A dark stage with a gradient story card that burns away from the bottom up along a jagged noise edge, a hot white-to-orange rim, embers and sparks rising, then reforms. Use for a dramatic delete, expire or reveal moment."
---

# Card burn particle dissolve

**Code name:** Noise edge ember sparks. Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
A 620x820 gradient card (purple to pink to orange) with story progress bars, an avatar, the title "My story" and two lines of text sits on a near-black stage. At 0.7s a burn line starts at the bottom edge and rises to the top by 2.3s. Below the line the card is gone; just above it is a 10px white-yellow rim, then 20px of orange blended into the card, then 60px of dark char fading back to the card colour. Under the line a soft orange glow hugs the missing area. Roughly 300 embers (soft round dots) and sparks (short streaks) are born where the line crosses them and drift up and sideways for 0.7 to 1.7s, fading from yellow to red. The stage gets a faint warm light that follows the line. The card is empty from 2.3 to 3.1s, then reforms from the top down with the same rim, 3.1 to 4.6s, and rests whole until the loop at 5.6s.

## When to use it
Deleting or expiring a story, post or message; a dramatic reveal that burns one screen away to show the next; "this disappears" moments. Wrong for calm or trustworthy finance screens.

## How it works
Per frame the card (drawn once to an offscreen canvas) is copied pixel by pixel into an ImageData. Each pixel gets a seeded fractal value noise (three octaves with 130, 48 and 22px cells, built from an integer hash, never `Math.random`) and a signed distance to the burn line:
```js
s = (cardBottom - y) + (noise - .5) * 0.34 * cardH - front     // front = lerp(-.3, 1.3, p) * cardH
s < 0   -> burnt: orange glow, alpha (1 + s/50)^2 * .6
0..10   -> white-yellow rim;  10..30 -> orange mixed into the card;  30..90 -> char fading out
```
Each particle picks a card pixel from the seeded hash, computes the time the line reaches it (`B0 + p*(B1-B0)`, p from the same formula), and from then on is a pure function of its age. Embers are drawn as two additive circles (glow and core), sparks as short lines along their velocity. The reform runs the same progress backwards with `eio`.

## Numbers that matter
| | |
|---|---|
| Timeline | burn 0.7 to 2.3s linear, empty to 3.1s, reform 3.1 to 4.6s ease in-out, hold to 5.6s |
| Card | 620x820 (720x980 tall), radius 48 |
| Noise | amplitude 0.34 of card height, cells 130 / 48 / 22px |
| Rim | 10px white-yellow, 20px orange, 60px char, 50px glow below |
| Particles | 300, 30% sparks, life 0.7 to 1.7s, rise 140 to 560px/s |

## Sound
Crackle bed with a low whoosh under the sweep; a few high ticks for sparks.

## Adapt it
- `B0`, `B1`, `R0`, `R1` for speed; drop the reform to make a one-way burn.
- The three colours in the rim branches for a cold (blue) or magic (violet) burn.
- `AMP` for a rougher or straighter edge; the noise cell sizes for bigger bites.
- The card art block, and `NP` for more or fewer embers.

## Files
- `code/demo.html` runs on its own and loops in 5.6s.
- `media/poster.jpg`
