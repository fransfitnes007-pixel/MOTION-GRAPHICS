---
name: card-flip-overshoot-rotatey-spring-back-face
description: "A tall dark green card with a date line, \"I'm feeling balanced\" and an SVG flower that flips in 3D on tap with a spring overshoot to a pale back face, with page dots switching. Use for check-ins, flash cards and reveal cards."
---

# Card flip with overshoot

**Code name:** RotateY spring back face. Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
On a light grey stage, a 500x760 dark green card shows "Mon, 14 Oct", "I'm feeling balanced" and a pink flower drawn in SVG. Two page dots sit below, the first a wide capsule. At 0.45s a translucent finger taps the card and ripples. The card dips 3% on press, then at 0.85s turns over around its vertical axis (perspective 2100px) in 1.15s, rising toward the viewer by about 90px while it turns and casting a shrinking shadow. It passes 180 degrees by about 9 degrees and settles, showing a pale sage back with a check badge and "First check-in feeling balanced". The dots swap with the turn. A second tap at 3.35s flips it back with the same spring, past zero and settling.

## When to use it
Reveal cards, daily check-ins, flash cards, before/after pairs. Wrong when both faces need to be read at once.

## How it works
One element holds `transform-style: preserve-3d`; the front face and the back face (pre-rotated 180deg) both use `backface-visibility: hidden`. The angle is a spring of normalised time:
```js
ang = 180 * spring(seg(t, F1, F1 + 1.15), 8, 8.5)      // 1 - e^(-8x) cos(8.5x): overshoots about 5%
card.style.transform = `translateZ(${lift}px) rotateY(${ang}deg) scale(${s})`
```
A black overlay on each face fades in with `|sin(angle)|` to shade it edge-on, the floor shadow scales with `|cos(angle)|`, and the dot widths interpolate with `clamp(ang/180)`.

## Numbers that matter
| | |
|---|---|
| Spring | `spring(x, 8, 8.5)`, 1.15s, peak about 189 degrees |
| Perspective | 2100px, origin at the card centre |
| Card | 500x760, radius 46 (x1.32 in the tall layout) |
| Lift | up to 90px translateZ, scale +5% mid-turn, press scale 0.97 |
| Taps | 0.45s and 3.35s, flip starts 0.4s later |

## Sound
A soft paper flick at the start of each turn and a tiny thud as it settles.

## Adapt it
- `k` and `f` in `spring(x, 8, 8.5)`: lower `f` and higher `k` for less overshoot.
- Both face blocks (colours, copy, the `flower()` SVG).
- `perspective` for a stronger or flatter turn.
- Use a drag (angle follows the finger) instead of a tap by driving `ang` from a path.

## Files
- `code/demo.html` runs on its own and loops in 5.6s.
- `media/poster.jpg`
