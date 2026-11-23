---
name: cover-wedged-kinetic-line-zoom-through-scale-origin-zoom
description: "A three-word headline builds on beats with a video cover popping in between the words, covers scatter around it, then the whole line scales 7.5x around the second cover until the cover fills the frame. The first beat of a video about content or visuals, where the words need pictures in them."
---

# Kinetic line with covers between the words, then zoom-through

**Code name:** Scale-origin zoom.

## What you see
A three-word headline builds on the beat, centred: "Content" rises 60px through a 10px blur at 0.35s, a small video cover pops between the words with an overshoot, "that" follows at 1.4s, another cover, and "sells." in a lilac gradient at 2.35s. At 2.5s ten more covers drift in around the line. From 3.2s the whole scene scales to 7.5x around the second cover until that cover fills the frame.

## When to use it
The first beat of a video about content or visuals, where the words need pictures in them. The zoom-through is a transition: end it on a frame that starts the next scene with the same image full-screen.

## How it works
Layout is computed every frame from measured word widths, so the line stays centred as items appear. Tiles are placed in sequence between the words. The zoom is a CSS scale on the scene container with `transform-origin` set to the second tile's centre.

```js
const total = widths.reduce((a, b) => a + b, 0) + 2 * (tileW + 2 * gap)
let x = 960 - total / 2                                  // then walk: word, tile, word, tile, word
const zoom = ei(seg(lt, 3.2, 3.75))
scene.style.transformOrigin = `${tileX[1] + tileW / 2}px 540px`
scene.style.transform = `scale(${lerp(1, 7.5, zoom)})`
```
The pop uses `back()` with an overshoot constant of 2.2.

## Numbers that matter
| | |
|---|---|
| Words | 168px weight 800, tracking -.05em |
| Beats | .35s, 1.4s, 2.35s; covers .5s after the word before them |
| Cover | 150 x 200, radius 18px, rotated -6 and 6 degrees plus a wobble |
| Float | 10 covers, 140 x 190, radius 470 to 730px |
| Zoom | 3.2s to 3.75s, `ei`, to 7.5x |

## Sound
A suggested soundtrack is a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. The intro (beats 0 to 12) is plucks and hats with a filter opening up, then a noise riser from beat 10 into the first hit.

## Adapt it
- Words, and which are accented.
- Cover images (the demo uses CSS portraits).
- Beat times `beats`.
- Zoom target and end time.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.
