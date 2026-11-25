---
name: animated-number__slide-up-down-by-trend
description: A number that swaps as a whole when it changes: on an increase the old value leaves upward and the new one comes in from below, on a decrease it is mirrored. Reach for it for counters with plus and minus, orders, stock, cart quantity, scores, anything where the direction of the change should read at a glance.
---

# Animated number

**Code name:** Slide up down by trend.

## What you see
White page. A small group in the middle: an outlined minus button, the number 1.208 in 30px semibold with a grey label "orders" under it, and an outlined plus button. A pointer taps plus at 0.9s, 1.5s and 2.1s: each tap swaps the whole number, the old value fades out while sliding 10px up, the new one fades in sliding up from 10px below. Three quick taps at 3.0, 3.2 and 3.4s stack three numbers on top of each other mid-swap. Six taps on minus from 4.3s run it in reverse: old value leaves downward, new one arrives from above. Ends back on 1.208. 8s loop.

## When to use it
Any single figure that goes up and down by steps: quantity steppers, likes, credits, a day streak. Good at 9:16 because the group scales to the width with nothing else on screen. Wrong for big jumps (use a count-up or the odometer): this only swaps, it does not roll through values.

## How it works
Two spans, one per value. Both run the same 0.3s curve at the same moment. Incoming: opacity 0 to 1 and translateY(+10px) to 0 on an increase (-10px on a decrease). Outgoing: opacity 1 to 0 and translateY 0 to -10px on an increase (+10px on a decrease). Measured from the live page every frame:
```
ms   in-opacity   ms   in-opacity
34   0.12         167  0.84
67   0.35         201  0.91
100  0.57         234  0.95
134  0.73         300  0.99     (done by ~335)
```
The demo uses that table as the easing, so a swap is the same shape as the original. If a new click lands before the last swap ends, the value that was coming in becomes the one going out from wherever it is (the demo does this by giving every value an enter and an exit time). The number is `tabular-nums`, 30px, weight 600, letter-spacing -0.03em, and its box has `overflow:hidden` so the slide is clipped.

## Numbers that matter
| | |
|---|---|
| Slide | 10px, same distance in and out |
| Duration | about 0.33s, curve table above |
| Number type | 30px / 600 / -0.03em, tabular-nums, colour oklch(0.145 0 0) |
| Label | 13px, oklch(0.556 0 0) |
| Buttons | 36px square, 8px radius, 1px oklch(0.922 0 0) border, shadow-sm |
| Number box | min-width 112px (7rem), centred |
| Locale | the page prints 1.208 (dot as thousands separator) |

## Sound
Silent. A tiny tick per swap if used in a reel.

## Adapt it
- `CONFIG.start`, `CONFIG.label`, `CONFIG.sep` (thousands separator).
- `CONFIG.clicks`: list of `[time, +1 or -1]`; the net can be anything, the demo builds every value from the list.
- Colours are in the `.btn`, `.num`, `.lab` rules; for a dark reel swap the white page and ink.

## Files
- `code/demo.html` self-contained, loops, `?w=1080&h=1920` for 9:16.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Animated Number" by ikascom (https://21st.dev/@ikascom/components/animated-number), MIT. Recreated by eye from the public preview; this demo is original code. Full notices: `THIRD_PARTY_NOTICES.md`.
