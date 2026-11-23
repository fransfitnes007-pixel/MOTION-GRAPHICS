---
name: verdict-chip-pop-spring-scale-rise
description: "A dark pill with a green check and the words \"Good to go\" pops up in the corner of a result screen with a springy overshoot and a green glow ring."
---

# Verdict chip pop

**Code name:** Spring scale rise.

## What you see
On a spoken cue word the chip rises 30px and scales from 60% to 100% with `spring(k=7, f=12)` over 0.58s, ending with a slight overshoot. It is a 34px bold white label on near-black (86% opacity) with a 30px green circle holding a white check. A green glow (`rgba(22,163,74,.55)`, 60px blur) and a 2px mint outline sit around it. It leaves with the window at 12.15s on the demo's timeline.

## When to use it
The payoff stamp on a result screen: approved, passed, verified, shipped. Put it where the eye lands after reading the result, bottom-right of the card. It is a stamp, not a toast: it does not move after landing.

## How it works
One spring drives scale, rise and fade-in together.

```js
const g = spring(seg(t, WT.live + .02, WT.live + .6), 7, 12)
S(chip, { opacity: clamp(g * 1.4) * (1 - out), transform: `scale(${.6 + .4 * g}) translateY(${(1 - g) * 30}px)` })
// spring(x,k,f) = 1 - exp(-k x) cos(f x)
```
`clamp(g * 1.4)` makes the fade finish early, before the overshoot, so the chip is solid while it bounces.

## Numbers that matter
| | |
|---|---|
| Chip | 800 34px, padding 16/28/16/18, gap 14px, radius 999px |
| Icon | 30px circle `#16a34a`, 18px white check |
| Shadow | `0 20px 60px -10px rgba(22,163,74,.55), 0 0 0 2px rgba(52,211,153,.6)` |
| Spring | k=7, f=12, 0.58s, scale .6 to 1, rise 30px |

## Sound
A soft rising pop as the chip lands (about 1.3 kHz with a pitch drop), quiet, under the voice.

## Adapt it
- The label and the icon colour (use red for "Needs work").
- `LIVE` time and the position.
- Spring k and f for a harder or softer landing.

## Files
- `code/demo.html`
