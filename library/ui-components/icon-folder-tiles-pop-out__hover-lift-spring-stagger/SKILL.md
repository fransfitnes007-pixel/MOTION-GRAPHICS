---
name: icon-folder-tiles-pop-out-hover-lift-spring-stagger
description: A dark glass folder with a tabbed back and front pocket; four app tiles spring up out of it, and hovering one lifts it above the folder with a label while its pill lights. Reach for it to show a group of tools or apps as one object.
---

# Icon folder with tiles that pop out

**Code name:** Hover lift, spring stagger.

## What you see
A near-black page with a faint dot grid and a 640px glass folder in the middle: a taller back panel with its tab on the right, a front pocket with its tab on the left, both with a hairline white rim that fades out downward. The word "Design" sits in the pocket at 30px, with four rounded text pills under it. At bottom right is a small dark capsule holding mini copies of the four tiles.

At 0.35s the folder opens by itself. Four rounded-square tiles (lime, orange, navy and a dark one), each about 138px, spring up out of the pocket one after another (0.07s apart) and sit fanned out with tilts from -10 to +8 degrees, overlapping like a hand of cards. A green and a blue glow bleed through the front panel under the lime and navy tiles. When the pointer enters the folder, all tiles rise another 16px.

Pointing at a tile (or its pill) lifts that tile about 118px above the folder, straightens it to 0 degrees, scales it up 12%, and shows a small dark label above it. Its pill gets a bright rim. Moving to the next tile drops the first and lifts the next. At the end the pointer goes to the mini capsule, whose icons swell slightly.

## When to use it
A "tools I use", "integrations" or "what is inside this bundle" block on a landing page, where a group of apps should read as one object that can be opened. It suits four to six tiles. It is wrong for long lists, since the tiles overlap and only the top edge of each shows when closed.

## How it works
Three layers stacked in this order: back panel (SVG path with a vertical gradient fill and gradient stroke), the tiles, and the front pocket (a second SVG path, nearly opaque at the top and fading to nothing at the bottom, so it hides the lower part of each tile). Hiding is done by the front panel, not by clipping: tiles slide down behind it when closed.

Each tile's rise is a spring on its own start time, and hover is an eased 0.3s in and out:
```js
const rise = spring(seg(t, riseAt + i * stagger, riseAt + i * stagger + 1.0), 6, 9)
const y = base.y + 118 * (1 - rise) - hoverFolderPx * folderHover - liftPx * lift
const rot = lerp(base.r, 0, lift)          // straightens as it lifts
```
Tile z-order is raised above the front panel only while lifted, so it comes out in front and drops back behind. The pointer, its path and which tile it is on are scripted in `PATH` and `HOVER` so the loop plays without a mouse.

## Numbers that matter
| | |
|---|---|
| Canvas | 960 x 720, folder 640 wide at x 160, front tab top at y 305, back tab top at y 155 |
| Tiles | 138px, radius 36, centres x 280/410/540/665, tilts -10, -4, 4, 8 degrees |
| Rise | spring k=6 f=9, 0.35s start, 0.07s stagger, 118px travel |
| Hover | lift 118px, scale 1.12, 0.3s ease-out, label 13px above the tile |
| Pills | 36px tall, 17px text, 1px rim at 8% white, 55% white when active |
| Colours | page #121212, tiles #2a2a2e #c9f23a #ff5a1f #16167a |

## Sound
Silent.

## Adapt it
- `CONFIG.title`, `CONFIG.tags` and `CONFIG.tileColors` for the folder name and the tiles. Swap the SVG glyphs in `glyph` for your own logos.
- `CONFIG.liftPx` and `CONFIG.hoverFolderPx` for how far things climb.
- `CONFIG.riseAt` and `CONFIG.riseStagger` for the opening timing; set `riseAt` large and bind it to a click to open on demand.
- `CONFIG.bg` for a light page (also flip the glass rim colours).

## Files
- `code/demo.html` runs on its own and loops. Placeholder art is CSS and SVG only.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Icon Folder" by romanvasnev on 21st.dev (https://21st.dev/@romanvasnev/components/icon-folder), MIT. This demo is an original recreation written from the public preview.
