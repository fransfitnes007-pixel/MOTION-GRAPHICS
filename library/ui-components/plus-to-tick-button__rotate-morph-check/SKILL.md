---
name: plus-to-tick-button-rotate-morph-check
description: "A dark pill \"Buy for $6.99\" with a round plus icon. A tap rotates the plus 45 degrees while it morphs into a check mark, the label crossfades to \"Added\", and the pill flashes green with a small scale bounce. Use for add-to-cart, add-to-list and quick purchase confirmations."
---

# Plus to tick button

**Code name:** Rotate and morph to check. **From:** original build for this library.
Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
Dark stage, a 820x170 near-black pill with a 118px round icon on the left, `Buy for $6.99` in 52px semibold. A finger taps at .9s. The plus rotates to 45 degrees (a spring) while its two strokes move into the three points of a check, the second stroke finishing slightly later so it reads as drawn. The label slides up 10px and fades to `Added` between 20% and 60% of the move. The pill tints green and glows (peak at about 1.35s) and bounces to 1.055 scale and back; then it settles, still showing the check. At 3.3s a second tap reverses it to the plus and `Buy`.

## When to use it
One-tap commit actions with immediate confirmation, where the state change should be visible without a new screen. Wrong for destructive or multi-step flows.

## How it works
Both icon strokes are single lines. Their endpoints are the plus endpoints rotated by an angle that grows to 45 degrees, then lerped to the check points: the first stroke to (A,B), the second to (B,C). Because a plus rotated 45 degrees is an X, whose two strokes already point along the check's two directions, the morph reads as the plus turning into the tick. The second stroke eases with a delay (`k2`) so the long arm seems to be drawn out.
```js
p0 = rot(-20,0,th); a0 = lerp(p0, A, k1); b1 = lerp(rot(0,-20,th), C, k2)
```

## Numbers that matter
| | |
|---|---|
| Pill | 820x170, `#1c1c24` |
| Rotation | 0 to 45 degrees, spring k5 f9 over .55s |
| Label swap | 20% to 60% of the morph, 10px |
| Flash | green `#1b5e34` tint plus glow, sine over .87s |
| Bounce | +5.5% scale over .45s, 3.5% dip while pressed |
| Taps | .9s and 3.3s, loop 5s |

## Sound
A soft tap, then a bright two-note chime as the check lands.

## Adapt it
- Label strings and the width of the pill.
- Flash colour and strength.
- Check points `A`, `B`, `C`.
- Hold time on `Added` (3.3s second tap).

## Files
- `code/demo.html` runs on its own and loops in 5s.
- `media/poster.jpg`
