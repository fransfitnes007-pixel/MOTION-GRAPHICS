---
name: dashboard-card-lift-out-spring-lift-dim-settle
description: "A dashboard pushes in from depth, then its four stat cards lift off the page one per half beat on a spring, enlarged and tilted into a row above it while the page dims, and the views chart lifts to the centre and draws left to right. Pulling the numbers out of a screen so they can be read: a UI screenshot gives context, the cards give the message."
---

# Dashboard cards lifting out of the page

**Code name:** Spring lift with page dim.

## What you see
A dashboard window pushes in from depth (tilted 28 degrees, 55 percent scale, to flat). From 0.75s the four stat cards lift off the page one per half beat, springing to 1.58x and settling in a row above it, each tilted a couple of degrees, while the page dims to 55 percent. A pill says the numbers are live. At 2.5s the views chart lifts to the centre at 1.75x and draws left to right behind a clip. At 3.35s the window zooms 3.2x into the camera as the exit.

## When to use it
Pulling the numbers out of a screen so they can be read: a UI screenshot gives context, the cards give the message. Needs a screen where cards are separate elements you can crop.

## How it works
Each card is a clone of a region of the page. `lift(card, window, box, k, tx, ty, scale, rot)` places the clone exactly over its region (`k = 0`) and moves it to a target (`k = 1`).

```js
const x0 = BZ[0] + x * ks, y0 = BZ[1] + 44 + y * ks            // card's resting place in the window
S(card, { left: lerp(x0, tx - w0 * sc / 2, k) + 'px', top: lerp(y0, ty - h0 * sc / 2, k) + 'px', transform: `scale(${ks * sc}) rotate(${rot * k}deg)` })
const k = spring(seg(lt, t0, t0 + .55))                        // spring overshoots, then settles
```
The cards can be cropped from a 2x capture of a real screen; the demo clones a CSS card instead.

## Numbers that matter
| | |
|---|---|
| Cards | 4 stat cards, 322 x 116, lift 0.5 beat apart starting at .75s |
| Spring | `1 - exp(-7x) cos(11x)` over 0.55s |
| Target | x 290 + 447 per card, y 225, scale 1.58, rot -3 to 3 degrees |
| Chart | 885 x 338, lifts to (960, 560) at 1.75x, wipe 2.55s to 3.4s |
| Dim | brightness to .55 from .7s to 1.1s |

## Sound
A suitable soundtrack is a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. Each card lift is on an eighth note; the chart wipe has a short swell.

## Adapt it
- The page and which cards lift (and their boxes).
- Target row positions and scale.
- Spring constants for more or less bounce.
- Dim amount.

## Files
- `code/demo.html` runs on its own with no network. Screens, covers, logos and the wordmark are CSS placeholders.
