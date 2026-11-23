---
name: multi-line-chart-white-total-coloured-accounts
description: "A line chart with a bold white 'all accounts' total and thinner coloured lines for each account, grey grid, a metric/mode segmented control, and a multi-row tooltip. Use it to show a total and its parts without a stacked area."
---

# Multi-line account chart

**Code name:** White total line over thinner coloured series.

## What you see
A card headed "Views · All running campaigns" with a pill control at the right (Views / Likes / Followers). Five coloured lines (violet, blue, green, amber, pink) at 1.4px and 85% opacity fan out below a thicker white line that is their sum. All six draw in left to right over 1.5s. At 3.2s a vertical cursor travels across and a tooltip lists "All accounts" in white and each account in its own colour.

## When to use it
When viewers should see both the headline number and who contributed. White for the total keeps it distinct from any series colour.

## How it works
```tsx
<LineChart data={series} margin={{ top: 6, right: 8, left: -8, bottom: 0 }}>
  <CartesianGrid stroke="#1A1A2E" vertical={false} />
  <Line type="monotone" dataKey="total" stroke="#ffffff" strokeWidth={2.2} dot={false} connectNulls />
  {uniq.map((a, i) => <Line ... stroke={COLORS[i]} strokeWidth={1.4} dot={false} connectNulls strokeOpacity={0.85} />)}
```
Colours cycle through `#A78BFA #60A5FA #34D399 #F59E0B #F472B6 #22D3EE #F87171 #C084FC`. Recharts animates every chart on mount for 1500ms with its default `ease` curve (`cubic-bezier(.25,.1,.25,1)`). For a line the stroke is drawn on with a dash animation; the demo uses a clip rectangle, which looks the same on a left-to-right monotone line. Axis ticks are 10px; y width 48. When only one account is selected the page swaps to the violet `AreaChart` (see `views-area-chart__monotone-gradient-clip-reveal`).

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Grid `#1A1A2E` here (the area chart uses 5% white).
- Total line 2.2px white; series 1.4px at 85% opacity.
- Chart 300px high; y width 48; ticks 10px.
- Series colour list above.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `NAMES`, `COLORS`, and the series data `acc`.
- Total: sum of series or an independent measure.
- Tooltip rows are built from the same arrays.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
