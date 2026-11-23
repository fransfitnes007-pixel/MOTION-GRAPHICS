---
name: ring-of-photo-cards-seen-from-outside-preserve-3d-cylinder-inertia
description: "A ring of ten rounded photo cards in 3D: the two at the front are large and facing you, the ones beside them are narrower and angled, and the ones at the sides are edge-on slivers. Dragging flicks the ring round and it slows to a stop. Reach for it for a photo gallery or a 'moments' section."
---

# Ring of photo cards seen from outside

**Code name:** Preserve-3d cylinder with inertia.

## What you see
On a white page with a faint dotted grid and two dashed horizontal lines, a horizontal row of cards about 240 by 250 with 30px corners. Two cards share the front, with about 25px between them; next to them, cards turned about 54 degrees look roughly 45% as wide, then slivers at the edges. Gaps show the cards on the far side of the ring peeking through. The ring is quiet until the pointer pulls it sideways; on release it keeps turning and eases to a stop, by about 3 cards in the preview over 0.4s. In the demo three flicks of 108, 108 and 144 degrees add up to 360, so the loop is seamless. The page is 1280 wide and the carousel sits in a 500px band; the preview cursor is a small arrow.

## When to use it
A photo or portfolio gallery in a section with room for one band of imagery. It shows about half the ring at once, so use 8 to 12 images. Dragging is the only way to move it, so add a hint or auto-rotate for visitors who will not try.

## How it works
A wrapper has `perspective: 2200px`. Inside it a zero-size `transform-style: preserve-3d` ring is moved by `translateZ(-R) rotateY(angle)`, and each card is placed with `rotateY(i * 36deg) translateZ(440px)`, so the front of the ring sits at z=0 at normal size. The big perspective value keeps the side cards from shrinking too much (front 250px tall, 54-degree cards about 92% of that). Cards keep their backs visible, which gives the glimpses between cards. The flick is `deg * (1 - exp(-(t - at) / tau))` with tau 0.45s, each deg a multiple of one card step, so the ring always lands with cards square to the viewer. The demo's pictures are generated gradients and shapes.

## Numbers that matter
- 10 cards, 240 by 250, corner radius 30px, ring radius 440px, perspective 2200px
- Start offset 18 degrees so two cards share the front
- Flick inertia tau 0.45s; flicks at 1.0s, 3.6s and 6.0s of -108, -108, -144 degrees
- Dotted background: 1px dots every 26px; dashed lines at y=78 and y=878

## Sound
Silent.

## Adapt it
- `count`, `card`, `radius`: ring size and number of images (keep `radius` near `card width * count / 5.5`).
- `perspective` for flatter or more dramatic depth.
- `pictures` or replace the SVG with `<img>` per card.
- `flicks` and `tau` for how far and how long it coasts.

## Files
- `code/demo.html` runs on its own, loops in 8s, and has a `CONFIG` block at the top of the script.

## Credit
Idea: "3D Carousel" by cult-ui on 21st.dev (https://21st.dev/@cult-ui/components/3d-carousel), MIT. This demo is an original recreation written from the public preview.
