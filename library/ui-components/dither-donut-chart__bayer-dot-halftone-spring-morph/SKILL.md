---
name: dither-donut-chart-bayer-dot-halftone-spring-morph
description: A donut chart drawn in chunky 1-bit dither dots on a dark card, with period tabs that spring the segments to new sizes. Use for share of something: plans, platforms, traffic sources.
---

# Dither donut chart

**Code name:** Bayer dot halftone, spring morph.

## What you see
Near-black page, a dark card with a blue users icon, the title Plan Distribution and four period pills. The donut is made of a 4px grid of square dots: white for the biggest segment, then slate-200, -300, -400 and -500, dots thinning out as the colour darkens, brighter toward the outer rim, with a small gap between segments. At 0.3s the ring sweeps out clockwise, at 1.7s the first legend row is hovered (its segment pushes out, the rest dim), at 3.4s Week is chosen: the five boundaries slide on a fast spring to the new shares and the legend numbers change; Quarter at 6.0s, Year at 8.6s, a second hover at 10.9s. 12.5s loop. On a phone the legend drops under the donut.

## When to use it
Share-of-total beats: where views come from, plan mix, spend by category. The dithered texture suits terminal, retro or 'engineered' brands; for a soft consumer look use the spring bar chart instead.

## How it works
Canvas, 180 x 180 logical, ring radius 48 to 78. Every 4px cell inside the ring finds its angle, picks its segment, and is switched on or off by a Bayer 4x4 threshold against the segment's brightness (`lum x (0.86 + 0.3 rim^2) + 0.06`), then drawn as a 3px square in the segment colour. Segments are gapped by about 5.5 degrees (the original's gaps measured about 3, but dots on a 4px grid need a wider gap to show).

The spring was measured by tracking the gap angles frame by frame after a period change: the first boundary went 142, 131, 122, 119, 117, 116 degrees against a target of 115.2, which fits a critically damped spring with omega 22 (`1 - (1 + 22t)e^(-22t)`), settling in about 0.25s. The demo uses that for the period changes. Boundaries are simulated from the previous targets, so `render(t)` is repeatable.

My additions, not seen in the original: the 0.3s intro sweep (omega 7), the hover look (segment grows 4px, others dim to 50%, row gets a 5% white wash). The legend swaps numbers at once. The card is widened to 430px so the legend fits on one line, and the dot density and rim shading are tuned by eye to the preview.

## Numbers that matter
| | |
|---|---|
| Grid | 4px pitch, 3px dots |
| Ring | radius 48 to 78 of a 180 canvas |
| Spring | critically damped, omega 22 (about 0.25s) |
| Gap | 5.5 degrees in the demo |
| Colours | #ffffff #e2e8f0 #cbd5e1 #94a3b8 #64748b |
| Card | #181818, 24px radius, white 5% border |

## Sound
A soft rattle of ticks as the dots resettle on each tab.

## Adapt it
- `CONFIG.data` (per period), `names`, `colors`, `plan` (when each tab is chosen), `hovers`, `pitch`, `gap`, `omega`. Fewer, brighter segment colours make the dither read faster on a phone.

## Files
- `code/demo.html` self-contained, loops, `?w=1080&h=1920` for 9:16.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Dither Donut Chart" by su2491251 (https://21st.dev/@su2491251/components/dither-donut-chart), MIT. Recreated by eye from the public preview; this demo is original code. Full notices: `THIRD_PARTY_NOTICES.md`.
