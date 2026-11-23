---
name: icon-promo-card-with-link-rounded-surface-card
description: "A compact dark promo card: blue icon, title, short description and a text link. Reach for it for a sign-up nudge, upgrade note or announcement tile."
---

# Icon promo card with link

**Code name:** Rounded surface card.

## What you see
A 400px card (#18181a, 24px radius, hairline border, deep soft shadow) holds, top to bottom: a 24px blue circle-dollar icon, the title `Become an Acme Creator!` (white, 14px, semibold), a two-line description in grey, and the link `Creator Hub ↗` in blue (`#60a5fa`). The 21st.dev clip is still.

The demo fades the card up (24px rise, 0.7s) and then moves a pointer onto the link: the arrow slides 2px up and right and a 1px underline draws in from the left over 0.2s.

## When to use it
A single call to action that does not deserve a banner: a creator programme, a plan upgrade, a docs pointer. For a card with an image or a button use the horizontal banner version.

## How it works
A plain flex column with 12px gaps; everything visible is static CSS. The link hover (arrow nudge plus underline) is added in the demo.

```css
.card { width:400px; border-radius:24px; padding:16px; background:#18181a;
        box-shadow: inset 0 0 0 1px rgba(255,255,255,.07), 0 12px 40px rgba(0,0,0,.45); }
.lnk .ul { transform: scaleX(hover); transform-origin: 0 50%; }
```

The icon is an inline SVG that takes `currentColor`, so one colour value drives icon and link.

## Numbers that matter
| | |
|---|---|
| Card | 400px wide, 24px radius, 16px padding, 12px gap |
| Type | title 14px 600, description 14px `#a1a1aa`, link 14px 500 |
| Accent | `#60a5fa` |
| Hover | arrow moves 2px, underline 0.2s |
| Loop | 6s |

## Sound
Silent.

## Adapt it
- `CONFIG.title`, `CONFIG.body`, `CONFIG.link` for the words.
- `CONFIG.accent` for icon and link colour.
- `CONFIG.scale` for size on the canvas.

## Files
- `code/demo.html` runs on its own and loops; every frame is `render(t)`. Edit the `CONFIG` block at the top of its script.
- `media/poster.jpg` is the page's preview image.

## Credit
Idea: "Card" by hero_ui on 21st.dev (https://21st.dev/@hero_ui/components/heroui-card), MIT. This demo is an original recreation written from the public preview.
