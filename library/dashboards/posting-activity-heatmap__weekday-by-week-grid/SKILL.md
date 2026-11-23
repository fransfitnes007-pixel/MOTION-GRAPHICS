---
name: posting-activity-heatmap-weekday-by-week-grid
description: "An eight-week, seven-row grid of small rounded cells: dark when empty, violet that deepens with the number of posts that day, blank for days still to come. Use it for streaks and cadence."
---

# Posting activity heatmap

**Code name:** Weekday by week grid with count-tinted cells.

## What you see
A small card "Posting activity, Posts per day, last 8 weeks." with Mon to Sun labels down the left in 9px grey and eight columns of 12px cells. In the demo the cells fill week by week from the left over about four seconds while a counter at the bottom ticks up ("51 posts tracked"); the last column stops after Wednesday because the rest of the week has not happened.

## When to use it
Cadence and consistency: posting, commits, check-ins. The ramp makes a busy stretch obvious. The app draws it statically; the fill sequence is a demo addition for video.

## How it works
One column per week (flex-1, 2px between cells, 4px between columns), seven cells per column. Each cell is `h-[12px] rounded-[3px] border border-white/5`:

```js
background: c.future ? 'transparent'
  : c.n ? `rgba(139,92,246,${0.25 + 0.75 * (c.n / activity.max)})`
  : 'rgba(255,255,255,0.04)'
```

The grid is built from `posts` grouped by day (`dayKey`), with Monday as row 0 and the current week as the last column; `activity.max` is the busiest day, so the strongest violet always appears somewhere. In the demo a progress value walks the cells in column order and counts the fills.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Cell 12px high, radius 3px, border 5% white; gaps 2px rows, 4px columns.
- Alpha 0.25 for one post up to 1.0 for the maximum.
- Weekday labels 9px, line height 14px.
- Fill sweep 4.2s (demo).

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- The seeded counts: change the `R()` thresholds to make it sparse or full.
- Colour: any rgb in the cell formula.
- Number of weeks: add columns; the cells flex.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
