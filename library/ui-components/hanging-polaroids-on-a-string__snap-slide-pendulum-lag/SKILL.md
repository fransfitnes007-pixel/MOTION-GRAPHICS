---
name: hanging-polaroids-on-a-string-snap-slide-pendulum-lag
description: White page, a string with wooden pegs, and polaroid prints hanging from it that slide sideways one at a time, swinging as they go. Reach for it as a photo or portfolio carousel with a physical feel.
---

# Hanging polaroids on a string

**Code name:** Snap slide with pendulum lag.

## What you see
A plain white page. A thin brown string runs across it in a chain of shallow curves, peaking in the gaps between prints and sagging 64px under each one. Each polaroid (506 x 580, off-white paper, soft shadow, a serif-italic caption under a square-ish photo) hangs from a wooden peg clipped over the string at its lowest point. About two and a half prints show at once; the middle one is full size and the others are cut off by the frame edges.

The carousel steps one print at a time. A print rests in the middle for about 1.1s, then the whole line, string included, slides left by one pitch (536px) in 0.9s with an ease-in-out. While it slides every print swings from its peg: it tilts against the direction of travel, rocks back a little past rest, and settles. Each print also carries a fixed tilt of up to 1.5 degrees so the row never looks ruled. Slides are placeholder landscape pictures here; the original uses real photographs and the caption is the photo title.

## When to use it
A gallery or travel block where photos should feel pinned up rather than boxed. It works on a plain light page with big photos and one-line captions. It is wrong for dense image grids and for dark, glossy brands.

## How it works
One position value `s` (in slides) drives everything. It holds for `hold` seconds, then eases to the next integer:
```js
const pos = t => { const k = Math.floor(t / P), r = t - k * P; return k + eio(seg(r, hold, P)) }
```
Prints are placed on a ring by their offset from `s`, so the loop is seamless after six steps. The string is one SVG path of repeated quadratic curves, each between two print boundaries with its control point at `peak + 2 * sag`, so the lowest point sits where the peg is, and it moves with `s`.

The swing is a lag, not a physics step: the tilt of every print is the speed of the line a moment ago minus the speed a bit earlier, which gives a push one way and a smaller return the other way:
```js
swing = 34 * (s(t) - s(t - .12)) - 20 * (s(t - .12) - s(t - .32))     // degrees
rotate(baseTilt + swing)   // transform-origin at the peg, 50% 0
```
Because it is built from earlier values of a pure function, `render(t)` stays pure.

## Numbers that matter
| | |
|---|---|
| Canvas | 1280 x 960, prints 506 x 580, photo inset 21px, caption 22px Georgia italic |
| Pitch | 536px between print centres |
| String | peak at y 187, sag 64, 2.4px, #6f6358 |
| Step | hold 1.1s, slide 0.9s, ease-in-out cubic, 6 slides, 12s loop |
| Swing | up to roughly 6 degrees, coefficients 34 and -20, lags .12s and .32s |
| Peg | 15 x 46, wood gradient #c58f4f to #e0b27a |

## Sound
Silent.

## Adapt it
- `CONFIG.slides` for the titles and the placeholder colours; swap the `photo()` SVG for an `<img>` of your own.
- `CONFIG.hold` and `CONFIG.travel` for pacing; `CONFIG.swing` at 0 turns off the pendulum.
- `CONFIG.pitch` and `paperW` to change how many prints are visible.
- `CONFIG.sag` and `stringPeakY` for a tighter or looser string.

## Files
- `code/demo.html` runs on its own and loops. Placeholder art is CSS and SVG only.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Hanging Polaroid Image Carousel" by kedhareswer on 21st.dev (https://21st.dev/@kedhareswer/components/polaroid-line-carousel), MIT. This demo is an original recreation written from the public preview.
