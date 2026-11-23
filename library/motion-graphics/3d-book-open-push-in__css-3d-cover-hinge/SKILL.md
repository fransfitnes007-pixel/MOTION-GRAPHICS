---
name: 3d-book-open-push-in-css-3d-cover-hinge
description: "A real-looking 3D hardback slides in tilted, a cursor clicks it, the cover swings open on its spine, and the camera pushes into the page until a white flash cuts to the next scene. Use it to introduce a book, report or any hinged object."
---

# 3D book open and push-in

**Code name:** CSS 3D cover hinge.

## What you see
A title headline slams in at the top while the book slides up from below, spinning from -62 degrees to -26. It bobs gently, with a light band sweeping across the glossy cover. At 3.6s a cursor clicks the cover; it swings open over 1.7s on its left edge up to 168 degrees while the book turns face-on and moves right so the open spread is centred. At 5.6s the camera pushes in: scale 1 to 3.6 with ease-in until the page fills the screen, a white flash rises to 90% in the last 0.25s and falls away over 0.6s on the next scene.

## When to use it
Opening a book, a report, a diary, a menu, a pitch deck: a "now the story begins" beat that justifies a change of scene. Heavy for a short video, so give it 6 to 8 seconds.

## How it works
Six absolutely positioned layers inside `#book` (`transform-style: preserve-3d`, parent `perspective: 2600px`): back cover at `translateZ(-BD)`, bottom and right page edges (`repeating-linear-gradient` stripes), the page block with the first page, the spine (`rotateY(-90deg)`, title in Rye), and the front cover hinged on its left edge. The front cover has two faces (`backface-visibility: hidden`): the outside with art and a gloss band, the inside rotated 180 degrees.

```js
$('front').style.transform = `rotateY(${-open * 168}deg)`
$('book').style.transform = `rotateX(${rx}deg) rotateY(${ry}deg)`
gloss.style.transform = `translateX(${lerp(-BW, BW, (Math.sin(t * 0.9) + 1) / 2)}px)`
// push: s = s0 * lerp(1, 3.6, ei(p(t, tPush, tEnd)));  flash = .9 * p(t, tEnd - .25, tEnd)
```
`sceneBook()` also moves the book sideways by `0.42 * BW * openK` so the opened spread, not the cover, is centred. On tall canvases the book scale `s0` drops (0.95 for 9:16, 0.8 for 4:5, 0.66 for 1:1). The page text is meant to be in Special Elite, but that file in the source fonts folder is a saved HTML page, not a font, so the page text renders in the browser's default serif, and the demo does the same. Cover art is a CSS placeholder.

## Numbers that matter
| | |
|---|---|
| Book | 540px wide (560 tall canvas), 1.5x tall, 46px thick |
| Perspective | 2600px; book rotateX 10 to 5, rotateY -62 to -26 to 0 |
| Cover | opens to 168 degrees over 1.7s (`eio`) at +3.6s |
| Push | +5.6s to the end, scale 3.6, `ei` |
| Flash | white, 90%, last 0.25s then 0.6s fall |
| Timeline | slide in 0 to 1.2s, title +0.75s, click +3.58s, push +5.6s, end +7.8s |

## Sound

## Adapt it
- Cover art, spine text, page text, `BW` for the size.
- `tOpen` and `tPush` to match the voice.
- `ry` start and end angles, `open` degrees (168).
- The flash can be dropped if the next scene fades in.

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. Playfair Display (SIL Open Font License, from Google Fonts) is copied into `code/fonts/` because the serif headline is half the look. Small labels use the system font stack. Rye and Great Vibes are also copied for the spine and cover. Photographs are gradient placeholders drawn in CSS.
- `code/fonts/` holds the fonts the demo loads.
