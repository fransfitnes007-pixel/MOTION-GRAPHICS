---
name: pastel-drifting-blobs-background-sine-drift-blur-110
description: "A pale grey-white ground with three huge pastel blobs (lavender, pink, ice blue) blurred to soft clouds, drifting slowly on sine paths behind the content. Reach for it as the base layer of any light, airy video."
---

# Pastel drifting blob background

**Code name:** Three blurred circles on slow sine drift.

## What you see
Behind everything, a flat `#f4f5f7` ground carries three very large soft colour clouds: a lavender one (`#dfe3ff`) off the top-left corner, a pink one (`#ffe1ec`) at the right, and an ice-blue one (`#dff6ff`) low at left of centre. Each is a circle 50 to 62% of the frame's long side, blurred by 110px and held at 62 to 75% opacity, so they read as washes of colour, not as shapes. They never stop moving: each wanders 30 to 50px on its own slow sine and cosine, with periods of 18 to 25 seconds, so no two frames match and it never loops visibly. Content sits on top untouched.

## When to use it
The base layer of a light product video, a UI walkthrough or a name reveal: it gives a white screen depth without competing with the text or screens. It is the light sibling of the dark glow orbs. Wrong behind photographs or video, where it just greys them.

## How it works
Three divs with `border-radius: 50%` and `filter: blur(110px)`. Each frame sets only a translate and an opacity from sines of time, so every frame is a pure function of `t`.

```css
.blob { position: absolute; left: 0; top: 0; border-radius: 50%; filter: blur(110px) }
```
```js
const M = Math.max(W, H)                                    // blob size is relative to the long side
tf(b1, -0.16 * M + Math.sin(t * 0.35) * 40, -0.2 * M + Math.cos(t * 0.3) * 30); b1.style.opacity = 0.75
tf(b2, W - 0.34 * M + Math.cos(t * 0.28) * 40, H * 0.3 + Math.sin(t * 0.33) * 40); b2.style.opacity = 0.62
tf(b3, W * 0.25 + Math.sin(t * 0.25 + 1) * 50, H - 0.3 * M + Math.cos(t * 0.31) * 30); b3.style.opacity = 0.65
```

Sizes are 0.62, 0.56 and 0.5 times the long side, so the same layer fits a 16:9 and a 9:16 frame. A large blur on a big layer is the most expensive thing on the page: moving only the transform keeps it cheap. In this demo the positions are rounded to whole pixels, because Chrome rasterises a blurred layer slightly differently for fractional offsets depending on which frame came before, and the library checker compares exact pixels. A real render does not need to round.

## Numbers that matter
| | |
|---|---|
| Ground | `#f4f5f7` |
| Blob 1 | `#dfe3ff`, size .62 x long side, opacity .75, at (-.16, -.2) x long side, drift sin(.35t) x 40 and cos(.3t) x 30 |
| Blob 2 | `#ffe1ec`, .56, opacity .62, at right (W - .34 x long side, .3H), drift cos(.28t) x 40 and sin(.33t) x 40 |
| Blob 3 | `#dff6ff`, .5, opacity .65, at (.25W, H - .3 x long side), drift sin(.25t + 1) x 50 and cos(.31t) x 30 |
| Blur | 110px on all three |

## Site version

| | |
|---|---|
| Blob 1 | 608px, `#dfe3ff`, opacity .7, top -160px, left -128px, delay 0 |
| Blob 2 | 544px, `#ffe1ec`, opacity .6, top 33%, right -160px, delay -6s |
| Blob 3 | 480px, `#dff6ff`, opacity .6, bottom 0, left 33%, delay -12s |
| Blur | 64px (Tailwind `blur-3xl`) |
| Drift | 18s ease-in-out infinite; at 50%, `translate(40px, -30px) scale(1.08)` |
| Base | `#f4f5f7` plus a white radial wash at the top |

Use it behind any `glass` surface: frosted panels only read as glass with soft colour behind them.

## Sound
Silent.

## Adapt it
- The three colours: pick a palette of light tints around your brand colour.
- Opacities and blur radius for a stronger or softer wash.
- Speed: the multipliers `0.25` to `0.35`.
- Ground colour.

## Files
- `code/demo.html` runs on its own (8s, not periodic).
