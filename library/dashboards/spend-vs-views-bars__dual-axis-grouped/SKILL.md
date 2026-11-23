---
name: spend-vs-views-bars-dual-axis-grouped
description: "Paired purple and blue bars per campaign with a dollars axis on the left and a views axis on the right, a legend of two dots, and a hover band with both values. Use it when two measures with different units need to sit together."
---

# Spend vs views grouped bars

**Code name:** Two y-axes, grouped bars, circle legend.

## What you see
A card "Campaign spend vs views". For each of six campaigns a violet bar (spend) and a blue bar (views) stand side by side, each scaled on its own axis: `$0` to `$4,500` at the left, `0` to `1.0M` at the right. Both grow from the baseline over 1.5s. A two-item legend with 8px dots sits underneath. From 3s a faint band marks the hovered category and a box lists the campaign, "Spend : $3,100" in violet and "Views : 604,000" in blue.

## When to use it
Cost against result, in against out, this week against last. The two-axis trick lets bars of unrelated size sit in one frame, but it can mislead if the axes are not read; keep the legend colours matched to the bars.

## How it works
```tsx
<BarChart data={campaignData} margin={{ left: 0, right: 8, top: 4 }} barGap={4}>
  <YAxis yAxisId="spend" tickFormatter={(v) => fmtUsd(v, 0)} width={64} />
  <YAxis yAxisId="views" orientation="right" tickFormatter={(v) => fmtNum(v)} width={48} />
  <Legend iconType="circle" iconSize={8} wrapperStyle={{ fontSize: 11, color: '#9ca3af' }} />
  <Bar yAxisId="spend" dataKey="spend" name="Spend" fill="#8B5CF6" radius={[6, 6, 0, 0]} />
  <Bar yAxisId="views" dataKey="views" name="Views" fill="#3B82F6" radius={[6, 6, 0, 0]} />
```
Recharts animates every chart on mount for 1500ms with its default `ease` curve (`cubic-bezier(.25,.1,.25,1)`). Each category band holds two bars with `barGap` 4px between them; the bars share 80% of the band. Each bar uses the scale of its own axis. The finance version swaps the colours to `#10B981` (money in) and `#F59E0B` (money out) with one axis and 30 daily categories; the creator version uses a grey `rgba(255,255,255,0.12)` bar for last week next to violet for this week. In those the tooltip cursor is `rgba(139,92,246,0.08)`.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Chart height 240; left axis 64px, right axis 48px.
- Bar gap 4px; radius 6px (4px in the finance and weekly versions).
- Series colours `#8B5CF6` and `#3B82F6`.
- Legend 11px `#9ca3af`, icon size 8.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `D`: label, spend, views.
- Series colours; `#10B981` / `#F59E0B` reproduce the finance chart.
- One axis only: use the same scale for both and drop the right labels.
- Tooltip rows in the `tip.innerHTML` line.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
