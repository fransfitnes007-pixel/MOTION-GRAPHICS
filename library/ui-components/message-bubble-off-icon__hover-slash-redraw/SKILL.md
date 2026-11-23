---
name: message-bubble-off-icon-hover-slash-redraw
description: An outline chat-bubble icon with a diagonal slash through it, meaning messages off. On hover the slash redraws itself and the bubble wobbles. Reach for it as a mute or disable-chat icon with a bit of life.
---

# Message bubble off icon

**Code name:** Hover slash redraw.

## What you see
A black 2px-stroke speech bubble drawn as an open arc with a tail at bottom left, struck through by a line from top-left to bottom-right, on a white page. When the pointer arrives the bubble shifts a few pixels and the slash is redrawn along its length, about half a second, ending where it started. The video is small and the movement is subtle: the bubble outline wiggles slightly and the slash appears to travel. Usage is `animateOnHover` at 32px.

## When to use it
Mute, do-not-disturb, comments-disabled and chat-off states, settings toggles, and empty states where messaging is unavailable. Keep it to small icon sizes.

## How it works
lucide message-circle-off paths in a 24px viewBox: an arc, the tail path and a slash `m2 2 20 20`. The slash uses `pathLength=1` with `stroke-dasharray: 1 1` and `stroke-dashoffset` going from 1 to 0, so it looks drawn from the top-left. The bubble group rotates with a damped sine.

```js
slash.style.strokeDashoffset = 1 - eo(h / 0.5)               // redraw
bubble.setAttribute('transform', `rotate(${Math.exp(-h * 5) * Math.sin(h * 22) * 7} 12 12)`)
```

The wobble amplitude and the exact easing are estimates; the video is 636px wide and the icon is 32px in it.

## Numbers that matter
| | |
|---|---|
| Icon | 24px viewBox, stroke 2, round caps, `#0a0a0a` |
| Slash redraw | 0.5s, ease out cubic |
| Bubble wobble | 7 degrees, damped, 22 rad/s, decay 5 per second |
| Usage size | 32px |

## Sound
Silent.

## Adapt it
- `CONFIG.stroke`, `strokeWidth`: look.
- `CONFIG.drawTime`: speed of the redraw.
- `CONFIG.shake`: wobble in degrees, 0 for none.
- Swap the slash colour to red for a stronger off state.

## Files
- `code/demo.html` runs on its own and loops. A scripted cursor hovers the icon.
- `media/poster.jpg` is a still of the component.

## Credit
Idea: "Message Circle Off Icon" by skyleen77 on 21st.dev (https://21st.dev/@skyleen77/components/icons-message-circle-off), MIT. This demo is an original recreation written from the public preview.
