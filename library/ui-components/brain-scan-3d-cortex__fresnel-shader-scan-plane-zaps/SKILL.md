---
name: brain-scan-3d-cortex-fresnel-shader-scan-plane-zaps
description: "A translucent violet 3D brain that swings to face whatever region is being read, regions glowing in their own colours and pulsing, a cyan scan plane sweeping through, jagged electric arcs and sparks jumping between active regions, and a chat bubble pinned to the focus. Use for an AI that reads or scores content and needs to look like it is thinking."
---

# Brain scan 3D cortex

**Code name:** Fresnel shader, scan plane and zaps.

## What you see
A dark violet panel with a glowing glass brain in the middle. The brain is see-through: its edge glows lilac where the surface turns away from you, and the folds are shaded slightly lighter on the ridges. As the review reaches each stage, one brain system lights up in its own colour (visual cortex blue, face area pink, language amber, auditory green, reward yellow, urgency red, and so on) and pulses. The one being read is brightest and the others drop to 35%. The brain turns to bring that region to the front and sways a little. A cyan plane slides back and forth through the brain, brightening the cortex it crosses. Every fifth of a second a jagged arc of light jumps between two lit regions, 65% of the time ending on the focus, and bursts into 14 sparks where it lands. A grey chat bubble with the system name, its score out of 10 and a line of evidence pops in beside the focus, with a dot on the spot. A pill at the top left names the current stage, and small chips at the bottom left list the lit systems.

## When to use it
The waiting screen for an AI review or analysis, where you want to show "reading, scoring" as a visible process. It carries a lot of attention, so use it once per screen and keep the rest of the screen quiet. It needs WebGL in the app (the component shows a fallback message without it).

## How it works
The real component loads a 20,484-vertex cortex mesh from a GLB. Vertex colour carries the region label (red), hemisphere (green) and sulcal depth (blue). A small `DataTexture` of 256 slots (label by hemisphere) holds each region's system colour and intensity, rewritten every frame. The fragment shader shades each vertex:

```glsl
float fres = pow(1.0 - abs(dot(n, v)), 2.2);
vec3 base = mix(vec3(0.20, 0.17, 0.42), vec3(0.42, 0.40, 0.78), 1.0 - sulc);   // gyri lighter than sulci
float body = 0.10 + 0.55 * fres;
vec3 col = base * body + vec3(0.62, 0.55, 1.0) * fres * 0.55;
col += glowC * act * (1.25 * pulse) * (0.55 + 0.45 * (1.0 - sulc));            // pulse = .72 + .28 sin(t*5 + y*.15 + x*.1)
float d = abs(vPos.y - uScan);                                                  // uScan = sin(t*1.3) * 80
col += vec3(0.55, 0.85, 1.0) * uScanOn * (smoothstep(3.0, 0.0, d) * 1.6 + smoothstep(16.0, 0.0, d) * 0.12);
```
It is drawn twice with additive blending, once for back faces (35% alpha) and once for front faces. Camera: perspective 32 degrees at z 330. Rotation is `yaw += d * min(1, dt * 2.4)` toward `-atan2(focus.x, -focus.y)` plus a `sin(t * .6) * .22` sway, or a free spin of 0.45 rad/s when nothing is focused. Zaps are seven pooled `THREE.Line`s with 18 points each, jittered by up to 4.5 units and regenerated every other frame at 30 fps; sparks are 160 pooled points. With TRIBE frames the glow follows a per-vertex activation prediction instead of the per-system scores.

The demo cannot load the mesh or three.js, so it rebuilds the scene on a canvas: two folded ellipsoid hemispheres (about 26,000 vertices) shaded per vertex with the same terms as the fragment shader, rasterised as additive triangles in JavaScript, with a faint flat fill added so the interior reads as translucent. Regions, pulses, the scan plane, the arcs and the sparks use the source formulas. The anatomy is a stand-in and the system centroids are approximate, so treat the shape as a placeholder and the shading, motion and timing as the reference.

## Numbers that matter
| | |
|---|---|
| Camera | perspective 32 degrees, z 330, tilt `.18 + sin(t * .4) * .05` |
| Yaw smoothing | `d * min(1, dt * 2.4)`, sway `sin(t * .6) * .22`, free spin .45 rad/s |
| Glow | `1.25 * pulse * (.55 + .45 * (1 - sulc))`, pulse `.72 + .28 sin(...)` |
| Dimming | non-focused systems at `.35` |
| Scan plane | `sin(t * 1.3) * 80`, core band 3 units, halo 16 units |
| Zaps | every .22s (.09s while scanning), life .35 to .6s, 18 points, jitter 4.5, 65% to the focus |
| Sparks | 14 per zap, speed up to 45 each axis, life .4 to .8s |
| Panel | `radial-gradient(ellipse at 50% 40%, rgba(124,58,237,.18), rgba(5,5,9,.9) 70%)`, border `rgba(139,92,246,.3)` |
| Bubble | iOS dark grey `#2C2C2E`, 260px wide, spring in from its tail corner |

## Sound
Silent in the app. A low electric hum with soft ticks on each zap would fit.

## Adapt it
- The system list: names, RGB colours, anchor regions and the evidence lines.
- Stage timing (`STAGE`, 1.0s here, 1.1s in the app).
- The base violet `vec3(0.20, 0.17, 0.42)` and rim colour for another palette.
- Any watertight mesh with per-vertex region ids can replace the cortex.

## Files
- `code/demo.html` runs on its own and loops in 12s (about 40 seconds to render).
