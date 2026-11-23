---
name: endless-logo-row-sliding-sideways-duplicated-track-linear-loop
description: A row of client or partner logos that slides sideways forever at a constant speed, with no visible seam. Reach for it as a 'trusted by' strip.
---

# Endless logo row sliding sideways

**Code name:** Duplicated track, linear loop.

## What you see
White page, one row of six logos about 58px tall in the vertical middle, 28px between them, running off both screen edges. Reverse is on in the preview, so the row travels right at a steady 100px a second (in a 1280px frame; the preview video measures nearer 60px a second because the page was zoomed out). Logos leave on the right and new ones enter from the left with no jump. There are no edge fades in the preview. In the demo the six logos are made-up wordmarks (a serif caps word, a bold word with a ring, a light word with a dot, a red boxed word, an italic word with a wave, a bold word with bars), so each style of logo is visible.

## When to use it
'Trusted by' and integration strips under a hero. It is a straight line at one speed, so it is quieter than a two-row opposed marquee (see the library's brand logo strip). Add fade masks at the edges if the row should dissolve instead of being cut.

## How it works
The children are drawn once in a measuring pass, then the row is moved by a translate from 0 to the width of one lap (sum of widths + gaps) in `lap / speed` seconds, and a second copy follows it, so when the first lap finishes the picture is identical to the start and the loop is seamless. The slider's props are `gap` (24 in the usage example), `reverse` (direction), `speed` (default 100) and `speedOnHover` (slows when the pointer is over it). In the demo `DUR` is computed as `TRACK / speed`, so the video loop is exactly one lap; there is no hover slow-down because the demo has no pointer.

## Numbers that matter
- Row height 58px, gap 28px, 6 logos, one lap 1,348px (13.48s at 100px/s)
- Speed 100px/s, linear, no easing
- Direction: right (`reverse`)
- Usage example: `gap={24}`, `reverse`, logos `h-[120px]`

## Sound
Silent.

## Adapt it
- `logos`: replace each entry with an image or SVG and set its `w`.
- `speed` and `reverse` for pace and direction.
- `gap` and `height` for spacing and size.
- Add `mask-image: linear-gradient(90deg, transparent, #000 10%, #000 90%, transparent)` on the row for soft edges.

## Files
- `code/demo.html` runs on its own, loops in 13.5s, and has a `CONFIG` block at the top of the script.

## Credit
Idea: "Infinite Slider" by ibelick on 21st.dev (https://21st.dev/@ibelick/components/infinite-slider), MIT. This demo is an original recreation written from the public preview.
