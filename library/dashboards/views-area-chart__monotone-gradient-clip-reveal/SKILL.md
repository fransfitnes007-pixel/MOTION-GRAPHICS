---
name: views-area-chart-monotone-gradient-clip-reveal
description: "A violet area chart: smooth monotone line, vertical fade fill, faint horizontal grid, no axis lines, and a tooltip that follows the cursor. It starts as a shimmer block, then draws in left to right. The default chart of the whole app."
---

# Views area chart

**Code name:** Monotone area with gradient fill and clip reveal.

## What you see
A "Views tracking" card. For the first 0.7s the chart slot is a rounded block with a soft violet shimmer sweeping across it (the loading state). Then the area draws in over 1.5s, left to right, the line first appearing with the fill under it. Axis labels are 11px grey with no lines; four or five horizontal grid lines sit at 5% white. From 2.9s a thin grey cursor line moves across with a ringed dot on the line and a small dark tooltip showing the date and "Views : 72,745" in violet.

## When to use it
Any "growth over time" beat, in a dark UI. It is the most common chart in a dashboard, so it is the safe default. For a rising-total story use cumulative data; for a daily story prefer the bar variant in `campaign-analytics-dashboard__stat-row-area-milestones`.

## How it works
```tsx
<AreaChart data={rows} margin={{ top: 8, right: 8, bottom: 0, left: 0 }}>
  <linearGradient id="clientViews" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stopColor="#8B5CF6" stopOpacity={0.45} /><stop offset="100%" stopColor="#8B5CF6" stopOpacity={0} />
  <CartesianGrid stroke="rgba(255,255,255,0.05)" vertical={false} />
  <Area type="monotone" dataKey="views" stroke="#8B5CF6" strokeWidth={2} fill="url(#clientViews)" dot={false} activeDot={{ r: 4, fill: '#A78BFA' }} />
```
Recharts animates every chart on mount for 1500ms with its default `ease` curve (`cubic-bezier(.25,.1,.25,1)`). For an area the reveal is a clip rectangle whose width grows from 0 to the plot width, so the line and fill appear together. The demo reproduces that with a `clipPath` rect:

```js
document.getElementById(id + 'r').setAttribute('width', box.x0 + (box.x1 - box.x0) * EASE(seg(t, t0, t0 + 1.5)))
```

The line is a d3 monotone-X spline (`monoPath` in the file), which is what Recharts' `type="monotone"` uses. The y-axis is 52px wide, ticks 11px `#6B7280`, formatted with a K / M compactor. The loading state is `.shimmer`: `linear-gradient(90deg, transparent 25%, rgb(var(--haze) / 0.1) 50%, transparent 75%)`, `background-size: 200% 100%`, `shimmer 2s infinite` moving the position from -200% to 200%. The tooltip box is `#0D0D1A`, 1px `#1A1A2E`, radius 12, 12px text, label `#9CA3AF`, value `#A78BFA`.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Chart: 800 x 260 in the demo (the app uses 240 to 300 high), margin top 8, right 8.
- Stroke 2px; fill 0.45 to 0 opacity.
- Reveal 1.5s `ease`; shimmer 2s.
- Active dot: radius 4 fill `#A78BFA`, white 2px ring in Recharts' default.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `vals` and `LAB`: any series and its date labels.
- `color` / `stroke` options of `areaChart()`; for other metrics the app uses `#EC4899`, `#F59E0B`, `#10B981`.
- `labelIdx`: which x ticks to show (the app uses `minTickGap={28}`).
- `topOp` and `botOp` for a stronger or weaker fade.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
