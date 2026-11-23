---
name: click-ripple-fill-match-cut-expanding-circle
description: "After a button click a purple circle grows from the button, slowly then fast on a cubic ease-in, until it floods the whole frame, and the next scene opens on the same colour. A click that leads to the next scene: sign up, buy, apply."
---

# Click ripple fills the screen

**Code name:** Expanding circle, ease-in radius.

## What you see
The camera is already on a button on a sign-up page. The cursor presses it, and from the click point a purple circle grows: slowly at first, then fast, until at the end of the scene it covers the frame. The next scene's background is the same purple, so the cut is invisible and the end card appears out of the colour.

## When to use it
A click that leads to the next scene: sign up, buy, apply. It is a match cut by colour, so the next scene must start on the same colour as the ripple.

## How it works
A circle element centred on the click point whose radius follows an ease-in cubic from just after the click to the end of the scene.

```js
const r = ei(seg(lt, clickT + .15, d)) * 2400            // d = scene length
S(ripple, { left: (1014 - r) + 'px', top: (704 - r) + 'px', width: 2 * r + 'px', height: 2 * r + 'px' })
// ripple: radial-gradient(circle, #8B5CF6, #6D28D9);  end card bg: radial-gradient(ellipse at 50% 45%, #7C3AED, #3B1D8F 60%, #12082e)
```
Cubic ease-in means most of the growth happens in the last half second, so the fill is a sweep at the end rather than a slow fade. 2400px covers a 1920 x 1080 frame from anywhere near the middle.

## Numbers that matter
| | |
|---|---|
| Start | 0.15s after the click |
| Ease | `ei` (cubic in) |
| Final radius | 2400px |
| Colours | #8B5CF6 to #6D28D9, then end card #7C3AED |

## Sound
A suggested soundtrack is a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. The cursor click is a short click sample 2.5s into the scene, and a swell rises under the ripple into the beat-60 impact.

## Adapt it
- Click point (centre of the button).
- Scene length `d` and the colour of the next scene.
- Final radius for larger frames.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.
