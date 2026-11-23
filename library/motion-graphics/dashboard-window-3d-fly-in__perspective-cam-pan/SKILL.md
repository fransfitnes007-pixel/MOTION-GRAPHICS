---
name: dashboard-window-3d-fly-in-perspective-cam-pan
description: "A dark browser window flies in from the right in 3D perspective, a virtual camera drifts across the screen capture inside it, the page swaps to a second view and back, then the camera dives to a button, the cursor clicks it, and the window zooms through the lens."
---

# Dashboard window fly-in with camera pan

**Code name:** Perspective cam pan.

## What you see
At 4.86s a 1000x562 window with a macOS title bar slides 420px from the right, rotating from -34 to -9 degrees about Y and 10 to 3 about X, scaling from 86% to 100% (0.74s). The picture inside slowly zooms from 1.0 to 1.18 and drifts. At 5.48s a second page fades over it for 0.7s and fades out at 6.18s. From 7.3s the camera slides to the top-right button and zooms to 1.68; a cursor flies in and clicks it at 7.76s with a ripple. At 8.1s the window scales 3.4x and blurs, filling the frame, so the next scene can start from inside it.

## When to use it
Showing a product screen in a video. It gives a static screenshot life without recording the screen: any 1920x1080 capture works. Pair it with a voiceover that names what is on the screen. Use the zoom-through exit to cut into a dark scene.

## How it works
The window is a clipped box; the capture is one large element scaled and translated inside it, so a "camera" is just a transform on that element. `cam(w, fx, fy, z)` takes a focal point in capture pixels and a zoom, and clamps so you never see past the edges. `camPt` runs the same maths backwards to give the on-screen position of any capture point, so the cursor lands on the button even while the camera is moving.

```js
const k = w.vw / capW * z
const x = clamp(w.vw / 2 - fx * k, w.vw - capW * k, 0), y = clamp(w.vh / 2 - fy * k, Math.min(0, w.vh - capH * k), 0)
img.style.transform = `translate(${x}px,${y}px) scale(${k})`
// where a capture point ends up on screen:  [box[0] + x + px*k, box[1] + 46 + y + py*k]
```
The window uses `perspective(2400px)` on its own transform with `transform-origin: 30% 50%`, and the same factors `(1 - zoomOut)` flatten the rotation as it scales up, so the zoom-through is straight on.

## Numbers that matter
| | |
|---|---|
| Window | 1000x562 view plus a 46px bar at (840,150); radius 22px; dark shadow stack |
| Fly in | `eo5` over 0.74s from 4.86s; X offset 420px; rotateY -34 to -9; rotateX 10 to 3; scale .86 to 1 |
| Camera zoom | 1 to 1.18 over 6.1s to 7.6s, then +0.5 over 7.55s to 7.95s |
| Focal point | (1072,560) to (1632,188) over 7.3s to 7.95s |
| Page swap | in at brief -0.05s for 0.35s, out at run -0.08s for 0.3s; the base page dims to 15% |
| Exit | 8.1s to 8.62s `eio5`, scale to 3.4x, blur 10px |

## Sound
A whoosh on the scene entry; a mouse click sound at 7.76s when the cursor presses. Music is in its groove.

## Adapt it
- Replace `dashCap()` with `<img src="your-capture.png">` set to 1920 wide (capture at 2x for crisp zoom).
- `BOX` for placement, `fx, fy` and `px, py` for where the camera and cursor go.
- `BRIEF`, `RUN`, `BRAND` times and the second page.
- Remove the cursor block if you only want the camera.

## Files
- `code/demo.html`: the captures are drawn with CSS.
- Related: `cursor-click-ring__glide-press-ring`, `checklist-steps-tick-in__spring-dot-blur-slide`.
- Close variants: `browser-window-3d-fly-in__perspective-rotate-blur-out` (fly-in and slow zoom only) and `browser-window-focal-camera-zoom__focal-point-transform` (camera with status pills). This one adds the cursor that is aimed through the camera (`camPt`) and the zoom-through exit.
