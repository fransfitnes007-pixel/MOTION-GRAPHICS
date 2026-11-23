---
name: glowing-border-light-chasing-around-frame-soft-comet-along-rectangle-perimeter
description: "A dark `#05070D` screen where a rectangle outline exists only as a travelling light: a white core with a cyan to deep blue tail running counter-clockwise around the frame. Reach for it as a hero background, a framing device or a loading state."
---

# Light chasing around a glowing frame

**Code name:** Soft comet along the rectangle perimeter.

## What you see
A near-black navy screen (`#05070D`). Inset about 8% from the sides and 11% from the top and bottom is an invisible rectangle; the only thing you see of it is a bright stretch of its edge. At the centre of that stretch the line is white (`#F2FBFF`), then cyan (`#35C4E8`) on both sides, then deep blue (`#1261A0`) fading to nothing. The tail behind the bright spot is longer than the front: the lit part covers about half of the perimeter, the tail about 20% and the front about 11.5%.

The bright spot travels counter-clockwise, bottom edge to the right, then up the right edge, along the top to the left and down the left side, with a soft glow about 36 px thick around a 16 px core. In the preview video it moves about a quarter of a lap in 3 seconds; the demo uses one lap per 9 seconds so it loops cleanly, and the spot breathes a little (12% in size, three times per lap).

## When to use it
A hero or section where a frame should feel alive without text: behind a headline, around a video, as the empty state of a dashboard. Keep one per screen. It is dark-theme only; on a light page the glow would need a different blend mode.

## How it works
The original is a WebGL fragment shader (Paper Shaders, "Pulsing Border", default variant, adapted by the 21st.dev Shader Builder) with a four-colour palette: `#05070D`, `#1261A0`, `#35C4E8`, `#F2FBFF`. The usage example mounts `<ShaderBackground className="h-full w-full" />` to fill its parent.

The demo needs no WebGL. It walks the rectangle in 760 short segments and gives each a colour from its distance to a moving head, using a different spread behind and in front:

```js
d  = (i / N) - head            // signed, wrapped to -.5..+.5 of the perimeter
k  = exp(-(d / (d < 0 ? tail : headLen)) ** 2)
colour = ramp(k)               // 0 deep blue, .5 cyan, 1 white
```

It draws those segments twice, a wide one blurred 9px for the glow and a narrow one blurred 2px for the core, onto two offscreen canvases that are stacked on the page canvas. This reproduces the look from watching the 3-second clip; the shader's own noise and its exact pulse timing are not reproduced, and the demo's corners are square.

## Numbers that matter
| | |
|---|---|
| Palette | page `#05070D`, tail `#1261A0`, body `#35C4E8`, core `#F2FBFF` |
| Frame | 800 by 500 box: x 65 to 735, y 55 to 445 |
| Strokes | glow 36px blurred 9px, core 16px blurred 2px |
| Spread | tail 20%, head 11.5% of the perimeter, Gaussian |
| Speed | 1 lap per 9s in the demo; the video moved about a quarter lap in 3s |
| Breathing | 12% size change, 3 times per lap |

## Sound
Silent.

## Adapt it
- `colors`: swap the three colours for a brand ramp (dark, mid, bright).
- `inset` to change the frame size, `glowWidth` and `coreWidth` for thickness.
- `tail`, `head` for how long the comet is; `lapSeconds` for speed (it sets the loop length).
- `pulse`, `pulsesPerLap` for the breathing, or set `pulse` to 0 for a steady light.

## Files
- `code/demo.html` runs on its own and loops. Rendered with canvas strokes and blur; the original is a WebGL shader.
- `media/poster.jpg` is a frame showing the component.

## Credit
Idea: "Pulsing Border" by paper-design on 21st.dev (https://21st.dev/@paper-design/components/pulsing-border), Apache-2.0. This demo is an original recreation written from the public preview.
