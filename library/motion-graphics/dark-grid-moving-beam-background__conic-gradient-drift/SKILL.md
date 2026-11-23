---
name: dark-grid-moving-beam-background-conic-gradient-drift
description: "A quiet moving background for dark, editorial videos: grid, beam and glow. Use it behind type and device mockups."
---

# Dark grid with moving light

**Code name:** Scrolling grid, rocking conic beam and drifting glow.

## What you see
A stage of #07070c with a grid of 1px lines at 4.5% white every 96px, drifting down and to the right at a slow pace (14px per second across, 8px per second down). Over it a conic gradient with a few soft indigo and violet wedges, blurred 40px, swings back and forth through 12 degrees. A 1400 by 1000 indigo glow at 22% moves in a lazy loop through the upper middle of the frame. Together they read as a studio light moving over a graph-paper wall.

## When to use it
Behind any dark video where content sits on top: type, laptops, phones, callouts. It gives life to long static scenes without competing. It is poorer as the only thing on screen.

## How it works
Three layers, each moved by a function of time.

```js
grid.transform = `translate(${(t * 14) % 96}px, ${(t * 8) % 96}px)`      // the 96px tile repeats, so the modulo is invisible
beam.transform = `rotate(${Math.sin(t * .15) * 12}deg) scale(1.2)`       // scale(1.2) keeps the blurred edge off-screen
glow: left = 900 + Math.sin(t * .23) * 300, top = -100 + Math.cos(t * .19) * 160
```

The beam is `conic-gradient(from 200deg at 70% 30%, transparent 0, rgba(91,92,230,.20) 40deg, transparent 90deg, rgba(139,92,246,.10) 200deg, transparent 260deg)` with `filter: blur(40px)`.

The motions are never repeated (the sine periods are 27 to 42 seconds), so they would jump on a loop. The demo rounds every motion to a whole number of cycles per `DUR` and rescales each amplitude so the speed matches the raw constants. The grid moves 16px by 8px per second at `DUR = 24`.

## Numbers that matter
- Stage `#07070c`; grid 96px, lines `rgba(255,255,255,.045)`.
- Grid speed 14 by 8 px/s; beam `sin(t*.15)*12` degrees; glow `sin(t*.23)*300` and `cos(t*.19)*160` px.
- Glow: `radial-gradient(closest-side, rgba(91,92,230,.22), transparent)`, 1400 by 1000, blur 30px.

## Sound
Silent.

## Adapt it
- The accent colours in the beam and glow (the same indigo as the headline accent).
- Grid spacing (96px) and line opacity.
- Beam rotation amplitude and the glow path.
- `DUR`: longer for slower motion.

## Files
- `code/demo.html` runs on its own and loops. The demo is the background alone.
