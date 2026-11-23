---
name: outreach-today-dashboard-one-gradient-hero-ring-fill
description: "A calm near-black dashboard with exactly one gradient card at the top, icon-tile stat cards, a violet area chart and a glowing ring that fills, appearing from shimmering skeleton blocks. Reach for it for a daily summary screen where the greeting matters more than the chart."
---

# Outreach today dashboard

**Code name:** One gradient hero ring fill.

## What you see
Black-violet ground (`#0A0A0F`), 16px-radius cards with 1px borders and no shadows. A top bar with a primary segmented control (the active segment is solid violet with a soft glow) and a quiet one. The hero card is the only gradient on the page: `120deg` from `#1B1838` to `#14132A` to `#111118`, a 60px violet tile with sparkles, a greeting at 26px bold, a one-sentence summary, a violet "Copy summary" button and a white "Open waiting list" button. Four stat cards follow, each with a 36px tinted icon tile top right, a 30px number, and a caption. Then a violet area chart beside a capacity card with a 150px ring, and a reply-rate card with bars.

- 0 to 1.3s: everything is a skeleton, grey blocks with a light band sweeping across (`shimmer 1.4s linear infinite`).
- 1.3s: the real content replaces the blocks in one step. The area chart reveals left to right in 0.4s and the ring fills to 74% in 0.4s, both ease-out.
- 3.2 to 6.6s: a crosshair, dot and small tooltip travel along the chart. In the app this follows the pointer.

## When to use it
A morning or end-of-day "where things stand" page, a founder or team summary, anything that should read as a person speaking to you before showing numbers. Use the gradient once. A second gradient card would remove the effect.

## How it works
- One gradient: `.hero-card { background: linear-gradient(120deg, #1B1838 0%, #14132A 40%, #111118 100%); border: 1px solid #2A2747 }`.
- Skeletons: `.skeleton { background: linear-gradient(90deg, #16161F, #1C1C27, #16161F); background-size: 200% 100%; animation: shimmer 1.4s linear infinite }` with `shimmer` moving `background-position` from `200% 0` to `-200% 0`.
- Ring: SVG circle, 12px round stroke, track in the border colour, rotated -90 degrees, with `filter: drop-shadow(0 0 6px #8B5CF666)`. The arc is `strokeDasharray = c` and `strokeDashoffset` animated from `c` to `c * (1 - pct)` by a `ring-fill 400ms ease-out both` keyframe through two custom properties.
- Chart: Recharts `Area` with a vertical gradient fill (`#8B5CF6` at .38 to 0), 2.25px stroke `#A78BFA`, horizontal grid only, no axis lines, and a custom `dot` that draws a ring only on the last point. It animates once for 400ms and never again, so updates do not replay it.
- The demo replaces the data load with a switch at 1.3s, since the app swaps skeleton for data when the query resolves.

## Numbers that matter
| | |
|---|---|
| Surfaces | bg `#0A0A0F`, card `#111118`, raised `#1C1C27`, border `#1F1F2A` |
| Accent | `#8B5CF6`, button fill `#7C4DEB`, text `#B79CFF`, line `#A78BFA` |
| Status | green `#22C55E` / `#4ADE80`, amber `#F59E0B` / `#FBBF24` |
| Radius | cards 16px, hero 20px, tiles 10px, segmented 12px |
| Type | Inter; display 30/36 bold, caps label 11px at .08em |
| Motion | shimmer 1.4s linear, ring and chart 400ms ease-out, hover 120ms |

## Sound
Silent.

## Adapt it
- Accent hue and the hero gradient stops.
- The sentence under the greeting. It is the useful part, so write it from real numbers.
- Stat definitions and the chart points.
- Flip `T_DATA` to 0 to drop the skeleton phase.

## Files
- `code/demo.html`: runs on its own, with invented numbers and names.
