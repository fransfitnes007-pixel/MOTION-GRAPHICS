---
name: tier-coloured-bars-per-bar-cell-fill
description: "A column chart that switches between views, likes and earnings: violet bars for counts, and when you pick Earned each bar takes the colour of the pay tier that post reached. Use it when bar colour carries a category."
---

# Tier-coloured bar chart

**Code name:** Per-bar Cell colours with a metric switch.

## What you see
A card "Views per post" with a Views / Likes / Earned pill control. Twelve violet bars (P1 to P12) grow from the baseline over 1.5s. At 4.2s the lamp springs to Earned, the title becomes "Earned per post" with the caption "Coloured by the tier each post reached", and the bars morph to the dollar values while changing colour: grey, blue, green, lilac, amber.

## When to use it
Per-item results where a second dimension (tier, stage, status) should be readable at a glance. Pair with a legend if the categories are not obvious from context.

## How it works
```tsx
<Bar dataKey={metric === 'earned' ? 'earnedDollars' : metric} fill="#8B5CF6" radius={[6, 6, 0, 0]}>
  {metric === 'earned' && chart.map((r, i) => <Cell key={i} fill={TIER_COLORS[r.tier.idx % TIER_COLORS.length]} />)}
</Bar>
```
`TIER_COLORS = ['#6B7280','#60A5FA','#34D399','#A78BFA','#F59E0B','#F472B6','#8B5CF6','#22D3EE']`. Grid is `rgba(255,255,255,0.06)` horizontal only, margin `{top:8, right:8, left:-16, bottom:0}`, y width 56 (64 for dollars). Recharts animates every chart on mount for 1500ms with its default `ease` curve (`cubic-bezier(.25,.1,.25,1)`). When the data key changes, Recharts animates the old heights to the new ones; the demo blends heights with the same curve and switches the fill at the moment of the switch. The stage-coloured bars on the deals pages use the same `Cell` idea with `STAGE_FILL` / `STEP_COLORS`.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Chart 224px high; bars 80% of each band; radius 6px.
- Tier colours above; default fill `#8B5CF6`.
- Switch lamp: spring 300 / 30.
- Morph 1.5s `ease`.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `D`: views and earned per bar.
- `tier()` thresholds map a value to a colour index.
- `TIER` colours.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
