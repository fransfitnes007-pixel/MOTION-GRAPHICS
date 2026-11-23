---
name: blur-threshold-morphing-words-svg-threshold-crossfade
description: A bold word that dissolves into the next through a gooey blur-to-sharp morph. Reach for it as a hero headline that cycles through a list of words.
---

# Words that melt into each other

**Code name:** SVG threshold crossfade.

## What you see
A single bold black word (Hello, Designali, Text, Animation, Design...) centred on white. Over 1.5s the word blurs and thins while the next word fades in from a heavy blur; for the middle of the change both are smudged into a rounded black mass with letter-shaped bumps, then edges snap clean again. The new word rests crisp for 0.5s before the next change. The clip shows about four changes in 7.8s.

## When to use it
A hero line that cycles through values (`Design`, `Build`, `Ship`), or a loading screen. Keep words close in length so the blob does not jump; very long words read poorly while blurred.

## How it works
Two stacked spans (current and next) and an SVG filter. Each span is blurred and faded by a fraction `f` of the morph; the container then runs an `feColorMatrix` that multiplies alpha by 255 and subtracts 140, which turns soft blur edges into hard shape edges. That threshold is what makes it look liquid.

```js
f = morphElapsed / 1.5;   inv = 1 - f
next.filter = `blur(${min(8 / f - 8, 100)}px)`;   next.opacity = f ** .4
prev.filter = `blur(${min(8 / inv - 8, 100)}px)`; prev.opacity = inv ** .4
container.filter = 'url(#thr) blur(.6px)'
// feColorMatrix values: 1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 255 -140
```

This is the same recipe the common open-source morphing text uses, rebuilt as a pure function of time (cycle = 1.5s morph + 0.5s rest).

## Numbers that matter
| | |
|---|---|
| Morph | 1.5s |
| Rest | 0.5s |
| Blur law | `8 / f - 8` px, capped at 100 |
| Opacity law | `f ** 0.4` |
| Threshold | alpha x 255 - 140, plus 0.6px blur |
| Type | 150px, weight 800 in the demo |
| Loop | 12s (6 words) |

## Sound
Silent.

## Adapt it
- `CONFIG.texts` for your words.
- `CONFIG.morphTime` and `cooldown` for pace.
- `CONFIG.threshold` for how gooey the blob is (raise the negative offset to thin it).
- `CONFIG.fontSize` and `color`; on a dark page invert both the background and the colour.

## Files
- `code/demo.html` runs on its own and loops; every frame is `render(t)`. Edit the `CONFIG` block at the top of its script.
- `media/poster.jpg` is the page's preview image.

## Credit
Idea: "Liquid Text" by designali-in on 21st.dev (https://21st.dev/@designali-in/components/liquid-text/liquid-text), MIT. This demo is an original recreation written from the public preview.
