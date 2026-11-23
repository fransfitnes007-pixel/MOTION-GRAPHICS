---
name: glass-folder-fan-out-icons-path-clip-pocket
description: "A frosted glass folder with a tabbed front pocket that pops in on scroll; hover fans three app-icon tiles up out of it, hovering a tile lifts it with a name pill and lights its tag. Use as a clickable index of case studies, projects or brands."
---

# Glass folder fan-out icons

**Code name:** Path clip pocket.

## What you see
A 460 by 300 folder in dark glass. The back plate has its tab on the right and the front pocket has its tab on the left, each with 24px rounded corners and a smooth S-curve into the tab. The front pocket has a bright top edge fading to nothing at the bottom, the title "Case studies" in 20px semibold, three grey tag chips and a tiny strip of the three icons at bottom right. Three 101px rounded app tiles sit tucked behind the pocket. On scroll the whole folder rises 34px from 92% scale and the tiles slide up one after another. On hover the tiles fan out left, centre and right on a shallow arc, rotated 12.5 degrees outward, and the pocket drops 6px. Hover one tile and it lifts 26px, grows 10%, straightens, and a pill reads "Name · Read the case" above it, while its chip in the pocket lights up and the other tiles dim a little. Click opens that brand's page. On touch screens a tap toggles open.

## When to use it
A compact index of three to five items where each item is a logo or app icon: case studies, integrations, projects. It rewards the pointer, so make sure the touch behaviour (tap to open) is acceptable. Not for long lists.

## How it works
The folder shapes are real vector paths: `pathL` and `pathR` build the outline from width, height, corner radius, tab depth, tab width and tab slope, and each is applied as `clip-path: path('...')` to a div. A `ResizeObserver` recomputes the path when the folder resizes. A separate SVG path with the same `d` draws the edge stroke, using a vertical gradient from 38% white to 0 for the front. Everything else is plain CSS transitions on transform, driven by `hover`, `open` and `hi` state.

```tsx
const wide = open || hover
const k = i - (n - 1) / 2                         // -1, 0, 1 for three tiles
const gap = wide ? spread * 1.15 : spread          // spread = 92
transform: `translate3d(${k * gap}px, ${k * k * 9 - (wide ? 4 : 0)}px, 0) rotate(${k * (25 / (n - 1)) * (wide ? 1.2 : 1)}deg)`
transition: `transform ${wide ? 0.6 : 0.9}s cubic-bezier(.2,.8,.2,1)`,
transitionDelay: wide ? `${i * 0.04}s` : `${0.35 + i * 0.08}s`
```
Opening is quick and almost simultaneous; closing waits .35s and steps tile by tile, so the tiles settle back in order. The hovered tile's inner link gets `translateY(-26px) rotate(-rot) scale(1.1)`, undoing the fan rotation so it stands upright.

The demo plays the sequence from a fixed timeline (scroll-in, pointer enters, hover tile, leave) and computes each CSS transition from its start time, including the per-tile delays. The tiles are invented placeholders.

## Numbers that matter
| | |
|---|---|
| Folder | 460 by 300, pocket 180 tall, back plate top 14px, corner radius 24, tab depth 24, tab slope 46, tab width 42% (front) and 40% (back) |
| Tile | 101px, radius 26px, `0 18px 40px rgba(0,0,0,.55)` and a 1px ring at 14% white |
| Fan | spread 92px (105.8 open), arc `k*k*9`, rotation `k * 12.5deg` (x1.2 open) |
| Easing | `cubic-bezier(.2,.8,.2,1)` for tiles, pocket and hover lift |
| Pocket fill | `linear-gradient(160deg, rgba(255,255,255,.09), rgba(255,255,255,.015) 55%)` over `rgba(12,12,12,.78)`, `backdrop-blur 18px` |
| Pill | `bg rgba(0,0,0,.55)`, 12px, slides 6px up while fading in .35s |

The demo leaves out the pocket's `backdrop-filter`.

## Sound
Silent. A soft paper slide on opening would fit.

## Adapt it
- The tiles: any 101px images or logos, and the tag labels.
- `spread` and the 25 degree total fan angle.
- The light theme values in the source (`THEMES.light`) for a white page.
- Tab geometry parameters in `pathL` and `pathR` for a different folder shape.

## Files
- `code/demo.html` runs on its own and loops in 9s.
