---
name: deals-money-dashboard-blur-masked-values-stage-bars
description: "A money page that starts with every figure blurred or dotted out, then reveals them: four stat tiles, collected-by-month and value-by-stage bar charts, earned-so-far progress cards and a biggest-deals list. Use it to show privacy-safe finances."
---

# Deals money dashboard

**Code name:** Blur-masked values, stage-coloured bars, earned progress.

## What you see
The page opens locked: the four tiles show `$•••••` in grey, and the two chart cards are blurred 12px with a pill in the middle reading "Values hidden. Click or press V to show." At 2.6s the values reveal at once: tiles show dollars, the charts sharpen with currency axis labels, and the eye pill at top right flips to "Values shown". Right after, the earned-so-far cards fill their emerald progress bars while their dollar figures count up, and the biggest-deals list shows amounts.

## When to use it
Finance screens that need a "safe to share" mode, or any film moment that wants a reveal on a dashboard. The blur-and-pill pattern is cheap and clear. Do not use it for a page with nothing sensitive; the lock adds friction.

## How it works
`masked(node)` wraps the chart in a relative container: `blur-md pointer-events-none select-none` on the content while values are hidden, and an overlay button centred with `absolute inset-0 grid place-items-center`. The money formatter returns `$•••••` when hidden (`moneyText(v, shown)`), so tooltips, axis ticks and tiles all follow one boolean. The axis formatter returns an empty string when hidden:

```js
const axis = (v) => shown ? '$' + Math.round(v / 100).toLocaleString('en-US') : ''
```

Bars are Recharts `Bar` with `radius {[6,6,0,0]}`; "Collected by month" is one violet series (`#8B5CF6`), "Value by stage" colours each bar by stage through `Cell` and `STAGE_FILL` (`sourced #6B7280, contacted #3B82F6, replied #8B5CF6, negotiating #F59E0B, won #10B981, delivered #34D399, paid #6EE7B7`). The blur in the demo is a plain CSS `filter: blur(12px)` toggled by the boolean; the app has no transition on it, so neither does the demo.

The earned card shows a 6px track (`bg-white/[0.06]`) and a `bg-emerald-400/70` fill sized `earned / projected`.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Blur: 12px (`blur-md`), no transition.
- Stage colours: see above; bars 6px radius on top corners.
- Earned fill `rgba(52,211,153,0.7)` on a 6px track.
- Chart height 224px; y-axis width 70px.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- The time the reveal happens (`shown = t >= 2.6`).
- `MON`, `STG`, `ACT`, `BG` data arrays.
- The masked string (`$•••••`) and the pill text.
- Set `shown = true` always for a plain money dashboard.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the brands and amounts are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
