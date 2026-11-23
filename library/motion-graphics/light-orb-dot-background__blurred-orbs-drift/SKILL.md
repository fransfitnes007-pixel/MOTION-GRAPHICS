---
name: light-orb-dot-background-blurred-orbs-drift
description: "A quiet animated background for a light-themed video: dots plus drifting colour. Use it behind type, cards and windows when white would look dead."
---

# Light orb dot background

**Code name:** Blurred radial orbs drifting on a dot grid.

## What you see
A very pale grey field, #f4f4f6, with dots on a 34px grid at 10% opacity. Four large soft blobs sit behind: indigo at top left, sky blue at right, a faint pink at the bottom, and a grey-slate one at the top right. Each one wanders up to 120px sideways and 90px up and down, on its own slow cycle (periods of roughly 9 to 21 seconds). A vignette darkens the corners by 10%.

## When to use it
Behind any light-themed scene where the content is type, cards or windows. The colour is low enough that black type stays crisp. It is not a hero visual on its own: if nothing else is on the screen, it looks empty.

## How it works
Four absolutely positioned circles with a `radial-gradient(closest-side, colour, transparent)` fill and a 70px `filter: blur`. Each frame they get a new position:

```js
left = o.x + Math.sin(t * o.sp * 6 + o.s) * 120
top  = o.y + Math.cos(t * o.sp * 5 + o.x) * 90
```

The dot grid is a plain `radial-gradient` tiled at 34px. Over a 25s video the drift never repeats, which is right; on a 20s loop it would jump at the seam, so the demo rounds each angular speed to a whole number of cycles per loop. The formula is otherwise unchanged. Orb positions use 1920 by 1080 numbers scaled to the stage.

## Numbers that matter
- Stage `#f4f4f6`; dots `rgba(20,16,40,.10)` 1.3px, 34px grid.
- Orbs (size, colour): 900 `rgba(91,92,230,.26)`, 820 `rgba(96,165,250,.24)`, 700 `rgba(236,72,153,.12)`, 600 `rgba(148,163,184,.28)`; blur 70px.
- Drift: amplitude 120px by 90px, speeds .09, .07, .11, .06 times 6 (x) and 5 (y) radians per second.
- Vignette: transparent to 62%, then `rgba(10,8,20,.10)`.

## Sound
Silent.

## Adapt it
- The four colours: use two stops of one brand hue for a calmer field.
- Orb sizes and start positions.
- `DUR` and the speeds, for a faster or slower wander.
- Dot colour and spacing.

## Files
- `code/demo.html` runs on its own and loops. Nothing to replace; the demo is the background alone.
