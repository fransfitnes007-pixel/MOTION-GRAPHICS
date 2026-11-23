---
name: gantt-chart-resource-tree-progress-bars-today-line
description: "A white Gantt chart: resource tree on the left, week and day columns across, tasks as rounded bars with a darker progress fill, grouped phases as thin grey bars with a percent, a shaded today column and a red line. Reach for it for project timelines and schedules."
---

# Gantt chart

**Code name:** Resource tree, day-grid bars and today line.

## What you see
A white card, 928 by 392 in the demo, with a 34px toolbar: "Today" on a grey chip, a "Month" dropdown, back and forward arrows, "July 2026" in semibold, and a "Settings" button on the right. Below it the left pane (151px) holds a "Resources" tree: Planning, Design and Build as groups with a chevron and bold text, and their tasks indented underneath (Project brief, Scope review, Wireframes, Visual design, Frontend, Backend, QA pass).

The right pane has two header rows. The top row shows weeks ("W30 Jul 19 - 25", "W31 Jul 26 - 1", "W32 Aug 2 - 8"); the second shows days, each column 48px wide. Wednesday 29 is shaded grey with a pill label and a red line with a dot at the top. Groups are thin 5px grey bars with the progress part darker and a percent at the end (100%, 55%). Tasks are 18px bars: Scope review blue, Wireframes and Visual design pale purple with a stronger purple progress part, Frontend and Backend pale green with a green progress part. Small scroll tracks sit along the bottom, with zoom + and - buttons bottom right.

The 21st.dev clip is only 1.8s and almost still. The demo adds a 7s loop: bars grow in from their left edge 0.08s apart, then a cursor drags the Backend bar 1.5 days right and drags it back.

## When to use it
Project plans, release schedules, staffing or booking views where tasks have a start, an end and a progress. The resource tree plus day grid suits tens of rows. Not for time series with values; use a line or area chart.

## How it works
Every bar position is `dx(day) = x0 + (day - firstDay) * dayW`, so dates map to pixels with one function. Header labels and vertical lines come from a loop over days using `Date.UTC`. Task bars are a track with an absolutely positioned fill of `width * progress`; group bars are the same at 5px height with a percent label after the end.

```js
const dx = (d) => X0 + (d - CONFIG.firstDay) * D
// bar: left = dx(start), width = (end - start) * D; fill width = that * progress
```

The 21st.dev page bundles the first five official ReUI examples (this clip shows the first one, with resources, drag to move and a settings popover). The usage code shows resources, events, nav and toolbar parts, so interactions like drag-to-create and unscheduled rows exist, but the clip does not show them.

## Numbers that matter
| | |
|---|---|
| Card | 928 x 392, 14px radius, 1px `#e4e4e7` |
| Toolbar / week row / day row | 34 / 25 / 25px |
| Resource pane | 151px wide, row height 30px |
| Day column | 48px, lines `#ececee`, week lines `#e2e2e5` |
| Task bar | 18px high, 5px radius, 11px label |
| Purple | track `#eadbfb`, progress `#c79df6`; green track `#c9f0e1`, progress `#73d4ae`; blue `#7dd3fc` |
| Group bar | 5px, track `#e1e1e4`, progress `#a9a9ad` |
| Today | line `#e5262d` 1.5px, column tint 4.5% black |
| Demo loop | 7s; drag moves 1.5 days |

## Sound
Silent.

## Adapt it
- `CONFIG.rows` and `CONFIG.bars`: names, start and end days, progress, colours.
- `dayW` for wider or narrower day columns, `today` for the red line.
- `dragBy` and the `drag: true` flag on a bar for the scripted drag.
- `month` and the week header list inside the loop for other date ranges.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "ReUI Gantt" by sean0205 on 21st.dev (https://21st.dev/@sean0205/components/reui-gantt), MIT. This demo is an original recreation written from the public preview.
