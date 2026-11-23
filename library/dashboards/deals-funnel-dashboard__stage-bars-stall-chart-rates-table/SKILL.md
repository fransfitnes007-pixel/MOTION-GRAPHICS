---
name: deals-funnel-dashboard-stage-bars-stall-chart-rates-table
description: "A sales-funnel analytics page: five stat tiles, a six-step funnel whose bars are widths relative to the first step with percent-of-previous at the right, a coloured stall bar chart, lost-reason bars and a reply-rate table with a segmented switch."
---

# Deals funnel dashboard

**Code name:** Stage-width funnel bars, stall chart, rate table.

## What you see
Five small tiles (median time to reply, reply to won, win rate, lost, not taken). Then a Funnel panel with six rows: a label, a track 32px tall and a right-hand note such as "75% of sourced". The bars grow from zero to their widths in turn (grey, blue, violet, amber, green, mint), each with its count inside at the left. Two panels follow: "Where open deals sit" (a bar chart of average days in each stage, every bar its stage colour) and "Why deals are lost" (thin red bars). The page scrolls and the "Reply and win rates" table appears; its pill switch steps Source, Category, Type while the violet reply-rate bars fill.

## When to use it
Revenue, sales or pipeline analytics: anything where a funnel and the reasons for drop-off matter. The funnel rows are the part to reuse on their own: width is `count / first count` with a 4% minimum, so a tiny final step is still visible.

## How it works
Funnel row: `grid-cols-[120px_1fr_150px]`; the track is `h-8 rounded-lg bg-white/[0.03]`, the fill `absolute inset-y-0 left-0` at `width: max(4, round(n/top*100))%` with the stage colour at 0.75 opacity and `transition-[width] duration-500`. Colours: `#6B7280 #3B82F6 #8B5CF6 #F59E0B #10B981 #34D399`. The right note is the percent of the previous step in white and its name in muted text.

The stall chart is a Recharts `BarChart` (no grid, x ticks 11px, y width 32) with one `Cell` per bar using the same step colours and `radius {[6,6,0,0]}`. Lost reasons use `h-2` tracks with `bg-red-400/60` fills; rate rows use an `h-1.5` track with `bg-rv-purple`.

All bars use width from the data, so the demo animates them from zero with the same 0.5s ease the CSS transition would give if the width changed.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Funnel track 32px high, 8px radius; label column 120px, note column 150px; rows 4px apart.
- Bar opacity 0.75; minimum width 4%.
- Stall chart height 224px, 1.5s Recharts ease; lost-reason tracks 8px high.
- Panel: `rounded-2xl border bg-rv-card/60`, header padding 16px 20px 8px.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- Step names, counts and colours in `STEPS`.
- `LOST` and `STALL` data arrays.
- The table rows in `RT` and the labels of the switch.
- Winning-rate maths is only the note text; change it freely.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the deal counts are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
