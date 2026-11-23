---
name: dot-sphere-thinking-pill-scatter-to-grid-latlong-rotation
description: "A dark status pill: a 56px sphere built from about 130 white dots in latitude rings, rotating slowly, plus 'Solving....' in dim grey. The dots begin scattered and settle into an ordered grid. Use as an AI 'thinking' avatar or inline agent status."
---

# Dot sphere thinking pill

**Code name:** Scatter to grid, lat-long rotation.

## What you see
A near-black page `#070707` with one pill in the middle, 74px tall and about 186px wide in life (shown 2.4x): fill `rgba(29,29,29,.42)`, a 1px inset ring `rgba(44,47,54,.31)`, fully rounded, with 9px on the left and 32px on the right of padding. On the left a 56px sphere made of white dots laid out in 11 latitude rings, 15 dots on the equator and fewer toward the poles, turning about 40 degrees a second with a 14 degree tilt. Front dots are brighter and slightly larger, back dots are faint. On the right 'Solving....' in 18px `rgba(251,251,251,.5)`. In the clip the dots start scattered with a few clumping in pairs, then over about 1.6s glide into straight rows, which is the 'solved' look. The demo holds the ordered sphere, then scatters it again from 3.8s so it loops.

## When to use it
An AI assistant's 'thinking', 'searching' or 'working' state in a chat bubble or toolbar, an agent avatar, or any wait where you want a calmer, more technical signal than a spinner. It needs a dark surface to read.

## How it works
Points sit on a sphere at fixed latitude and longitude. Each frame adds the spin to every longitude, tilts the sphere around the horizontal axis, projects to x and y (orthographic), sorts by depth and draws each point as a dot with size and opacity from its depth. The scrambled state adds a hashed offset to latitude and longitude, scaled by a single `disorder` value that eases from 1 to 0.

```js
const lat = p.lat + (hash(id*5.1+9) - .5) * 2 * scatter * d, lon = p.lon + (hash(id*2.3) - .5) * 2 * scatter * d + spin
let x = cos(lat) * sin(lon), y = sin(lat), z = cos(lat) * cos(lon)
opacity = .1 + .62 * ((z + 1) / 2) ** 1.6
```

The real component draws to a canvas and has six states (working, searching, solving, listening, composing, shaping) and two sizes, 64px for avatars and 20px inline. The clip only shows solving, so only that state is rebuilt here, and the exact point layout is a guess.

## Numbers that matter
| | |
|---|---|
| Pill | 74 tall, radius full, fill `rgba(29,29,29,.42)`, ring `rgba(44,47,54,.31)`, gap 12 |
| Orb | 56px box, radius 25, 11 rings, 15 on the equator, about 130 dots |
| Dot | 1.35px radius scaled .65 to 1.15 by depth |
| Opacity | .1 at the back to .72 at the front |
| Motion | 40 degrees per second, tilt 14 degrees |
| Solve | scattered to ordered 0.15s to 1.7s, ease-out quint |
| Text | 18px `rgba(251,251,251,.5)` |

## Sound
Silent.

## Adapt it
- `label`: the status words.
- `orb`, `radius`, `rings`, `perRing`, `dot`: size and density of the ball.
- `spin` and `tilt`: how fast and from what angle it turns.
- `solveAt` and `scrambleAt`: how long it takes to settle, and when it scatters again.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Thinking Orbs" by larsen66 on 21st.dev (https://21st.dev/@larsen66/components/thinking-orbs), MIT. This demo is an original recreation written from the public preview.
