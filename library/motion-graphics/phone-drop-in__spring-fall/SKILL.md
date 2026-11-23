---
name: phone-drop-in-spring-fall
description: "A phone mockup falls in from above the frame and settles with a small overshoot while a sentence builds under it. Reach for it to introduce the product or a piece of content."
---

# Phone drop-in

**Code name:** Spring fall from above.

## What you see
After a black LED scene the video cuts to white. A black phone with a thin grey bezel and a video on its screen is above the frame. Over 0.6s it drops into place at the top of the frame, overshoots slightly and settles; on the wide layout its top is 30px above the frame edge, so only the lower part shows. Below it a sentence builds word by word: "your brand", "had a", then a bold gradient phrase. On the tall layout the phone is bigger (470px wide), sits 90px from the top, and the phrase moves to its own second line.

## When to use it
Introducing the product, a video or the audience on a device. It works as the first light scene after a dark pivot beat, because it comes in from the same direction the eye is already pulled. It is wrong for a hero product shot that needs to be fully in frame from the first frame.

## How it works
The phone is a plain CSS box: a dark rounded rectangle whose radius is `width * .13` and whose bezel is `width * .024`, with the screen a second rounded box inset by the bezel (radius `width * .11`). Everything scales from the width, and the height is `width * 2.05`. The fall is one spring on `top`:

```js
const ph = spring(seg(t, t0, t0 + .6), 7, 10)
phone.style.top = lerp(-PH - 80, pTop, ph) + 'px'      // starts fully above the frame
```
The sentence uses the word-by-word reveal and is placed just under the phone: `sy = pTop + PH + 90`. Its words start 0.02s, 0.48s and 0.88s after the phone starts. The sentence can be followed by small tiles dropping from above (see the tile skill).

## Numbers that matter
| | |
|---|---|
| Phone | 330px wide (470 on tall), height `width * 2.05`, bezel `width * .024`, radius `width * .13` |
| Fall | spring k7 f10 over .6s, from `-PH - 80` to -30 (90 on tall) |
| Sentence | 78px (64 on tall), words +.02, +.48, +.88 after the phone starts |
| Frame colour | `#0c0c10` with an inner ring `#35353f` |

## Sound
A whoosh on the cut from the LED scene, a soft pop for each word, then (a beat later) a quick run of small pops for the tiles that follow.

## Adapt it
- The screen content (image or video frame).
- Phone width: bezel and radius follow.
- The start and end `top` for a rise from below or a slide from the side.
- The sentence under it.

## Files
- `code/demo.html` runs on its own. The screen is a gradient placeholder.
