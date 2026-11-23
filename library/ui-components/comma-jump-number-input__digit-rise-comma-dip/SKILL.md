---
name: comma-jump-number-input-digit-rise-comma-dip
description: "A huge white dollar amount typed digit by digit from a number pad. Each digit rises in with a spring, commas dip and slide when a new thousands group appears, and past $1,000,000 the grey line crossfades to a red warning. Use for payment, transfer or top-up amount screens."
---

# Comma-jump number input

**Code name:** Digit rise and comma dip. **From:** original build for this library.
Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
Dark stage. A 200px bold white `$0` sits centred with a small grey converted line (`≈ 0.00 units`) under it and a 3x4 number pad below. From 0.5s a simulated finger taps 1 to 7 every .28s. Each new digit rises about 0.6em from below with a spring and fades in over .25s while the existing characters slide to their re-centred positions. When the 4th digit lands (`$1,234`) a comma appears and dips about .17em for .6s while sliding; the same happens at the 7th. At `$1,234,567` the grey line crossfades (.35s) to red "Not enough balance". At 3.4s the delete key is tapped every .22s: digits drop and fade out, commas dip as they vanish, the red line returns to grey, and the amount ends on `$0` so frame 6s meets frame 0.

## When to use it
Any screen where a user types a money value: send, buy, top-up, tip. The comma motion tells the eye the grouping changed. Wrong for decimals-heavy input or very long numbers (the centred layout would shift constantly).

## How it works
Every character is its own absolutely positioned element with a fixed-width box (tabular figures). `lay(n)` returns centred x positions for n digits and the commas that go with them. On each key event the previous and current layouts are known, so each element is either kept (x lerps from old to new on a spring), entering (rises from below, fades in) or exiting (drops, fades out). Commas are identified from the right, so the comma 3 digits from the end keeps its identity as digits are added.
```js
x = lerp(lp.d[i], lc.d[i], spring(seg(t, ev.t, ev.t+.7), 6, 10))
dip = commaCountChanged ? F*.17*Math.sin(Math.PI*seg(t, ev.t, ev.t+.6)) : 0
```

## Numbers that matter
| | |
|---|---|
| Type size | 200px (x .74 in tall), weight 700, -.02em |
| Digit rise | .6em, spring k7 f12 over .55s, opacity in .25s |
| Layout slide | spring k6 f10 over .7s |
| Comma dip | .17em down and back, .6s sine |
| Warning crossfade | .35s ease in out at 7 digits |
| Taps | typing every .28s from .5s; deleting every .22s from 3.4s |
| Loop | 6s |

## Sound
A soft key tick per tap, a slightly lower thud for delete, and a short low buzz when the warning appears.

## Adapt it
- `DIGITS` and the thresholds (`n >= 7`) for the limit.
- Message text and red `#ff453a`.
- `F` (size) and the `.17` dip depth.
- Remove the pad and the finger to use it as a bare readout.

## Files
- `code/demo.html` runs on its own and loops in 6s.
- `media/poster.jpg`
