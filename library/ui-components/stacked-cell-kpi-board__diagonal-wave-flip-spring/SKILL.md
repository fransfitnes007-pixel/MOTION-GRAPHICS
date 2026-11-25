---
name: stacked-cell-kpi-board-diagonal-wave-flip-spring
description: A dashboard card whose chart is a grid of tiny stacked cells; KPI tabs flip the board to a new metric in a diagonal spring wave. Use for growth and analytics beats: runs, failure rate, latency, hours saved.
---

# Stacked-cell KPI board

**Code name:** Diagonal wave flip, spring.

## What you see
White page, one warm-white card (Automation health, Weekly, Nov 2025 to Oct 2026) with a chart of 52 columns of 12 rounded cells and four KPI tabs underneath (Workflow runs 1.46M, Failure rate 1.92%, p95 latency 412ms, Hours saved 3,074h). At 0.35s the first board builds from the bottom-left corner to the top-right in a diagonal wave: every cell starts squashed and tilted back (scaleY 0.15, rotateX 80deg, invisible) and springs flat with a little overshoot. The lit cells are blue, the top cell of each column paler, the rest faint grey. At 2.7s a hover glides over two columns: other columns dim to 38%, the column goes full blue, a dashed vertical line, a white tooltip (week label, value) and a dark pin on the axis follow it. At 4.6s the tab indicator springs to Failure rate and the board re-flips; the y labels (8.0%, 6.0%...) rise into their new scale. Then p95 latency at 8.4s and Hours saved at 12.2s. 16s loop. In the tall layout the four tabs become a 2 by 2 grid and the card is scaled up.

## When to use it
Growth and results beats where one number should flip the whole picture: runs per week, failure rate, latency, hours saved, followers by week. The wave is the draw, so give it a clear second or two before the next tab.

## How it works
Each cell is its own element with `--c` (column) and `--r` (row from the bottom). Cell animation, copied from the page's CSS:

```css
animation: flip .55s linear(0,0.009,0.035 2.1%,0.141,0.281 6.7%,0.723 12.9%,0.938 16.7%,1.017,1.077,1.121,1.149 24.3%,...,1) both;
animation-delay: calc(var(--c)*11ms + var(--r)*16ms);
@keyframes flip { 0% { transform: scaleY(.15) rotateX(80deg); opacity: 0 } 100% { transform: none; opacity: 1 } }
```

The `linear(...)` string is a sampled spring (overshoots to 1.16). The demo parses that same string (`LIN`) and evaluates it per cell, so the wave is a pure function of time. Switching tab replaces the cells, so the old board vanishes at once and the new one waits out its delays (the delay is max 0.74s, so the wave takes about 1.3s end to end). Hover state: `.hot .col {opacity:.38}`, the active column's lit cells go solid accent and its unlit cells a 10% accent tint. Tooltip, line and pin glide on a 0.4s spring on the same `linear()` curve; the tab indicator slides on a 0.5s one.

Tooltip numbers are derived from the column's cell count (count x top label / 12), so they are placeholders. The week labels run from 3 Nov 2025 in 7-day steps like the original.

## Numbers that matter
| | |
|---|---|
| Grid | 52 columns x 12 cells, 3px gaps (2px on a phone) |
| Wave | delay = col x 11ms + row x 16ms, 0.55s spring each |
| Start pose | scaleY(.15) rotateX(80deg), opacity 0 |
| Colours | accent #2d5bff; lit 82% mix, cap 45% mix, off rgba(20,22,28,.055) |
| Hover | others 38% opacity, tooltip 0.35s spring, glide 0.4s |
| Tab indicator | 0.5s spring |

## Sound
A soft rising whoosh on each flip, one tick when the tooltip lands.

## Adapt it
- `CONFIG.metrics` (name, value, delta, top-of-scale, unit, icon path, 52 cell counts), `CONFIG.plan` (which tab at what time), `CONFIG.hovers`, `CONFIG.accent`. Swap the accent for a brand colour; counts are 0 to 12 per column.

## Files
- `code/demo.html` self-contained, loops, `?w=1080&h=1920` for 9:16.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Animated Bar Chart Dashboard (cell-column-trend)" by kedhareswer (https://21st.dev/@kedhareswer/components/cell-column-trend), MIT. Recreated by eye from the public preview; this demo is original code. Full notices: `THIRD_PARTY_NOTICES.md`.
