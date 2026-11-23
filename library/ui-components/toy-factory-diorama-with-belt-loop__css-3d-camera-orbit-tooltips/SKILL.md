---
name: toy-factory-diorama-with-belt-loop-css-3d-camera-orbit-tooltips
description: "An interactive 3D workshop scene: a dark slab with five small orange-and-white machines around an oval conveyor belt, orange cards riding the loop, station tooltips and a camera dolly into close-up. Reach for it as a hero that explains a pipeline as a physical machine."
---

# Toy factory diorama with a belt loop

**Code name:** CSS 3D camera orbit, station tooltips.

## What you see
A black page with a thin app header (logo, name, "Machine running" with an orange dot) and a mode bar at the bottom (Assembled is lit orange; Cutaway, Stations, One order beside it) over a row of view names (Overview, Side, Top, Station, Flight).

In the middle sits a dark glossy slab seen from about 57 degrees above, with screws in the corners and "No. 001" on a plate. On it: a white projector gantry with an orange lid and two film reels at the left, a low black unit with white pins behind it, a monitor on a stand showing a tiny landing page, a green "+ $29" sign, an orange-lidded cabinet with an orders screen at the right, and a white register with a keypad in the middle. An oval conveyor runs around the register; white rails, dark treads moving, and six white cards with an orange tile and a play triangle ride around it.

In the 9s loop the machine sits small for 3s while a pointer touches the cabinet and a tooltip ("Orders") fades in, then the camera swings in over about 1.8s to a close-up with the slab filling the frame and a "Checkout" tooltip at the register, then pulls back out. The original is a live 3D scene you can orbit; the video shows the same pointer-driven tooltips and a camera move.

## When to use it
A landing-page hero for a product that is a pipeline or a set of steps (from idea to payment), where each station can carry a tooltip and a link. Good for a workshop, course or "how it works" page. It is a heavy scene in the original; for a light page use a flat diagram instead. Not for pages that need to load fast on phones.

## How it works
The original is a lit 3D scene with real models (the library is not visible from the video or the usage example). This demo is a simplification: CSS 3D. One `perspective` wrapper holds a world that is rotated and scaled for the camera. Everything sits on a plane with x right, y toward the viewer, z up, and two helpers build the parts:
```js
box(parent, x, y, z, w, d, h, [top, side, end])   // five faces, side shading baked in as three greys
stand(parent, x, y, z, w, h, css, rz)             // upright panel: translateZ(z) rotateZ(rz) rotateX(-90deg), origin bottom centre
```
The belt is one flat SVG on the slab: dark stroked ellipse, a dashed ellipse for the treads whose `stroke-dashoffset` is `-t*34`, and two white rails. Cards are standing panels placed on the same ellipse: `x = cx + rx*cos(u)`, `y = cy + ry*sin(u)`, with `u = 2*pi*((t/period + i/n) % 1)`.

The camera is a keyframe list `[t, scale, rotZ, panX, panY, rotX]` eased with `eio` between rows and written to the world transform: `scale(s) rotateX(rx) rotateZ(rz) translate3d(px,py,0)`. Tooltips are plain DOM over the scene, faded by a window per station.

Simplified from the original: that is a lit 3D scene with models and shadows; this is flat-shaded CSS boxes, no reflections, and the tooltip positions are scripted, not tied to the 3D objects. The orbit is two keyframed camera moves, not free rotation.

## Numbers that matter
| | |
|---|---|
| Canvas | 1280 x 844, slab 1000 x 640 x 34 |
| Camera | pitch 57 degrees, overview scale .5, close-up scale 1.2, 2400px perspective |
| Camera timing | hold to 3.0s, dolly in 3.0 to 4.8s, drift to 7.6s, back out by 9s |
| Belt | ellipse 300 x 118, rails 19px outside the track, tread speed 34 units/s |
| Cards | 6, 50 x 66, one lap per 14s, evenly spaced |
| Accent | #ff7a1a lids, card tiles, active tab |
| Tooltip | 190px wide, 0.25s fade, a station at a time |

## Sound
Silent.

## Adapt it
- `CONFIG.accent`, the title strings and `CONFIG.stationNames` / `stationText` for your own product and steps.
- `CONFIG.cards` and `CONFIG.beltPeriod` for how busy the belt is.
- `CAM` (inside the script) for the camera moves, and `TIPS` / `PTR` for which station is highlighted when.
- Replace a station by editing its `box(...)` / `stand(...)` calls; the rest of the scene does not depend on it.

## Files
- `code/demo.html` runs on its own and loops. Placeholder art is CSS and SVG only.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Agentic Factory — Interactive 3D Machine" by eugeneshilow on 21st.dev (https://21st.dev/@eugeneshilow/components/agentic-factory-3d), MIT. This demo is an original recreation written from the public preview.
