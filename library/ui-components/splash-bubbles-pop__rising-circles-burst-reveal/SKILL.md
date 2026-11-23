---
name: splash-bubbles-pop-rising-circles-burst-reveal
description: "A splash screen where soft bubbles rise from the bottom, grow and pop one by one with a ring and droplets, revealing the wordmark letter by letter. Use for an app launch screen or a brand intro."
---

# Splash bubbles pop

**Code name:** Rising circles burst reveal. Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
A deep navy-to-teal screen with a glow at the bottom edge. 22 glass-like bubbles (a pale rim, an inner highlight arc) rise from below the frame with a gentle sway, growing as they go. Four of them are key bubbles that rise to the position of the letters of "Acme" and pop at 2.3, 2.85, 3.4 and 3.95s; each pop is an expanding ring plus nine droplets that fall with gravity, and the letter springs in at that spot with a cyan glow. The other 18 pop at seeded times between 1.1 and 4.7s. The line "Say hello to something new" fades in at 4.5s and everything fades out 6.0 to 6.6s.

## When to use it
App launch or onboarding intro, a playful brand reveal, kids, wellness or cleaning products. Wrong for serious finance.

## How it works
Each bubble is `{x, y0, ty, b, tp, r0, r1, sw}`: born at `b`, pops at `tp`. Between them `p = seg(t, b, tp)`, `y = lerp(y0, ty, 1 - (1-p)^1.7)`, `r = lerp(r0, r1, eo(p))`, `x = x0 + sin(2.3t + ph) * sw * (1 - 0.7q)`. After `tp` the same object draws a pop from `age = t - tp`. Letter x positions come from `measureText`, and key bubble j targets letter j, so the reveal is tied to the pops. Seeded hash, no `Math.random`.

## Numbers that matter
| | |
|---|---|
| Timeline | key pops 2.3 / 2.85 / 3.4 / 3.95s, tagline 4.5s, exit 6.0-6.6s |
| Bubbles | 4 key (r 22 to about 110) + 18 decor (r 10-22 to 26-78) |
| Pop | ring to 1.75x radius over 0.5s, 9 droplets over 0.7s |
| Wordmark | 800 weight, 250px (210 tall), spring(6, 12) |

## Sound
Soft water bloops on each pop, a pitched-up sequence across the four letters, airy bed.

## Adapt it
- `WORD` and the tagline text.
- `NB` for more or fewer extra bubbles.
- The pop times `tp = 2.3 + 0.55 j` for pace.
- The gradient colours for another mood.

## Files
- `code/demo.html` runs on its own and loops in 6.8s; wide 1920x1080 or `?w=1080&h=1920`.
- `media/poster.jpg`
