---
name: chapter-rail-progress-line-active-label-swap
description: "A numbered chapter indicator (01 LOOK 02 03 04 05) and a progress bar. Use it in longer explainers so the viewer always knows where they are."
---

# Chapter rail with progress line

**Code name:** Numbered rail with active-label swap and full-width progress bar.

## What you see
At the top left, in small capitals with wide letter-spacing, a row reads "01 LOOK  02  03  04  05". The numbers are lavender; the current chapter's whole entry is white and shows its name, the other four are dim grey and show only a number. When a new chapter begins, the white and the name jump to the next entry in one frame, so the row changes width. Along the very bottom a 4px indigo-to-lavender line grows from the left edge to full width across the video. A small round mark sits at the top right.

## When to use it
Videos longer than about 30 seconds that are organised in clear chapters: demos, walkthroughs, long explainers. It helps pacing: five chapters in 54 seconds. It does nothing for a 10-second spot. The jump is instant; pair it with a wipe so the change of state is hidden.

## How it works
Nothing is tweened. The current chapter is the last entry whose start time has passed:

```js
let ci = -1; CHAP.forEach((c, i) => { if (t >= c[2]) ci = i })
chapEls.forEach((c, i) => { const on = i === ci; c.style.color = on ? '#fff' : '#4a4a5e'; vis(c.nm, on) })
progress.style.width = (t / DUR * 1920) + 'px'
```

The rail fades in with `eo5` when the first chapter starts and fades out before the end card. The bar has no easing, so it is a clock.

## Numbers that matter
- Rail: left 112px, top 58px, 20px bold, uppercase, letter-spacing .14em, gap 22px.
- Colours: number `#a5b4fc`, active `#fff`, inactive `#4a4a5e`, rail default `#9b9bb3`.
- Bar: 4px high, `linear-gradient(90deg,#5b5ce6,#a5b4fc)`, width `t / DUR * 1920`.
- Demo chapters start at 7.44, 17.45, 31.45, 40.57 and 44.5s.

## Sound
Silent. Chapter changes are covered by the wipe whoosh (see the chapter wipe skill).

## Adapt it
- The chapter names and count; keep the times array in step.
- Colours (active, inactive, bar).
- Position of the rail and the mark.
- Fade the rail out before your end card.

## Files
- `code/demo.html` runs on its own and loops. The demo uses the system font stack; small labels would use your brand font. The mark is a CSS placeholder.
