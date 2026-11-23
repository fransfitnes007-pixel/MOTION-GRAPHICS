---
name: three-frosted-glass-folders-lean-and-open-perspective-tilt-fan-files
description: Three frosted-glass folder cards on a dotted white desk; hover tips the front pane toward you, click fans file cards up out of the pocket. Reach for it for a file or project picker with a tactile, glassy feel.
---

# Three frosted glass folders that lean and open

**Code name:** Perspective tilt, fanned files.

## What you see
A white page with a faint dot grid (22px) and three folder cards in a row, each 310 x 250, with a back panel that has its tab on the right and a front pane whose tab is on the left. The left folder has a striped red-white-blue print behind frosted milk glass, a label "My Files / 3 items" bottom-left and a black "+" button. The middle one is plain milk glass with "Archives / 4 items" at the top-left and a light "ooo" more-button. The right one is smoked glass over a red and teal liquid print, with "My Files / Wed 19 Aug" at the top-right. A mono hint line below says what to do.

At the start the folders drop in one after another (0.14s apart) with their files briefly out, then the files tuck away. Pointing at a folder tips its front pane toward you by 11 degrees (a 3D tilt about the bottom edge) and lifts the file cards underneath a little, so a sliver shows above the pocket. Clicking fans three or four file cards up out of it, each rotated a few degrees and spaced about 34px higher than the one in front. Cards are a mix of art tiles and white or dark paper rows with a name and a mono size.

The loop shows the right folder, then the middle one, then the left one, which stays open longest.

## When to use it
A file manager, project library or asset picker landing visual. It needs light backgrounds so the glass reads, and works best with two to four folders. Sibling: `glass-folder-fan-out-icons__path-clip-pocket` is a dark single folder fanning app icons; this one is a light trio with file cards and 3D lean.

## How it works
Each folder is a stack of layers sharing one 310 x 250 box:
1. back panel, CSS `clip-path: path(...)` with the art as its background
2. file cards, absolutely placed, normally tucked behind the front
3. front pane: the same box clipped to a second path, a translucent white gradient (34% at the top, 93% by 62%) with `backdrop-filter: blur(16px)`, so the art behind shows blurred near the tab
4. a 1.5px rim stroke path, label and button

Lean and open are two eased values per folder, `hov` and `op`:
```js
front.style.transform = `perspective(700px) rotateX(${hov * 11 + op * 5}deg)`   // origin 50% 100%
lift = hov * 22 + op * (70 + rank * 34)          // rank 0 is the card nearest the front
rot  = (k - (n-1)/2) * 3.2 * stagger             // fans the stack
```
The pointer script is `CONFIG.script`: `[hoverFrom, openFrom, openTo, hoverTo]` per folder. The art is CSS gradients standing in for the original prints.

## Numbers that matter
| | |
|---|---|
| Canvas | 1280 x 766, folders at x 128, 488, 851, y 249 |
| Folder | 310 x 250, radius 22, back tab starts at x 128, front tab drops 29px at x 108 to 158 |
| Lean | 11 degrees on hover, +5 when open, perspective 700px |
| Cards | 270 x 112, lifted 70 + 34 per rank, 3.2 degrees of fan each |
| Drop-in | spring k=6 f=8 over 0.9s, 0.14s stagger |
| Button | 54px, radius 17, black or light |

## Sound
Silent.

## Adapt it
- `CONFIG.folders`: label, meta, art (`aurora`, `ember`, `dusk`, `verdant`, `none`), tone (`light` or `dark`), action, and the file list.
- `CONFIG.x` and `CONFIG.y` to space or stack the folders; `CONFIG.lean` for how far the glass tips.
- `ART` to define new gradient prints, or replace them with images.
- `CONFIG.script` to change which folder opens when.

## Files
- `code/demo.html` runs on its own and loops. Placeholder art is CSS and SVG only.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Glassmorphism Folder Cards" by kedhareswer on 21st.dev (https://21st.dev/@kedhareswer/components/glass-folder-cards), MIT. This demo is an original recreation written from the public preview.
