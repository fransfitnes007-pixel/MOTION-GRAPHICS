---
name: pink-dot-matrix-crt-404-page-cell-grid-framebuffer-static-burst
description: "A 404 page drawn as a glowing pink dot-matrix CRT: pixel text, an extruded 404, palms, clouds and a pyramid \"take me home\" button, with channel-change static between messages. Reach for it on a retro, synthwave or playful error page."
---

# Pink dot-matrix CRT 404 page

**Code name:** Cell-grid framebuffer with static bursts.

## What you see
A near-black maroon screen covered in a grid of round dots, 160 across by 130 down (8px pitch on a 1280 x 1040 canvas). Unlit dots are faint; lit ones swell and brighten in shades of pink, and the whole picture blooms softly. A vignette and fine horizontal scanlines sit on top. A tiny mono hint at the top right says to click the screen to change the channel.

The picture: "PAGE NOT FOUND" in a 5x7 pixel font between two pairs of short double rules; a huge pink "404" with a stepped 3D extrusion in a darker pink and a pale glint that sweeps across it; bobbing music notes and treble clefs around it; a hearted status line; two palm trees plus two smaller ones, a row of pink clouds along the bottom and a pyramid in the middle carrying the button text "TAKE ME HOME" in dark pink.

Every 3s the channel changes: for 0.5s the screen turns to random-dot static with a few torn lines, then settles on the next message ("SIGNAL LOST", "THIS PAGE DRIFTED OFF", "TRY ANOTHER CHANNEL"). A white dot with a short pale tail is the pointer. In the last channel it goes down to the pyramid, which brightens, and small arrow marks appear either side of the button text.

## When to use it
A 404, maintenance or "offline" page for a playful or retro brand, or a hero behind a synthwave landing page. The look carries one message and one button; it is not for dense text. It runs a canvas the size of the screen, so keep it to one per page.

## How it works
The picture is drawn into a tiny off-screen canvas, one pixel per dot (160 x 130). Each frame that canvas is read back and every pixel is redrawn on the main canvas as a circle: its radius is `8 * (.2 + .27 * alpha)` and its colour blends from the dim dot colour to the pixel colour. So anti-aliased edges become soft dots instead of jagged ones.
```js
for each cell: a = pixel.alpha
  fill = lerp(DIM, pixel.rgb, a * 1.15);  r = C * (.2 + .27 * a)
// then bloom:
g.filter = 'blur(9px)'; g.globalCompositeOperation = 'lighter'; g.globalAlpha = .55; g.drawImage(canvas, 0, 0)
```
Text is a hand-written 5x7 bitmap font (A to Z, 0 to 5 and a few marks) drawn with 1x1 rectangles. The 404 is polygons drawn five times, offset one cell down and 0.8 cell left each time in the dark pink, then once in the light pink. Static is `hash(x, y, frameIndex)` per cell, blended in by `1 - eo(seg(t, 0, .5))`, with a few rows shifted sideways; the hash is a sine hash, so it is repeatable.

Simplified from the original in small ways: the palm trees and clouds here are drawn with a few strokes and circles rather than the original's detailed sprites, the 404 glint is a plain sweep, and the pointer trail is a straight comet tail.

## Numbers that matter
| | |
|---|---|
| Grid | 160 x 130 cells, 8px pitch, dot radius 1.6 to 3.8px |
| Colours | hot #ff8bbb, mid #d6548a, deep #602844, unlit #2c1620, screen #150a10 |
| Channel | 3s each, static burst 0.5s, noise frames at 24 per second |
| Bloom | 9px blur added at 55% |
| Big 404 | 28 x 36 cells per digit, 36 cell pitch, extrusion 5 steps |
| Hover | pyramid brightens from 1.0 to 1.25 over 0.35s |

## Sound
Silent.

## Adapt it
- `CONFIG.messages`, `header`, `big` and `button` for your copy (letters A to Z, digits and `. ! ?` are in the font).
- `CONFIG.hot`, `mid`, `deep` and `dim` to recolour the screen, for example green for a terminal.
- `CONFIG.cell` for chunkier or finer dots (the pixel layout redraws at any size).
- `CONFIG.channelSeconds` and `staticSeconds` for how often the channel changes.

## Files
- `code/demo.html` runs on its own and loops. Placeholder art is CSS and SVG only.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Retro CRT 404 Page" by kedhareswer on 21st.dev (https://21st.dev/@kedhareswer/components/phosphor-crt-404), MIT. This demo is an original recreation written from the public preview.
