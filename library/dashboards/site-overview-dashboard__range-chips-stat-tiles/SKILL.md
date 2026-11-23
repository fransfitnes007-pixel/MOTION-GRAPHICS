---
name: site-overview-dashboard-range-chips-stat-tiles
description: "A site overview screen: a glass sidebar, a title, 7D / 30D / 90D range chips with a refresh button, four stat tiles with change-versus-previous, a views-and-clicks area chart, five small ranked tables, and a live phone preview on the right. Reach for it as a template for a simple first-party analytics screen."
---

# Site overview dashboard

**Code name:** Range chips and stat tiles.

## What you see
Three columns on the pastel page. A 232px glass sidebar with the site name and 20 links, "Overview" in a black pill. In the middle: "Overview" and a one-line description; chips 7D, 30D (selected, black) and 90D, then a round refresh chip. Four tiles (Page views, Unique visitors, Link clicks, Inbound) show 0 on a new site, a flat dashed chart and "No clicks yet" in each of five panels. A pointer taps refresh: the arrow spins for about 0.8s and the screen fills in: 2,244 views with a green "18% vs previous", a views area with a dashed clicks line, top links, recent clicks, countries, devices and referrers. Tapping 7D and then 90D each spin the arrow and swap every figure and the chart. On the right a preview of the site in a phone-width glass frame stays put.

## When to use it
A first-party analytics screen for a small site or product where the owner wants the numbers at a glance and nothing else. Wrong for dashboards with filters, segments or many metrics; it is deliberately four numbers and five lists.

## How it works
No chart library and no animation library: the screen is data-driven and redraws when `days` changes. `useEffect(load, [days])` fetches `analytics?days=N`, the refresh icon gets `animate-spin` while `loading`, and everything else re-renders from the response.

```tsx
<button onClick={() => setDays(d)} className={cn("chip", days === d && "chip-active")}>{d}D</button>
<button onClick={load} className="chip" aria-label="Refresh"><RefreshCw className={cn("h-3.5 w-3.5", loading && "animate-spin")} /></button>
```

Each `Stat` shows the value with `toLocaleString()` and, when the previous period exists, a delta `Math.round((now - prev) / prev * 100)` with an up or down arrow in green or red. The chart is one SVG, `viewBox` 600 by 140 with `preserveAspectRatio="none"` and `vector-effect: non-scaling-stroke` so the 2px lines stay crisp when it stretches: an area (`accent / .12`), a solid views line and a dashed clicks line in ink, scaled by the shared max. Missing days are filled with zero so the x axis is continuous. Empty states are plain sentences, not skeletons. The demo draws all three states from time.

## Numbers that matter
| | |
|---|---|
| Sidebar | 232px, glass-strong, rounded-3xl; active item ink pill |
| Chips | `chip` and `chip-active`; refresh icon 14px, `animate-spin` (1s linear) |
| Stat tiles | `glass`, rounded-2xl, 16px padding; label 12px ink-3; value 24px semibold tabular |
| Delta | 12px, success #166534 or red-600, arrow icon |
| Chart | glass, rounded-3xl; svg 600 x 140, area accent/12, views 2px accent, clicks 2px ink dashed 4 3 |
| Panels | two columns, 16 to 20px padding, rows divided by ink/5 |
| Ranges | 7, 30, 90 days; default 30 |
| Loading | spinner only; no skeletons, no easing between datasets |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The sidebar items and the panels (`Top links`, `Countries`, and so on).
- The ranges `[7, 30, 90]`.
- The stat tiles: each is `icon, label, value, delta`.
- Chart series: add a third line by repeating the path with another stroke.

## Files
- `code/demo.html` runs on its own and loops. Names, hosts and all figures are invented placeholders. The preview pane is drawn as a simple placeholder, not a real site.
