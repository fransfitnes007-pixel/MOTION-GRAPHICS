---
name: graph-scrub-highlight-glow-clip-path-split-line
description: "A dark finance card with a big rolling-digit balance and a jagged line chart that glows left of a scrubbing finger and dims to the right, with a dot riding the line. Use for portfolio, balance or analytics charts."
---

# Graph scrub highlight glow

**Code name:** Clip path split line. Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
A 1240x780 dark card shows "Total balance", the number $1,234,567 in 128px bold, a green percentage pill and a 56-point jagged green line with a faint area fill. A translucent finger lands at 0.4s and presses at 0.9s: a vertical guide line with a date chip springs from the right end to the finger, the part of the line left of the guide gets a blurred green glow, the part to the right dims to 20%, and a glowing white dot sits on the line at the guide. Dragging (1.2 to 2.8s right, 3.6 to 4.3s back) the number rolls: every digit scrolls like an odometer and the percentage follows. At 4.4s the finger lifts and the guide, dot, glow and number spring back to the full line and $1,234,567 by 5.3s.

## When to use it
Portfolio or balance cards, analytics, any chart where the value under the finger matters. Wrong for charts with many series.

## How it works
Two copies of the same SVG line are stacked. The bright copy sits in a wrapper clipped with CSS `clip-path: inset(-60px (width - x)px -60px -60px)`, so everything left of the split stays bright and a blurred copy inside it gives the glow; the dim copy underneath fades to 20% while pressed.
```js
x   = lerp(endX, fingerX, spring(seg(t, P0, P0 + .4), 8, 9))     // press; release springs x back to endX
dot = (x, yAt(x));  value = toMoney(valAt(x(t - .05)))           // number lags the line a touch
off = (m % 10) + smoothstep((frac - .78) / .22)                  // per digit place k: m = floor(v / 10^k)
strip.style.transform = `translateY(${-off * lineHeight}px)`
```
Each digit is a 0 to 9 strip (plus a repeated 0) in an overflow-hidden column, so a digit only rolls when the places below it wrap. Data comes from a seeded integer hash.

## Numbers that matter
| | |
|---|---|
| Card | 1240x780 wide, 960x1010 tall, radius 44 |
| Chart | 56 points, line 5px, glow blur 11px, dimmed to 20% |
| Press spring | `spring(x, 8, 9)` over 0.4s; release `spring(x, 7, 10)` over 0.9s |
| Number | 7 digit columns, 128px, 0.6em wide, odometer roll starts at 78% |
| Timeline | press 0.9s, sweep to 2.8s, back to 4.3s, release 4.4 to 5.3s |

## Sound
A soft tick per few dollars of change while scrubbing, a low click on press and release.

## Adapt it
- `GREEN` for another accent; use red when the trend is down.
- `toMoney` scale and the digit count (`strips`) for other magnitudes.
- `TRAVEL` keyframes for a different scrub path.
- The chip text and the percentage label.

## Files
- `code/demo.html` runs on its own and loops in 6s.
- `media/poster.jpg`
