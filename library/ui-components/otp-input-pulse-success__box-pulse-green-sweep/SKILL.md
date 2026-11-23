---
name: otp-input-pulse-success-box-pulse-green-sweep
description: "Six code boxes take typed digits with a pop, the active border pulses, then a green fill sweeps left to right and a check draws. Use for verification and sign-in code screens."
---

# OTP input pulse and success fill

**Code name:** Box pulse and green sweep.
Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
A light stage with the heading Enter your code, a grey line of help text, and six white rounded boxes with soft shadows.
- 0s: the first box is active: blue border, a pulsing blue halo (1.5 pulses a second) and a blinking caret (2 blinks a second).
- .9, 1.3, 1.7, 2.1, 2.5, 2.9s: digits 4 8 2 9 1 7 appear one per box. Each pops from 50% to full size with a spring overshoot, and the active state hands over to the next box in .18s.
- 3.15s: a green fill wipes through the boxes from left to right, each box starting .1s after the last and taking .42s; digits turn white, borders turn green, each box bumps 5% as its fill passes.
- 3.95 to 4.65s: a green circle springs in under the boxes and a white check draws itself, then Code verified fades in.
- 5.15 to 5.65s: fills, digits and badge fade out; the first box becomes active again for the loop.

## When to use it
Sign-in, two-factor and verification screens, or any ad that needs to show a code being accepted. Wrong for codes of variable length, or for showing a failed attempt (swap the green for red and add a shake).

## How it works
All state is derived from `t` and the per-box times in `T`. Active strength for box `i` is `eo(seg(t, T[i-1], T[i-1]+.18)) * (1 - eo(seg(t, T[i], T[i]+.18)))`. The pulse is `.5 + .5 * sin(2 * PI * t * 1.5)`, which has a whole number of cycles in the 6s loop so frame DUR meets frame 0. The green fill is a gradient layer inside each box clipped with `clip-path: inset(0 X% 0 0)`, where `X = (1 - eo(seg(t, s0, s0 + .42))) * 100` and `s0 = 3.15 + i * .1`. The check is an SVG path with `pathLength="1"` and `stroke-dashoffset` driven by `eo(seg(t, 4.2, 4.65))`. Colours are mixed in RGB between grey, blue and green by the active and sweep amounts.

## Numbers that matter
| | |
|---|---|
| Digit times | .9, 1.3, 1.7, 2.1, 2.5, 2.9s; pop = `spring(x, 7, 13)` over .45s |
| Box | 150 x 180px, gap 24px, radius 20%, 3px border (130 x 156, gap 18 tall) |
| Active | border `#3478f6`, halo 4 to 11px at 14% opacity, caret 4px wide |
| Sweep | 3.15s start, .1s stagger, .42s each, ease-out cubic |
| Green | `#3ddc84` to `#1fb860` gradient, `#1fb860` border |
| Loop | 6s, clear at 5.15 to 5.65s |

## Sound
Silent. A soft click per digit or tap, and a light chime on success, would fit.

## Adapt it
- `CODE` and `N`: digits and box count (for a 4-digit PIN change `N` and the width maths follows).
- The blue and green values, or swap green for another brand colour.
- `T`: typing speed.
- Heading, help text and the success label.

## Files
- `code/demo.html`
- `media/poster.jpg`
