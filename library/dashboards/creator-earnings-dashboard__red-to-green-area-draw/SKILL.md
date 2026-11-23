---
name: creator-earnings-dashboard-red-to-green-area-draw
description: "Dark purple glass dashboard with a sidebar, four stat cards that spring in with counting dollar figures, an earnings area chart whose line runs red to amber to green as it draws, and deal rows with mini sparklines. Reach for it when a screen should make money going up feel earned."
---

# Creator earnings dashboard

**Code name:** Red-to-green area draw.

## What you see
A near-black purple app. Left sidebar with a gradient logo tile and a lit "Dashboard" item. Top bar with a greeting. Four stat cards (earnings, active deals, pending, completed), each with its own tint, a blurred glow blob in the corner and an icon tile.

- 0 to 0.4s: the page body fades up 8px.
- 0 to 0.7s: the cards spring in one after another, 0.1s apart, rising 24px and scaling from 0.96. They overshoot slightly.
- 0 to 1.6s: every number counts up from zero on an ease-out cubic. When the count lands, a small green sparkle floats up and fades (1.2s).
- The earnings card has a glow ring that breathes between 30% and 60% opacity every 2.5s.
- 0 to 1.8s: the earnings area chart is revealed left to right. The line is red at $0, amber around 40%, green at the end, and the fill under it fades from green at the top to red at the base.
- Below, three deal rows slide in from the left. Each has a tiny sparkline in the same red to green gradient and a progress bar that fills over 1.2s.

The demo holds the finished state until 6.6s, then fades to the background and loops.

## When to use it
A creator, affiliate or sales dashboard where the story is "you started at zero and this is where you are". The red start colour is deliberate: it makes $0 feel like a low point and the green end like a result. It is wrong for neutral operational data, where a red to green sweep would imply good and bad that is not there.

## How it works
Everything starts on mount and runs in parallel, so there is no sequencing beyond per-card delays.

- Cards: framer-motion spring, `stiffness 120`, default damping 10, delay `i * 0.1`. In the demo `fmSpring(t - i*.1, 120, 10)` is the exact underdamped spring.
- Counter: `eased = 1 - (1 - p)^3`, `p = elapsed / 1600ms`, shown as `floor(eased * value)`.
- Chart: Recharts `Area` with `animationDuration 1800` and `ease-out`. Recharts reveals the area with a clip rect that grows in x. The demo does the same with a clipPath.
- The line uses `stroke="url(#lineColorGrad)"` with an x-axis gradient (`x1=0 x2=1`). On a nearly flat bounding box an objectBoundingBox gradient can collapse, so the demo uses `userSpaceOnUse` across the plot width.

```tsx
<linearGradient id="lineColorGrad" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"  stopColor="oklch(0.60 0.22 25)" />   {/* red */}
  <stop offset="40%" stopColor="oklch(0.75 0.20 75)" />   {/* amber */}
  <stop offset="100%" stopColor="oklch(0.72 0.22 145)" /> {/* green */}
</linearGradient>
```

The source's glass cards add `backdrop-filter: blur(12px)` and the corner glow is a blurred circle; the demo uses a flat translucent card and a radial gradient for the glow, because blur filters rendered slightly differently between two draws of the same frame. The sparkline data in the source uses `Math.random()` for noise on every render. The demo uses a fixed-seed generator, so each frame is repeatable.

## Numbers that matter
| | |
|---|---|
| Palette | background `oklch(.07 .012 285)`, card `oklch(.10 .012 285 / .8)`, border `oklch(.22 .03 285)`, primary `oklch(.55 .22 290)` |
| Stat tints | green `oklch(.72 .22 145)`, purple `oklch(.65 .22 290)`, amber `oklch(.78 .18 75)` |
| Card spring | stiffness 120, damping 10, mass 1, 0.1s stagger |
| Counter | 1.6s, ease-out cubic |
| Glow ring | 2.5s, opacity .3 to .6 to .3, easeInOut |
| Chart reveal | 1.8s ease-out; sparkline 1.2s; progress bar 1.2s easeOut |
| Radius | cards 16px, icon tiles 12px, pills 999px |

## Sound
Silent. A soft tick per card or a rising tone under the counters would suit a video.

## Adapt it
- The five numbers and the monthly fractions `[0, .05, .12, .30, .62, 1]` that shape the curve.
- The tint of each card (`color`, `glow`, `border`).
- Swap the red start for the card tint if the sweep should not imply a bad starting point.
- Primary hue (290 here) drives the sidebar, buttons and glow.

## Files
- `code/demo.html`: runs on its own, placeholder creator and brands.
