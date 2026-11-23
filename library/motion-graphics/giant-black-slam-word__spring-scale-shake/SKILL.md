---
name: giant-black-slam-word-spring-scale-shake
description: "A giant black two-line word slams onto a white frame from 135 percent with a short screen shake, over a blurred drifting band of thumbnails. Reach for it for the one headline the whole video is building to."
---

# Giant black slam word

**Code name:** Spring scale with screen shake.

## What you see
On a light stage, two lines of giant black type (236px, weight 800, very tight) appear at 135% of their size and spring down to 100% in half a second, overshooting once. For the first 0.22s the whole frame shakes by up to 6px in both directions. Underneath, two rows of blurred post thumbnails fade in and drift left, the lower one faster than the upper. The type sits in the upper half, the thumbnails in the lower half. The slam stays until the next cut at 7.8s.

## When to use it
The line the video exists to say: the thesis, the pain word, the name of the problem. One per video. It needs a bright empty stage and a spoken beat to land on. It is wrong for a calm sentence, and the shake should not be used if the next scene is also shaking.

## How it works
Three things happen from the same start time:

```js
const q = spring(seg(t, t0, t0 + .5), 9, 12)                 // overshoots about 20% before settling
slam.transform = `translate(-50%,-50%) scale(${lerp(1.35, 1, q)})`
const sh = Math.sin(Math.PI * seg(t, t0, t0 + .22)) * 6      // shake amplitude: up, then back to 0
stage.style.transform = `translate(${sh * Math.sin(t * 200)}px, ${sh * Math.cos(t * 170)}px)`
```
The shake moves the whole stage, not just the word, so everything jolts together. Two different high frequencies (200 and 170 rad/s) keep x and y out of step so it feels random without using `Math.random()`. The thumbnail rows are the same blurred, modulo-wrapped rows as the strip skill, at half the size (150px cards), blur 6px, fading in over .4s. The word's `zIndex: 6` keeps it above the rows.

## Numbers that matter
| | |
|---|---|
| Spring | k9 f12 over .5s, scale 1.35 to 1 |
| Shake | .22s, 6px peak, frequencies 200 and 170 rad/s |
| Type | 236px wide layout, 190px tall, weight 800, tracking -.055em, line height .88, centred |
| Rows | 150px cards at 168px pitch, blur 6px, opacity .9, speeds 700 and 910 px/s |
| Position | wide `CY - 190`, tall `CY - 330` |

## Sound
The loudest moment of the video: a low impact (a 38Hz sine falling quickly, with a 1.4s tail and some air) lands exactly on the slam, after a 2s noise riser that builds from the strip. The kick and clap drum groove starts here.

## Adapt it
- The two lines of copy, and their size so the longer line fits.
- Shake amplitude (6) or remove it by setting it to 0.
- The spring `k`: lower for a looser landing.
- Swap the thumbnail rows for any supporting texture, or drop them.

## Files
- `code/demo.html` runs on its own. Thumbnails are gradient placeholders.
