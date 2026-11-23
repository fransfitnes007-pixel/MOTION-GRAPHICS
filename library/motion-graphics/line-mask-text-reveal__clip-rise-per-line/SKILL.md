---
name: line-mask-text-reveal-clip-rise-per-line
description: "Headline lines slide up out of invisible masks one after another, tilting flat as they land, then leave through the top. Reach for it as the default clean headline reveal for explainers, intros and section titles."
---

# Line mask text reveal

**Code name:** Clip, rise per line. **From:** original build, neutral copy.

Original code; the move name follows the vocabulary catalogued by motionvideo.xyz.

## What you see
A near-black stage with a soft indigo glow. At 0.35s the first line of the headline rises out of nothing: it travels 108% of its own height upward and rotates from 5 degrees to flat in 0.95s with a strong ease-out (`eo5`). The second and third lines follow 0.14s apart. A faint hairline draws under each line at the mask edge, marking where the text is cut. At 1.7s a grey subline rises from its own mask and a short gradient rule grows beneath it. The last two words are tinted `#a5b4fc`. At 3.95s every line leaves upwards (`ei`, 0.6s, 0.09s apart) and the hairlines fade, ending on empty black for a clean loop.

## When to use it
The default for any headline: it is quiet, readable and fast, and the hard mask edge looks printed rather than animated. Use it for intros, chapter titles and claims. For energy use a shorter stagger; for gravity a longer ease. It is wrong where text must be readable from the first frame, since the first 0.3s of each line is partly hidden.

## How it works
Each line is a block with `overflow: hidden`. Inside it sits one child that is translated in percent of its own height, so the same code works at any font size. A little bottom padding with matching negative margin stops descenders being clipped.

```css
.ln { display:block; overflow:hidden; padding:0 .06em .1em; margin-bottom:-.02em }
```
```js
const pI = eo5(pr(t, .35 + i * .14, .95))          // entrance
const pO = ei(pr(t, 3.95 + i * .09, .6))           // exit, accelerating
y = (1 - pI) * 108 - pO * 112                      // translateY in %
rotate = (1 - pI) * 5 - pO * 3                      // degrees, origin 30% 100%
```
Origin at the bottom left of the line makes the tilt look like the line swinging up out of a slot rather than spinning in place.

## Numbers that matter
| | |
|---|---|
| Headline | 158px weight 800, tracking -0.045em, line height 1.1 (150px, five lines on tall) |
| Stagger | 0.14s per line in, 0.09s out |
| Entrance | `eo5`, 0.95s, 108% travel, 5 degrees tilt |
| Exit | `ei`, 0.6s, 112% travel |
| Hairlines | 2px, `#a5b4fc` at 55%, drawn over 0.55s |
| Subline | 34px `#8c8ca6`, rises at 1.7s; rule 300px by 4px |

## Sound
One soft whoosh at the first line, a quieter tick for each following line, and the same whoosh reversed on the exit. Silence under the hold.

## Adapt it
- `L` for the copy, `FS` for the size, and the `acc` class for the highlight colour.
- `.14` stagger and `.95` duration for pace.
- Remove the tilt for a stricter look; remove the hairlines if the mask edge should stay invisible.
- Set the background to match your scene and put the lines over video instead of black.

## Files
- `code/demo.html` runs on its own and loops.
- `media/poster.jpg`
