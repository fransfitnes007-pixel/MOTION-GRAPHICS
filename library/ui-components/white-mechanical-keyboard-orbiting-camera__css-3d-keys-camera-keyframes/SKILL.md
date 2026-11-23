---
name: white-mechanical-keyboard-orbiting-camera-css-3d-keys-camera-keyframes
description: An interactive 3D mechanical keyboard in off-white with orange accent keys, knobs, an orange display and a red cable on a white page; drag to rotate, scroll to zoom, and keys press when typed. Reach for it as a hardware or typing-tool hero.
---

# White mechanical keyboard with an orbiting camera

**Code name:** CSS 3D keys, camera keyframes.

## What you see
A white page with one keyboard: an aluminium case in two greys with a thin black well, 78 keys in six rows (esc and F1 to F12, number row, QWERTY, home row, shift row, bottom row with a long space bar), off-white keycaps with small dark legends, orange accent keys for esc and four in the bottom-right corner, two black round knobs and a tall orange-to-cream display in the top-right showing 12:37. A red and black twisted cable runs from the top right edge away along the desk.

The video is a tour of the camera: it starts near top-down and large, pulls back to a small keyboard, dives to a close-up of the letter keys, returns, swings the board round to vertical (cable then points sideways), tips to a low grazing angle along the keys, and settles at a 3/4 view, over 12s. Along the way keys press: each sinks about 11px and comes back over 0.22s, which is how typing looks in the original (`typingInteraction`). A pointer arrow wanders over the board.

## When to use it
A hero or feature section for a keyboard, a typing app, a keyboard-shortcut tool or anything with a physical-gadget feel. The original is interactive (drag to orbit, type to press keys), so the best use is a hero that invites play. For a light page only: the white scene is part of the look.

## How it works
This demo is a CSS 3D rebuild. The board is a group in a `perspective: 2200px` view; every key is a five-face box (a top, a darker front and two darker sides) built with the same helper, so it can be rotated to any angle without gaps:
```js
box(parent, x, y, z, w, d, h, [top, front, side], radius)
key.z = 24 - pressDepth * sin(clamp((t - start) / .22) * pi)       // a press pulse
world.transform = `translate(${px}px,${py}px) scale(${s}) rotateX(${rx}deg) rotateZ(${rz}deg)`
```
Rows are lists of `[legend, width in units]`; one unit is 58px with a 5px gap, and widths sum to 15 for rows 0 to 4 and about 16 for the bottom row, which runs under the knob column. The camera is a keyframe list `[t, scale, rotX, rotZ, panX, panY]` eased between rows. The usage example is `<MechanicalKeyboard interactive typingInteraction />` in a full-screen white or near-black container.

Simplified from the original: the real component is a lit 3D scene (reflections, soft shadows, a twisting cable, real orbit and key-press controls). This demo uses flat-shaded CSS boxes, a fixed cable path and a scripted camera and typing, so it matches the shapes and colours but not the lighting.

## Numbers that matter
| | |
|---|---|
| Canvas | 1280 x 1014, perspective 2200px |
| Keys | 78, unit 58px, gap 5px, height 15px, radius 8 |
| Colours | keys #f0f0f2, accent #ee4b22, case #a9abb2, cable #e2461e |
| Press | 11px down, 0.22s, 46 presses in the loop |
| Camera | scale .42 to 2.1, pitch 6 to 74 degrees, rotation -28 to 78 degrees |
| Loop | 12s |

## Sound
Silent.

## Adapt it
- `ROWS` for the layout and legends, `CONFIG.keyColor` and `accent` for colours.
- `CAM` for the camera tour; `TYPE` (generated near the top of the script) for which keys press when.
- `CONFIG.screenText` for the display, `cable` for the cable colour, `page` for the background (a dark page needs lighter shadows).
- `CONFIG.unit` and `gap` to resize the keys.

## Files
- `code/demo.html` runs on its own and loops. Placeholder art is CSS and SVG only.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Mechanical Keyboard" by ayushmxxn on 21st.dev (https://21st.dev/@ayushmxxn/components/mechanical-keyboard), MIT. This demo is an original recreation written from the public preview.
