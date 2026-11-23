---
name: how-it-works-four-step-icon-rail-bordered-tile-connector-line
description: "A plain white onboarding section: 'How It Works' pill, 44px heading, grey lead paragraph, and four steps stacked vertically, each with a square icon tile joined by a hairline to the next. Use for how-it-works or onboarding sections."
---

# How it works, four-step icon rail

**Code name:** Bordered tile, connector line.

## What you see
White page, left-aligned column about 900px wide. A small pill reading 'How It Works' (13px semibold, 1px light border, 8px radius). Under it the heading 'Up and running in four steps' at 44px, weight 800, tight tracking. Then an 18.5px grey intro of two lines. Then four rows 128px apart: on the left a 46px square tile (`#f5f5f6`, 1px border, 3px radius) holding a 20px outline icon (person-plus, hexagon gear, group, rocket), a 1px grey line dropping from each tile to the next, and to the right a 19px bold title with a 16.5px grey description of two lines. The page gave only a still, so the motion is added: in the demo the pill, heading and intro fade up in turn, then each step fades up 0.4s after the last while its connector line grows downward from the tile, and the whole block fades out at 6.2s to loop. Treat that reveal as a suggestion; the original may be static.

## When to use it
A product, onboarding or process section with three to five sequential steps and short copy. It is quiet and text-led, so it needs a hero or an image section above or below it to carry the page.

## How it works
Each row is a tile plus a text block. The connector is a 1px line from just below one tile to just above the next, so the rail reads as one line broken by the tiles. In the demo the line is a div scaled from 0 to 1 vertically from its top edge, which gives the draw-down effect.

```js
fade(tile, eo(seg(t, a, a + .45)))           // fade + 14px rise
line.style.transform = `scaleY(${eo(seg(t, a + .3, a + .4 + .2))})`   // grows toward the next tile
```

The real component's source is locked, and the still shows square tiles although the description says circles, so the demo follows the still.

## Numbers that matter
| | |
|---|---|
| Pill | 13px semibold, border `#e4e4e7`, radius 8 |
| Heading | 44px, weight 800, letter-spacing -.035em |
| Lead | 18.5px, `#6b6b72`, line height 1.5 |
| Tile | 46px, `#f5f5f6`, radius 3, icon 20px stroke 1.6 |
| Step pitch | 128px, connector 1px `#e4e4e7` |
| Title / text | 19px bold / 16.5px grey, text starts 98px right of the tile |
| Reveal (demo) | .4s stagger, ease-out cubic, 14px rise |

## Sound
Silent.

## Adapt it
- `badge`, `heading`, `lead` and `steps`: all the copy and icon keys.
- `ICONS`: swap in any 24px outline icons.
- `pitch`: spacing between steps; keep it a little over the tile plus two text lines.
- `stagger`: set it to 0 to show everything at once.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "How It Works Timeline" by olewandowski1 on 21st.dev (https://21st.dev/@olewandowski1/components/how-it-works-2), MIT. This demo is an original recreation written from the public preview.
