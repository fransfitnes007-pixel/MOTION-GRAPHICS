---
name: cover-orbit-ring-title-pop-polar-orbit-radius-ease
description: "A 190px title snaps in from 140 percent through a blur while twelve small video covers fly out from the centre and settle into a slowly rotating ellipse around it. Closing a list with a title that names it, \"Every niche\", \"Everyone\", \"All of this\"."
---

# Cover orbit ring around a title

**Code name:** Polar orbit with eased radius.

## What you see
A 190px title snaps in from 140 percent through a 16px blur in 0.25s. At the same time twelve small portrait covers fly outward from the centre, each 20ms after the last, to an ellipse 800px wide and 380px high around the title, where they keep turning slowly.

## When to use it
Closing a list with a title that names it, "Every category", "Everyone", "All of this". The ring gives a sense of many without more cuts.

## How it works
Each cover sits on a polar angle that increases with time. Its radius is the full radius times an eased 0 to 1, so it flies out to the ring and then rides it.

```js
const a = i / 12 * Math.PI * 2 + lt * .9, k = eo(seg(lt, T0 + i * .02, T0 + .3 + i * .02))
S(o, { left: (960 + Math.cos(a) * 800 * k - 60) + 'px', top: (540 + Math.sin(a) * 380 * k - 80) + 'px', opacity: k, transform: `rotate(${Math.cos(a) * 12}deg)` })
```

## Numbers that matter
| | |
|---|---|
| Title | 190px, scale 1.4 to 1, blur 16px to 0, `eo5` over 0.25s |
| Ring | 12 covers, 120 x 160, ellipse 800 x 380 |
| Fly-out | 0.3s `eo`, 20ms stagger |
| Spin | .9 rad per second |

## Sound
A suggested soundtrack is a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. A two-beat noise riser (300 Hz up to 9 kHz) is building under this scene and resolves into the beat-12 impact.

## Adapt it
- Cover count and ring size.
- Spin speed `.9`.
- Title.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.
