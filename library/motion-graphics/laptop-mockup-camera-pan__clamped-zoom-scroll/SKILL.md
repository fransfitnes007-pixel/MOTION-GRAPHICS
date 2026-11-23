---
name: laptop-mockup-camera-pan-clamped-zoom-scroll
description: "A laptop mockup whose screen content can be panned and zoomed like a camera. Use it to take the viewer down a long page to one section, with a phone alongside for the mobile view."
---

# Laptop mockup with camera pan

**Code name:** Clamped focus-and-zoom camera inside a laptop screen.

## What you see
A matte-black laptop, 900px wide with a 22px hinge strip, shows the top of a long web page. As the headline "Your videos play right on the page." comes in, the page scrolls from the top down to the video section (from y 450 to 1180 in the capture, over 0.9s with ease in and out) while zooming from 100% to 125%. A phone, 220px, springs up from 160px below at the bottom right with a 6 degree tilt. A callout names the section. The whole group pushes in from the right at the start and out to the left at the end.

## When to use it
A page or app that is longer than the screen: you want the viewer to see where on it a feature lives, without a scroll bar or a real scroll. Fits any dark video with device mockups. The camera is a virtual one, so it works on a still image of the whole page.

## How it works
The page is one tall image inside an overflow-hidden screen. `cam(L, fx, fy, zoom, capH)` computes a scale from the screen width and the zoom, centres on the focus point, and clamps the translate so that the edge of the image never shows:

```js
const k = L.vw / 1440 * z
const x = clamp(L.vw / 2 - fx * k, L.vw - 1440 * k, 0)
const y = clamp(L.vh / 2 - fy * k, Math.min(0, L.vh - capH * k), 0)     // capH is the page height: 3191 here
img.style.transform = `translate(${x}px,${y}px) scale(${k})`
```

Animating `fy` and `z` together gives a scroll-and-zoom. The camera state is saved on the laptop, so `lpt` can convert a page point to stage coordinates for callouts and cursors.

## Numbers that matter
- Laptop: width 900, screen height 563+28, bezel 14px, radius 18px; base strip 22px, 100px wider than the screen, gradient `#3a3a46` to `#1c1c24`.
- Camera: focus y 450 to 1180 and zoom 1 to 1.25 with `eio` from 0.25s to 1.15s.
- Phone: 220px, `spring(k=7, f=11)`, 160px low, 6 degree tilt to 2.
- Strip in and out as in the filmstrip skill.

## Sound

## Adapt it
- The page capture and its real height (`capH`).
- Focus point and zoom range.
- Laptop size and position; the phone's page.
- The callout text and target.

## Files
- `code/demo.html` runs on its own and loops. The page and phone are CSS placeholders. The demo uses the system font stack; SF Pro Display is a good match.
