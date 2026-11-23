---
name: one-word-in-nine-type-styles-preloader-camera-pan-over-tile-wall
description: "A typographic loader: the word PORTFOLIO shown in nine different styles (lime on indigo, ransom-note letters, a lime counter, chunky 3D and more), with a camera that pans to the ransom tile, pulls back to a 3 x 3 wall and ends on a plain version. Reach for it as a portfolio or studio intro."
---

# One word in nine type styles, preloader

**Code name:** Camera pan over a tile wall.

## What you see
It opens full-frame on an indigo scene: small mono header text across the top ("October 2025 - 2026", "Graphic design", a handle), "A DESIGN" in white, and the word split over two lines in giant lime heavy type (PORT / FOLIO). Over the letters sit design-tool props: an eye icon on the O, a pen nib with handles under the R, three stacked rings above the T, a selection box with handle squares around the F, and a round badge of rotating text bottom right with a lime dot. A cursor arrow wanders across.

At 1.5s the camera slides sideways and down to a black scene (0.5s, with a slight pull-back mid-move). Nine cutout letters (white-on-black and black-on-white, in different faces, each tilted a few degrees) drop in one after another, 0.09s apart, then "PERSONAL PROJECT" and a handle in grey italic mono fade in, and a yellow smiley pops in with a spring.

At 3.7s the camera pulls back over 0.9s to a 3 x 3 wall of nine scenes, one per style: cream letters with stickers, tall black letters on purple, rainbow letters on navy, a cream index card, the ransom tile, a lime "100" counter, chunky pink-and-blue 3D letters, the opening indigo scene and a blue italic script. The wall holds for 2.7s (the counter runs up to 100), zooms into the middle tile and fades to a plain near-black scene where the word drops in letter by letter in off-white at 280px. Then it loops to the opening scene.

## When to use it
A portfolio, studio or agency site that wants a first impression of range before the content, or an intro film whose subject is typography itself. A 10s preloader is long; it is meant to run behind real loading, or as a showreel piece. Not for products that need a quick spinner.

## How it works
All nine scenes live in one `world` div laid out on a 3 x 3 grid of 1280 x 1040 tiles with a 40px gap. There is no per-scene scene-switch; the camera just moves the world:
```js
world.style.transform = `translate(${DW/2 - cx*s}px, ${DH/2 - cy*s}px) scale(${s})`   // origin 0 0
// focus tile centre (cx, cy), scale s: 1 for a full-frame tile, ~0.3 for the wall
```
Keyframes in `cam(t)`: tile 7 at scale 1, an eased move to tile 4 with a dip of `.18 * sin(pi * u)` in scale, then a pull-out to `sOver = (1280 - 2*pad) / (3*1280 + 2*gap)`, a hold with a 3% breathe, then a zoom in. Tile corners round as `s` falls (`lerp(0, 40, 1 - s)`).

Scene motion is tied to the global clock: the cutout letters use `spring(seg(lt, i*.09, i*.09+.45), 6, 10)` with a seeded tilt, the badge turns 40 degrees per second, the eye blinks for 0.1s every 3.4s. The last plain scene is an overlay on top, shown from `tPlain` and not part of the wall.

Simplified from the original: the nine scenes are rebuilt with plain fonts, shapes and emoji-free CSS art, so the stickers, the pirate hat and wheel, the textured letters and the 3D type are rough approximations. Only the opening and ransom scenes have their own motion here; the other seven tiles are still pictures.

## Numbers that matter
| | |
|---|---|
| Canvas | 1280 x 1040, 9 tiles of the same size, gap 40 |
| Camera | slide 0.5s, pull-out 0.9s, hold 2.7s, push in 0.8s |
| Overview scale | about 0.3 |
| Lime scene | #d5ef3a on #28246e, 272px heavy sans, 34px tracking on PORT |
| Cutouts | 104 x 124, 9 of them, 8px apart, spring k=6 f=10 |
| Loop | 10.4s |

## Sound
Silent.

## Adapt it
- `CONFIG.word`, `name`, `handle`, `dates` and `kind` change every scene at once.
- `CONFIG.lime` and `indigo` for the opening colours; each other tile has its own colours in the script.
- `tToRansom`, `tOut`, `tHold`, `tIn` and `tPlain` set the timing of the camera moves.
- Delete tiles you do not want; the wall then needs a new grid size in `sOver`.

## Files
- `code/demo.html` runs on its own and loops. Placeholder art is CSS and SVG only.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Typography Portfolio Preloader" by kedhareswer on 21st.dev (https://21st.dev/@kedhareswer/components/type-remix-preloader), MIT. This demo is an original recreation written from the public preview.
