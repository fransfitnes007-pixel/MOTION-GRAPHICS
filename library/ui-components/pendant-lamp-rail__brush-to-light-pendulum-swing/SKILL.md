---
name: pendant-lamp-rail__brush-to-light-pendulum-swing
description: Eight pendant lamps hang from a brushed-metal ceiling track; brush the pointer across them and each switches on with a warm glow on the wall and swings on its cord like a pendulum, while a caption follows the last lamp lit. Reach for it for lighting, home, hospitality and any product row where "turn it on" is the demo.
---

# Pendant lamp rail

**Code name:** Brush to light, pendulum swing.

## What you see
A white page with a faint grey vignette. A small spaced eyebrow "LIGHTING STUDIO · EIGHT PENDANTS", a bold headline, then a thin brushed-metal track across the width with eight grey mounts and black cords: a green enamel dome, a clear glass globe, a brass cone, a rattan dome, a paper sphere, a concrete cone, an opal fluted cylinder, a copper dome. Under the lamps a caption (name, price chip, one line) and two buttons (Shop lighting, Lift to dim). The pointer sweeps along the lamps (0.4 to 2.2s): each lamp under it lights, its bulb turns bright, a warm pool and bloom appear under it, and as it passes it keeps swinging on its cord for a second or more, the next lamp starting just as the previous one dims. The caption swaps to the lamp last lit. A second sweep back (3.2 to 5.0s) kicks the cords the other way. At 9:16 the lamps form two rails of four. 9s loop.

## When to use it
Lighting-store, furniture, restaurant and "pick your style" reels: eight options at once and the answer to "what does it look like on?". The swing makes it feel hung rather than pasted. Replace the SVG lamps with real cut-out product shots (off and on versions crossfaded) for client work.

## How it works
Each pendant is a group with `transform-origin: 50% 0` at its track mount; `rotate()` of the group is the swing. Measured after a fast sweep: a peak of about 2.7 degrees at 0.4s, a zero near 0.8s, the other way -1.3 at 1.1s, +0.6 at 1.8s, i.e. a damped sine, period about 1.4s, halving every 0.7s; neighbours swing in opposite directions. The demo uses `theta = A e^(-1.05 d) sin(w d)` with A = 4.2 degrees times the pointer speed (capped), w = 4.5 rad/s scaled by sqrt(200/cord length) so longer cords are slower, as the original describes. Lit is a 0..1 value driven by the pointer being over the lamp's column; the lit image's opacity is `lit * bloom-k`, the bloom is the lit image blurred (`blur(10px) saturate(1.35) brightness(1.1)`), and a radial warm pool sits on the wall. Lit rises in about 60ms and falls in about 130ms (read: bloom opacity 0.22 at the end of the pass, 0.03 by 0.4s). Each lamp is a 133px-wide column on a 150px pitch. In the demo the lit and swing states are integrated from t=0 each frame.

## Numbers that matter
| | |
|---|---|
| Track | 10px high, gradient #d7d7d7 / #fff / #b0b0b0 / #8e8e8e / #4e4e4e, 1px knurl lines at 40% overlay |
| Pitch | 150px (wide), 170px (tall) |
| Swing | A 4.2 degrees, period 1.4s, decay 1.05 per second, origin at the mount |
| Lit | rise tau 0.06s, fall tau 0.13s |
| Bloom | blur 10px, warm pool radial rgba(255,196,96,.62) |

## Sound
Silent. A soft relay click per lamp and a faint glass chime would fit.

## Adapt it
- `CONFIG.lamps`: kind (`dome`, `globe`, `cone`, `wick`, `paper`, `conc`, `flute`), colours, cord drop, name, price, line.
- `CONFIG.swingA`, `swingW`, `swingC` for heavier or lighter pendants.
- The pointer path `PATH` is in design pixels; make it dwell on one lamp for a product close-up.

## Files
- `code/demo.html` runs on its own and loops; the values to change are in its `CONFIG` block.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Pendant Lamp Rail" by dhxwhy (https://21st.dev/@dhxwhy/components/pendant-lamp-rail), MIT. Recreated by eye from the public preview; this demo is original code. Full notices: `THIRD_PARTY_NOTICES.md`.
