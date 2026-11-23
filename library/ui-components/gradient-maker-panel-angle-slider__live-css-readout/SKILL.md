---
name: gradient-maker-panel-angle-slider-live-css-readout
description: "A gradient generator card: preview square, two stop colours and positions, linear or radial, angle slider, noise toggle, copyable CSS and a download button. Reach for it as a small tool widget on a design site."
---

# Gradient maker panel with angle slider

**Code name:** Live CSS readout.

## What you see
Breadcrumbs (`Home › Products › Graaadients`) sit above a bordered panel (890x441, 20px radius). Left: a 381px preview square running from light cyan to pure blue. Right, top to bottom: two round colour swatches each with a number box (`0` and `100`) and a `+` button; a row `Linear [switch] Radial  Angle [slider] 90°`; a `Noise` switch; `CSS Code` with a field holding `background: linear-gradient(90d…` (clipped) and a copy button; a white `Download JPG` button and a dark reset button. Below the panel: `All gradients are 100% free.`

In the clip the pointer drags the angle slider from 90 to 119 and on to 281 degrees; the preview turns with it and the CSS text updates each frame. Then it clicks the Linear/Radial switch: the preview becomes a radial glow (cyan centre, blue edge) and the Angle control disappears.

Demo: drag 0.9 to 2.7s (90 to 281 degrees), radial at 3.6s, noise on at 5.0s (a fine grain overlay), reset click at 6.4s.

## When to use it
A small interactive tool on a site: gradient, shadow or colour generators. The live CSS readout is the useful part; keep it selectable.

## How it works
One state object (angle, mode, noise) feeds three things: the preview background, the control states and the code string. Controls are drawn in the same 960x724 space as the page, so positions match the clip.

```js
lg = `linear-gradient(${angle}deg, ${c0} ${p0}%, ${c1} ${p1}%)`
rg = `radial-gradient(circle, ${c0} ${p0}%, ${c1} ${p1}%)`
preview.background = radial ? rg : lg;  code.text = 'background: ' + (radial ? rg : lg)
thumb.left = angle / 360 * 127 px;  fill.width = thumb.left + 13
```

Noise is an inline SVG `feTurbulence` tile blended over the preview with `overlay`. The original's noise look was not visible in the clip at that size, so its strength is a guess.

## Numbers that matter
| | |
|---|---|
| Panel | 890 x 441 in a 960 x 724 scene, scaled 1.1x |
| Stops | `#5ee9ff` at 0%, `#0000ff` at 100% |
| Slider | track 149px, 0 to 360 degrees |
| Switch | 52 x 28, knob 22 |
| Drag | 1.8s, ease in-out |
| Loop | 7.4s |

## Sound
Silent.

## Adapt it
- `CONFIG.stops` for the two colours and positions.
- `CONFIG.angle0` and `angle1` for where the slider starts and ends.
- `CONFIG.dragA`, `dragB`, `radialAt`, `noiseAt`, `resetAt` for the timeline.
- `CONFIG.breadcrumb` and `footer` for copy.

## Files
- `code/demo.html` runs on its own and loops; every frame is `render(t)`. Edit the `CONFIG` block at the top of its script.
- `media/poster.jpg` is the page's preview image.

## Credit
Idea: "Graaadeints" by designali-in on 21st.dev (https://21st.dev/@designali-in/components/graaadeints), MIT. This demo is an original recreation written from the public preview.
