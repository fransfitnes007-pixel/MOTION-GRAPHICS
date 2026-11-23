---
name: logo-slam-shake-spark-burst-scale-shake-radial-sparks
description: "On the beat a wordmark slams in from 170 percent with a hard 26px shake, a white flash and 26 sparks bursting outward, then zooms through the screen at the end. The hit on a beat drop, such as the logo reveal after a hook."
---

# Logo slam with shake and spark burst

**Code name:** Scale, shake, radial sparks.

## What you see
A white flash (55 percent, gone in 0.12s) as the wordmark lands from 170 percent, blurred 12px, in 0.32s with a hard 26px random shake that decays over 0.35s. Twenty-six small lilac dots burst out of the centre in random directions at 300 to 1000px, fading as they go, stretched flatter vertically. A tagline fades up at 0.45s. In the last 0.42s the wordmark scales up to 9x while it fades and blurs, so the camera appears to fly through it.

## When to use it
The hit on a beat drop, such as the logo reveal after a hook. The zoom-through at the end is built to hand over to a screen that starts small and pushes in (see the dashboard cards skill). Use it once per video.

## How it works
Entry is `eo5` over 0.32s. The shake is a seeded random offset per frame (60 Hz hash) scaled by `1 - lt/.35`. Sparks take a seeded angle and speed and ride `eo(seg(lt, 0, .9))`.

```js
const shake = lt < .35 ? (rand(Math.floor(lt * 60)) - .5) * 26 * (1 - lt / .35) : 0
const out = ei(seg(lt, d - .42, d))                      // zoom-through exit
transform: `translate(${shake}px,${shake*.6}px) scale(${lerp(1.7, 1, k) * lerp(1, 9, out)})`
// spark i: angle = rand(i) * 2pi, speed = 300 + rand(i+3) * 700, y squashed by .6
```

## Numbers that matter
| | |
|---|---|
| Entry | 0 to 0.32s, `eo5`, scale 1.7 to 1, blur 12px to 0 |
| Shake | 26px peak, 0.35s, y at 60 percent |
| Sparks | 26 dots, 8px, 0.9s life, radius 300 to 1000px |
| Exit | last 0.42s, `ei`, scale to 9x, blur 10px |
| Flash | (1 - k) * .55 over 0.12s |

## Sound
Suggested bed: a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. The beat-12 impact sits exactly on the flash, and a riser (noise swell, 300 Hz to 9 kHz) builds over the two beats before.

## Adapt it
- The wordmark and tagline.
- Spark count (26) and radius range.
- Scene length `d` so the zoom-through lands on your cut.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.
