---
name: admin-analytics-dashboard-metric-tabs-heatmap-creator-roll
description: "The team-side analytics page: four stat cards, eight counter tiles, an area chart whose tabs morph between views, likes and posts, a posting-activity heatmap, then a creators table and a per-platform campaigns table. Use it for a power-user dashboard in a product film."
---

# Admin analytics dashboard

**Code name:** Metric tabs, posting heatmap, creator roll.

## What you see
Four stat cards fade up 16px at 0.05s intervals, then a row of eight small tiles (Views, Posts, Likes, Comments, Shares, Saves, Avg views / post, Engagement) each with a tinted icon. Below, a wide glow card "Views by day" draws a violet area with a dot on every day, and a card on the right shows Posting activity: eight week columns by seven weekday rows of rounded cells, from dark grey to bright violet. At 3.6s the Likes tab is selected and the line morphs to the pink likes curve over 1.5s; at 6s the Posts tab flips the chart to blue bars that grow from the baseline. From 7.4s the page scrolls to a Creators table (avatar, campaign, accounts, posts, views, average, likes, comments, top post with a platform tag) and an Active campaigns table whose headers are TikTok pink, Instagram pink-red, Facebook blue and YouTube red.

## When to use it
Operator or agency dashboards where a lot of numbers have to feel organised. The tabs and the morph carry the movement, so it suits a screen recording replacement for a "see everything in one place" line. Too dense for a phone-sized frame; use the tall variant of the single-chart skills instead.

## How it works
`PerformancePanel` builds the counter tiles (`grid lg:grid-cols-8 gap-2.5`, each `rounded-xl border bg-rv-card px-3 py-2.5` with a 10px uppercase label and an 18px bold tabular value), the chart card and the heatmap card in a `lg:grid-cols-3` grid (chart spans two).

The chart is an `AreaChart` for views, likes, comments and shares and a `BarChart` for posts. Margin `{left:-8, right:8, top:4}`, y-axis width 44, ticks 10px `#6B7280`, area stroke 2px with a gradient from the metric colour at 0.4 to 0, and a 3px dot per point while there are 14 or fewer days. Metric colours: views `#8B5CF6`, posts `#3B82F6`, likes `#EC4899`, comments `#F59E0B`, shares `#10B981`. The tab strip is `bg-rv-bg/60 border rounded-lg p-0.5`; the active tab is white on `${colour}33` (20% alpha).

Heatmap cells: `h-[12px] rounded-[3px] border border-white/5`, fill `rgba(139,92,246, 0.25 + 0.75 * n / max)` when `n > 0`, `rgba(255,255,255,0.04)` when empty, transparent for days that have not happened yet.

Switching tabs re-renders the Recharts series with new data, so the line interpolates from the old points to the new ones. The demo does the same by blending pixel positions of the old and new point sets with the 1500ms `ease`:

```js
const P = L.pts.map((p, i) => [p[0], P0[i][1] + (p[1] - P0[i][1]) * EASE(seg(t, tSwitch, tSwitch + 1.5))])
```

Cards below the fold use `GlowCard`, which fades up 24px over 0.6s when it scrolls into view (`whileInView`, once). The demo works out when each card enters the viewport from the scroll curve (`inViewAt`) and starts its fade then.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Counter tile: 10px label, 18px value, 10px 12px padding, 10px gap between eight tiles.
- Chart card 2/3 width, heatmap card 1/3, 16px gap; chart height 220.
- Table text 12px, header 10px uppercase `tracking-wide`, row padding 10px, row rule `rgba(26,26,46,0.6)`.
- Platform colours: TikTok `236,64,122`, Instagram `225,48,108`, Facebook `24,119,242`, YouTube `255,0,0`.
- GlowCard: `rgba(13,13,26,0.8)` fill, `rgba(139,92,246,0.12)` border, a 1px violet line at the bottom edge, 75% wide.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- Names, campaigns and numbers in the `CR`, `tiles` and `SER` arrays.
- The `METRICS` list: label and colour per tab.
- `SCHED` sets when each tab is selected.
- Heatmap density: the two `R2() <` thresholds control how busy it looks.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the creators, campaigns and numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
