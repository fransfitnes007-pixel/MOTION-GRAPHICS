---
name: skewed-bar-chapter-wipe-staggered-eio5
description: "A transition wipe of three parallel slanted bars in graded indigo, with the content swapping while they cover the frame. Use it between chapters of a longer video."
---

# Skewed bar chapter wipe

**Code name:** Three skewed bars sweeping across with eio5 stagger.

## What you see
A headline on the dark stage. At 1.0s three slanted bars, each 900px wide and taller than the frame, leave from beyond the left edge: first a mid indigo (#5b5ce6), then a lighter one (#7b7cf5) a tenth of the way behind, then a pale lavender (#a5b4fc). They cross the frame in 0.7s on a steep ease in and out, leaving at slightly different times so the front of the wipe is a stack of three stripes. While the frame is covered (around 1.38s) the content changes from "Start with a look." to "Then fill it in." and the new headline is there as the bars clear on the right.

## When to use it
Chapter breaks in a longer video, with the chapter rail updating behind the wipe. Six uses in 54 seconds is about the upper limit. Too heavy for short spots. The wipe must be covered by a whoosh, because it is loud visually.

## How it works
Each bar is a tall absolutely positioned div skewed -18 degrees. A single `wp` (0 to 1) drives all three with a stagger of 0.1 in the clamped input:

```js
const wp = (t - WIPE) / .7                                 // only while 0 <= wp < 1
BARS.forEach((b) => { const p = eio5(clamp(wp * 1.25 - b.i * .1))
  b.style.left = lerp(-1300, 2400, p) + 'px'; b.style.transform = 'skewX(-18deg)'; b.style.opacity = .95 - b.i * .1 })
```

The `1.25` factor makes the last bar (with its .2 delay) just finish at wp = 1. The content swap is an ordinary `vis` toggle timed in the middle of the wipe; the bars hide it. The layer is hidden (`display:none`) when no wipe is active.

## Numbers that matter
- Bars: 900px wide, top -300px, 1700px tall, skewX(-18deg); colours `#5b5ce6`, `#7b7cf5`, `#a5b4fc`; opacity .95, .85, .75.
- Travel: left -1300px to 2400px, `eio5`, duration 0.7s, stagger .1 on the input (times 1.25).
- Trigger: .35s before the first word of the next chapter.

## Sound

## Adapt it
- Bar colours and count (two or four bars work).
- Skew angle (-18 degrees) and direction; flip `lerp` ends to wipe right to left.
- `WIPE` and the swap time.
- Duration (0.7s).

## Files
- `code/demo.html` runs on its own and loops. The two headlines are placeholders.
