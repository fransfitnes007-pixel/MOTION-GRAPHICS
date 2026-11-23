---
name: platform-donut-chart-pie-sweep-circle-legend
description: "A four-colour donut (52px hole, 82px radius, 3 degree gaps) that sweeps round on mount, with a circle-icon legend and a hover tooltip. Use it for any share-of-total split such as platforms."
---

# Platform donut chart

**Code name:** Pie sweep with padding angle and circle legend.

## What you see
A narrow card titled "Platform distribution". The ring grows from nothing: each sector's angle scales up over 1.5s, so the whole ring unwinds from the 3 o'clock position and all four colours appear together (violet, pink, blue, red) with thin gaps. A one-line legend with round dots sits beneath. At 3s a tooltip appears at the TikTok sector, "TikTok : 1,130,000 views · 71 posts (42%)", then moves to the Instagram sector at 4.3s.

## When to use it
A share-of-total with three to six slices. Keep the labels in the legend, not on the ring. Do not use it for more than six categories or for values that should be compared precisely; use the horizontal bars.

## How it works
```tsx
<Pie data={platformData} dataKey="value" nameKey="label" cx="50%" cy="50%" innerRadius={52} outerRadius={82} paddingAngle={3} stroke="none">
  {platformData.map((e, i) => <Cell key={i} fill={PLAT_COLORS[e.name]} />)}
<Legend iconType="circle" wrapperStyle={{ fontSize: 12, color: '#9CA3AF' }} />
```
Recharts animates every chart on mount for 1500ms with its default `ease` curve (`cubic-bezier(.25,.1,.25,1)`). For a pie each sector's span is scaled from 0 to its full angle, one after the other around the ring, starting at 3 o'clock and running counter-clockwise (Recharts angles are anticlockwise). `donutPaths()` builds the sectors:

```js
const span = d.value / total * (360 - pad * n) * k       // k = EASE(seg(t, t0, t0 + 1.5))
a0 = a1 + pad * k                                       // gap grows with the sweep
```

Platform colours in the pie are not the chips' colours: `tiktok #8B5CF6, instagram #EC4899, facebook #1877F2, youtube #EF4444`. The legend is Recharts' own, circle icons 14px wide with 10px dots and 12px `#9CA3AF` text. The tooltip's formatter returns `[text, label]`, so the row reads `Label : text`.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Inner radius 52px, outer 82px, padding 3 degrees, `stroke: none`.
- Chart box 224px high; legend about 24px under it.
- Sweep 1.5s `ease`.
- Colours: `#8B5CF6 #EC4899 #1877F2 #EF4444`.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `DON`: label, value, colour, post count.
- Inner and outer radius in the `donutPaths(cx, cy, 52, 82, ...)` call.
- The tooltip text format in `render`.
- `pad`: 0 gives a solid ring.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
