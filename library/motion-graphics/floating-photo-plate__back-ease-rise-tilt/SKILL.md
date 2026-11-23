---
name: floating-photo-plate-back-ease-rise-tilt
description: "Rounded photo cards that slide 90px into place with an overshoot, slightly tilted in 3D, with a gold PHOTO caption underneath. Use it to drop archive photos or screenshots into a layout."
---

# Floating photo plate

**Code name:** Back-ease rise with tilt.

## What you see
Over a dark gold-lit stage, a small portrait plate drops in from 90px above (0.75s), then a second one. A larger 16:9 photo plate slides up from below, tilted 8 degrees on Y and 4 on X, with a deep shadow and a 1.5px inner highlight. 0.6s later a caption fades in under it: "PHOTO" in tracked gold capitals and a grey description. The photo inside keeps zooming at 0.6% per second.

## When to use it
Evidence photos, archive images, a screenshot beside a headline. Works for any rectangular image. Use `dir: -1` for plates that should drop from above.

## How it works
`plate(el, t, opts)` positions a fixed-size rounded box and animates it with `tf()`:

```js
const ki = backS(p(t, t0, t0 + 0.75), 1.4), ko = p(t, out, out + 0.5)
im.style.transform = `scale(${zoom + (t - t0) * 0.006})`           // slow push on the photo itself
tf(el, { x, y: y + (1 - ki) * 90 * S * dir, s: lerp(0.86, 1, ki) * s * lerp(1, 0.94, ko), rx, ry, a: a * p(t, t0, t0 + 0.3) * (1 - ko) })
```
`tf` composes `translate3d rotate rotateX rotateY scale`. There is no perspective on the parent, so the tilt reads as a gentle foreshortening, not a card flip. The plate's look is a 28px radius, `box-shadow: 0 80px 160px -50px rgba(0,0,0,.9)` and a 1.5px white 10% inset ring, plus an `.edge` overlay with an inner shadow. Captions use `caption()`, which fades and rises 14px over 0.5s.

## Numbers that matter
| | |
|---|---|
| Travel | 90px over 0.75s, `backS(1.4)`; up for `dir: 1`, down for `dir: -1` |
| Scale | .86 to 1; exit .94 over 0.5s |
| Tilt | bedroom plate ry -8, rx 4; portraits 0 |
| Sizes | portraits 150px by 1.34x; photo plate 38% of the width |
| Caption | 22px, gold bold label tracking .18em, grey text #cfd2da |

## Sound
A whoosh (`whoosh.wav`, volume 0.5) cued on every plate.

## Adapt it
- The photo, size (`w`, `h`) and position.
- `ry`/`rx` for tilt, `dir` for entry direction, `zoom` for the crop.
- Caption wording; keep the gold label.

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. Playfair Display (SIL Open Font License, from Google Fonts) is copied into `code/fonts/` because the serif headline is half the look. Small labels suit SF Pro Display; the demo uses the system font stack instead. The demo draws gradient placeholders in CSS instead of photographs.
- `code/fonts/` holds the fonts the demo loads.
