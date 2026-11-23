---
name: campaign-analytics-dashboard-stat-row-area-milestones
description: "A dark analytics page: four stat cards, a violet area chart of views over time with a Total / Per day toggle, milestone bars, an efficiency list and a row of video tiles. Reach for it when a video needs a believable brand-side analytics screen."
---

# Campaign analytics dashboard

**Code name:** Stat row, area chart, milestone bars.

## What you see
The page is already up when the clip opens: an eyebrow "PERFORMANCE" in violet, a 30px "Analytics" title and one line of subtitle. Four stat cards (Views, Engagement rate, Link clicks, Store visits) rise 14px and fade in, 0.05s apart. Under them a "VIEWS OVER TIME" card draws its violet area from left to right over 1.5s, then a white cursor line scrubs across it with a small tooltip (date and total views). At 4.8s the lamp on the Total / Per day control springs across and the area is replaced by 31 violet bars that grow from the baseline. The milestone bars (Over 100K ... Over 3.0M) fill with a purple-to-sky gradient. At 6.3s the page scrolls up to show the efficiency list and six 9:16 video tiles with play buttons and amber view-count badges.

## When to use it
A brand-side or creator-side proof screen: "here is what the campaign did". It reads as a customer-facing results page, so it works for a product walkthrough, a case-study cut or a pitch. It is a full page, so give it three to eight seconds of screen time; do not cut it into small pieces. Wrong choice for a quick stat flash; use the stat tile skills for that.

## How it works
`Analytics()` in BusinessView lays out `Header`, a `grid xl:grid-cols-4 gap-4` of `Stat` cards, a `Card` holding a `SegmentedControl` and `ViewsChart`, then a two-column grid (milestones, efficiency) and a six-column grid of `VideoTile`.

Each `Stat` is a framer-motion div with `initial {opacity:0, y:14}`, `animate {opacity:1, y:0}` and `ease [0.16,1,0.3,1]` over 0.45s. The demo adds the app's usual 0.05s stagger per card.

`ViewsChart` is a Recharts `AreaChart` (`mode=cumulative`) or `BarChart` (`mode=daily`). Margin is `{top:6, right:6, left:-12, bottom:0}`, grid lines `#1A1A2E` horizontal only, ticks 10px `#6B7280` with `interval={4}` (every fifth date), no axis lines. The area uses `type="monotone"`, stroke `#A78BFA` 2px and a vertical gradient `#8B5CF6` from 0.45 to 0 opacity. Recharts animates on mount for 1500ms with its default `ease`; the area is revealed by a clip rectangle growing from the left, bars grow from the baseline.

```js
const clipW = box.x0 + (box.x1 - box.x0) * EASE(seg(t, t0, t0 + 1.5))   // EASE = cubic-bezier(.25,.1,.25,1)
```

The demo rebuilds the curve with d3's monotone-X spline (`monoPath` in the file) so the line matches Recharts exactly, and picks the y-axis ticks with Recharts' own step rounding (`niceMax`): 0, 3.5M, 7M, 10.5M, 14M for 12.5M of views.

Milestone bars are `motion.div` from `width: 0` to `count / delivered`, class `bg-gradient-to-r from-rv-purple to-sky-400`. The scroll at the end and the hover scrub are demo additions; the app page scrolls with the user.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Layout: 224px sidebar, 52px top bar, content `max-w-7xl` with 32px padding, cards `rounded-2xl` (16px) with 20px padding, 16px gaps.
- Stat: icon tile 40x40 `rounded-xl` at 15% tint, value 24px bold, label 12px, sub 11px.
- Chart card: 300px tall, 1.5s ease reveal, tooltip `#0D0D1A` with `#1A1A2E` border and 12px radius.
- Milestones: label 112px wide, bar 8px high, count 32px wide, rows 8px apart.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- The numbers in the `stats`, `MS` and tile arrays, and the brand name in `shell()`.
- `TOTAL` (total views) and the day count: the curve is generated from a seeded shape so it always sums to the total.
- Swap `#8B5CF6` / `#A78BFA` for another accent; the gradient, the bars and the lamp all read from those two values.
- For a glass variant, see `glass-card-border-beam__conic-light-chrome-rim`.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the creator names and numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
