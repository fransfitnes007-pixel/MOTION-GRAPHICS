---
name: circuit-board-node-diagram-right-angle-traces-travelling-pulse
description: A light diagram of grey rounded icon tiles with labels, joined by right-angle traces on a faint dot grid. Short dark pulses with a fading tail travel along each wire from source to target, and a node grows when hovered. Use for architecture, data-flow or how-it-connects visuals.
---

# Circuit board node diagram

**Code name:** Right-angle traces, travelling pulse.

## What you see
A white board with a faint grid of light-grey dots 20 units apart. Four 34-unit rounded tiles (fill `#e9e9e9`, 2px grey border `#8e8e8e`) with a 16-unit outline icon and a grey label under each: Cloud on the left at (80, 150), Server at (250, 80), Validate at (250, 220) and Database on the right at (420, 150), on an SVG 500 x 300 units (shown at 1.95x). Wires are 2.2-unit light grey `#cacaca` lines that leave a node horizontally, turn at the mid x, and enter the next node horizontally. Cloud splits to Server and Validate; both join into Database. A dark pulse about 38 units long with a faded tail, drawn 4 units thick with a soft glow, runs along each wire in 0.9s, one after another (offsets 0, 0.55, 1.0 and 1.45s inside a 2.4s cycle). Hovering a node scales it to 1.14 and darkens its label.

## When to use it
Showing how services, steps or systems connect: an architecture slide, an integrations section, a 'how data flows' hero, or an empty state for a workflow builder. It is a light, quiet diagram, so it suits white pages.

## How it works
Each connection is one SVG path built as `M x1 y1 H midX V y2 H x2`. A second path of the same shape is drawn on top for the pulse, using `stroke-dasharray` and `stroke-dashoffset`: the dash is as long as the visible part of the pulse, and the offset moves its start along the wire. Three layers at 100, 62 and 30 percent length with rising opacity make the fading tail. Phase is `(t - start) % period`, so each wire's pulse loops on its own offset.

```js
const head = ((t - start) % period) / travel * (len + pulseLen)
const st = Math.max(0, head - L), en = Math.min(len, head)
path.setAttribute('stroke-dasharray', `${en - st} ${len * 2}`)
path.setAttribute('stroke-dashoffset', -st)
```

## Numbers that matter
| | |
|---|---|
| SVG | 500 x 300 units |
| Tile | 34, radius 9, `#e9e9e9`, border 2 `#8e8e8e` |
| Wire | 2.2 wide `#cacaca`, route H-V-H at the mid x |
| Pulse | 38 long, 4 wide, `#3a3a3a`, three-layer tail, 1.1 blur glow |
| Timing | 0.9s per wire, starts 0 / .55 / 1.0 / 1.45s, period 2.4s |
| Hover | scale 1.14, label `#8a8a8a` to `#4a4a4a` |
| Loop | 4.8s, two pulse cycles |

## Sound
Silent.

## Adapt it
- `nodes` and `connections`: your own graph. Keep the node y values aligned so the H-V-H wires stay tidy.
- `pulse` and `pulseLen`: colour and length; a bright accent on a dark board works well.
- `start`, `travel`, `period`: when each pulse leaves and how fast it moves.
- `ICON`: swap in your own 24-unit outline icons.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Circuit Board" by componentry on 21st.dev (https://21st.dev/@componentry/components/circuit-board), MIT. This demo is an original recreation written from the public preview.
