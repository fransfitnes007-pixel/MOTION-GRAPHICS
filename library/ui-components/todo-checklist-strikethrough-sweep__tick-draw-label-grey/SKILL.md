---
name: todo-checklist-strikethrough-sweep-tick-draw-label-grey
description: A minimal checklist where completing a row draws the tick and wipes a strike-through over the label. Reach for it for onboarding checklists, walkthrough steps and task lists.
---

# Todo checklist with strike-through sweep

**Code name:** Tick draw label grey.

## What you see
Three rows on a near-white page: a small light-grey rounded checkbox and a black label, "Complete documentation", "Review pull requests", "Update dependencies". A cursor clicks each checkbox in turn at about 0.8s, 1.7s and 2.5s. On a click, a thin dark tick draws into the box in about 0.2s, and a strike-through line runs across the label from left to right in about 0.3s while the text fades from black to mid-grey. Done rows stay grey with the line through them. After a pause the demo clicks the three again to undo, and the line retracts right to left.

The component also has swipe actions with complete and delete buttons, driven by the `showActions` and `onShowActions` props in the usage code. Those do not appear in the preview, so the demo does not include them.

## When to use it
Onboarding or dashboard walkthrough checklists, setup steps, simple task lists. The strike sweep gives a clear reward for a click without needing colour. For a list with drag and swipe, the original component's swipe actions would be the next layer.

## How it works
Each row has a tick (an SVG path drawn with `stroke-dashoffset`), a label, and a separate 3px line the same width as the label (measured once) whose width goes from 0 to the label width. All three follow one eased progress per row, started by the click time. The label colour is interpolated from `rgb(17,17,17)` to `rgb(156,156,175)`.

```js
tick.dashoffset = 1 - eo(seg(t, t0, t0+.18))
strike.width    = labelWidth * eo(seg(t, t0+.06, t0+.36))
label.color     = lerp(#111, #9c9caf, a)
```

The line is a real element rather than `text-decoration`, because `text-decoration` cannot animate its length.

## Numbers that matter
| | |
|---|---|
| Rows | 74px apart, label 33px, checkbox 34px with 9px radius |
| Tick | 2px stroke, draws in .18s |
| Strike | 3px, `#9ca3af`, sweeps in .3s starting .06s after the click |
| Text | `#111` to `#9ca3af` |
| Timing | check 0.8 / 1.7 / 2.5s, undo 3.7 / 4.0 / 4.3s, loop 5.4s |

## Sound
Silent.

## Adapt it
- `items`: the labels.
- `clicks`: when each is ticked or undone.
- `tickSec`, `strikeSec` for faster or slower.
- `done` for the completed colour; a brand colour tick is a one-line change in the SVG stroke.

## Files
- `code/demo.html` runs on its own and loops. Everything is read from the `CONFIG` object at the top of the script.
- `media/poster.jpg` is one frame of it.

## Credit
Idea: "Todo List Item" by serafimcloud on 21st.dev (https://21st.dev/@serafimcloud/components/to-do-item), MIT. This demo is an original recreation written from the public preview.
