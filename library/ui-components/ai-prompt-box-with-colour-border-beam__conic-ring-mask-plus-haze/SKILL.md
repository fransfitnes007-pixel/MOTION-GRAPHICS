---
name: ai-prompt-box-with-colour-border-beam-conic-ring-mask-plus-haze
description: A dark prompt composer (at-sign chip, 'Build anything...', Agent and Auto selectors, send arrow) whose 1.6px border has travelling colour patches, with a faint glow inside the card. Use for an AI chat input, a focus state or a highlighted card.
---

# AI prompt box with colour border beam

**Code name:** Conic ring mask plus haze.

## What you see
A near-black page `#0d0d0f` with one card, 348 x 122 in life (shown 2.2x): `#1d1d1d`, 20px corners, a faint grey inset ring and a barely-there inner glow. Top left a 24px pill holding an @ icon. Below it 'Build anything...' in 13px `#4e4e4e`. At the bottom, two pills 'Agent' and 'Auto' with small chevrons in 12px `#caccd2`, and a 28px circular send arrow on the far right. The border carries coloured light: a pink to purple patch near the top right, an orange edge beside it, a blue to light-blue patch low on the bottom edge, a green patch down the left. They are separate patches with dark border between them. All of it turns once round in 3.6s, so a patch leaves the top right, runs down the right, along the bottom and up the left, with the hues sliding through the card as they go. A soft blurred copy of the same colours shows just inside the border, strongest at the corners.

## When to use it
The focus or 'working' state of an AI prompt box, a featured pricing or product card, or any one element that should draw the eye on a dark page. Keep it to one or two on a screen, since it is loud next to anything else.

## How it works
Two stacked layers hold the same conic gradient. The first is a ring: the element fills the card and has 1.6px padding, and a two-layer mask (a `content-box` layer and a full layer combined with `exclude`) cuts out everything but the 1.6px border strip, so the gradient only shows on the border. The second is a thicker 7px ring blurred 12px at 30 percent opacity, which is the inner haze. The gradient's start angle advances with time, which rotates the colours round the border.

```css
.ring { padding: 1.6px; border-radius: 20px;
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor; mask-composite: exclude; }
```
```js
ring.style.background = `conic-gradient(from ${t / 3.6 * 360}deg at 50% 50%, ${stops})`
```

The real component's `size` and `colorVariant` props pick the beam thickness and palette; the clip shows size md with the colourful palette. Hue and stop positions are matched by eye. A conic gradient maps angles to a wide card unevenly, so patches slow down along the long edges and speed up round the corners; that is part of the look.

## Numbers that matter
| | |
|---|---|
| Card | 348 x 122, `#1d1d1d`, radius 20, padding 7 |
| Ring | 1.6px, one turn per 3.6s |
| Haze | 7px ring, blur 12px, opacity .3 |
| Stops (deg from top) | orange 8, pink 22, purple 40, blue 172 to 190, green 282 to 296, gaps of dark between |
| Chips | 24px tall, `rgba(255,255,255,.04)`, 12px text `#caccd2` |
| Send | 28px circle, arrow `#8b8b8b` |
| Page | `#0d0d0f` |

## Sound
Silent.

## Adapt it
- `stops`: the colours and where they sit. Two stops of one hue make a single comet-like beam.
- `period`: seconds per turn.
- `ringWidth` and `hazeOpacity`: sharp line weight and how much glow reaches into the card.
- The card contents; the beam wraps any box that has a border radius, so match the `border-radius` on `.ring` and `.haze` to it.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Border Beam" by larsen66 on 21st.dev (https://21st.dev/@larsen66/components/border-beam), MIT. This demo is an original recreation written from the public preview.
