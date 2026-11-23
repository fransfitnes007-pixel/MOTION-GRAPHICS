---
name: phone-grid-tilted-row-preserve-3d-stagger-spring
description: "A tilted row of seven phones rises into place from the centre outward, each playing a video cover; \"Syncing\" spinners turn into green \"Synced\" ticks outward from the middle phone, under a \"device row - live\" pill and a headline."
---

**Code name:** Preserve-3d stagger spring.

## What you see
Seven phone bodies (228px wide, 472px tall, 58px corner radius, dynamic-island pill) in one row at 262px pitch. The row is tilted 18 degrees back (`rotateX`) and levels to 6 degrees as it rises 160px. Phones spring in from the centre outward, 0.07s per step, each with a slight `rotateY` fan (-5 degrees per step away from the middle) and a slow 6px bob. A small pill under each phone reads "Syncing" with a spinning ring, then flips to a green tick and "Synced", centre first, 0.12s per step, 0.45s after its cue. At 14.2s the row sinks and shrinks to 74% with a 1.2px blur to make room for what comes next.

## When to use it
Showing scale in the physical world: many devices each doing a job. The status pills tell the story, so each cover needs to be different. Seven is the most that fits at this size; use five for a tall frame.

## How it works
`wall` carries `perspective: 2200px`; `wallIn` has `transform-style: preserve-3d` and holds the tilt. Each phone's entrance is a spring on its own distance `d = |i - 3|` from the middle:

```js
const d = Math.abs(p.i - 3), pin = spring(seg(t, 12.32 + d * .07, 12.95 + d * .07), 7, 11)
S(p, { opacity: clamp(pin * 1.5), transform: `translateY(${(1 - pin) * 120 + Math.sin(t * 1.4 + p.i) * 6}px) rotateY(${(p.i - 3) * -5}deg)` })
const at = WT.post + d * .12, posted = t > at + .45   // flips the pill's text and icon
```
The spinner is a bordered circle rotated at `t * 720` degrees per second, not a CSS animation. The picture inside each phone scales gently (`1.04 + .04 * sin(t*.8 + i)`) so the screens look alive.

## Numbers that matter
| | |
|---|---|
| Phone | 228 wide, height = width x 2.07, bezel 11px, island 34% x 30px |
| Layout | x = 960 - 3.5x262 + i x 262 + 17, y = 330 + 18|i-3| |
| Tilt | rotateX 18 to 6 degrees, `eo5` 0.7s, perspective 2200px, origin 50% 60% |
| Spring | k=7, f=11, 0.63s, delay 0.07s x distance |
| Pills | 18px bold, spinner 12px, "Synced" at cue + 0.45s, 0.12s per step |
| Settle | 14.2s to 14.6s `eio5`: y +30px, scale .74, blur 1.2px |

## Sound
Soft pops as each phone's pill flips to Synced (about 820 Hz rising 60 Hz per step, panned left and right). Music is the groove after the dark scene; an impact marks the return to light.

## Adapt it
- Cover images (`coverBg(n)` to `url(...)`), phone count and pitch.
- Pill text ("Syncing"/"Synced") and the cue `WT.post`.
- Tilt angles, `swap` time.
- Remove the bob and cover scale for a calmer look.

## Files
- `code/demo.html` (phones filled with gradient placeholder covers).
