---
name: case-study-chart-set-grow-on-reveal
description: "Four hand-built SVG and CSS charts that draw themselves when scrolled into view: horizontal bars, a stacked share bar, a column per post, and a cumulative line with labelled markers. No chart library. Reach for them for case-study results where numbers should arrive with the page."
---

# Case study chart set

**Code name:** Grow on reveal.

## What you see
Four white-glass panels. "Views by platform": five rows with a label, a track and a value, the longest bar in indigo, the others in black-to-grey, each growing from the left 80ms after the one above and carrying a "posts" note inside when it is long enough. "Share of views": one rounded bar built from five segments that grow in turn, with a legend of squares and percentages. "Views per post": 48 thin columns that rise one by one left to right (12ms apart), the ones above 100,000 in indigo and the rest in faint grey. "Cumulative views": a dashed grid with labels, a line that draws across over 1.8 seconds, a soft indigo area that fades in beneath it, and three white-filled markers that pop in with a spring, each with a halo-stroked label.

## When to use it
Results pages, case studies and reports where each chart is shown once and the data is small (under 100 points). Charts have a text equivalent for screen readers and respect reduced motion. Wrong for interactive analysis, big data, or charts that need axes, zoom or tooltips.

## How it works
Every chart uses `useRevealed(ref, "-40px")`, which is `useInView` plus a 3s fallback so a chart in a background tab still ends up drawn, and animates once.

- **Bars**: `motion.div` `initial={{ width: 0 }} animate={revealed ? { width: `${w}%` } : {}}` with `duration: 1.1, delay: i * 0.08, ease: [0.22, 1, 0.36, 1]`. The highlighted row uses `from-accent to-accent-soft`, the rest `from-ink to-ink-2`.
- **Share bar**: segment widths from the `value / total`, `duration: 1, delay: i * 0.12`.
- **Columns**: `height` from 0 to `max(v / max * 100, 1.5)%`, `duration: .7, delay: .25 + i * .012`; bars at or above the highlight threshold get the indigo gradient.
- **Line**: points mapped into a 640 by 240 viewBox; the stroke is a `motion.path` with `pathLength` 0 to 1 over 1.8s, the area `opacity` 0 to 1 over 1.2s after .6s, markers `scale` 0 to 1 with `type: "spring", stiffness: 300, damping: 18` at `1.2 + at / points.length` seconds.

Every chart wraps its picture in `aria-hidden` and gives a `sr-only` sentence with the real numbers, e.g. `${label}: ${value} views`. With reduced motion every transition is `{ duration: 0 }`.

## Numbers that matter
| | |
|---|---|
| Bar row | grid 128px, 1fr, 80px; track 36px, rounded-xl, ink/5 |
| Bars | 1.1s, delay i x .08, ease [.22, 1, .36, 1] |
| Share bar | 20px high, 1s, delay i x .12 |
| Columns | gap 3px (4px at sm), height 224px, .7s, delay .25 + i x .012 |
| Line | 3px #5b5ce6, round caps, pathLength 1.8s; area gradient .28 to 0 |
| Markers | r 5, white fill, 3px indigo stroke, spring 300 / 18 |
| Format | `fmt`: 1.2M, 340K, plain below 1000 |
| Tones | ink, ink-2, ink-3, ink-4, accent-soft for share segments |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The data arrays and the unit strings.
- The `highlight` label or `highlightFrom` threshold.
- Colours: they read the ink and accent tokens, so a theme change recolours all four.
- Grid layout: the demo puts them in a 2 by 2; the live page stacks them in sections.

## Files
- `code/demo.html` runs on its own and loops. All data is invented and generated from a seeded function.
