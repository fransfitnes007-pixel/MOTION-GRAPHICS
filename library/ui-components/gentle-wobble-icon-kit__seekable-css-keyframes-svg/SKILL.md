---
name: gentle-wobble-icon-kit__seekable-css-keyframes-svg
description: 30 line icons whose hover animations (AnimateIcons by Avijit Dey, MIT) were rebuilt as plain SVG plus CSS keyframes that auto-play and loop. A softer motion style than the first kit - small wobbles, swings and pulses - on a light page. Reach for it for camera, star, trophy, gift, gamepad, dumbbell, book, music, thumbs-up, crown, target and similar creator icons.
---

# Gentle wobble icon kit

**Code name:** Seekable CSS keyframes SVG.

## What you see
Warm off-white page, heading "Gentle wobble icon kit", then a grid of 30 white tiles (8 across wide, 5 across tall). One dark or coloured line icon per tile with its name under it. The tiles spring in over the first 0.6 s, then each icon does its own small move on a loop, shifted 0.1 s from its neighbour: the camera lens pinches and swells, the star rocks, the trophy hops and tilts, the gift lid lifts and settles, the globe's meridian flips, the dumbbell curls twice, the gamepad rumbles and its buttons pop to double size, the ghost's eyes look left then right, the sun's rays dim and the centre pulses, the target rings pulse outward from the middle. 6 s loop with no seam.

## When to use it
Creator and fitness/gaming/media beats: a camera for filming, a trophy for a win, a crown for top creator, a gift for a reward, a megaphone for an announcement, a lightbulb for a tip, a thumbs-up for a like. Motion is small (0.3 to 1.1 s, rotations of 4 to 20 deg, scales of 0.6 to 1.7), so it reads well at tab-bar and chip sizes. For bigger draw-in and spring moves (heart, bell, send, check) use `spring-draw-wobble-icon-kit__seekable-css-keyframes-svg`.

## How it works
Same engine as the first kit: every moving part has a class and its own `@keyframes`, all spanning one loop length `L` (2 s here for every icon), motion plays once from 0.15 s then rests. `render(t)` pauses each icon's animations and sets `currentTime`, so a frame is a pure function of time:

```js
for (const a of svg.getAnimations({ subtree: true })) { a.pause(); a.currentTime = (t + offset) * 1000 }
```

The source components use motion variants with `transformBox: "view-box"` and explicit `originX/originY` in px, which become `transform-box: view-box; transform-origin: 7.5px 15.5px` etc. unchanged. Each variant uses `ease: "easeInOut"` and a `times` array; those map to `cubic-bezier(.42,0,.58,1)` on every keyframe interval and percentages of `L`. The style differs from the first kit by construction: nearly every move here is a multi-point wobble (`[0,-8,6,-3,0]`) rather than a draw-in or a spring.

Changes from the source: hover became a loop; durations are the source's default (`duration = 1`) times each variant's own factor (0.3 to 1.1 s); the rocket and flame variants are left out because the first kit already has them (different motion); party-popper is the AnimateIcons version (streamers pinch, confetti dots swell), a different motion from the first kit's draw-in.

## Numbers that matter
| | |
|---|---|
| Icons | 30, 24 x 24 viewBox, stroke 2, round caps, `currentColor` |
| Loop | 2 s each, motion starts at 0.15 s |
| Camera | lens scale 1, 0.6, 1.15, 1 (times 0, .35, .7, 1) over 0.7 s, body scaleY 0.97 over 0.35 s |
| Trophy | y 0, -2, 0, -1, 0 and rotate 0, -8, 6, -3, 0 over 0.8 s, origin 12px 22px |
| Gift | lid rotate 0, -5.5, 1.5, 0 about 3px 11px; bow scaleY 0.92; ribbon scaleY 1.06; 0.7 s |
| Gamepad | rumble rotate 0, -4, 4, -3, 2, 0 in 0.6 s; D-pad scale 0.7 then 1.08 in 0.5 s; each button scale 1 to 2 to 1 in 0.3 s, 0.15 s apart |
| Bell-ring | rotate 0, -12, 10.2, -6, 3, 0 over 1.1 s about the top centre, clapper x +-1.7, waves fade and pulse |
| Target | rings scale to 1.7 (inner), 1.22, 1.08 (outer), 0.1 s apart |
| Grid | stagger 0.1 s, tile spring(7, 11), accents coral, blue, green, amber |

## Sound
Silent. A short pop for the camera shutter, a coin for trophy and gift, a chime for lightbulb.

## Adapt it
- Colours and page: `CONFIG` (`bg`, `tile`, `ink`, `accents`). Icons are `currentColor`.
- Show some only: `CONFIG.only = ['camera','trophy','gift']`.
- Standalone: each file in `code/svg/` auto-plays by itself with its own `<style>`.
- Slower or faster: change the `2s` in `animation:` of that icon's classes.
- New icon: add the children from the upstream `icons/lucide/<name>-icon.tsx` and a spec in `code/generator/ai_specs.py`, run `gen.py`.

## The 30 icons
bell-ring, book-open, camera, crown, dumbbell, film, flag, gamepad, ghost, gift, globe, hand-heart, heart-plus, image-plus, key, lightbulb, link, map-pin, medal, megaphone, music, party-popper, share, star, sun, target, thumbs-up, trophy, video, wand-sparkles.

## Files
- `code/demo.html` runs the grid and loops; `CONFIG` at the top.
- `code/svg/<name>.svg` 30 standalone auto-playing icons.
- `code/generator/` the Python that built the CSS (`core.py`, `ai_specs.py`, `gen.py`).
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "AnimateIcons / Lucide" by Avijit Dey (https://21st.dev/community/icons), MIT. "Lucide" by Lucide Contributors (https://lucide.dev/), ISC. Rebuilt as render(t) from the published code. Full notices: `THIRD_PARTY_NOTICES.md`.
