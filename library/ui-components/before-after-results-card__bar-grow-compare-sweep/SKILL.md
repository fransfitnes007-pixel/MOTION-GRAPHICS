---
name: before-after-results-card-bar-grow-compare-sweep
description: "A glass result card: a green \"+312% gross sales\" badge, two progress bars that grow to the before and after figures, two small tallies, and a full-width image slider you drag to compare two monthly reports. Reach for it for a before-and-after proof of a result."
---

# Before and after results card

**Code name:** Bar grow and compare sweep.

## What you see
A large glass card. Left: a client name, a period, and a green pill with a trend arrow and a number counting up to +312%, over the words "gross sales", then two short paragraphs. Right: two labelled bars: a dark-grey one that grows to about a quarter of the track, a green one that grows to the full width, each with its dollar figure; below, two white tallies. Across the bottom, two report screenshots are stacked and clipped at a draggable handle. The handle sweeps left, then right, then back to centre, revealing the quiet month on the left and the record month on the right.

## When to use it
A results page that must show proof, not claim it: sales reports, dashboards, rankings. The slider needs two same-size images. Wrong where the screenshots contain private data you cannot show at full width.

## How it works
Bars wait for the card to enter the viewport (`useRevealed`) and then animate width: `initial={{ width: 0 }} animate={{ width: inView ? pct% : 0 }} transition={{ duration: 1.1, delay, ease: [0.22, 1, 0.36, 1] }}`, where `pct = max(8, value / max * 100)` so a small bar never vanishes. The before bar is `bg-ink/70`, the after bar `bg-success`.

The compare slider stacks the after image beneath and the before image on top, and clips the top one with `clipPath: inset(0 ${100 - pos}% 0 0)`. The handle is a 2px ink line at `left: pos%` with a 48px ink circle, white 2px border and two chevrons. Pointer events with `setPointerCapture` set `pos` from the pointer's x; the keyboard moves it 5% per arrow key. The demo animates `pos` on a timeline instead of a drag.

## Numbers that matter
| | |
|---|---|
| Card | `glass-strong`, rounded-4xl, 32px padding, columns 1.1fr and .9fr, gap 40px |
| Lift badge | bg success/10, rounded-2xl, 48px semibold figure, 11px uppercase label, icon 24px |
| Bars | 12px high, track white/70, before ink/70, after #166534, 1.1s, delays .1s and .3s |
| Tallies | rounded-2xl, bg white/60, 12px padding, label 10px uppercase, value 18px |
| Slider | aspect 1589 / 570, rounded-3xl, line 2px, handle 48px |
| Keyboard | left and right arrows move 5% |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The two images and their labels; keep identical aspect ratios.
- Bar colours: the after colour reads as the success token.
- The `max(8, ...)` floor for the smallest bar.
- Hide the two tallies by dropping the `dl` for a simpler card.

## Files
- `code/demo.html` runs on its own and loops. The report images are drawn in CSS with invented figures; the client name is made up.
