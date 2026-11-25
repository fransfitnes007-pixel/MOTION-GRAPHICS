---
name: mechanical-odometer-drum-carry-spring
description: A black metal plate with numeral drums that roll like a real odometer. The last drum is driven and the others carry, so 1,099 to 1,100 turns three drums together. Reach for it for view counts, money totals and any number reveal that should feel physical, for example in the Blender-style reels.
---

# Mechanical odometer

**Code name:** Drum carry spring.

## What you see
A dark anodised-aluminium plate with four screws and a small spaced label (VIEWS). In the middle a window of five numeral drums with soft top and bottom shading and a glass glint. At 0.35s the number spins up from 0 to 1,099 (fast drums blur), settles with a tiny overshoot; leading drums stay blank. At 3.0s it goes to 1,100 and you see the carry: only the last drum turns, then the tens and hundreds roll over together at the end of its turn. At 4.6s it spins to 12,480 with a comma plate appearing between the thousands. 7s loop.

## When to use it
Any number that should be earned: views, followers, money earned, orders, days streak. Best on a dark hero beat. For a live product, install the original MIT component from its page (CSS 3D drums and real DOM text) and screen-record it; `demo.html` is the render(t) version for video. Wrong for tiny numbers in running text.

## How it works
Three rules, all kept verbatim in the demo from the original:

1. The carry. Drum 0 moves with the value; drum k moves only while drum k-1 passes 9 to 0. The first carry takes the last tenth of that step, the others turn in lock-step:
```js
below = digit + clamp((below - 10 + w) / w, 0, 1)   // w = 0.1 for k=1, else 1
```
2. A spring on the value, not the digits: `stepSpring` with stiffness 140, damping 0.85, sub-stepped at 1/120s. A drum faster than `maxSpin` (24 digits/s) is smeared (`smear`).
3. Light that does not turn: `drumLight` gives one shading ramp per drum from the lamp angle (315 degrees), Lambert plus a specular band plus occlusion at the window lip.

The demo is a flat 2D rebuild of the drums (translating digit strips with the same shading ramp), because the original's ten-sided CSS 3D drum would not be a pure function of time with its live font probe. The value is simulated from t=0 each frame so any `render(t)` is repeatable. The original font (Big Shoulders Bold) is embedded in the source as base64; the demo falls back to a condensed system face.

## Numbers that matter
| | |
|---|---|
| Spring | stiffness 140, damping 0.85 |
| Carry | first carry over the last 0.1 of a step |
| Face height | 1.12 em; window 1.56 em; radius = face / (2 tan(pi/10)) |
| Spin cap | 24 digits/s, smeared above a third of it |
| Lamp | 315 degrees, gloss 0.34 (ink finish) |
| Finishes | ink (anodised), bone (steel), steel (graphite), brass (blackened), red signal drum |

## Sound
Silent in the demo; the original has an optional `sound` prop. Pair with a quiet ratchet tick per drum step and a soft clunk on landing.

## Adapt it
- `CONFIG.script`: list of `[time, targetValue]`. Money: set `decimals: 2` and a $ prefix plate.
- `CONFIG.digits`: number of drums; `label`: engraved word.
- Plate and drum colours are in the `.plate`, `.win`, `.strip div` CSS; swap for the bone/steel or brass finish from the table.
- For a 9:16 reel the plate sizes itself to the width (`size`).

## Files
- `code/demo.html` runs on its own and loops; the values to change are in its `CONFIG` block.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Mechanical Odometer" by cipriantitire (https://21st.dev/@cipriantitire/components/mechanical-odometer), MIT. Formulas follow the original MIT component; the demo is rewritten as render(t). Full notices: `THIRD_PARTY_NOTICES.md`.
