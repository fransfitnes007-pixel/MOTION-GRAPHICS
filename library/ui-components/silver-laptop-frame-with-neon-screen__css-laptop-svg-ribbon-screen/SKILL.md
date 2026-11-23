---
name: silver-laptop-frame-with-neon-screen-css-laptop-svg-ribbon-screen
description: A flat front view of a silver MacBook Pro style laptop (notch, hinge, base) on a dark dotted page, with an image or content filling the screen. Reach for it to show a website or design in a laptop.
---

# Silver laptop frame with a neon screen

**Code name:** CSS laptop, blurred ribbon screen.

## What you see
A near-black page (#0a0a0c) with a faint 30px dot grid. A silver laptop sits dead centre: a lid 606 x 409 with a thin pale rim and a black bezel, a screen 590 x 384 with 8px corners and a small notch with a camera dot at the top, a dark hinge strip, then a wide base (722 x 27) in two greys with a finger dip at the middle and two feet. In the example the screen shows a neon gradient: soft broad bands of green, blue, red and lime curving across black, with a yellow script word "Neon" over a white serif title.

The original is static: you pass an image `src` and it fills the screen. The demo adds life: four blurred ribbons slide and bend across the screen, each making one or two whole turns in the 8s loop, the laptop bobs 4px, and the script word floats 2px.

## When to use it
Showing a website, landing page or design on a laptop. It works on dark pages and for gradient or UI screenshots. For other angles or an open-lid 3D look you need a different mockup.

## How it works
The laptop is plain boxes with gradients; nothing but the screen moves. The screen art is an SVG with two groups of stroked paths, one blurred by 22px at full width and one by 9px at 35% width laid over it. Each ribbon is a smooth cubic path through eight control points whose y comes from two sine waves:
```js
y = H * r.y + sin(i * .9 + turn * r.sp + r.ph) * 62 + sin(i * 1.7 - turn * r.sp + 2 * r.ph) * 28
// turn = t / DUR * 2pi, and r.sp is a whole number so the loop closes
```
A dot-grain layer in `overlay` blend adds the noise seen in the picture. To use a real screenshot, delete the SVG and put an `<img>` in the `scr` box.

## Numbers that matter
| | |
|---|---|
| Canvas | 960 x 822 |
| Lid | 606 x 409 at (172, 203), screen 590 x 384 at (180, 210) |
| Base | 722 x 27 at (114, 612), hinge 14px |
| Ribbons | green 150px, blue 70, red 52, lime 30; blur 22px and 9px |
| Motion | 8s loop, bob 4px |

## Sound
Silent.

## Adapt it
- Replace the SVG screen with your own image or an `<iframe>` look-alike.
- `CONFIG.script` and `title` for the text; `CONFIG.ribbons` for colours, widths and speeds (whole turns per loop).
- `CONFIG.page` for the page colour; `CONFIG.float` at 0 for a still laptop.

## Files
- `code/demo.html` runs on its own and loops. Placeholder art is CSS and SVG only.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Macbook Pro" by designali-in on 21st.dev (https://21st.dev/@designali-in/components/macbook-pro), MIT. This demo is an original recreation written from the public preview.
