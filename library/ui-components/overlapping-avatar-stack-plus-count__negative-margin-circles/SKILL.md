---
name: overlapping-avatar-stack-plus-count-negative-margin-circles
description: A row of overlapping round avatars with a black overflow circle (+99). Reach for it as social proof next to a sign-up button or inside a card.
---

# Overlapping avatar stack with a +99 count

**Code name:** Negative margin circles.

## What you see
Five 40px circles in a row, each with a 2px white ring, each tucked 16px under the one to its right (so only 24px of each is visible except the last). The first four are photos; the fifth is solid black with white `+99`. The 21st.dev page gives only a still image (on a light dotted grid), with no video; this skill's `clip-wide.mp4` is a render of the demo instead.

The demo pops the circles in left to right with a 0.09s stagger (0.5s each, small overshoot), then moves a pointer onto the `+99` circle, which turns grey (#4b5563) while hovered, as the original link does.

## When to use it
Next to a call to action ("Join 99 others") or in a card footer to show who is involved. Keep it to four or five faces plus a count.

## How it works
A flex row. Every avatar after the first gets a negative left margin equal to the overlap; later siblings paint over earlier ones, so each circle's right edge sits on top of the one before it.

```css
.av { width:40px; height:40px; border-radius:50%; border:2px solid #fff; margin-left:-16px; }
.more { background:#000; color:#fff; font:500 12px system-ui; }   /* hover: #4b5563 */
```

Faces in the demo are drawn with SVG (a head, shoulders and hair on a gradient) because no photos can be bundled.

## Numbers that matter
| | |
|---|---|
| Circle | 40px plus 2px ring (44px) |
| Overlap | 16px |
| Count circle | black, white 12px text, hover `#4b5563` |
| Scale in demo | 4.2x |
| Entrance | 0.09s stagger, 0.5s each |
| Loop | 5s |

## Sound
Silent.

## Adapt it
- `CONFIG.count` for the number.
- `CONFIG.faces` for the four placeholder faces, or replace each with an `<img>`.
- `CONFIG.size` and `CONFIG.overlap` for tighter or looser stacks.

## Files
- `code/demo.html` runs on its own and loops; every frame is `render(t)`. Edit the `CONFIG` block at the top of its script.
- `media/poster.jpg` is the page's preview image.
- Similar looks already in the library: `overlapping-avatar-stack__hover-lift-overflow-count`.

## Credit
Idea: "Avatar Circles" by dillionverma on 21st.dev (https://21st.dev/@dillionverma/components/avatar-circles), MIT. This demo is an original recreation written from the public preview.
