---
name: glass-panel-fly-through-perspective-z-stack-blur
description: "Five frosted glass interface panels stacked in depth with the camera flying forward through them; each panel blurs and fades as it passes and the last, with a call to action, stops in focus. Reach for it to introduce a product's range of screens in one move."
---

# Glass panel fly-through

**Code name:** Perspective Z stack blur. **From:** original build for this library.
Original code; informed by the structure of popular AI-made showreels (see motionvideo.xyz and revid.ai).

## What you see
On a dark stage with two soft light pools (blue, violet), a stack of five translucent panels fades in at 0 to 0.6 s, the nearest ones sharp and the far ones softly blurred. From 0.7 s to 4.0 s the camera pushes forward on an ease-in-out curve while weaving to line up with each panel: a revenue figure with bars, an activity list, a growth line, a team row, then a closing card with a title and a button. A panel in front of the focus plane blurs up to 30 px and fades out as it goes past the lens; panels still far ahead are blurred up to 9 px. A slight parallax tilt (up to 13 degrees) eases to zero as the camera arrives, so the last panel lands flat and sharp. It holds to 5.3 s, then fades so the loop restarts clean.

## When to use it
Showing several screens or steps in one continuous move, the hand-off from a problem beat into the product, or a reveal of what is inside an app. It is wrong where each panel must be read in full: they are in focus for only a fraction of a second each.

## How it works
Real CSS 3D, driven by a function of time. The stage has `perspective: 1100px`; a zero-size `.world` with `transform-style: preserve-3d` holds five panels, each given a fixed `translateZ(-i * 440px)`. Each frame the world is moved, not the panels:

```js
world.style.transform = `rotateX(a) rotateY(b) translate3d(-camX, -camY, camZ)`
```
`camZ` goes from -340 to `4 * 440` on `eio`; `camX` and `camY` smoothstep between the offsets of the two nearest panels so the camera lines up with each in turn. Depth of field is a blur keyed to `z = camZ - i * 440`, the panel's distance from the focus plane: `passed = seg(z, 60, 600)` gives `blur = passed * 30` and opacity `1 - passed`; `ahead = seg(-z, 0, 1500)` adds up to 9 px blur and a 55 % fade for panels far in front of the camera. A panel with `z` beyond 86 % of the perspective distance is hidden. The frost is faked with a diagonal translucent white gradient, a 1.5 px light border, an inset top highlight and a faint sheen band, so nothing depends on `backdrop-filter`.

## Numbers that matter
| | |
|---|---|
| Panels | 5, 1200x720 (960x900 tall), radius 30 px |
| Spacing | 440 px in z, perspective 1100 px |
| Camera | 0.7 s to 4.0 s, `eio`, z from -340 to 1760 |
| Blur | passed up to 30 px, ahead up to 9 px |
| Tilt | rotateY 9 sin(1.15 t) + 4, rotateX 5 cos(0.9 t), eased to 0 by 4.8 s |
| Colours | ink `#0b0b10`, paper `#f2f2f4`, accent `#6aa8ff` |

## Sound
Silent in the demo. A soft whoosh for every panel that passes the lens (five, about 0.4 s apart at the start, bunching toward the end), and a low settle thud when the last panel lands.

## Adapt it
- The `content` array: five HTML strings, one per panel (screenshots can go in as CSS gradients or SVG).
- `N`, `GAP` and the camera times `T0`, `T1`.
- Accent colour `#6aa8ff` and the two orb colours.
- `OX` and `OY`: where each panel sits, which shapes the weave of the camera path.

## Files
- `code/demo.html` runs on its own, loops every 6 s, composes at 1920x1080 and at `?w=1080&h=1920`.
- `media/poster.jpg`
