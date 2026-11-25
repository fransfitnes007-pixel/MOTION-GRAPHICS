---
name: iris-blade-aperture-photo-open-six-blade-hex-aperture
description: A dark disc made of six camera iris blades snaps open around a hexagonal hole onto a photo, holds, and closes again. Rebuilt by eye from a public motion video (see Credit); use it in app promos and launch reels.
---

# Iris blade aperture photo open

**Code name:** Six-blade hexagon aperture. Rebuilt by eye from a public motion video; original code, credited below.

## What you see
A dark grey disc pops in on a spring at 0.15s. It is six blades meeting in the middle, each a slightly different shade with hairline seams. At 0.75s the blades rotate and slide outward around a growing hexagon; within 0.38s the hole is larger than the disc and a photo (here a lit orange doorway in a dark room) fills it. The disc holds and pushes in 4% until 2.65s, then the blades close in 0.32s and the disc shrinks away at 3.3s.

## When to use it
A camera or photo product, a "snap" moment, or any scene change that should feel mechanical rather than soft. It is the more specific cousin of the plain circle iris (`iris-transition__circle-mask-open-close` in motion-reel-kit): use this when the brand is about photos or capture. Wrong on a dark background unless you lighten the blades.

## How it works
The aperture is a regular hexagon with circumradius `a` and rotation `rot`. Each blade is the region bounded by one hexagon edge, that edge's extension out to the rim, the short arc along the rim, and the previous edge's extension back to the hexagon (the build rule in @twoclipping's public prompt: "two vertices, both edge extensions and the SHORT arc between them"). The six blades tile the ring between hexagon and circle exactly.
```js
// extend edge P_i -> P_i+1 beyond P_i+1 to the circle of radius R
const b = p.x*ux + p.y*uy, c = p.x*p.x + p.y*p.y - R*R, s = -b + Math.sqrt(b*b - c)
E_i = p + u * s
// blade i: P_i, P_i+1, E_i, arc(E_i -> E_i-1, short way), back to P_i
```
Opening is one number: `a = op * R * 1.2` (1.2 so the hexagon clears the rim) and `rot = -62deg * (1 - op)`. The photo is drawn first inside a circle clip and the blades over it.

## Numbers that matter
| | |
|---|---|
| Open | .38s, ease-out quintic |
| Close | .32s, ease-in-out cubic |
| Blade turn | 62 degrees from closed to open |
| Disc | radius 210 at 1920 wide, spring pop f 2.2 zeta .6 |
| Blades | #2b2b2e / #1e1e21 alternating, seams white 16% at 1.5px |

## Sound
A short mechanical shutter click on the open (a 30 ms noise burst with a 2 kHz band-pass) reads well; the source film used a downloaded camera-shutter SFX. The demo is silent.

## Adapt it
- Replace `photo()` with `g.drawImage(img, ...)` of your screenshot or photo.
- `radius`, `turn`, `openDur`.
- Blade colours to match the background.

## Files
- `code/demo.html` runs on its own; every value to change is in the `CONFIG` block at the top of the skill script.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "revid.ai Claude Opus 5.5 wall #8: Develop: a photo print app launch" by @twoclipping (https://x.com/twoclipping/status/2103835273813496100), Video belongs to its creator; not included. Recreated by eye from watching the public video; this demo is original code and contains none of the video. Full notices: `THIRD_PARTY_NOTICES.md`.
