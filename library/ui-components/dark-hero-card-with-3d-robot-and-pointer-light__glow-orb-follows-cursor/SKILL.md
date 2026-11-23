---
name: dark-hero-card-with-3d-robot-and-pointer-light-glow-orb-follows-cursor
description: "A dark card 'Interactive 3D' with a grey-gradient title and two lines of body text, and a glossy black humanoid robot on the right. It opens zoomed in on the head, pulls back over about a second, then follows the mouse: a soft white orb tracks the pointer and the robot turns its head and reaches an arm toward it. Reach for it for a 3D hero where the model reacts to the cursor."
---

# Dark hero card with a 3D robot and a pointer light

**Code name:** Glow orb follows cursor.

## What you see
A page-white frame holding a near-black card (735 by 341 in a 960 by 624 frame, 7px corners, `rgba(0,0,0,.96)` black). Left half: 'Interactive 3D' in bold 36px with a top-to-bottom gradient from `#fafafa` to `#a3a3a3`, then two lines of 12.5px `#d4d4d4`. Right half: a black glossy robot, its head a dome with a dark visor and two short light bars; it is centred on the head and at first fills the right half, showing only the head, shoulders and arms. From 0.8s over 1.1s the camera pulls back to the full torso with arms at its sides, and the robot stands there. When the pointer enters the card a soft white orb about 40px radius fades in under it (0.12s) and trails it by about 0.14s; the head turns slightly toward it and the arm on that side stretches toward the orb. When the pointer leaves, the orb fades out over about 0.2s and the arms drop. In the preview the orb goes to the robot's right hand, then up-left, then lower-left as the pointer moves.

## When to use it
A product hero or feature card that wants one memorable 3D object with a response to the pointer. It needs a model (Spline scene or similar) and a decent GPU, and the scene file loads over the network, so show a poster or skeleton while it loads. On touch screens there is no pointer to follow.

## How it works
The card is an ordinary dark Card with the text on the left, and a `SplineScene` component on the right that loads a `.splinecode` scene URL; the pointer-following light and arm movement come from inside the Spline scene (its mouse-follow events), not from page code. A decorative `Spotlight` (a blurred white ellipse at the top left) is also in the usage example but does not show in the preview. The demo cannot load a Spline scene, so it draws a 2D robot from SVG shapes with gradients for the gloss, moves a radial-gradient orb to the pointer with a short delay, and bends each arm as a quadratic curve from the shoulder toward the orb (reach limited to 150px), turning the head up to 6px toward it. The opening zoom is a scale from 2.3 to 1 around the head. It reads as the same idea, not the same model.

## Numbers that matter
- Card 735 by 341, fill `#0b0b0b`; title 36px bold, gradient `#fafafa` to `#a3a3a3`
- Open zoom 2.3 to 1, from 0.8s over 1.1s, cubic out
- Orb radius about 60px with a soft edge, fade in 0.12s, out 0.18s, trails the pointer 0.14s
- Arm reach 150px; head turn up to 6px; robot head centre (673, 232)
- Usage: card height 500px, `bg-black/[0.96]`, text flex-1 left, scene flex-1 right

## Sound
Silent.

## Adapt it
- `title` and `body` copy; `card` colour.
- `robot` position and `zoomFrom`, `zoomAt`, `zoomSec` for the opening camera move.
- `reach`, `lag`, `orbRadius` for how the model responds to the pointer.
- In production replace the SVG robot with the Spline scene element or your own 3D canvas; `path` scripts the demo pointer.

## Files
- `code/demo.html` runs on its own, loops in 8.2s, and has a `CONFIG` block at the top of the script.

## Credit
Idea: "Spline Scene" by serafimcloud on 21st.dev (https://21st.dev/@serafimcloud/components/splite), MIT. This demo is an original recreation written from the public preview.
