---
name: night-city-tower-street-diorama-three-canvas-window-grids
description: "A dark low-poly three.js city at night: a grid of skyscrapers with lit window patterns and red blinking antenna tips, one taller dark-glass tower with a glowing sign and blue accent lines that pulse upward, glowing street lamps and taxis driving the avenues. Reach for it as a moody 3D backdrop for a finance, data or enterprise story."
---

# Night city tower street diorama

**Code name:** Three canvas window grids.

## What you see
Deep navy sky with fine stars. A camera hovers above an avenue, looking down the street toward a central tower. Rows of grey-blue skyscrapers 20 to 80 units high, their faces checkered with warm yellow and pale blue lit windows and dark ones. The tallest ones carry a thin antenna with a red tip that blinks. The central tower is darker and glassier, with a lit blue sign and twenty thin blue lines that glow one after another from the bottom up. Street lamps along the roads are white dots. Yellow and silver cars slide along the avenues in both directions. A sign floats in the sky. The camera drifts sideways and bobs slowly. The loop is 14 seconds.

## When to use it
A night-time background for a fintech, analytics or "the city runs on this" story, or a hero where the product is an operations layer. Dark and busy, so keep foreground text large and on a panel. Wrong for a friendly or daytime brand.

## How it works
- Windows. The app places a separate 2x2 glass plane for every window, around four thousand meshes, which is slow. The demo draws each building's window grid once on a small canvas (8 pixels a cell, random lit or dark, nearest-neighbour filtering) and uses it as both `map` and `emissiveMap` on the two visible faces, so the lights glow without any lights. Same look, one material per building.
- Layout. Buildings are on a 7x7 grid at 40-unit spacing with `height = 20 + rand * 60`, width and depth `12 + rand * 8`, six blue-grey colours; the centre is left for the tower. The source puts the streets on the same coordinates as the buildings, so avenues cross them. The demo shifts the streets by 20 units so the blocks sit between them.
- Tower: `B(20, 80, 20)` in `#1a2a4a`, metalness .7; a sign plane and 20 thin accent bars with emissive `#3b82f6`. The demo animates their emissive intensity in sequence upward.
- Antennas: a cylinder plus a red sphere that blinks on `sin(w * 8 + i)`. The app uses a small red point light.
- Cars: the app places 8 static yellow boxes and has a `CarMover` class that is unused here. The demo moves 12 cars along streets, each wrapping across the 300-unit map once per loop.
- Lamps: the app adds a point light to every lamp (dozens of lights); the demo uses glowing heads and four real lights near the tower, which keeps the scene cheap.
- Seeded random replaces `Math.random`. The sky colour is the app's night `#0a0a2a`, with exp2 fog. The real sign text is replaced with "NORTHSTAR".

## Numbers that matter
| | |
|---|---|
| Blocks | 7x7 at 40 units, 48 buildings plus the tower |
| Building height | 20 to 80 units, antenna above 50 |
| Tower | 20 x 80 x 20, 20 blue bars every 4 units |
| Window cell | 8 px on the canvas, ~55% lit, `#ffe9a8` or `#bfe0ff` |
| Sky | `#0a0a2a`, fog exp2 .004 |
| Camera | fov 52, 180 units back, 62 high, swings 84 units sideways |

## Sound
Silent. A distant traffic wash and a low synth pad would carry it.

## Adapt it
- Window colours and lit ratio in `windowTexture`.
- Building count, heights and the tower's colour and sign.
- Camera: lower it into the street for a ride-through feel.
- Add rain by reusing the points from the snow skill.

## Files
- `code/demo.html`: runs on its own, including from a double-click. `code/three.global.js` is three.js (MIT) bundled as a plain script, so no server is needed.
