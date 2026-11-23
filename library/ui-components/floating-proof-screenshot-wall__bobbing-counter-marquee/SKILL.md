---
name: floating-proof-screenshot-wall-bobbing-counter-marquee
description: "Two counter-scrolling rows of white glass cards holding payment slips and analytics screenshots, each card floating up and down on its own phase. Reach for it as a receipts wall."
---

# Floating proof screenshot wall

**Code name:** Bobbing counter marquee.

## What you see
Under a centred heading, two rows of screenshot cards glide in opposite directions with the edges faded. Payment slips are short (96px) and wide, analytics panels tall (230px); a card's width follows its screenshot's own aspect ratio, so the rows have an uneven, collected look. Every card sits in a white glass frame with 6px of padding and bobs 6 to 10px up and down on a 5.5 to 7.5 second cycle, staggered by .35 seconds per position.

## When to use it
Social proof made of screenshots: payments, dashboards, messages. It is meant to be glanced at, not read; a click opens each in a lightbox. Wrong when the screenshots hold small text that matters, or when there are fewer than about 10 (the page shows one non-looping row instead).

## How it works
One row height per kind, width from the image ratio: `h = kind === "payment" ? 96 : 230; w = round(item.w / item.h * h)`. With 10 or more items the list splits into even and odd rows; a row of 7 or more becomes an `InfiniteSlider` (`duration = row.length * 7`, `durationOnHover = row.length * 26`, odd rows `reverse`); shorter rows are plain horizontal scrollers so nothing shows twice.

```tsx
<motion.button animate={reduced ? undefined : { y: f.y }}
  transition={{ duration: f.d, repeat: Infinity, ease: "easeInOut", delay: (i % 5) * 0.35 }}
  style={{ width: w, height: h }} className="glass-strong group relative shrink-0 overflow-hidden rounded-2xl p-1.5 shadow-glass ...">
```

The images are `object-contain` on white inside `rounded-xl`, and scale 1.02 on hover. The demo draws payment slips and analytics panels in CSS with invented numbers.

## Numbers that matter
| | |
|---|---|
| Card heights | 96px payment, 230px analytics; width from aspect ratio |
| Frame | glass-strong, rounded-2xl, 6px padding |
| Row gap | 16px; rows have py-3 |
| Speed | half width in (cards x 7)s per row, hover (cards x 26)s, second row reversed |
| Bob | y -10, 8, -7, 9, -6 px over 6, 7, 5.5, 6.5, 7.5 s, delay (i % 5) x .35 s |
| Edge fade | mask 8% each side |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The two heights (96 and 230) for your screenshot types.
- The row split: keep rows above 7 cards or switch to the static scroller.
- Bob amplitudes; set `reduced` behaviour on for a still wall.
- Frame padding for a heavier or lighter bezel.

## Files
- `code/demo.html` runs on its own and loops. The screenshots are invented placeholder slips and charts.
