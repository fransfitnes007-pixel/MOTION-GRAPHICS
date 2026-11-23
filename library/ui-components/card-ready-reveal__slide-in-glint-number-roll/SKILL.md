---
name: card-ready-reveal-slide-in-glint-number-roll
description: "A neutral bank-style card slides up on a spring while tilting in 3D, a diagonal glint sweeps across it, the last four digits roll in like an odometer and a green Ready pill pops. Use for a card-issued, order-ready or activation moment."
---

# Card ready reveal

**Code name:** Slide in glint number roll. Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
On a dark stage a 780x480 slate-grey card ("Acme", a chip, three dot groups, a cardholder name and 12 / 29) rises from below the frame between 0.25 and 1.35s on a spring with overshoot, starting tilted 38 degrees back. Once it has arrived it keeps a small held tilt (about 5 degrees on X, 8 on Y, 1.2 on Z). A 150px diagonal white glint crosses it from 1.45 to 2.35s. From 1.9s four digit columns spin upward, 0.22s apart, each easing out over 1.1s to land on 4 8 2 1. At 3.35s a dark-green pill with a drawn check and the word Ready springs in under the card. The pill fades 5.3 to 5.7s and the card slides back down 5.6 to 6.3s.

## When to use it
Fintech or wallet onboarding, "your card is ready", order or ticket ready states. Wrong for anything that must feel instant.

## How it works
The card is DOM; per frame one `transform` is set on its wrapper: `perspective(1700px) translateY() rotateX() rotateY() rotateZ()`. The held tilt uses sines with a whole number of cycles per loop (`2*2pi*t/DUR`), so the loop closes. Each digit is a 72px-high column of 40 rows (0-9 four times) inside an overflow-hidden mask; the roll is `translateY(-lerp(0, 20 + digit, eo5(p)) * 72)`, so it passes two full turns before stopping. The glint is a skewed gradient div moved with `eio`. The check is an SVG path drawn with `stroke-dashoffset`.

## Numbers that matter
| | |
|---|---|
| Slide-in | spring(k 5.2, f 10) over 1.1s, from 62% of the screen height |
| Glint | 150px wide, 22 degrees, 0.9s, eio |
| Digits | 4 columns, 0.22s stagger, 1.1s eo5, 20 + d rows |
| Pill | spring(6.5, 12) at 3.35s, check draws in 0.4s |
| Card | 780x480, radius 38, perspective 1700px |

## Sound
Whoosh with a soft thud as the card lands, a fast ticker for the digits, a bright ding for Ready.

## Adapt it
- `DIG` for the four digits.
- The gradient and `.brand` text for your colours and name.
- `.pill` text and colours for another status.
- Tilt amplitudes in the `rx`, `ry`, `rz` lines.

## Files
- `code/demo.html` runs on its own and loops in 6.4s; wide 1920x1080 or `?w=1080&h=1920`.
- `media/poster.jpg`
