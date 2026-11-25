---
name: theme-toggle-dark-flood-clip-circle-from-knob
description: A light scene with a headline and a phone; a toggle is clicked, its knob slides, and a dark circle grows from the knob until the same scene is in dark mode; then it flips back. Rebuilt by eye from a public motion video (see Credit); use it in app promos and launch reels.
---

# Theme toggle dark flood

**Code name:** Clip circle grown from the knob. Rebuilt by eye from a public motion video; original code, credited below.

## What you see
Warm white with pastel blobs (yellow, blue, pink). Left: a small blue "DARK MODE" eyebrow, the heavy two-line headline "Day or night, easy on the eyes.", a grey line and a toggle; right: a phone with list rows. A cursor glides to the toggle and clicks at 0.9s; the knob springs across and the track turns blue. From 1.02s a circle centred on the knob grows to past the far corner in 0.32s (fast start, slowing), and inside it the same layout is navy with dark cards and blue glows. At 3.2s the toggle is clicked again and the circle shrinks back into the knob.

## When to use it
Any light/dark or before/after switch where the control causes the change: dark mode, a filter, a "pro" toggle, turning automation on. The flood from the control is what makes it read as cause and effect. Wrong when the two states have different layouts (use a match cut).

## How it works
Build the scene twice, once per theme, stacked; the dark copy gets `clip-path: circle(r at knob)`. Because the clip centre follows the knob, the flood starts exactly from the thing that was clicked.
```js
const Rmax = max distance from the knob to the four corners * 1.05     // overscale past the corner
const r = Rmax * eo(seg(t, 1.02, 1.34)) * (1 - ei(seg(t, 3.32, 3.64)))
D.root.style.clipPath = `circle(${r}px at ${kx}px ${ky}px)`
```
The source prompt's gotcha applies: a flood must overscale past the corners and take about 0.3s, or half the screen changes in one frame.

## Numbers that matter
| | |
|---|---|
| Knob | spring f 2.6 zeta .7, 38px travel on an 84 x 46 track |
| Flood | .32s ease-out cubic, radius to 105% of the farthest corner |
| Back | .32s ease-in |
| Headline | 70px weight 800, -0.035em |

## Sound
A switch click on the press and a low soft whoosh with the flood. The demo is silent.

## Adapt it
- `light` and `dark` theme objects (bg, ink, card, row, blobs).
- `head`, `sub`, `eyebrow`.
- Replace the phone rows with two screenshots (one per theme).

## Files
- `code/demo.html` runs on its own; every value to change is in the `CONFIG` block at the top of the skill script.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "revid.ai Claude Opus 5.5 wall #15: Meet Peggy: an app launch made in 20 minutes" by @likithareddy (https://x.com/likithareddy/status/2104202329805467984), Video belongs to its creator; not included. Recreated by eye from watching the public video; this demo is original code and contains none of the video. Full notices: `THIRD_PARTY_NOTICES.md`.
