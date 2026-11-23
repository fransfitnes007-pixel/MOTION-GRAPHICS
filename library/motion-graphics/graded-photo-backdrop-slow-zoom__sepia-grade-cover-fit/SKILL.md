---
name: graded-photo-backdrop-slow-zoom-sepia-grade-cover-fit
description: "Full-screen photos that dissolve into each other while each pushes in 12%, with a warm desaturated grade and a bottom shade for text. Use it as the moving background of a scene made of stills."
---

# Graded photo backdrop with slow zoom

**Code name:** Sepia grade, cover-fit.

## What you see
A garden photo dissolves in (0.6s) and drifts toward you. At 66.75s it is replaced by a wall with orange window light, which was not graded because it is already a stylised plate. Each photo scales from 1.0 to 1.12 over its time on screen plus one second. A dark shade runs from 25% black at the top, clear at 35%, 20% at 60%, up to 92% at the bottom, so captions stay legible.

## When to use it
Any stills-based sequence: documentary, real estate, history, a story told over photographs. A graded plate behind cards or text. Not for video footage.

## How it works
`bg(name, t, opts)` cover-fits a 16:9 image (2048 by 1152) into whatever W by H the canvas is, then animates only transform and opacity:

```js
const sc = Math.max(W / iw, H / ih) * (grade ? 1.02 : 1)
im.style.filter = grade ? 'contrast(1.08) saturate(.82) brightness(.9) sepia(.12)' : ''
im.style.transform = `scale(${lerp(zoomFrom, zoomTo, p(t, t0, t0 + dur))})`
tf(el, { a: a * p(t, t0, t0 + 0.6) * (1 - p(t, out, out + 0.6)) })
```
Set each photo's `out` to the next photo's start minus 0.15s so the fade-out and fade-in overlap. `dur` is the length of the push; a good default is the photo's time plus 1s so it never stops moving. `y` shifts the crop vertically (a portrait plate moves up 4% of the height).

## Numbers that matter
| | |
|---|---|
| Grade | contrast 1.08, saturate .82, brightness .9, sepia .12 |
| Zoom | 1.0 to 1.12 (house plate 1.0 to 1.08) |
| Dissolve | 0.6s fade each way, overlapping 0.45s |
| Shade | `linear-gradient(180deg, rgba(7,8,11,.25), 0 at 35%, .2 at 60%, .92 at 100%)` |

## Sound
Silent by itself. It pairs with narration, a low drone and a thud on cards.

## Adapt it
- The photos and their order.
- `grade: false` for images already treated.
- `zoomTo` for a stronger or weaker push, `shade` for text-heavy frames.

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. The demo draws gradient placeholders in CSS instead of photographs.
- `code/fonts/` holds the fonts the demo loads.
