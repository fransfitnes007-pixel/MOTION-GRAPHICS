---
name: isometric-line-bars-spring-lift-neighbour-wave
description: A line-art isometric bar chart on a slab. Bars spring up from zero, then the bar under the pointer lifts and its neighbours follow. Use for a calm, premium stats reveal: sales by month, growth, ranking.
---

# Isometric line bars

**Code name:** Spring lift, neighbour wave.

## What you see
White page, an isometric rounded slab drawn in a thin grey outline with a faint inner rim and short tick lines. At 0.4s six white bars (hexagonal outlines, grey 0.9px strokes, pale inner edges) spring up from flat diamonds together, overshoot by about 2% and settle. From 2.0s a scripted pointer moves across: the bar under it turns to a black outline and lifts about 20 units off the slab, the bars either side lift about 8, all on a springy settle, and a mono caption underneath names the month and value (APR 24 sales). It runs Feb, Apr, Jun, Mar, then lets go at 6.4s. 8s loop.

## When to use it
A quiet premium stat beat on a light screen: sales by month, sign-ups, a ranking. It reads well tall because the slab is wide and the bars are tall. Keep to six bars or fewer so the lifts stay readable.

## How it works
All geometry is plain isometric projection in a 400 x 320 SVG: bar i sits at x = 117.19 + 26.052 i, base-left y = 198.02 + 13.026 i, half width 17.68, top diamond rise 8.84, height `h = 5.62 x value`. A bar's hexagon is `TL, apex, TR, BR, bottom, BL` and three inner edges draw the visible faces. Bars are painted left to right so the front ones cover the back ones. The slab paths are copied verbatim from the page.

Two springs, mass 1, measured by logging the path data frame by frame:

| | stiffness | damping | result |
|---|---|---|---|
| grow | 120 | 17 | peak overshoot 1.8%, peak at about 0.46s |
| lift | 200 | 22 | peak overshoot 1.8%, peak at about 0.36s |

Lift target: hovered bar 20.5 units, bars at distance 1 7.8 units (0.38 x), others 0. The demo integrates both springs from t=0 at 1/240s on every frame, so `render(t)` is repeatable. The bars only start growing when the original scrolls into view; here that is `CONFIG.growAt`. The caption is described in the listing but did not show in the preview, so its look is mine.

## Numbers that matter
| | |
|---|---|
| Grow spring | k 120, c 17 |
| Lift spring | k 200, c 22 |
| Lift | main 20.5, neighbours 7.8 (svg units) |
| Strokes | 0.9px non-scaling, #737373 edge, #e5e5e5 inner, #0a0a0a hovered |
| Bar pitch | x 26.05, y 13.03 |
| Height | 5.62 per unit |

## Sound
A short wooden tick per lift; a single rising tone as the bars grow.

## Adapt it
- `CONFIG.data`, `labels`, `unit`, `hover` (time, bar), `growAt`. Change the data and the slab stays; more than six bars needs a longer slab path.

## Files
- `code/demo.html` self-contained, loops, `?w=1080&h=1920` for 9:16.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Isometric Bars Chart (bars)" by abhishek-mallick (https://21st.dev/@abhishek-mallick/components/bars), MIT. Recreated by eye from the public preview; this demo is original code. Full notices: `THIRD_PARTY_NOTICES.md`.
