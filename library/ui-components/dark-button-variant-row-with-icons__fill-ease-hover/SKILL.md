---
name: dark-button-variant-row-with-icons-fill-ease-hover
description: "A reference row of buttons: primary, secondary, tertiary and ghost variants, with leading and trailing icons and three icon-only sizes, on a dark page. Use it as the button style sheet for a dark UI."
---

# Dark button variant row with icons

**Code name:** Fill ease hover.

## What you see
On a near-black page, one row of six controls with 16px gaps. 1) "Add item" with a plus on the left, a white pill with dark text. 2) "Continue" with an arrow on the right, a dark grey pill with white text. 3) "Search" with a magnifier on the left, a transparent pill with a thin `#27272a` outline. 4) A bare gear icon in grey, no fill (ghost, icon only). 5) A small dark circle with a plus (secondary, small icon). 6) A larger white circle with a dark arrow (primary, large icon). In the preview, each button takes a hover in turn, about 0.8s each, and its fill eases to a lighter shade in about 0.18s: white goes to light grey, dark grey to a lighter grey, the outline button fills with dark grey, the ghost icon gets a dark grey disc. No click motion is visible in the clip.

The page description also promises an animated loading state. It does not appear in the clip, so the last 2 seconds of the demo are my addition: Add item is clicked and its plus becomes a spinner turning two times a second with the label "Adding".

## When to use it
As the button reference for a dark app, a design-system page, or when you need to see all variants and sizes together. For a single standout CTA use the glass or liquid-metal button skills instead.

## How it works
Four variants share one rule: a rest fill, a hover fill, a text colour and a border. The fill is mixed by a 0 to 1 hover value that follows the scripted cursor with an `eo`-style ease of 0.18s. Sizes are plain width and height, with leading and trailing icon positions and three icon-only sizes (45, 42 and 52px). Variant table in `CONFIG.variants`.

```js
primary   ['#fafafa', '#e2e2e5', text '#0a0a0a']
secondary ['#262628', '#38383c', text '#fafafa']
tertiary  [transparent, '#1c1c1f', text '#fafafa', border '#27272a']
ghost     [transparent, '#262628', text '#a1a1aa']
```

Icons are inline SVG paths in the style of the Lucide set that the usage example imports (Plus, ArrowRight, Search, Settings).

## Numbers that matter
| | |
|---|---|
| Sizes | 139x46, 139x46, 125x46, 45 round, 42 round, 52 round; 16px gaps; labels 19px weight 500 |
| Hover | fill ease .18s; primary to `#e2e2e5`, secondary to `#38383c`, tertiary fill `#1c1c1f`, ghost disc `#262628` |
| Hover order | Add item .5s, Continue 1.5s, Search 2.5s, gear 3.6s, plus 4.5s, arrow 5.3s |
| Loading (added) | 6.7 to 8.2s, spinner 720 degrees a second |
| Loop | 9s |

## Sound
Silent.

## Adapt it
- `buttons`: label, icon, size and variant of each one.
- `variants`: the four colour sets, for a light theme.
- `hovers` and `loading` times, or remove the cursor and keep only the row.
- `Z` to scale the whole row.

## Files
- `code/demo.html` runs on its own and loops. Everything is read from the `CONFIG` object at the top of the script.
- `media/poster.jpg` is one frame of it.

## Credit
Idea: "Button" by micka_design on 21st.dev (https://21st.dev/@micka_design/components/button/icons), MIT. This demo is an original recreation written from the public preview.
