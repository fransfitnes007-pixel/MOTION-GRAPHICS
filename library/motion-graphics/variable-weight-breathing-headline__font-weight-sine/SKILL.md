---
name: variable-weight-breathing-headline-font-weight-sine
description: "A headline whose font weight rises and falls like breathing, with a phase offset per letter so a wave runs through the word. Reach for it as an ambient headline, a calm title card or a loop behind copy."
---

# Variable weight breathing headline

**Code name:** Font weight sine. **From:** original build, neutral copy.

Original code; the move name follows the vocabulary catalogued by motionvideo.xyz.

## What you see
The word "Breathe" in a large serif, centred on a deep indigo glow. Each letter swings between weight 400 (thin strokes) and 900 (heavy strokes) on a sine with a period of 3 seconds, and each letter is 0.55 radians behind the one before, so a wave of weight travels left to right across the word. Heavier letters are also brighter (grey-blue at 400 to near white at 900), so the wave shows in colour too. The whole word scales by 1.2% and its glow pulses with the breath. Under it a slider thumb and a "wght 640" readout follow the weight of the middle letter. Nothing enters or leaves: 6s is exactly two breaths, so the loop is seamless.

## When to use it
An ambient title that must stay interesting for several seconds without moving position: a calm intro, a meditation or wellness brand, a quote hold, a loop behind a call to action. It is wrong for fast or aggressive messaging and for any font that is not variable, where weight steps instead of sliding.

## How it works
Each letter is its own inline-block span so each can have its own `font-weight`. The weight is a continuous number, not a keyword, so the font must have a `wght` axis; the demo uses an open-licensed variable serif (Playfair Display, axis 400 to 900, in `code/fonts/`).

```css
@font-face { font-family: PF; src: url(fonts/PlayfairDisplay[wght].ttf); font-weight: 400 900 }
```
```js
const ph = 2 * Math.PI * t / P                        // P = 3s
weight[i] = 650 + 250 * Math.sin(ph - i * .55)        // 400 to 900, wave along the word
color[i]  = lerp(grey-blue, white, (weight - 400) / 500)
```
Because letters get wider as they get heavier, the line is re-centred by the browser every frame, which is the gentle sideways breathing you see. For no sideways movement, give each cell a fixed width.

## Numbers that matter
| | |
|---|---|
| Font | Playfair Display variable, 400 to 900, 300px wide layout (250px tall) |
| Wave | 650 plus or minus 250, period 3s, 0.55 rad per letter |
| Scale pulse | 1 plus or minus 0.012 |
| Glow | text shadow 60 to 100px at 35% `#828cff` |
| Loop | 6s = two periods |

## Sound
A slow warm pad swelling with the weight, or a soft breath-like noise. Keep it quiet; this is an atmosphere move.

## Adapt it
- `TXT` and `FS` for the copy and size; any variable font with a `wght` axis (`font-family` and the `@font-face` range).
- `250` (amplitude) and `650` (centre) for how bold it gets; `.55` for how steep the wave is (0 makes the whole word breathe together).
- `P` for the pace; keep `DUR` a whole multiple of `P`.
- Drop the gauge for a cleaner frame.

## Files
- `code/demo.html` runs on its own and loops.
- `media/poster.jpg`
