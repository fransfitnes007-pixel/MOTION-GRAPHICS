---
name: violet-ai-dashboard-score-ring-push-in-counting-ring-glow-brain
description: "A dark violet analytics dashboard: a glowing brain heatmap on the left, a \"potential score\" ring on the right counting up to 85-88 with the word Excellent, benchmark bars and glowing columns rising, while the camera pushes in and then pulls back to show the whole window. Reach for it as a stand-in \"our AI scores your work\" screen."
---

# Violet AI review dashboard with counting score ring

**Code name:** Counting ring, rising bars, glowing brain, push-in camera.

## What you see
A dark violet-black analytics window fills the frame. On the left a glowing translucent brain, violet outside with orange-hot patches in its lobes, floats in a panel called "Brain Heatmap" with four small dotted callouts (curiosity, trust, emotional engagement, shareability) and a vertical orange-to-violet legend. On the right a ring labelled "Potential Score" fills in a violet gradient while a big white number counts up from 0 (it hits the high 70s within a second, then wanders between about 73 and 88, ending near 85); next to it the word "Excellent" in violet and a one-line note. Under it a "Platform Benchmarks" panel with four horizontal violet bars (92, 85, 78, 70) and a set of pink-white glowing columns that rise out of its bottom edge. Small violet motes float up. Over eight seconds the camera pushes in about 20% on the brain and score, holds, and in the last two seconds pulls back to show the whole window framed on a dark blue ground with glass diamonds at the edges.

## When to use it
A stand-in for "our AI analyses it and gives it a score": content review, audience analysis, SEO audit, credit score, fitness score. The glowing brain sells "AI" instantly. Wrong where numbers need to be trustworthy: it is a look-alike built from drawn pieces, so do not use it as evidence of a real product.

## How it works
The demo is a look-alike dashboard built from scratch. The score wanders a little on purpose (it hits the high 70s, dips, then settles near 85), which a real counter would not do, so keep it as a stand-in.

The dashboard is a 1280 x 720 dashboard drawn with absolutely positioned divs and two SVGs. The brain is two overlapping ellipse lobes filled with a violet-to-orange radial gradient, with 26 sine-wave "fold" lines clipped to the lobes and two blurred orange ellipses whose opacity pulses; the ring is two SVG circles (one blurred for glow) whose `stroke-dashoffset` is `circumference * (1 - value / 100)`, with a white head dot placed on the arc.

```js
const up = eo(seg(t, .15, 2.6)), val = up * 88 - 3 * eio(seg(t, 3.5, 7.5)) + Math.sin(t * 2.3) * .6 * seg(t, 2.6, 3)
arc.setAttribute('stroke-dashoffset', 515.2 * (1 - val / 100))
const a = (-90 + 360 * val / 100) * Math.PI / 180        // the head dot rides the end of the arc
head.setAttribute('cx', 100 + 82 * Math.cos(a)); head.setAttribute('cy', 100 + 82 * Math.sin(a))
dash.style.transform = `translate(${CX - fx * sc}px,${CY - fy * sc}px) scale(${sc})`   // camera: scale about a focus point
```

Camera: one container, scaled and translated so that a focus point (in dashboard coordinates) sits at the frame centre; the focus and zoom are eased from 1x on the centre to 1.22x on the brain and score, then back to .97x. The timings above are design choices; only the score's range matters.

## Numbers that matter
| | |
|---|---|
| Ground | `#07070f`; window `#0b0b17`, panels `#10101e` with 1px rgba(255,255,255,.07) borders |
| Accent | violet gradient `#6d4cff` to `#b27cff`; hot patches orange `#ff9a4d` |
| Window | 1280 x 720 design size, radius 14px |
| Ring | r 82 in a 200 box, stroke 12, round caps; arc shown twice, once blurred 5px |
| Score | 0 to 88 over 0.15s to 2.6s, ease-out-cubic; sinks to 85 by 7.5s |
| Bars | scaleX 0 to 1, 1.7s each, 0.15s apart from 0.5s |
| Columns | 8, rise 1.6s each, 0.22s apart from 0.8s, pink-white to violet, glow `0 0 14px rgba(190,140,255,.6)` |
| Camera | 1x to 1.22x over 0 to 4s; hold; to .97x over 5.6s to 7.8s |

## Sound

## Adapt it
- The labels and the numbers (`NAV`, the score formula, bar values).
- The accent: swap the violet gradient and the brain gradient for another hue.
- Camera: zoom 1.22 and the focus points for a different framing.
- Remove the brain panel to keep just the score ring and the bars.

## Files
- `code/demo.html` runs on its own (8s loop). It is a look-alike built for this library.
