---
name: cursor-click-ring-glide-press-ring
description: "A white arrow cursor glides in on an eased path, squeezes on the click and sends out a blue ring while a pill button dips. Reach for it to show someone pressing a button in a product video."
---

# Cursor click with ring

**Code name:** Glide, press and expanding ring.

## What you see
A blue pill button springs in. A white arrow cursor with a dark outline sits low and to the right, then slides to the middle of the button along a smooth curve in half a second. As it arrives it shrinks to 82% and back over 0.16s while a blue ring, 3px thick, starts at 20px and grows to 140px, fading to nothing in half a second. The button itself dips to 94% and back at the same moment (repeat it for later buttons if you have several). The cursor then fades out.

## When to use it
Any "and then you click it" beat: launching a project, booking a call, pressing send. It is a helper for UI scenes, not a scene on its own. It is wrong when the click target is tiny: the ring is 140px wide and swallows small controls.

## How it works
One function, `clickAt(t, tc, x, y, from)`, is a pure function of time, so it can be called every frame with no state:

```js
const g = eio(seg(t, tc - .55, tc - .05))                     // glide: .5s ending .05s before the click
cursor.left/top = lerp(from, [x, y], g)
const press = 1 - .18 * Math.sin(Math.PI * seg(t, tc - .06, tc + .1))   // squeeze: .16s
const r = seg(t, tc, tc + .5)                                  // ring: .5s
ring.size = 20 + 120 * r; ring.opacity = 1 - r
```
`eio` is the cubic in-out ease. The cursor is an inline SVG polygon, 44px, with a drop shadow. The ring is a bordered circle centred on the click point.

## Numbers that matter
| | |
|---|---|
| Glide | `eio` over .5s, ends .05s before the click |
| Cursor squeeze | to 82%, `sin` curve over .16s, from .06s before the click |
| Ring | 3px `#2f6bff`, 20px to 140px over .5s, opacity 1 to 0 |
| Button dip | to 94% over .2s |
| Cursor | 44px, white fill, `#0b0b10` stroke 1.4, shadow `0 8px 14px rgba(0,0,0,.45)` |

## Sound
A short click: a burst of high-passed noise about 60ms long with a 1600Hz blip, placed on `tc`. It is a different kind of sound from a pop or a whoosh.

## Adapt it
- `tc`, the click time: set it to the beat in your audio.
- `from`: where the cursor enters from. Lower right is the default.
- The ring colour (match the button).
- Target position `x, y`.

## Files
- `code/demo.html` runs on its own.
