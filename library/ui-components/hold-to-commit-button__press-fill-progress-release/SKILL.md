---
name: hold-to-commit-button-press-fill-progress-release
description: "A black Hold to send pill with a finger: an aborted press springs back, a full hold fills left to right with a shimmer, pops and turns to Sent. Use for destructive or irreversible actions."
---

# Hold to commit button

**Code name:** Press fill progress and release.
Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
A wide black pill labelled Hold to send on a light stage, with a soft drop shadow. A translucent grey finger circle slides in from the lower right.
- .7 to 1.1s, aborted press: the finger presses (a ripple spreads, the finger shrinks 16%, the pill compresses 3.5%), a lighter fill grows from the left to about 27%, and a ring around the finger tightens.
- 1.1s: the finger lifts; the fill springs back to zero with a small overshoot and the pill rebounds. The finger drifts away and returns.
- 2.05s, full hold: the same press, but the fill keeps going at a steady 1.5s from empty to full, with a diagonal shimmer band sweeping across it. The ring tightens from 2.35 to 1.5 finger widths and thickens.
- 3.55s: the fill reaches the end. The pill pops (a damped scale bounce of about 8% and a short white flash), the label slides up out and Sent with a check that draws in .4s slides in.
- 3.7 to 4.2s: the finger leaves. 5.0 to 5.5s: the fill fades and the label returns to Hold to send.

## When to use it
Actions that should not fire by accident: sending money, publishing, deleting, ending a session. The aborted press up front teaches that a tap does nothing. Wrong for frequent, low-stakes actions, where a hold would feel slow.

## How it works
The fill is a layer whose width is `pw * f`, with `f` from a piecewise function of time: linear `(t - 2.05) / 1.5` while held, and `ABORT * (1 - spring(seg(t, 1.1, 1.7), 6, 9))` after the early release, clamped at zero. The press and release of the pill use one helper:
```js
const pr = (t, a, b) => t < a ? 0 : t < b ? eo(seg(t, a, a + .1)) : (1 - spring(seg(t, b, b + .55), 6, 10))
scale = 1 - .035 * (pr(t, .7, 1.1) + pr(t, 2.05, 3.55)) + pop
pop = .085 * exp(-6.5 * p) * sin(19 * p)      // p = t - 3.55
```
The shimmer is a skewed gradient bar whose left offset is `((t * 520) % (pw + 300)) - 200`, clipped by the fill. The check is a `pathLength="1"` stroke-dashoffset draw.

## Numbers that matter
| | |
|---|---|
| Fill time | 1.5s linear, empty to full |
| Aborted press | .7 to 1.1s, springs back over .6s |
| Pill | 960 x 210px (900 x 190 tall), compress 3.5%, pop 8.5% |
| Ring | 2.35 to 1.5 finger widths, border 2 to 5px |
| Fill colours | `#3d3d47` to `#6b6b79` on `#0b0b10` |
| Loop | 6s |

## Sound
Silent. A soft click per digit or tap, and a light chime on success, would fit.

## Adapt it
- The hold time (the 1.5 in `fillAt`) and the times of the two presses.
- Pill, fill and label colours; the labels Hold to send and Sent.
- Drop the aborted press by removing the first `pr`, `env` and `fillAt` branch.
- The finger design: size, border and the ripple.

## Files
- `code/demo.html`
- `media/poster.jpg`
