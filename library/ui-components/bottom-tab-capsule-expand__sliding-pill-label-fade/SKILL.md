---
name: bottom-tab-capsule-expand-sliding-pill-label-fade
description: "A floating dark tab bar with five grey line icons and a pale capsule that slides to each tab under a swiping finger, widening to fit the label that fades in. Use for app navigation with a few top-level sections."
---

# Bottom tab capsule expansion

**Code name:** Sliding pill label fade. Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
A dark rounded bar floats in the middle of a near-black stage with five line icons in grey: clock, search, bookmark, grid, gear. The first tab is selected: a pale capsule holds the dark icon and the label NEW. A translucent finger lands at 0.45s and swipes right. At 1.1, 1.8, 2.5 and 3.2s the capsule springs to the next tab (BROWSE, SAVED, LIBRARY, SETTINGS), widening to fit the new label; the old label fades out and the new one fades in a beat later, and the whole bar re-centres as its width changes. At 3.9s the finger swipes back to the start and the capsule sweeps all the way across in 0.75s. The finger lifts at 5.0s.

## When to use it
Floating bottom or top navigation with three to six sections. Wrong for tabs with long labels or more than six items.

## How it works
Each tab has a weight `w[i]`; the weights always sum to 1 and come from one spring per switch:
```js
u = spring(seg(t, ts, ts + .55), 9, 10); w[from] = 1 - u; w[to] = u
width[i] = SLOT + (gap + labelWidth[i]) * max(0, w[i])          // tabs widen with their weight
capsule.left  = sum(w[i] * left[i]);  capsule.right = sum(w[i] * right[i])
labelAlpha[i] = clamp((w[i] - .3) / .5)                          // old fades first, new appears after
```
Label widths come from `measureText` plus letter spacing. Icon colour mixes grey to dark with `w`. The bar is re-centred every frame from the summed widths. The finger path is eased between the capsule centres of each selected state.

## Numbers that matter
| | |
|---|---|
| Spring | `spring(x, 9, 10)`, 0.55s per step, 0.75s for the long return |
| Sizes | slot 104px, bar 128px, capsule 100px, icon 42px, label 28px bold, 0.08em tracking (x1.55 wide, x1.1 tall) |
| Colours | bar `#1d1d25` to `#15151b`, capsule `#f3f4f8` to `#dfe2ea`, icon grey `rgb(140 143 154)` |
| Finger | 96px, steps at 1.1 / 1.8 / 2.5 / 3.2s, return swipe 3.9 to 4.5s |

## Sound
A light tick as the capsule lands on each tab.

## Adapt it
- `names` and the `ICONS` path strings.
- `SW` times to slow or speed the swipe; drop the return to end on the last tab.
- Capsule and bar colours (invert for a light bar).
- Spring `k`/`f` for more or less bounce.

## Files
- `code/demo.html` runs on its own and loops in 5.6s.
- `media/poster.jpg`
