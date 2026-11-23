---
name: dotted-night-globe-with-pulsing-pins-fibonacci-land-dots-rotate
description: A dark dotted globe on black that turns slowly, with a few cyan pins that pulse expanding rings on locations such as New York and San Francisco. Reach for it for a 'global customers' or 'live activity' hero.
---

# Dotted night globe with pulsing pins

**Code name:** Fibonacci land dots, slow rotate.

## What you see
On pure black, a sphere about 45% of the frame height, body dark grey `#171717` fading to `#0a0a0a` with a faint lighter rim. Land is drawn only as small white dots (about 2px, roughly 5px apart), brighter where the surface faces you and dimmer near the edge, so the continents look like a halftone. The globe is tilted about 17 degrees so the north pole leans toward the viewer, and it turns at 0.3 radians a second (a full turn is 20.9s), features sliding right. Each pin is a cyan dot 5px across with a white centre, a steady ring at 11px, and a second ring that grows from 11px to 23px and fades every 2s. Pins fade out as they reach the edge of the globe and are hidden on the far side.

## When to use it
A hero or section background for a global product: traffic, live visitors, regions. It has no data of its own, so each pin is just a latitude, longitude and a start time. The look is sparse and dark, so it needs a black or near-black page.

## How it works
Points on the sphere come from a Fibonacci spiral (`y = 1 - 2(i+.5)/N`, golden-angle longitude), and only the ones on land are kept, found once at load. Every frame, each land point is turned by `lon + phi`, then tilted about the horizontal axis, and drawn if its depth `z` is above zero; alpha follows `z`. Pins use the same projection. The land test in the demo is a hand-simplified polygon set (about 5 degree detail), so coastlines are rough, and the dots are drawn with canvas 2D instead of the original's WebGL shader.

## Numbers that matter
- Globe diameter 0.45 of stage height; 16,000 sample points, about 4,800 land dots
- Dot radius 0.95px at 800px height, alpha `0.25 + 0.9 * z^0.8`
- Tilt 0.3 rad, speed 0.3 rad/s, one turn 20.9s
- Pin accent `rgb(45,212,232)`, core 5.2px, rings 11px and 11 to 23px, 2s period

## Sound
Silent.

## Adapt it
- `pins`: latitude, longitude and the second each one appears.
- `accent` for the pin colour, `dotColor` for the land.
- `speed` and `tilt` for the rotation, `startLon` for which side faces you at the start.
- `dots` and `dotRadius` for a finer or chunkier halftone.

## Files
- `code/demo.html` runs on its own, loops in 20.9s, and has a `CONFIG` block at the top of the script.

## Credit
Idea: "Globe Pulse" by shuding on 21st.dev (https://21st.dev/@shuding/components/cobe-globe-pulse), MIT. This demo is an original recreation written from the public preview.
