---
name: round-icon-only-buttons-grey-grey-red-press-scale-hover-fill
description: "Three round icon-only buttons (more, settings, delete): two light grey, one red. Each darkens on hover and shrinks to 97% on press. Reach for it for toolbars and row actions."
---

# Round icon-only buttons, grey grey red

**Code name:** Press scale and hover fill.

## What you see

## When to use it
Row actions, card toolbars, close and delete buttons where there is no room for a label. Give each one an aria-label; the usage example does (More, Settings, Delete).

## How it works
A button with `isIconOnly`, which makes it square and fully rounded, plus a variant for colour (`secondary`, `tertiary`, `danger`). Hover swaps the fill to the next shade, press applies `scale(.97)`. The demo drives both from time with `win()` windows per button.

## Numbers that matter
- 40px circles, 12px gap, icons 18px
- Grey `#ebebed`, hover `#dfdfe2`; red `#ff3b3f`, hover `#e8272c`
- Press scale 0.97, 0.06s in and out
- Hover fade 0.15s

## Sound
Silent.

## Adapt it
- `buttons`: icon, fill, hover fill and colour for each one.
- `size`, `gap` and `iconSize` for a larger toolbar.
- `pressScale` for a stronger press.
- `steps` and `press` to change who gets hovered and clicked, and when.

## Files
- `code/demo.html` runs on its own, loops in 6s, and has a `CONFIG` block at the top of the script.

## Credit
Idea: "HeroUI Button" by hero_ui on 21st.dev (https://21st.dev/@hero_ui/components/heroui-button/icon-only), MIT. This demo is an original recreation written from the public preview.
