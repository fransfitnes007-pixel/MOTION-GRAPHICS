---
name: odometer-number-roll-digit-column-translate
description: "A large figure whose digits roll up like a slot machine or odometer and land on the final value, each column a little later than the one before, beside a row of smaller figures that count up. Reach for it when one number is the headline of the section."
---

# Odometer number roll

**Code name:** Digit column translate.

## What you see
A white glass card with a case-study title on the left. On the right, a pale green tile holds a 60px figure, "$1,284,500", in dark green. Every digit sits in its own one-character window and is a tall strip of 0 to 9 repeated; the strips slide upward at different times so the figure resolves from the left, the last digit still turning after the first has landed. Commas and the dollar sign stay put. Under the tile, three white tiles count up from zero to 48.2M, 312 and 9.4K over 1.5s.

## When to use it
One headline number that should feel earned: revenue, views, payouts. Needs a tabular, monospaced-width font setting. Wrong for numbers that change often, or lists of many figures (use the count-up tiles), because a roll on every number turns to noise.

## How it works
Each digit column is `overflow-hidden`, `height: 1em`, `width: 0.60em`. Inside it, a `motion.span` holds `stops + 10` stacked 1em lines cycling `k % 10`, where `stops = cycles * 10 + digit` and `cycles = 2`. It animates `y` from 0 to `-stops em`, so the digit lands on the target after two full turns. The duration grows with the column index, which is what makes the figure resolve left to right.

```tsx
<motion.span initial={{ y: 0 }} animate={inView ? { y: `-${stops}em` } : { y: 0 }}
  transition={{ duration: duration + i * 0.07, ease: [0.16, 1, 0.3, 1] }}>
```

Two safety nets in the source matter for real use: if the in-view observer never fires within 3s, or the roll has had well over its own duration, the component prints the plain figure instead of leaving columns parked on 0 (which would read as "no revenue"). With reduced motion it prints the figure at once. The smaller tiles use `CountUp`: cubic ease-out `1 - (1 - p)^3` over 1500ms, with the prefix and suffix kept static.

## Numbers that matter
| | |
|---|---|
| Figure | 60px (sm:text-6xl), semibold, -.025em, success green #166534 |
| Column | height 1em, width .60em, overflow hidden, tabular numbers |
| Roll | cycles 2, duration 1.5s + index x .07s, ease [.16, 1, .3, 1] |
| Tile | bg success/10, rounded-3xl, 24px padding; label 12px semibold uppercase tracking-wider |
| CountUp | 1500ms, cubic ease-out, grouping on when the value is 1000 or more |
| Fallbacks | plain figure after 3s with no in-view event, and for reduced motion |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The value string; any digits and symbols work, non-digits stay still.
- `cycles` for a longer or shorter roll and `duration` for the speed; keep the .07 stagger.
- The colour: it inherits text colour, so a brand colour is one class.
- Swap the tile background for white glass when the page has no green.

## Files
- `code/demo.html` runs on its own and loops. Figures and the case-study title are invented placeholders.
