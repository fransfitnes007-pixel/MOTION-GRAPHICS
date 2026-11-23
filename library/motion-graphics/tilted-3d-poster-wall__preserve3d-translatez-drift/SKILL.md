---
name: tilted-3d-poster-wall-preserve3d-translatez-drift
description: "A grid of portrait thumbnails in a rotated 3D plane that fills in diagonally and keeps drifting. Use it as a background that says \"lots of content\" behind a headline."
---

# Tilted 3D poster wall

**Code name:** Preserve-3d grid with staggered translateZ and drift.

## What you see
A flat plane of sixteen portrait tiles, 196 by 348 each, laid in four rows that alternate by 40px so they interlock. The plane is rotated 14 degrees back and 18 degrees round, with 1800px of perspective, so it reads as a wall seen from the left. The tiles appear in a diagonal wave: each starts 400px behind the plane, invisible, and flies forward to opacity .55 over 0.45s, tile after tile 0.05s apart along row plus 0.6 times column. The whole plane drifts up at 70px per second.

## When to use it
A background behind a title that talks about video, content, a catalogue, or a community. It stays at half opacity on purpose, so text in front remains readable. Not for hero use: the tiles have no detail at that opacity.

## How it works
Two nested divs: an outer one carries `perspective`, the inner one `transform-style: preserve-3d`, rotated and translated. Each tile is a child that moves along Z.

```js
wall.style.perspective = '1800px'
inner.transform = `rotateX(14deg) rotateY(-18deg) translateY(${-((t - t0) * 70)}px)`
tile: d = r + c * .6; p = eo5(seg(t, VIDEOS - .1 + d * .05, VIDEOS + .35 + d * .05))
      opacity = p * .55; transform = `translateZ(${(1 - p) * -400}px)`
```

The stagger key `r + c * .6` makes the wave run mostly down the rows. The tile images are meant to be real video posters; the demo draws gradient cards with a circle so the grid still reads.

## Numbers that matter
- Grid: 4 by 4, tile 196 by 348, column step 218px, row step 370px, odd rows shifted 40px.
- Tilt: rotateX 14, rotateY -18 degrees, perspective 1800px.
- Entry: `eo5` over 0.45s, translateZ -400px to 0, opacity to .55, stagger .05s times (row + .6 column).
- Drift: 70px per second upward.

## Sound
None.

## Adapt it
- The tile images (use real posters; keep them the same 196 by 348 ratio).
- Tilt angles and drift speed.
- Final opacity (.55) for a stronger or fainter wall.
- Stagger weight (.6) to change the wave direction.

## Files
- `code/demo.html` runs on its own and loops. Poster tiles are coloured gradients.
