---
name: stat-stack-slot-roll-landing-ring-blurred-digit-reels
description: Three big stats stack up one per beat, each number spinning in on slot-machine digit reels with vertical motion blur and landing with an expanding light ring; then the stack tilts away in 3D. Rebuilt by eye from a public motion video (see Credit); use it in app promos and launch reels.
---

# Stat stack slot roll with landing ring

**Code name:** Blurred digit reels. Rebuilt by eye from a public motion video; original code, credited below.

## What you see
Warm near-black (#110a08) with a red-brown glow. At 0.3s "11,294" appears as digit columns spinning downward, smeared vertically; the left digits stop first and the right ones keep spinning a little longer, all landing by about 0.9s with a slight overshoot. As it lands a thin pale ring expands from it (to 620px, fading) with a soft warm flash, an orange "+" pops in and "creators" slides in grey to the right. "400K+ posts sent" follows 0.42s later, "5B+ impressions" 0.42s after that. At 3.35s the whole stack swings away: it slides left, turns 38 degrees in Y and 14 in X, blurs and fades.

## When to use it
Social proof in a launch reel or app promo: users, posts, views, payouts. Three lines is the sweet spot. Dark backgrounds only; the ring needs contrast. Wrong for a single number (use `giant-number-count-up-accent__eo5-colour-flip`).

## How it works
Each digit is a reel: a position `pos` that ends on the digit and starts `10 * turns` earlier, so it passes through every digit `turns` times. Digits further right get more turns and a slower clock, so the number settles left to right.
```js
const turns = 2 + j, sl = 1 + j * .1
const u = sstep((t - a) / sl, 2.5, .8)                 // closed-form spring, tiny overshoot
const pos = final - 10 * turns * (1 - u)
// draw digits floor(pos)-1..+1 at y + (pos - k) * 1.3 * size, clipped to one cell
```
Motion blur: the reel speed is measured from the same pure function one frame ahead, and the column is drawn 7 times spread over that frame's travel (a shutter smear) at reduced alpha. The 3D exit is a CSS transform on the canvas element itself.

## Numbers that matter
| | |
|---|---|
| Lines | .3s, then every .42s |
| Reels | spring f 2.5 Hz zeta .8, 2 + j turns, clock 1 + .1j |
| Ring | lands at start + .3s, radius 40 to 660px over .75s ease-out, 3px, alpha .4 to 0 |
| Type | 124px heavy at 1920, line height 1.34; label 30% size, 62% white |
| Accent | + in #ff5a3c, spring f 2.4 zeta .5 |
| Exit | .5s ease-in: -500px x, rotateY 38, rotateX 14, rotate -8, blur 10 |

## Sound
A ratchet tick under the spin and a low hit on each landing, 20 to 40 ms before the frame, plus a whoosh on the 3D exit. The demo is silent.

## Adapt it
- `lines`: values may contain commas or letters (K, M, B); only digits spin.
- `accent`, `bg`, `glow`.
- `t.every` to match the BPM (120 BPM: .5).

## Files
- `code/demo.html` runs on its own; every value to change is in the `CONFIG` block at the top of the skill script.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "revid.ai Claude Opus 5.5 wall #18: SuperX: a one-shot launch reel" by @robj3d3 (https://x.com/robj3d3/status/2103875898349088830), Video belongs to its creator; not included. Recreated by eye from watching the public video; this demo is original code and contains none of the video. Full notices: `THIRD_PARTY_NOTICES.md`.
