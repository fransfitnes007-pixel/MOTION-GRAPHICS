---
name: cast-chip-pills-staggered-back-pop
description: "A row of small dark pills, each with a gold initial avatar, a name and a grey role, popping up one after another. Use it to introduce people or tags over a photo."
---

# Cast chip pills

**Code name:** Staggered back-pop.

## What you see
Over a full-bleed photo with a big headline, four rounded pills appear at the lower left: a gold gradient circle with the person's initial, a bold white name, and a grey role ("author", "editor", "17"). Each pill rises 24px and scales from 80% with an overshoot, 0.22s after the one before. They leave together 0.2s before the headline swaps. On a 9:16 canvas the same chips stack in a column.

## When to use it
Introducing a cast, a team, or a list of tags while the voiceover names them. Short labels only: pills do not wrap.

## How it works
`chips()` builds all pills from an array of `{n, r, img}` once (cached by a key string), measures their widths, and lays them out in a row or column with a gap of `0.5 * fs`:

```js
const ti = t0 + i * gap, ki = backS(p(t, ti, ti + 0.5), 1.9)
tf(e, { x: cx, y: cy + (1 - ki) * 24 * S, s: lerp(0.8, 1, ki) * lerp(1, 0.9, ko), a: p(t, ti, ti + 0.15) * (1 - ko) })
```
Pill padding is `0.35fs` all round with `0.75fs` on the right; the avatar is a `1.5fs` circle filled with `linear-gradient(135deg,#e8b43a,#8a5a10)` holding the initial in Playfair 700. If `img` is given the avatar becomes a background image (for example a real portrait on the first chip). Each pill cues a `tick` sound.

## Numbers that matter
| | |
|---|---|
| Stagger | 0.22s between pills |
| Entry | 0.5s `backS(1.9)`, rise 24px, scale .8 to 1 |
| Size | font 30px wide, 26px tall, avatar 1.5x the font |
| Fill | rgba(18,20,26,.8), 1.5px border rgba(255,255,255,.14), blur 14px |
| Layout | row on wide and 4:5 / 1:1; column when height/width > 1.4 |

## Sound
A tick (`tick.wav`, volume 0.35) per pill.

## Adapt it
- The `cast` array: names, roles, optional `img`.
- `t0` and `gap` to match the voice naming each person.
- `dir: 'col'` and `align: 'right'` for other layouts.
- The avatar gradient.

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. Playfair Display (SIL Open Font License, from Google Fonts) is copied into `code/fonts/` because the serif headline is half the look. Small labels use the system font stack. Photographs are gradient placeholders drawn in CSS.
- `code/fonts/` holds the fonts the demo loads.
