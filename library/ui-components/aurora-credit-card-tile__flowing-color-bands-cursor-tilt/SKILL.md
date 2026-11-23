---
name: aurora-credit-card-tile-flowing-color-bands-cursor-tilt
description: "A dark bento tile with a portrait credit card on it: a chip, a contactless mark, a two-circle network logo, and a face of slowly flowing pink, violet, blue, cyan, green and orange bands with a bright diagonal streak. It tilts in 3D toward the cursor. Reach for it in fintech or card-product pages."
---

# Aurora credit card tile

**Code name:** Flowing colour bands with cursor tilt.

## What you see
A black page with one tile 426 by 592 (38px radius, `#0a0a0c`, 1.5px border `#1b1b20`). Title "Launch a card programme" in 28px semibold, top left, wrapped to two lines. Top right is a 48px rounded button with an expand-arrows icon: dark grey at rest, lilac-purple (`#a06bff`) while the cursor is over the tile. Below is a portrait card 270 by 423 with 22px corners and a drop shadow. Its face is a vertical rainbow: violet and pink at the top, blue, cyan, green, then orange and pink, darkening to deep purple at the bottom. A chip (39 by 52, pale grey with a fine grid) sits upper right with a contactless symbol beside it, and two overlapping circles, one white and one translucent, sit at the bottom right. A bright narrow streak slants across the face, about 22 degrees, and its colour shifts with the bands under it.

In the 12s clip the bands drift slowly and the streak slides, while the cursor wanders over the card: the card tilts a few degrees toward it and the tile's border picks up a lilac glint at a corner. The 21st.dev description also mentions caustics and grain, and says the chip is placed where ISO 7816 puts it.

The demo flows the six colour bands by one full period in 12s (so it loops), sweeps the streak down and back over 9s, and tilts the card by up to 6 degrees from the scripted cursor. Grain and caustics are not reproduced.

## When to use it
A card, wallet or banking product page, or any hero where one object should feel physical. The colour flow keeps it alive without a video. It needs a dark surround to glow; on white it looks flat. Respect reduced-motion by stopping the flow.

## How it works
The face is a tall gradient with the six colours repeated twice. It is moved up by exactly one period over `flowSec`, so the loop has no jump.

```js
background: linear-gradient(180deg, c1 0%, c2 8.3%, ... c6 41.7%, c1 50%, ... c6 91.7%, c1 100%)   // height 2 x card
translateY(-(t / 12 % 1) * cardHeight) rotate(-8deg)
```

A darkening overlay at the bottom and a pale sheen at the top sit above it, then the streak (a blurred white bar with `mix-blend-mode: screen`, rotated -22 degrees). The tilt is `rotateY(dx * 6deg) rotateX(-dy * 6deg)` with `dx, dy` the cursor's offset from the card centre, inside a perspective of 900px, faded in by a hover value. The page's props are `title brand="mastercard" color1..color6 glow`; the six colours and glow are in `CONFIG`.

## Numbers that matter
| | |
|---|---|
| Tile | 426 x 592, 38px radius, border `#1b1b20`, hover glint ~`#9682eb` |
| Card | 270 x 423, 22px radius, perspective 900px, max tilt 6deg |
| Bands | `#ff7ac1 #a06bff #4f46e5 #22d3ee #4ade80 #ffb26b`, slant -8deg |
| Flow | one period in 12s |
| Streak | 16px bar, blur 3px, screen blend, -22deg, 9s sweep |
| Chip | 39 x 52 at (145, 58) on the card |
| Button | 48px, 13px radius, `#24242a` to `#a06bff` |
| Title | 28px / 600, `-.015em` |

## Sound
Silent.

## Adapt it
- `CONFIG.colors` and `glow`: six band colours and the accent.
- `flowSec`, `streakSec`, `bandAngle`: pace and slant.
- `tiltDeg`: 0 for a flat card, 10 for more drama.
- `title`, and the SVG for the network logo at the bottom right.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Aurora Credit Card Bento" by yura on 21st.dev (https://21st.dev/@yura/components/aurora-credit-card-bento), MIT. This demo is an original recreation written from the public preview.
