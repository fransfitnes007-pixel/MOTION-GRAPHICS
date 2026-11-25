---
name: notification-storm-then-one-card-accelerating-spawn-3d-fly-in
description: A serif question builds over an app dock while notification cards fly in faster and faster until they bury the frame, blow outward, and leave one card in the centre with the answer line. Rebuilt by eye from a public motion video (see Credit); use it in app promos and launch reels.
---

# Notification storm then one card

**Code name:** Accelerating spawn with 3D fly-in. Rebuilt by eye from a public motion video; original code, credited below.

## What you see
Warm white with a soft pink glow top-right and a blue glow bottom-left. "How many apps / did you check today?" appears word by word in a light serif from 0.1s (0.12s apart, blur to sharp). A row of six app icons sits near the bottom with red badges whose counts climb. From 0.6s white notification cards fly in from the edges, tilted in 3D and slightly blurred, settling at scattered spots: one, then three by about 1.05s, ten by 2s, about 28 by 2.6s, covering the headline. At 2.62s the whole storm blows outward (cards scale up 60%, blur to 14px, fade) with the headline and dock. At 2.85s one card drifts in from the upper right and settles, 25% bigger, in the middle; at 3.45s "And you still missed this one." builds under it, "this one." in red italic.

## When to use it
A hook for anything that replaces app-switching or catches what you miss: an inbox, a scheduler, a multi-account dashboard, a CRM. The accelerating count is the joke; the single card is the payoff. 5 seconds is the whole video in the source. Wrong for calm brands.

## How it works
The spawn schedule is a formula, so it is the same every render and accelerates on its own: card `i` arrives at `t_i = start + sqrt(i / rate)`, which means `rate * (t - start)^2` cards are on screen at time t.
```js
const ti = C.t.spawn + Math.sqrt(i / C.rate)           // rate 7.2 -> ~28 cards by 2.6s
const far = (1 - p) * 700 + storm * 900                 // fly in along the ray from the centre, blow out the same way
card.style.transform = `rotateX(${rx*(1-p)}deg) rotateY(${ry*(1-p)}deg) rotate(${rz*.4}deg) scale(${1.15 - .15*p + storm*.6})`
```
Final spots, tilts and avatar colours come from a seeded hash, never `Math.random()`. Each card enters along the ray from the frame centre through its final spot, so they all seem to come from off-screen behind the viewer.

## Numbers that matter
| | |
|---|---|
| Question | 66px serif at 1920, words .12s apart, .38s eo5, blur 9 to 0 |
| Spawn | start .6s, rate 7.2 (t^2), 30 cards max, each .45s eo5 from 700px out, blur 6 to 0 |
| 3D tilt in | rotateX up to 20 degrees, rotateY up to 35 degrees, settles to a 2 degree z-tilt |
| Storm out | 2.62s, .32s ease-in-out, scale +60%, blur 14, out 900px |
| Hero card | 2.85s, spring f 1.4 zeta .82, scale .7 to 1.25 |
| Answer | 46px serif, words .1s apart from 3.45s, accent #d63a2f italic |

## Sound
Notification pings that speed up with the spawn (one per card, quiet, pitch randomised by the same seed), a whoosh on the blow-out, silence before the hero card. That silence is the beat. The demo is silent.

## Adapt it
- `q` and `a` word lists (`*` marks accent words).
- `apps` icon colours (or `url()` icons), `rate` and `cards` for density.
- Card text: the two grey bars are placeholders; put real sender names in `.tx`.

## Files
- `code/demo.html` runs on its own; every value to change is in the `CONFIG` block at the top of the skill script.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "revid.ai Claude Opus 5.5 wall #44: How many apps did you check today?" by @dhruvalgolakiya (https://x.com/dhruvalgolakiya/status/2102854634536866099), Video belongs to its creator; not included. Recreated by eye from watching the public video; this demo is original code and contains none of the video. Full notices: `THIRD_PARTY_NOTICES.md`.
