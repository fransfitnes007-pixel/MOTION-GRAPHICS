---
name: snow-cabin-ski-lift-diorama-three-points-snowfall
description: "A cosy low-poly winter scene in three.js: a log cabin with glowing windows and a pillared porch, snow-capped pines, a ski lift with chairs gliding along its cable, a steaming geyser and hot spring, and a drifting snowfall of 2000 points. Reach for it as a calm looping 3D backdrop with a winter or seasonal mood."
---

# Snow cabin ski lift diorama

**Code name:** Three points snowfall.

## What you see
Pale blue-grey haze and a snow-white ground rolling in gentle hills. A long log cabin with a peaked roof, four tall cream pillars on a porch, and warm yellow windows that breathe slightly, as if lit by a fire. A dark drive runs to the door. Snow-capped dark green pines stand around it. Behind, a row of ski-lift poles with a cable and blue chairs that travel along it and wrap. At left a rocky hot spring with a plume of steam rising from a geyser mound. White flakes fall continuously with a small side sway. The camera drifts slowly left and right in front of the cabin. A text sign floats in the sky.

The loop is 12 seconds. The chairs make one pass, the steam cycles two or three times, the camera makes one sway and the fire flickers, and every snowflake returns to its start, so the last frame joins the first.

## When to use it
A seasonal beat (holiday, winter sale, cold-weather clothing), a calm background behind a big headline, a quiet 3D idle for an app. The haze and low contrast mean text must sit on a panel or be large and white. It would be wrong for a tech-forward look.

## How it works
- Terrain: a 400x400 plane with 80x80 segments. Each vertex gets `z = sin(x*0.02)*3 + cos(y*0.03)*2 + sin(x*0.05 + y*0.04)*1.5` and normals are recomputed, which is the whole hills effect.
- Cabin: four stacked wall rows of 0.7-high logs every 0.8 units, a custom roof built from four triangles in a `BufferGeometry`, pillars as 16-segment cylinders. The app's glass windows are dark; here they are warm emissive planes plus two point lights, to get the cosy dusk read.
- Pines: a trunk cylinder plus four green cones, each with a flatter white cone on top as snow, 35 of them, none inside the cabin footprint.
- Snow: one `Points` object, 2000 positions, additive blending in the source. The app's `updateBiomes` lowers each flake by `dt * (0.8 + sin(i) * 0.4)` and drifts it sideways by `sin(elapsed + i * 0.1) * dt * 0.3`, respawning it near the top at a random spot when it reaches the ground. The demo keeps those speeds but gives every flake a fall band of `speed * DUR` units and wraps inside it, so each flake is back where it started after one loop. A soft round canvas sprite replaces the default square points.
- Steam: 90 points that rise 1.5 to 2.5 units a second to y 12 and restart low, while the material opacity pulses `0.3 + sin(elapsed * 2) * 0.15`. The demo uses a whole number of rises per loop and a pulse that repeats four times.
- Ski chairs: four groups spaced a quarter of the line apart, `x = -60 + ((t/DUR + i/4) mod 1) * 105`, with a tiny sway. In the app the chairs are static, so the travel is new.

Other changes: `Math.random` is a seeded generator, the sky is a fixed haze chosen for the scene (the app sets it per biome), and the real brand sign is replaced by "NORTHSTAR WEAR". Interior furniture is left out.

## Numbers that matter
| | |
|---|---|
| Snow | 2000 points, 300x300 area, 60 high, fall 0.4 to 1.2 units/s, size 0.7 with a round sprite |
| Steam | 90 points, size 2.4, opacity 0.5 |
| Haze | background and exp2 fog `#8fa3bf`, density 0.006 |
| Lights | ambient `#dde6ff` .55, hemisphere .55, low warm sun `#ffe2c0` 1.7, fire point light `#ff8833` |
| Tone mapping | ACES, exposure 0.95 |
| Camera | fov 50 (64 tall), 78 units out, sways 0.55 rad |

## Sound
Silent. Soft wind and a faint crackle would suit it.

## Adapt it
- `SKY` colour for a night or a blue-sky day (and lower the ambient for night).
- The flake speed `0.8 + sin(i) * 0.4` for heavier or lighter snow, and the 2000 count.
- The window light colour, the cabin proportions and the sign text.
- Remove the ski lift or geyser for a simpler scene.

## Files
- `code/demo.html`: runs on its own, including from a double-click. `code/three.global.js` is three.js (MIT) bundled as a plain script, so no server is needed.
