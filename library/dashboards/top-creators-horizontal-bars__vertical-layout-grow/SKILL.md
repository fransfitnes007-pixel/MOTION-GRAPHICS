---
name: top-creators-horizontal-bars-vertical-layout-grow
description: "A ranked horizontal bar chart: eight names down the left in grey, violet bars with rounded right ends growing out to a number axis, and a faint violet highlight band on hover. Use it for rankings."
---

# Top creators horizontal bars

**Code name:** Vertical-layout bar chart with category labels.

## What you see
A card "Top creators by views". Eight bars, longest first, grow rightwards together over 1.5s from the axis. Names sit at the left in 11px grey, tick numbers (0, 250K, 500K ...) along the bottom in 10px. From 3s a dark violet band marks the hovered row and a tooltip shows "views : 604,118", stepping down the first five rows.

## When to use it
Leaderboards and top-N lists where the name matters. Longer labels fit better here than on a column chart.

## How it works
```tsx
<BarChart data={topCreators} layout="vertical" margin={{ left: 8, right: 16 }}>
  <XAxis type="number" tick={{ fill: '#6b7280', fontSize: 10 }} tickLine={false} axisLine={false} tickFormatter={(v) => fmtNum(v)} />
  <YAxis type="category" dataKey="name" tick={{ fill: '#9ca3af', fontSize: 11 }} tickLine={false} axisLine={false} width={110} />
  <Tooltip cursor={{ fill: 'rgba(139,92,246,0.08)' }} />
  <Bar dataKey="views" fill="#8B5CF6" radius={[0, 6, 6, 0]} />
```
Recharts animates every chart on mount for 1500ms with its default `ease` curve (`cubic-bezier(.25,.1,.25,1)`). Bars animate their length from 0. Row height is the plot height divided by the number of rows, and each bar takes 80% of its row (Recharts' default `barCategoryGap` of 10% each side). The demo's x scale uses Recharts' tick rounding so the axis ends at 1.0M for an 812K maximum.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Chart 260px high in the app; y-axis 110px wide; margins 8 left, 16 right.
- Bar radius 6px on the right corners; fill `#8B5CF6`.
- Hover band `rgba(139,92,246,0.08)`.
- Name ticks 11px `#9ca3af`; value ticks 10px `#6b7280`.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `D`: names and values; add or drop rows, the row height recomputes.
- Bar colour; use one colour per row with `Cell` if rows have categories.
- `width={110}` for longer names.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
