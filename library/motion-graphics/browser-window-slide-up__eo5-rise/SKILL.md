---
name: browser-window-slide-up-eo5-rise
description: "A dark app window with traffic-light dots and a URL bar rises from below the frame and settles under a headline, growing from 92 to 100 percent. Reach for it to reveal a dashboard or web app under a sentence."
---

# Browser window slide-up

**Code name:** Eased rise with scale settle.

## What you see
A sentence has just built itself across the upper third of the frame. Below it, a dark browser window rises from beyond the bottom edge. It is 1400px wide (1000 on tall) with 22px corners, a title bar with three coloured dots on the left and a centred rounded URL pill, and a dark analytics screen inside: a sidebar, four stat tiles and a purple area chart. It moves very fast at first and slows into its place over 0.75s while growing from 92% to full size; its top edge ends 20px above the frame's centre line, so the lower third of the window stays cut off by the frame.

## When to use it
Showing a product screen under a sentence about what it does. The cropped bottom is part of the look: it suggests more below. It is wrong where the whole screen needs to be seen, and the dark window on a light stage is high contrast, so use it once.

## How it works
One eased value drives both position and size, so the window both rises and swells:

```js
const dq = eo5(seg(t, t0, t0 + .75))                       // quintic ease-out
window.top = lerp(H + 40, CY - 20, dq)                      // starts 40px below the frame
window.transform = `scale(${.92 + .08 * dq})`; transformOrigin = '50% 0'    // grows from the top edge
```
`eo5` is `1 - (1 - x)^5`, much steeper than the usual cubic, so most of the movement happens in the first quarter. The transform origin is the top centre, so the title bar stays put as the window grows. The window itself is `position: absolute; overflow: hidden; border-radius: 22px` with a 46px title bar in front of an image; use a screenshot of your dashboard, the demo draws one in HTML.

## Numbers that matter
| | |
|---|---|
| Window | 1400 by 868px (1000 by 620 tall), radius 22px, bar 46px |
| Motion | `eo5` over .75s, start `H + 40`, end `CY - 20` (`CY - 100` tall) |
| Scale | .92 to 1, origin top centre |
| Shadow | `0 60px 140px -40px rgba(0,0,0,.55)` plus a 1px ring |
| Dots | `#ff5f57`, `#febc2e`, `#28c840`, 13px |

## Sound
A whoosh on the scene cut (about 0.18s early). Nothing on the window itself.

## Adapt it
- The screen content: swap the placeholder for a screenshot at 700px wide.
- Width and end position.
- The ease: `eo` for a softer arrival, `eo5` for a snappier one.
- Colours of the bar and the URL text.

## Files
- `code/demo.html` runs on its own. The dashboard is drawn in HTML and SVG.
