---
name: extruded-logo-slab-stacked-slices-translatez
description: "A flat logo turned into a solid chrome slab by stacking 18 copies 1.6px apart in 3D, bright front and back faces and darkened inner slices, turning a full 360 on a 12 degree tilt every 5 seconds. Use for a brand mark in a footer, a loader or a hero."
---

# Extruded logo slab

**Code name:** Stacked slices translateZ.

## What you see
A chrome letter with real thickness spinning on a vertical axis, one turn in 5 seconds at constant speed. It is tipped 12 degrees towards you so you see a little of its top. Front and back faces are bright and read the right way round. When it turns edge-on you see a dark metal rim about 29px thick, the same outline as the face. There is no floor, rim light or reflection: only a soft drop shadow under the faces.

## When to use it
A single mark that deserves to be a product shot: footer, loading state, a closing frame. Needs a transparent, roughly square image of the mark. Poor for thin or very detailed artwork, where the stacked edges blur into grey.

## How it works
No WebGL. The same square image is rendered 18 times as absolutely positioned layers inside a `preserve-3d` container, each pushed back by `translateZ(-i * 1.6px)`. Slice 0 is the front face. The last slice is the back face, mirrored with `rotateY(180deg)` so it reads correctly from behind. Both faces use `backface-visibility: hidden`, so you only see the outer face of each. The 16 inner slices stay visible from both sides, darkened with `brightness(.42) contrast(1.15)` so the stack reads as metal edge. A parent adds `perspective: 1100px` and a tilt, and a motion div spins the stack.

```tsx
<div style={{ perspective: 1100 }}>
  <div style={{ transformStyle: 'preserve-3d', transform: 'rotateX(12deg)' }}>
    <motion.div style={{ transformStyle: 'preserve-3d' }}
      animate={{ rotateY: 360 }} transition={{ repeat: Infinity, duration: 5, ease: 'linear' }}>
      {Array.from({ length: 18 }, (_, i) => <img style={{
          transform: i === 17 ? `translateZ(${-i*1.6}px) rotateY(180deg)` : `translateZ(${-i*1.6}px)`,
          backfaceVisibility: (i === 0 || i === 17) ? 'hidden' : 'visible',
          filter: (i === 0 || i === 17) ? 'drop-shadow(0 24px 40px rgba(0,0,0,0.75))' : 'brightness(0.42) contrast(1.15)' }} />)}
```
Slice count times gap is the thickness: 17 gaps of 1.6px is 27px. Use more slices for a smoother edge on large marks. The demo draws the mark as chrome-gradient text.

## Numbers that matter
| | |
|---|---|
| Slices | 18, gap 1.6px, thickness about 27px |
| Spin | `rotateY` 0 to 360, 5s, linear |
| Tilt | `rotateX(12deg)` |
| Perspective | 1100px |
| Face filter (on dark) | `drop-shadow(0 24px 40px rgba(0,0,0,.75))` |
| Face filter (on white) | `drop-shadow(0 20px 30px rgba(15,17,26,.28))` |
| Edge filter | `brightness(.42) contrast(1.15)` on dark, `brightness(.6) contrast(1.1)` on white |

## Sound
Silent. A low, slow whoosh per turn would fit a trailer.

## Adapt it
- The image, and `SLICES` and `SLICE_GAP` for thickness.
- `seconds` for faster or slower.
- Tilt angle: 0 for a flat turntable, 25 for a more dramatic look.
- The edge `brightness` to match the logo colour: a gold mark wants warmer, lighter edges.

## Files
- `code/demo.html` runs on its own and loops in 5s.
