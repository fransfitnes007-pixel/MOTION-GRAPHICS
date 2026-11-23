---
name: payout-breakdown-stacked-bar-base-cpm-bonus
description: "A payout card: creator and total at the top, a single 12px stacked bar split into base, CPM and bonuses, and a legend of coloured dots with amounts above a Total line. Use it to explain how an amount is made up."
---

# Payout breakdown bar

**Code name:** Stacked share bar with legend rows and total.

## What you see
A card with the creator's avatar and name at the left and "$6,014" in 30px bold at the right with an "Accruing, due Jan 4" pill. Below, "PAYMENT BREAKDOWN" in tracked uppercase, a pill-shaped bar made of violet (base), sky (CPM) and amber (bonuses) segments that grow from zero over 0.7s, and three legend rows with the matching dots and amounts. At 3.4s extra CPM lands: the sky segment grows, the other two shrink in share, and the total rises.

## When to use it
Anything that is a sum of parts: pay, price, budget. It is easier to read than a donut when the parts have names and amounts.

## How it works
```tsx
<motion.div initial={{ width: 0 }} animate={{ width: `${(p.v / Math.max(1, s.total)) * 100}%` }}
  transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }} className={p.c} />
```
Segments are `bg-rv-purple`, `bg-sky-400`, `bg-amber-400` inside `flex h-3 overflow-hidden rounded-full bg-white/5`. Legend rows are `flex justify-between text-sm`, the muted name with a `size-2 rounded-full` dot, and a tabular amount. The total row has a top border and `text-lg font-bold`. `PayStructure` (also in the file) is the companion list of three numbered rules with a green "Max per video" line.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Bar 12px high, full radius; segments 0.7s `[0.16,1,0.3,1]`.
- Segment colours `#8B5CF6`, `#38BDF8`, `#FBBF24`.
- Legend text 14px; total 18px bold.
- Card 20px padding.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `PARTS`: name, amount, colour.
- The `k2` extra amount at 3.4s shows how the bar re-balances.
- Amount format `usd()`.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
