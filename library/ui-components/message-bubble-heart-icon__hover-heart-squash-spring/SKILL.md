---
name: message-bubble-heart-icon-hover-heart-squash-spring
description: An outline chat-bubble icon with a heart in it. Hover and the heart shrinks, then springs back with a small overshoot. Reach for it as an animated like or reaction icon.
---

# Message bubble heart icon

**Code name:** Hover heart squash spring.

## What you see
A black 2px-stroke round speech bubble with its tail at bottom left, a small outline heart in the middle, on a white page. Moving the pointer onto it makes the heart squash to about 60% of its size over roughly 0.2s, then bounce back past 100% and settle by about 0.9s. The bubble outline barely moves, a pixel or two. When the pointer leaves, nothing more happens. The usage is `animateOnHover` at 40px, so the motion only plays while hovering. The demo shows a 216px copy and a real-size copy.

## When to use it
Like, reaction or favourite buttons, empty states for comments, nav icons that should respond to a pointer. It is small, so keep it to one or a few icons per screen. Do not trigger it on touch devices without an explicit tap.

## How it works
The icon is an SVG (lucide message-circle-heart paths) with two groups, the bubble and the heart. On hover the heart group gets a scale animation from 1 down to about .62 and back, with a spring on the return; the bubble group moves by 1 to 2 pixels. In the demo the dip is eased in-out over 0.22s, then `spring(p, 5, 9)` takes the heart from .62 up through 1.1 and settles at 1.

```js
heart.setAttribute('transform', `translate(12 12.6) scale(${hs}) translate(-12 -12.6)`)
// hs: ease 1 to .62 in 0.22s, then lerp(.62, 1, spring(p, 5, 9)) over 0.75s
```

The original (an icon from a motion-icon pack) uses framer-motion variants. The numbers here are read off the video frame by frame, so the overshoot size is an estimate.

## Numbers that matter
| | |
|---|---|
| Icon | 24px viewBox, stroke 2, round caps and joins, `#0a0a0a` |
| Heart dip | scale .62 in 0.22s |
| Return | spring, about 0.75s, overshoot near 1.1 |
| Bubble | shifts about 1.5px at the dip |
| Usage size | 40px |

## Sound
Silent.

## Adapt it
- `CONFIG.stroke` and `strokeWidth`: colour and weight.
- `CONFIG.heartDip`, `dipTime`, `settle`: how hard and how fast the heart pumps.
- Swap the heart colour for a fill on hover if you want a like state.
- `CONFIG.big`: size of the large preview.

## Files
- `code/demo.html` runs on its own and loops. A scripted cursor hovers the icon.
- `media/poster.jpg` is a still of the component.

## Credit
Idea: "Message Circle Heart Icon" by skyleen77 on 21st.dev (https://21st.dev/@skyleen77/components/icons-message-circle-heart), MIT. This demo is an original recreation written from the public preview.
