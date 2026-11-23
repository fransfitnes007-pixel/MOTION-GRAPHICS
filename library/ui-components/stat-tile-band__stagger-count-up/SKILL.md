---
name: stat-tile-band-stagger-count-up
description: "A row of four frosted-glass stat tiles that rise in 70 milliseconds apart while each figure counts up from zero. Reach for it right under a hero as a proof band."
---

# Stat tile band

**Code name:** Stagger count up.

## What you see
Four rounded glass tiles in a row, each with a big semibold figure over a small grey label. They start 18px low and transparent, then rise into place in sequence, 70ms apart over .6s each. As they rise, the figures count up from 0 to their final values over 1.5s, easing out so the last digits arrive slowly, with the "+", "M" and "$" kept in place.

## When to use it
A proof band under the hero or above pricing. Works with two to four figures; each should read in under a second. Wrong with long labels (they wrap and break the row) or with figures that cannot be rounded, because the count-up passes through numbers that were never real.

## How it works
A `Stagger` wrapper sets `staggerChildren: 0.07` and starts when it scrolls into view (`whileInView`, `once`, margin -60px). Each tile is a `motion.div` using the shared `item` variant, the same as `Reveal`: `hidden: { opacity: 0, y: 18 }` to `show: { opacity: 1, y: 0, transition: { duration: 0.6, ease: [0.22, 1, 0.36, 1] } }`. `CountUp` parses the string with a regex, `^([^\d]*)([\d,]*\.?\d+)(.*)$`, keeps prefix and suffix, counts the number from 0 with `1 - (1 - p)^3`, and re-applies grouping and decimals with `toLocaleString`.

Two guards stop a figure ever being shown as 0 for good: after 3s with no in-view event it prints the final value, and a timer sets the final value 150ms after the animation should have finished in case the frame loop was paused (a background tab).

## Numbers that matter
| | |
|---|---|
| Tile | `glass` (white/55, blur 24px, white/70 border), rounded-3xl, 20px padding |
| Figure | 36px at lg, semibold, -.025em, tabular numbers |
| Label | 14px medium, ink-3 |
| Stagger | .07s between tiles |
| Reveal | opacity 0 to 1, y 18 to 0, .6s, ease [.22, 1, .36, 1] |
| CountUp | 1500ms, cubic ease-out |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The four values and labels; the parser handles `$`, `,`, `.`, `K`, `M`, `B` and `+`.
- The stagger interval (.07) and the count duration (1500).
- Columns: `grid-cols-2 lg:grid-cols-4` collapses to 2 by 2 on phones.
- Use `glass-strong` for more contrast over a busy background.

## Files
- `code/demo.html` runs on its own and loops. The figures are invented.
