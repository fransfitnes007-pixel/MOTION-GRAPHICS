---
name: browser-window-3d-fly-in-perspective-rotate-blur-out
description: "A browser frame with traffic lights and an address bar holding a screenshot, entering with perspective rotation and leaving with blur. Use it to show a real website or app screen inside a motion graphic."
---

# Browser window 3D fly-in

**Code name:** Perspective rotate with slow camera zoom.

## What you see
An off-white browser window, 1240 by 775 with traffic lights and a centred address pill, slides in from 460px to the right. It starts rotated 30 degrees about its vertical axis and 10 degrees about its horizontal one, at 86% scale, and flattens to face the camera over 0.7s with a strong ease-out. Once it lands the page inside slowly pushes in from 100% to 112% over 2.7s. At the end it drifts up 60px, shrinks to 82% and blurs to 12px as it leaves over 0.4s.

## When to use it
Showing a real site or app screenshot as proof, in a video where the layout around it is simple. Good when the same window then changes content (new address, new page) without leaving the frame. Not good for dense UI that needs to be read: the window is mid-size and the push-in is slow.

## How it works
The window is a normal absolutely positioned div. All the 3D is one transform with its own `perspective()`, so every window can have its own vanishing point, and the origin is shifted to 30% 50%, which makes the right edge swing more than the left.

```js
transform: perspective(2400px) translateX((1 - wi) * 460px) translateY(out * -60px)
           rotateY(lerp(-30, 0, wi)deg) rotateX(lerp(10, 0, wi)deg) scale((.86 + .14 * wi) * lerp(1, .82, out))
```

Inside, the page is a fixed 1440 by 900 capture. `cam(w, focusX, focusY, zoom)` scales it to the window width times `zoom`, centres on the focus point and clamps so the edge of the capture never shows. Use real 2x screenshots; the demo draws six placeholder layouts in CSS at the same size.

## Numbers that matter
- Entry: `eo5` over 0.7s; translateX 460px, rotateY -30, rotateX 10, scale .86 to 1.
- Exit: `eio5` over 0.4s; translateY -60px, scale to .82, blur to 12px.
- Camera: zoom 1 to 1.12 over 2.7s with `eio`, focus (720, 420) on a 1440 by 900 capture.
- Window: radius 22px, shadow `0 60px 140px -40px rgba(24,16,52,.5)`, bar 46px.

## Sound
A whoosh swelling into the entry (0.4s before the window lands) at 4.45s. No sound is needed on the exit.

## Adapt it
- The screenshot, and the address text.
- Window size (`BW`) and its position.
- Entry angles (-30 and 10 degrees) and `transformOrigin` for a different swing.
- Zoom end (1.12) and focus point to aim at the part of the page that matters.

## Files
- `code/demo.html` runs on its own and loops. The page is a CSS placeholder; swap in real screenshots.
