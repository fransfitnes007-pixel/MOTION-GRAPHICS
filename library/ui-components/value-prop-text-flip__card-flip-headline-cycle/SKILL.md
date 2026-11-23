---
name: value-prop-text-flip-card-flip-headline-cycle
description: "Three value-prop lines cycle on a card, each flipping down like a split-flap with 3D rotateX while a small icon morphs between a circle, a rounded square and a star. Use for onboarding screens and landing hero rotators."
---

# Value prop text flip

**Code name:** Card flip headline cycle. Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
A 1240x740 dark card with an icon on top, a split-flap panel in the middle and three page dots below. The panel holds one line at a time ("Save hours every week", "Stay in sync, effortlessly", "Ship with confidence"). Every 2.2s the line holds 1.6s, then the top half falls toward the viewer (0 to -90 degrees, ease in, darkening) and the next line's bottom half swings down from +90 to 0 with a small bounce. While it flips, the icon morphs from circle to rounded square to star outline (blue, violet, mint), turning 120 degrees and dipping to 84% size, and the active page dot stretches to the next position. After the third flip the cycle is back at the first line.

## When to use it
Onboarding value props, hero taglines, feature rotators, any place that swaps short lines in place. Wrong for long copy.

## How it works
Four half-panels: a static top (shows the next line while flipping), a static bottom (current line), a flap top (current line, `transform-origin: 50% 100%`, `rotateX(0 to -90)`) and a flap bottom (next line, origin 50% 0, `rotateX(90 to 0)` on a spring). Each half is an overflow-hidden box holding a full-height text div, shifted by half a panel for the bottom. The icon canvas morphs by interpolating 90 polar radii: circle `r = .78`, squircle `r = (|cos|^4.5 + |sin|^4.5)^(-1/4.5)`, star `r = .74 + .26 cos(5 theta + pi)`.

## Numbers that matter
| | |
|---|---|
| Cycle | 2.2s each: hold 1.6s, flip 0.6s; 3 lines = 6.6s |
| Flap | top 0-0.4 of the flip (ei), bottom from 0.38 spring(7, 13) |
| Panel | 1120x230, radius 26, perspective 1500px |
| Icon | morph eio over 0.05-0.85 of the flip, 120 degree turn |

## Sound
Mechanical flap clacks, one per flip, with a soft chime under the icon morph.

## Adapt it
- `LINES` for your copy.
- `HUE` and `SHP` for icon colours and shapes.
- `CYC` and `HOLD` for pace.
- Panel gradients in `TOPG` and `BOTG`.

## Files
- `code/demo.html` runs on its own and loops in 6.6s; wide 1920x1080 or `?w=1080&h=1920`.
- `media/poster.jpg`
