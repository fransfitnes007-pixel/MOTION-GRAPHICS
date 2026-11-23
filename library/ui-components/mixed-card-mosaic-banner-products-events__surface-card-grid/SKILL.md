---
name: mixed-card-mosaic-banner-products-events-surface-card-grid
description: A 12-column dark card mosaic mixing a promo banner, a notification, group tiles, product cards with photo headers and event rows. Reach for it as a dashboard homepage layout.
---

# Mixed card mosaic: banner, products, events

**Code name:** Surface card grid.

## What you see
A 768px-wide grid with 12px gaps. Top row: the cherry banner (full width). Below, two columns. Left: a tall `PAYMENT` notification (small spaced caps, title `You can now withdraw on crypto`, a blue `Go to settings` link, close X) above two square-ish group tiles (`Indie Hackers 148 members`, `AI Builders 362 members`, each with an icon tile and a `By John` byline). Right: two product cards (`NEO Home Robot` with a photo, white text over a bottom gradient, a pill button each: `Notify me` and `Get now`) above three event rows with a 48px thumbnail, title and time. All cards share one fill (#18181a) and 24px corners. The clip is still and cuts the grid off at the bottom.

The demo replaces every photo with a CSS gradient. Cards fade up with a 0.07s stagger, then a pointer hovers `Notify me` (button greys and shrinks 5%).

## When to use it
A dashboard or community home that mixes content types in one view. The mixed card sizes carry the layout, so keep the fills identical or the grid turns noisy.

## How it works
A CSS grid with two columns inside a full-width first row. The left column stretches its notification card (`flex:1`) so both columns end at the same height; the right column's cards keep fixed heights.

```css
.g { display:grid; grid-template-columns:1fr 1fr; gap:12px; width:768px }
.c { background:#18181a; border-radius:24px; box-shadow: inset 0 0 0 1px rgba(255,255,255,.07) }
```

Product photos use `object-cover` with a `from-black/70 to-transparent` gradient so white text stays readable on any image.

## Numbers that matter
| | |
|---|---|
| Grid | 768px wide, 12px gap, 2 columns under a full-width banner |
| Cards | `#18181a`, 24px radius, hairline border |
| Photo header | 144px tall, bottom gradient 0.72 black |
| Entrance | fade up 18px, 0.07s stagger |
| Loop | 7s |

## Sound
Silent.

## Adapt it
- `CONFIG.events` and `CONFIG.groups` for the rows and tiles.
- `CONFIG.accent` for the link colour.
- Replace the gradient placeholders (`robot()`, the tile `background` values) with real images.

## Files
- `code/demo.html` runs on its own and loops; every frame is `render(t)`. Edit the `CONFIG` block at the top of its script.
- `media/poster.jpg` is the page's preview image.

## Credit
Idea: "Card" by hero_ui on 21st.dev (https://21st.dev/@hero_ui/components/heroui-card/with-images), MIT. This demo is an original recreation written from the public preview.
