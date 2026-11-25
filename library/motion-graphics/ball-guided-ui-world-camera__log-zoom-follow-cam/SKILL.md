---
name: ball-guided-ui-world-camera-log-zoom-follow-cam
description: On a dark dot grid a white ball pops out of a toggle, drives a slider to 100, bounces across three cards as they arrive, then rides home while the camera follows and pulls back. Rebuilt by eye from a public motion video (see Credit); use it in app promos and launch reels.
---

# Ball guided UI world with follow camera

**Code name:** Log-space zoom follow cam. Rebuilt by eye from a public motion video; original code, credited below.

## What you see
Near-black (#0b0b0c) with a faint dot grid, charcoal controls, one blue (#1d77de). The camera starts close on a toggle; a cursor clicks it at 0.6s, the toggle turns blue and its white knob (the ball) springs free in an arc to the start of a slider, landing at 1.35s with a squash. It rolls the knob to the end by 2.6s while the blue fill and a value bubble (0 to 100) follow. At 100 it launches toward three dark cards that slide in one per beat ("Slider", "Gravity", "Messages") and bounces once on each icon. The camera pulls back to show the whole world, the ball rides a long arc home, the slider drains and the toggle switches off as it lands, matching the first frame.

## When to use it
A product tour where the features are small controls and you want one thread through them: settings, an onboarding, a design system reel. The ball is the narrator. Wrong when each feature needs a full screen.

## How it works
The ball's whole route is one function of time (arcs are a lerp plus `sin(pi u) * lift`). The camera is the moving average of the last 0.35s of that route, which gives a smooth trailing follow and is still pure:
```js
for (let k = 0; k < 14; k++) { const p = ball(t - k * .025); x += p[0]; y += p[1] }
const z = Math.exp(lerp(Math.log(z0), Math.log(z1), eio(u)))   // zoom in log space: equal-looking speed in and out
g.setTransform(z, 0, 0, z, CX - x * z, CY - y * z)
```
Squash keeps volume: `sx = 1 + .3 q, sy = 1 / sx`, anchored at the contact point. The slider value is computed from the ball's x, so they cannot drift apart (a gotcha in the source prompt).

## Numbers that matter
| | |
|---|---|
| Camera trail | 14 samples x .025s; zoom keys 1.9 / 1.35 / 1.2 / .78 / 1.9 |
| Toggle | 128 x 68; knob slide .16s ease-out |
| Arcs | lift 220 (to slider), 260 (to cards), 90 (card to card), 520 (home) |
| Cards | spring f 2 zeta .75 from +260px, .25s apart from 2.95s |
| Squash | .16s per impact, 30% stretch |

## Sound
A soft tick on each ball contact (lower for the slider landing, higher for the cards), a click for the cursor, nothing else. The source asks for "a subtle UI sound on each contact". The demo is silent.

## Adapt it
- `cards` and `subs` text, `accent`.
- Move the world pieces (`TG`, `SL`, `CARDS`) and the route in `ball()` follows.
- `zoom` keys to frame more or less.

## Files
- `code/demo.html` runs on its own; every value to change is in the `CONFIG` block at the top of the skill script.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "motionvideo.xyz gallery: White dot UI motion system" by @rossaxbt (https://x.com/rossaxbt/status/2108933141406638456), Video belongs to its creator; not included. Recreated by eye from watching the public video; this demo is original code and contains none of the video. Full notices: `THIRD_PARTY_NOTICES.md`.
