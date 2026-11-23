---
name: analytics-bento-line-and-funnel-path-draw-day-scrub
description: "A three-tile bento: a white tile with a big weekly number and a line chart that draws itself, with day buttons that scrub a dot and tooltip along the line; a black tile with three funnel bars that fill; and a small inbox card. Reach for it to show what a dashboard will tell you, on a marketing page."
---

# Analytics bento: line and funnel

**Code name:** Path draw with day scrub.

## What you see
Left, a large white tile: "Page views, this week" over 2,244 at 48px, a "Sample data" pill, and a line chart that draws across over about a second with an indigo area fading in beneath. A dashed vertical guide, a ringed dot and a black pill reading "402 views" sit on Friday. Below the chart are seven day buttons, Friday selected in black. A pointer moves along the buttons; each one moves the dot, guide and pill to that day and changes the label. Right, a black tile, "From view to deal", lists Site visits, Link taps and Brand inquiries with numbers and indigo bars filling to 100%, 46% and 14% (.9s, .15s apart). Under it a white card with an inbox icon.

## When to use it
A marketing page for a product with analytics: it shows the shape of the dashboard with sample data, and says so ("Sample data"). Wrong for a real data view (use the dashboard skill) or for more than about 12 points per line.

## How it works
The line is drawn from `WEEK`, mapped into a 320 by 120 viewBox with 10% headroom (`max * 1.1`). Reveal uses `useInView(ref, { once: true, margin: "-80px" })`:

```tsx
<motion.path d={line} fill="none" stroke="rgb(var(--c-accent))" strokeWidth="2.5" strokeLinecap="round"
  initial={{ pathLength: 0 }} animate={{ pathLength: seen ? 1 : 0 }} transition={{ duration: 1.1, ease: "easeOut" }} />
```

The area is a second path (`line + L W H L 0 H Z`) filled with a vertical gradient, fading in with `duration: .8, delay: .5`. The scrub is not framer: `hover` is an index in state, set by `onMouseEnter`, `onFocus` and `onClick` on each day button, and the guide line, the dot (`cx, cy` from `pts[hover]`) and the tooltip (`left` and `top` as percentages of the viewBox) all read it, so it moves instantly. Funnel bars are `motion.div` with `whileInView={{ width: pct }}`, `duration: .9, delay: .15 * i, ease: "easeOut"`. Tiles use `Reveal` with delays .06 and .12.

## Numbers that matter
| | |
|---|---|
| Grid | 1.25fr and 1fr at lg, gap 16px |
| Tiles | white, rounded-[28px], hairline border black/6; black tile ink with white/60 text |
| Big number | 48px bold tabular, -.025em |
| Line | 2.5px #5b5ce6, easeOut 1.1s; area .8s after .5s |
| Tooltip | black pill, 12px bold white |
| Day buttons | seven equal columns, 12px semibold; active ink on white |
| Funnel bars | h-2, track white/10, fill accent, widths 100, 46, 14% |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- `WEEK`, `FUNNEL` and the big figure.
- The funnel widths (they are percentages of the first figure, set by hand).
- The headroom factor 1.1 if your data has outliers.
- The "Sample data" pills: remove them once the tile shows real numbers.

## Files
- `code/demo.html` runs on its own and loops. The week and funnel numbers are the sample data the source itself uses.
