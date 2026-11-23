---
name: avatar-row-name-tag-tooltip-cursor-follow-spring-rotate
description: A row of overlapping avatars where hovering one shows a black name-and-role tag that tilts and slides as the pointer moves. Reach for it for a team row or a credits list.
---

# Avatar row with a name tag that follows the cursor

**Code name:** Cursor-follow spring rotate.

## What you see
On a light dotted page, six 56px circular photos overlap by 16px. Hovering one lifts it 5% and brings it to the front. A black tag (7px radius, soft shadow) pops in above it with `John Doe` in bold white and `Software Engineer` in smaller white text, and a hairline green and blue glow along its bottom edge. The tag enters from 20px below at 60% size with an overshoot, then follows the pointer: moving right slides it right and tips it clockwise, moving left does the opposite. It keeps swinging for about a second after the pointer stops. Moving to the next avatar swaps in that person's tag (`Robert Johnson`, `Product Manager`...); leaving the row fades the tag out.

The demo scripts a pointer along the row, left and right within each avatar and across all six, through 8s.

## When to use it
Team rows, contributor lists and avatar piles where the names must stay out of the layout until asked for. Mouse-only, so give touch users another way to see names.

## How it works
Pointer x inside the hovered avatar, measured from its centre, drives two springs: rotation (`-100..100px` maps to `-45..45 deg`) and slide (`-100..100px` maps to `-50..50px`). Both use stiffness 100 and damping 5, which is lightly damped and so rings. The enter animation is a separate, stiffer spring (about 260 and 10).

```js
tilt = clamp(offsetX / 100, -1, 1) * 45        // target rotation
slide = clamp(offsetX / 100, -1, 1) * 50       // target translateX
// per step: v += (-k * (x - target) - c * v) * dt;  x += v * dt     (k 100, c 5)
tag.transform = `translateX(${slide}px) rotate(${tilt}deg) scale(${.6 + .4 * enter})`
```

Springs are integrated once at 240 steps a second into a lookup table, so `render(t)` stays a pure function of time. Faces are drawn SVGs.

## Numbers that matter
| | |
|---|---|
| Avatar | 56px, 2px white ring, 16px overlap, hover scale 1.05 |
| Tag | black, 7px radius, name 16px bold, role 12px |
| Follow spring | stiffness 100, damping 5 |
| Range | +-100px pointer offset gives +-45 deg and +-50px |
| Enter | from 20px low, 60% size, spring |
| Loop | 8s |

## Sound
Silent.

## Adapt it
- `CONFIG.people` for names, roles and faces.
- `CONFIG.spring` (k, c): raise c to 12 for a calmer tag.
- `CONFIG.tilt`, `slide`, `range` for how far it moves.

## Files
- `code/demo.html` runs on its own and loops; every frame is `render(t)`. Edit the `CONFIG` block at the top of its script.
- `media/poster.jpg` is the page's preview image.
- Similar looks already in the library: `overlapping-avatar-stack__hover-lift-overflow-count`.

## Credit
Idea: "Animated Tooltip" by manuarora700 on 21st.dev (https://21st.dev/@manuarora700/components/animated-tooltip), MIT. This demo is an original recreation written from the public preview.
