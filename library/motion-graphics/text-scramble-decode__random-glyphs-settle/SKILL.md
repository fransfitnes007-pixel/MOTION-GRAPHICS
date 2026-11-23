---
name: text-scramble-decode-random-glyphs-settle
description: "A headline decodes from random flickering characters into real letters, each settling at its own time, then re-scrambles out. Reach for it on tech, security or data themes, or to make a title feel computed rather than typed."
---

# Text scramble decode

**Code name:** Random glyphs settle. **From:** original build, neutral copy.

Original code; the move name follows the vocabulary catalogued by motionvideo.xyz.

## What you see
From 0.3s the first characters appear as flickering blue symbols (`#`, `%`, `K`, `}`) that change 30 times a second at 55 to 85% opacity. Each cell keeps churning until its own settle time, then snaps to the real letter with a cyan-white flash and a glow that fades over 0.5s. The decode runs left to right with a seeded wobble, so it looks random but is not: the first letter locks at 0.65s and the last at about 2.4s. A progress bar and label below read "DECODING 37%" and finish on "DECODED". At 3.9s the whole line scrambles again from the right and fades out by 4.8s so the loop starts from empty.

## When to use it
Titles about code, security, data, AI or anything "computed": a hook line, a section name, a reveal of a product name. It buys attention in the first two seconds. Avoid it for long sentences (the churn gets hard to read) and for warm brands where it feels cold.

## How it works
Every character is a fixed-width cell (a monospace face at 0.62em per cell) so nothing shifts while glyphs change. Each cell has a start time and a settle time, and the glyph shown before settling is a pure hash of the cell index and the 30 fps frame number:

```js
const hsh = (a, b) => { const x = Math.sin(a*127.1 + b*311.7) * 43758.5453; return x - Math.floor(x) }
const f = Math.floor(t * 30)
glyph = GL[Math.floor(hsh(i, f) * GL.length)]      // same t, same glyph: no Math.random
settle[i] = .65 + i * .062 + hsh(i, 7) * .4        // left to right with a random wobble
```
The flash is a colour lerp from `rgb(140,230,255)` to white over 0.45s with an extra text shadow that shrinks. Exit reverses the order: cell `i` leaves at `3.9 + (N-1-i) * .02`.

## Numbers that matter
| | |
|---|---|
| Font | `ui-monospace` stack, weight 700, 150px wide layout (165px tall), cell 0.62em |
| Churn | 30 fps hash, glyph set of 44 symbols and capitals |
| Start | `.3 + i*.03 + line*.12` s |
| Settle | `.65 + i*.062 + hash*.4` s |
| Flash | 0.45s colour lerp, glow 40px to 0 over 0.5s |
| Exit | 3.9s, right to left, 0.02s apart, 0.35s fade |
| Colours | glyphs `#8ea0ff`, settled `#fff`, bar `#6d7bff` to `#9bf0ff` |

## Sound
Fast tiny ticks or a data-chirp bed while cells churn, a soft click per settled letter (or every third), and a low confirm tone on "DECODED". Pair with the "tick per item" recipe.

## Adapt it
- `LINES` for the copy, `GL` for the glyph set (digits only, katakana, or dots).
- `.062` (settle spacing) for speed, and the `* .4` wobble for how random the order looks.
- The accent `#8ea0ff` and the font; any monospace works, a proportional font needs measured cells.
- Delete the bar and label for a clean title.

## Files
- `code/demo.html` runs on its own and loops.
- `media/poster.jpg`
