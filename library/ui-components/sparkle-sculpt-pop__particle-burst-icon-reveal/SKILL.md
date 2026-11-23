---
name: sparkle-sculpt-pop-particle-burst-icon-reveal
description: "A glossy dark blob hides an icon; a tap bursts trailing sparkles outward, the blob dissolves and a gold star pops in with overshoot and a ring pulse. Use to reveal an icon, reward or unlocked item."
---

# Sparkle sculpt pop

**Code name:** Particle burst icon reveal. Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
A 540px wobbly black blob with a rim light and a soft shadow sits centre stage. A simulated finger arrives, presses it at 1.1s (the blob squashes to 94%) and ripples. At 1.18s 78 sparkles (four-point stars in gold, white, pink, cyan and orange) burst outward from the centre with 9-segment trails, a short warm flash and a little gravity; 70 dark dust specks leave the blob edge. The blob shrinks and fades between 1.3 and 2.5s. At 1.7s the star springs in (about 1.2x overshoot, a small rotation) with a gold glow, and two rings pulse out from it, 1.75 to 2.55s. From 5.0s the star shrinks away and the blob reforms by 6.2s for the loop.

## When to use it
Reward and unlock moments, empty-state-to-content reveals, achievement pop-ups. Wrong for restrained enterprise screens.

## How it works
Particles are pure functions of age, with drag: `d = v * (1 - exp(-k*age)) / k + d0`, so any trail point is just the same formula at an earlier age (`age - 0.022 * n`). All randomness comes from an integer hash `rnd(i, seed)`. The blob outline is polar, `r = 1 + sum(a * sin(n*theta + w*t))`, with every temporal frequency a multiple of `2pi / DUR` so the wobble loops; the dissolve adds high-frequency edge noise while radius and alpha fall. Particles are drawn with `globalCompositeOperation = "lighter"`.

## Numbers that matter
| | |
|---|---|
| Timeline | tap 1.1s, burst 1.18s, blob out 1.3-2.5s, star 1.7s, blob back 5.4-6.2s |
| Particles | 78 sparkles, speed 380-1140px/s, life 0.9-1.8s, drag 2.4-3.6; 70 dust specks |
| Star | outer radius 118, spring(6.5, 12), glow blur 50 |
| Rings | 12px to 2px stroke, radius 150 to 470 over 0.8s, second ring 0.14s later |

## Sound
Soft thump on the press, glassy sparkle shimmer on the burst, a rising chime as the star lands.

## Adapt it
- The star path (`star()`) for any icon or logo.
- `col` for the sparkle palette.
- `NP` and the speed range for a bigger or gentler burst.
- Blob colours in the radial gradient.

## Files
- `code/demo.html` runs on its own and loops in 6.4s; wide 1920x1080 or `?w=1080&h=1920`.
- `media/poster.jpg`
