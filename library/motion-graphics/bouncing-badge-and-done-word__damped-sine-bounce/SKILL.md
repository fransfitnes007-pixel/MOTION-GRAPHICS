---
name: bouncing-badge-and-done-word-damped-sine-bounce
description: "A round badge bounces on a soft shadow with a slight wobble while a bold word springs in beside it. Reach for it as the payoff beat after a step has been completed."
---

# Bouncing badge and done word

**Code name:** Damped sine bounce with shadow.

## What you see
The popup is gone. A round chrome badge that sat higher in the frame drops to a point lower down and at once starts to bounce. It jumps about 120px, falls back, jumps about 60px, then 30px, each hop shorter than the last. Directly under it a soft grey oval shadow shrinks and fades when the badge is high and returns to full size and opacity when it lands. Throughout, the badge tilts left and right by up to 8 degrees, and at the start it is 30% bigger than normal and eases back to size. To the right a bold dark phrase, "And done..!", springs up out of a lower, smaller start.

## When to use it
The payoff of an action: "launched", "sent", "all set". It gives the video a bit of play after the stiffer UI. It works with any compact mark or icon. It is wrong when the badge is a serious logo in a formal video; the wobble makes it a mascot.

## How it works
`Math.abs(Math.sin(...))` makes a series of bounces off the floor, and an exponential multiplies it down:

```js
const bounce = Math.abs(Math.sin(dt * 7)) * Math.exp(-dt * 1.6) * 120      // dt = seconds since the cut
badge.top = baseY - bounce
shadow.scale = 1 - bounce / 300; shadow.opacity = .9 - bounce / 200            // shadow reacts to the same value
badge.transform = `scale(${1.3 * dq + (1 - dq) * .8}) rotate(${Math.sin(dt * 5) * 8}deg)`
```
`dq = spring(seg(t, done, done + .5), 8, 12)` drives the badge's scale (it goes from .8 to 1.3, so the badge ends 30% bigger than it started) and the word's rise. The wobble `sin(dt * 5) * 8` is not damped. In the original timing the scene ends at 0.94s, before that shows. The demo runs 1.7s past the cut, so you will see the wobble continue while the hops fade; to damp it, multiply by the same `exp`.

## Numbers that matter
| | |
|---|---|
| Bounce | `abs(sin(dt * 7))`, decay `exp(-dt * 1.6)`, height 120px |
| Shadow | 220x40 oval, blur 10px, scale `1 - bounce/300`, opacity `.9 - bounce/200` |
| Badge | 170px, scale 1.3 at rest after the spring, wobble 8 degrees at 5 rad/s |
| Word | 96px bold `#0b0b10`, the same pop-in as the LED word: spring k8 f12 over .5s, rises 30px, scale .7 to 1 |

## Sound
Three small pops on the beat, 700Hz, 900Hz and 1100Hz, 0.12s apart, each about a tenth of a second long: they step up with the bounces.

## Adapt it
- Bounce height (120) and decay (1.6): higher decay gives a single hop.
- Wobble amplitude and rate.
- The mark, and where the word sits.
- The word and its colour.

## Files
- `code/demo.html` runs on its own. The badge is a chrome-gradient placeholder.
