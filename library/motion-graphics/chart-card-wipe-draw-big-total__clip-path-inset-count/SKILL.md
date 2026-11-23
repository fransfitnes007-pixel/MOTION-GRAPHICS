---
name: chart-card-wipe-draw-big-total-clip-path-inset-count
description: "An analytics page whips up from below and dims, the line chart lifts out of it to the centre and draws left to right as a 150px total above it counts up from zero. One growth number, one chart."
---

# Chart card wipes in with a big counting total

**Code name:** Clip-path inset wipe and count.

## What you see
An analytics page whips in from below. It dims, and its line chart lifts out to the centre at 1.3x and draws left to right as a 150px total above it counts up from zero, with a spaced lilac caption under the total. At the end everything whips left off the frame.

## When to use it
One growth number, one chart. "Views tracked" or any cumulative total. The wipe reads as the line being drawn, though the chart is a finished image.

## How it works
A `clip-path: inset(0 X% 0 0)` that shrinks from 100 percent to 0 reveals the card left to right; the same `eio` window drives the count so total and line finish together.

```js
const wipe = eio(seg(lt, .4, 1.4))
chart.style.clipPath = `inset(0 ${(1 - wipe) * 100}% 0 0 round 16px)`
total.textContent = fmt(12480200 * eo(seg(lt, .3, 1.5)))
```
Lifting uses the same `lift()` as the card lift-out skill.

## Numbers that matter
| | |
|---|---|
| Wipe | 0.4s to 1.4s, `eio` |
| Count | 0.3s to 1.5s, `eo` |
| Total | 150px weight 800, purple glow, at y 96 |
| Chart | 1336 x 396 lifted to (960, 650) at 1.3x |

## Sound
A suggested soundtrack is a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. 

## Adapt it
- The total and caption.
- The chart.
- Wipe direction (change the inset side).

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.
