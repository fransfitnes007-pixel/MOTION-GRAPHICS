---
name: weekly-schedule-glass-panel-back-pop-dots
description: "A frosted-glass panel slides up showing seven weekday cells; coloured square dots pop into each cell left to right with a bounce, two per day, to show a week filling with scheduled items."
---

# Weekly schedule glass panel

**Code name:** Back-ease pop dots.

## What you see
A 1200x200 glass panel (72% white, 24px backdrop blur, 30px radius) rises 80px into place at 15.47s on the demo's clock. Its header reads "This week" at left and a small grey summary at right. Below, seven rounded day cells in a grid, each labelled Mon to Sun. From 15.86s two 26px squares per day, one violet and one blue, scale in with an overshoot of about 25%. Days follow 0.06s apart; the second square of each day follows its first by 0.03s. The effect is a calendar filling left to right in about 0.8s.

## When to use it
Whenever the claim is "planned" or "scheduled": content calendars, shifts, deliveries. The dots are marker shapes, not content, so keep the labels short. It is a supporting element: it sits at the bottom while the headline says the word "schedule".

## How it works
A single `back()` ease (the overshoot curve) drives every dot's scale. The delay is a linear function of the day and the dot index.

```js
const back = (x, s = 1.9) => { const c3 = s + 1; return 1 + c3 * Math.pow(x - 1, 3) + s * Math.pow(x - 1, 2) }
const p = back(seg(t, SCHEDULE + i * .06 + k * .03, SCHEDULE + .3 + i * .06 + k * .03))
dot.style.transform = `scale(${clamp(p, 0, 1.25)})`
```
`clamp(p, 0, 1.25)` caps the overshoot so dots never look inflated. The panel's slide is `eo5` over 0.55s.

## Numbers that matter
| | |
|---|---|
| Panel | 1200x200, `rgba(255,255,255,.72)`, blur 24px, padding 26/34, radius 30px |
| Days | 7 columns, 14px gap, 100px high, cell `rgba(20,16,40,.05)`, radius 16px |
| Dots | 26px squares, radius 9px, `#8b5cf6` and `#4f7bff`, at left 14 and 48, bottom 14 |
| Timing | panel 0.55s; dots 0.3s each, 0.06s per day, 0.03s per dot |
| Overshoot | `back` s=1.9, capped at 1.25 |

## Sound
Silent. A light tick per day would suit it.

## Adapt it
- Day labels, number of columns and dots per cell.
- Dot colours (one per channel).
- `SCHEDULE`: the start of the fill.
- The `back` strength `s` for a gentler bounce.

## Files
- `code/demo.html`
