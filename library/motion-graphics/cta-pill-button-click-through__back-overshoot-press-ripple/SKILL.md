---
name: cta-pill-button-click-through-back-overshoot-press-ripple
description: "A black pill button pops in with a small overshoot, a large cursor glides to it, presses it with an indigo ripple, and the button swells and fades as the next scene takes over. Reach for it as the \"click to continue\" beat before an end card."
---

# Call-to-action pill with cursor click-through

**Code name:** Back-overshoot pop, press and ripple.

## What you see
After the previous scene clears, a black pill ("Work with me" with a small up-right arrow) pops in from 70% with a small overshoot over 0.45s. A big arrow cursor, 1.25 times the size of a normal one, fades in at the lower right and glides 0.6s to the right half of the button. At the click the button shrinks to 94% and the cursor to 84%, and a thick indigo ring grows from 20px to 170px across the button and fades over 0.5s. The button then swells to 112% and fades out in 0.35s while the cursor leaves, and the end card takes over.

## When to use it
The last beat before an end card or a handoff: "and the action is this". It makes the CTA feel pressed, not just displayed. Pairs with the end card skill. Wrong where there is no click to show, such as a plain text CTA.

## How it works
Three small tracks off one click time `CTACLICK`. The button: a back-ease scale-in (overshoots by about 10%), a press window of 0.15s at 94%, then a scale-up and fade-out 0.2s after the click. The cursor: a glide to a point offset 16% of the button width right of centre, then a fade-out. The ripple: one 0.5s progress value drives both size (20px to 170px) and opacity (.8 to 0).

```js
const bs = lerp(0.7, 1, back(bin)) * press2 * lerp(1, 1.12, bout)
btn.style.opacity = clamp(bin * 2) * (1 - bout)
const k2 = eio(p(t, 25.5, 26.1)); tf(c2, lerp(W * 0.8, tx2, k2), lerp(H * 0.84, ty2, k2), (press2 < 1 ? 0.84 : 1) * (V ? 1.5 : 1.25))
const rk2 = p(t, CTACLICK, CTACLICK + 0.5), rs2 = 20 + 150 * eo(rk2)
```

`back` is the standard ease-out-back: `1 + c3 * (x-1)^3 + c1 * (x-1)^2` with c1 = 1.70158, c3 = c1 + 1. The click time is also the cue for the click sound.

## Numbers that matter
| | |
|---|---|
| Button | 440 x 116 (540 x 136 tall), fully rounded, `#0b0c10`, white 46px (54 tall) semibold, shadow `0 18px 40px -16px rgba(15,17,26,.55)` |
| Pop in | 25.0s to 25.45s, scale .7 to 1 with ease-out-back |
| Cursor glide | 25.5s to 26.1s from (80%, 84%) of the frame, ease-in-out-cubic |
| Click | 26.2s: button .94 for 0.15s, cursor .84 |
| Ripple | 26.2s, 0.5s, 20px to 170px, opacity .8 to 0, 4px `#5b5ce6` |
| Exit | 26.4s to 26.75s: scale to 1.12 and fade |

## Sound
One mouse click on the press frame at 26.2s. It sits on a thinned-out music bed.

## Adapt it
- The label and the arrow icon.
- `CTACLICK` and the pop-in time to fit your voice.
- Button colours: `#btn` background, the ripple colour.
- Cursor size (1.25) or remove the cursor for a plain pop.

## Files
- `code/demo.html` runs on its own (2.5s loop).
