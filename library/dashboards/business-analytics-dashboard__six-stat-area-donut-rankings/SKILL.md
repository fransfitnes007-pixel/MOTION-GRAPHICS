---
name: business-analytics-dashboard-six-stat-area-donut-rankings
description: "A customer-facing analytics page: a range toggle with Export, six stat cards, a views-tracking area chart beside a platform donut, and a creator rankings table with amber top-three badges. Use it as an account owner's view of a campaign."
---

# Business analytics dashboard

**Code name:** Six stat cards, area chart, platform donut, rankings table.

## What you see
A 30px title with the subtitle "Performance overview across all campaigns" on the left; on the right a 7d / 30d / 90d toggle (30d active, violet) and an Export CSV button. Six stat cards fade up one after another. Two glow cards follow: Views tracking (area chart, 1.5s reveal, tooltip scrubbing from 3.2s) and Platform distribution (a four-colour donut that sweeps round from 3 o'clock while the legend sits under it). At 4.9s the toggle moves to 7d and the area redraws for a week. Finally the page scrolls to Creator rankings: rank badges 1 to 3 in amber, a "TOP CREATOR" tag on the first row, views in white semibold.

## When to use it
Anything addressed to the paying customer: a case-study cut, a onboarding video, a weekly report mock. It shows the page where the customer checks spend and results. The platform split uses four platform colours, so keep those if you want it to match.

## How it works
Six `StatCard`s (`grid grid-cols-2 md:grid-cols-3 xl:grid-cols-6`) with delays 0, 0.05 ... 0.25. Two `GlowCard`s in `xl:grid-cols-3`: the first spans two columns and holds `ViewsChart` at height 260, the second holds a `PieChart` in a 224px box.

The pie: `innerRadius 52`, `outerRadius 82`, `paddingAngle 3`, `stroke none`, cells `#8B5CF6` TikTok, `#EC4899` Instagram, `#1877F2` Facebook, `#EF4444` YouTube, and a circle-icon `Legend` in 12px `#9CA3AF`. Recharts sweeps sectors in by scaling each sector's angle from zero over 1500ms (`ease`), starting at 3 o'clock and running counter-clockwise; `donutPaths()` in the demo does that.

```js
donutPaths(cx, cy, 52, 82, data, 3, EASE(seg(t, 0.5, 2)))   // last argument is the sweep 0..1
```

The rankings table is `TableShell` (`rounded-2xl border bg-rv-card`), header cells 11px uppercase `tracking-wider`, rank chip 28px `rounded-lg`, amber (`bg-amber-500/15 text-amber-300 border-amber-500/30`) for the first three. `RangeToggle` is `p-1 rounded-xl bg-rv-card border`, active button `bg-rv-purple/20 text-white border-rv-purple/30`.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Donut: 52px inner, 82px outer radius, 3 degrees between sectors, 1.5s `ease` sweep.
- Stat cards: 16px padding in the six-up row, 24px value, 12px label.
- Views card 2/3 width, donut card 1/3, 24px gap; chart height 260.
- Range toggle buttons: 12px text, 4px 12px padding, 8px radius.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- Platform names and colours in `DON`; swap for any four series.
- Creator rows in `RK`.
- The range toggle time (`4.9`) and what it switches to.
- Stat labels and values in `SC`.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the creators and numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
