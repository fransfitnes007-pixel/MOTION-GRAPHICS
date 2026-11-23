---
name: performance-radar-chart-five-axis-polar-fill
description: "A five-axis radar with grey polygon rings, a translucent violet polygon with dots at each score, and a tooltip giving the score and its raw figure. Use it for a creator or account 'shape' at a glance."
---

# Performance radar chart

**Code name:** Five-axis polar fill growing from the centre.

## What you see
A card with a pentagon grid: four concentric grey polygons (25, 50, 75, 100) and five spokes, with labels Reach at the top, Engagement, Consistency, Growth and Views per post clockwise. The violet polygon (28% fill, 2px stroke, a 3px light-violet dot at each vertex) grows from the centre outwards over 1.5s. At 2.8s a tooltip pins to Growth ("Score : 44 / 100 · +3,120 followers in 30d"), then to Engagement.

## When to use it
Comparing one entity across a handful of normalised measures. Needs the axes to share a 0 to 100 scale; the app normalises each with a log or ratio so a radar reads fairly.

## How it works
```tsx
<RadarChart data={scores} outerRadius="72%">
  <PolarGrid stroke="rgba(255,255,255,0.08)" />
  <PolarAngleAxis dataKey="axis" tick={{ fill: '#9CA3AF', fontSize: 11 }} />
  <PolarRadiusAxis angle={90} domain={[0, 100]} tick={false} axisLine={false} />
  <Radar dataKey="score" stroke="#8B5CF6" fill="#8B5CF6" fillOpacity={0.28} strokeWidth={2} dot={{ r: 3, fill: '#A78BFA', strokeWidth: 0 }} />
```
Recharts animates every chart on mount for 1500ms with its default `ease` curve (`cubic-bezier(.25,.1,.25,1)`). The radar draws its polygon by scaling every vertex from the centre by the animation progress. Axes start at 12 o'clock and run clockwise, five apart by 72 degrees; the outer radius is 72% of half the smaller side. The scores come from `radarScores`: reach is `log10(views+1) / log10(10M+1)`, engagement `rate / 10%`, consistency `posts per week / 7`, growth `30-day follower change / 10%`, views per post `log10(avg+1) / log10(1M+1)`, each clamped to 0..100.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Chart 280px high; outer radius 72% of the shorter half-side (about 100px).
- Rings at 25 / 50 / 75 / 100, stroke `rgba(255,255,255,0.08)`.
- Fill 28% violet; stroke 2px; vertex dot 3px `#A78BFA`.
- Reveal 1.5s `ease`.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `D`: axis name, score, raw text.
- Number of axes: change the 72 degree step to 360 / n.
- Colour: use the shared tone for a per-platform radar.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
