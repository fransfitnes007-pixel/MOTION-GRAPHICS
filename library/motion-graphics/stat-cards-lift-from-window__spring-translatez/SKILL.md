---
name: stat-cards-lift-from-window-spring-translatez
description: "A row of three small stat cards separates from the bottom of a product window, one after another, springing forward toward the viewer with a slight rotation straightening out, as if the numbers were lifted off the screen."
---

# Stat cards lifting out of a window

**Code name:** Spring translateZ.

## What you see
Cards of 348x126px sit over the lower part of the dashboard window, hidden at first. Starting at 6.23s, 0.1s apart, each one moves up 40px into place (then 14px further), comes 160px toward the camera and straightens from -10 degrees rotateY, with a bounce from `spring(k=7, f=11)`. They fade out together at 7.2s to 7.5s so the camera move that follows is clean.

## When to use it
To call out the three numbers that matter on a dashboard, one per spoken word or beat. It only reads when the cards overlap the screen they came from, so they should be crops of it, not new design. Do not use more than four.

## How it works
Each card is its own element with its own `perspective(1600px)` in its transform, so translateZ shows as a size increase rather than a shared 3D scene.

```js
const p = spring(seg(t, RUN + .05 + i * .1, RUN + .65 + i * .1), 7, 11), o = ei(seg(t, 7.2, 7.5))
S(c, { left: (868 + i * 336) + 'px', top: (612 - i * 4) + 'px', opacity: clamp(p * 1.5) * (1 - o),
  transform: `perspective(1600px) translateZ(${p * 160}px) translateY(${(1 - p) * 40 - p * 14}px) rotateY(${-10 * (1 - p)}deg)` })
```
The cards are meant to be close crops (322x117 enlarged 8%) of a real dashboard screenshot; the shadow and 1px violet outline make them feel like separate layers. The demo stands them in with drawn cards. They fade out at 7.2s in the timing above; the demo holds them to 8.3s so the loop shows the settled state.

## Numbers that matter
| | |
|---|---|
| Card | 322x117 scaled 1.08 (348x126), radius 18px, shadow `0 40px 90px -24px`, 1px outline `rgba(167,139,250,.35)` |
| Positions | left 868 + 336i, top 612 - 4i |
| Spring | k=7, f=11, 0.6s, 0.1s stagger |
| Z | 160px toward the camera; start 40px low, finish 14px high |
| Rotation | rotateY -10 to 0 degrees |

## Sound
A soft pop per card works well.

## Adapt it
- The card crops or contents, `STATS`.
- Stagger (0.1s) and the Z distance.
- `top` offsets for a stair-step look.
- The fade-out time.

## Files
- `code/demo.html`
