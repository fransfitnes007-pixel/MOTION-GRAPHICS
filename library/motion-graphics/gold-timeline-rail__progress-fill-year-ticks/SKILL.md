---
name: gold-timeline-rail-progress-fill-year-ticks
description: "A thin rail that fills with gold as big serif years pop onto it one by one, the last in red, with portrait plates and a closing headline. Use it for a history or milestone sequence read out by a narrator."
---

# Gold timeline rail

**Code name:** Progress fill with year ticks.

## What you see
A grey rail runs across the frame at 40% height. A gold fill with a glow starts at the first dot: "1882" with a two-line caption above it. The fill eases to the next tick, which pops (scale .6 to 1 with overshoot): "1907", then "1927". Small portrait plates drop in under the first and third ticks. The last tick, "1981", has a red dot that pulses. Then a bedroom photo plate rises, a caption fades in, and "In the bedroom." and "Her bedroom." slam in at the left. On the 9:16 canvas the rail is vertical at the left with years and captions beside the dots.

## When to use it
A voiceover that walks through dates. Four or five ticks is the sweet spot. Each tick arrives when the narrator says it, so the times are scaled by the voice length (see `voiceover-driven-scene-schedule__max-min-vo-duration`).

## How it works
Beat times are offsets times `r = (tEnd - t0) / 19`, so the whole scene stretches with the voice. Tick `i` sits at `lerp(rx0, rx1, i / (n-1))`. The fill length is the progress through the ticks:

```js
let prog = 0
for (let i = 0; i < items.length - 1; i++) { const a = items[i].at, b = items[i + 1].at
  if (t >= a) prog = lerp(i / (items.length - 1), (i + 1) / (items.length - 1), eio(p(t, a + 0.3, b))) }
```
Each tick: `k = backS(p(t, it.at, it.at + 0.55), 1.8)` scales the group from .6; the red dot pulses with `1 + .12 * sin((t - it.at) * 9)`. The dot is 22px with a 6px halo and a gold glow. Year numerals are Playfair 800 at 86px, captions SF Pro 26px grey. The first caption left-aligns, the last right-aligns, so they stay inside the margin. The demo compresses a 21.5s timeline to 10.5s by passing a smaller `tEnd` (every beat scales by `r`).

## Numbers that matter
| | |
|---|---|
| Rail | 6px, rgba(255,255,255,.14); fill `#e8b43a` to `#f7d873` with a 24px glow |
| Dot | 22px gold, red `#d8463a` for the last |
| Year | Playfair 800, 86px wide / 96px tall, white |
| Beats (r = 1.13) | ticks at 0.5s, 5.6r, 8.4r, 11.4r; bedroom plate 14.2r; slams 14.6r and 16.4r |
| Fill move | `eio` from 0.3s after a tick to the next tick |

## Sound
A click (`click_002.ogg`, 0.55) on every tick, a whoosh on each plate, a thud on the two closing lines.

## Adapt it
- The `items` array: year, label, `at`, and `red` for the emphasis tick.
- `M` (margin) and the rail y (`H * 0.4`).
- Plate images and the closing slams.
- The gold gradient on `#railfill`.

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. Playfair Display (SIL Open Font License, from Google Fonts) is copied into `code/fonts/` because the serif headline is half the look. Small labels suit SF Pro Display; the demo uses the system font stack instead. The demo draws gradient placeholders in CSS instead of photographs. The year labels in the demo are neutral placeholders.
- `code/fonts/` holds the fonts the demo loads.
