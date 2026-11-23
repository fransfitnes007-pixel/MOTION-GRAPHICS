---
name: four-tone-surface-cards-surface-level-variants
description: "Four card shades on a dark page: transparent, default, secondary and tertiary. Reach for it when you need to show how much weight a panel carries by how light its fill is."
---

# Four-tone surface cards

**Code name:** Surface level variants.

## What you see
Four 320px cards sit in a column, 16px apart. The first, `Transparent`, has no fill at all, so its text floats on the page. `Default` is `#18181a`, `Secondary` `#272729`, `Tertiary` `#3f3f47` (a faint blue-grey). All have 24px corners, 16px padding, a white 14px title, grey 14px description and white body text. The 21st.dev clip is a still of this stack.

The demo fades the cards up one after another (0.14s apart) and then walks a pointer down them. As it reaches each card, a small code chip slides in beside it naming the token (`bg-surface  #18181a` and so on) and the card grows 1.5%.

## When to use it
Documenting a design system, or building a dashboard where a card nested inside another card needs one step more or less contrast. The tone is the only hierarchy cue, so keep the text colours the same across all four.

## How it works
There is no motion in the source: the only difference between the cards is the background value. The demo's entrance and callouts are added for presentation.

```js
cards[i].bg = ['transparent', '#18181a', '#272729', '#3f3f47'][i]
box-shadow: inset 0 0 0 1px rgba(255,255,255,.07)      // hairline edge on filled cards
```

Because `Tertiary` is the lightest, put the most important content on it and nest a darker card inside rather than the reverse.

## Numbers that matter
| | |
|---|---|
| Card | 320px wide, 24px radius, 16px padding, 16px gap |
| Fills | transparent, `#18181a`, `#272729`, `#3f3f47` |
| Text | title `#fafafa` 14px 500, description `#a1a1aa` |
| Entrance | fade up 16px, 0.5s each, 0.14s apart |
| Loop | 7s |

## Sound
Silent.

## Adapt it
- `CONFIG.cards` for the four fills, titles and token labels.
- `CONFIG.width`, `CONFIG.gap`, `CONFIG.scale` for sizing.
- Change `radius` in the `.card` CSS for squarer or rounder corners.

## Files
- `code/demo.html` runs on its own and loops; every frame is `render(t)`. Edit the `CONFIG` block at the top of its script.
- `media/poster.jpg` is the page's preview image.

## Credit
Idea: "Card" by hero_ui on 21st.dev (https://21st.dev/@hero_ui/components/heroui-card/variants), MIT. This demo is an original recreation written from the public preview.
