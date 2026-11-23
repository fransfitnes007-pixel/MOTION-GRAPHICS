---
name: hover-expand-icon-sidebar-width-collapse-label-fade
description: An app-shell sidebar that expands on hover and collapses to icons, with an animated main area beside it. Use it for admin, B2B and customer dashboards.
---

# Hover-expand icon sidebar

**Code name:** Width collapse label fade.

## What you see
A rounded, thinly bordered shell on a faint dotted white page. Left: a light-grey sidebar with a black blob logo and "Acet Labs", four rows with line icons and labels (Dashboard, Profile, Settings, Logout) and a round avatar with "Manu Arora" at the bottom. Right: a white panel with a large rounded top-left corner holding grey placeholder blocks, four small ones over two tall ones. The clip begins with the cursor resting in the sidebar, which is wide (about 448px of 968px here). As the cursor moves out to the panel, over about 0.4s the sidebar narrows to a 89px rail: the labels fade out while they are still being clipped by the shrinking width, the brand text goes and only the logo, the four icons and the avatar remain. The white panel grows into the freed space and its blocks widen with it. In the demo the cursor comes back after 3.2s and the sidebar opens again.

## When to use it
Admin, CRM and customer-portal shells where screen width matters and the menu is used in bursts. Wrong when the sidebar must stay open for orientation, and awkward on touch, where the original switches to a mobile drawer.

## How it works
One value `k` from 0 (rail) to 1 (open) is eased with `eo` over 0.4s. The sidebar width is `lerp(89, 448, k)`; the main panel is positioned at that left edge, so its width and the skeleton tiles are recomputed from the remaining space every frame. Labels use opacity `clamp((k - .45) / .55)`, so they are fully visible only in the second half of opening and gone early on closing. The original sidebar is 300px open and 60px closed and uses framer-motion `animate={{ width }}`, with hover handlers on the sidebar to call `setOpen`.

```js
sidebarW = lerp(89, 448, k)
labelOpacity = clamp((k - .45) / .55)
tile widths = (innerWidth - gaps) / 4 and / 2
```

The avatar is an SVG stand-in.

## Numbers that matter
| | |
|---|---|
| Shell | 968x736, 9px radius, `#f4f4f5`, 1px `#dcdce0` |
| Sidebar | 448 open, 89 closed, .4s `eo` |
| Rows | 66px apart, 30px icons, 22px labels |
| Main panel | white, 34px top-left radius, tiles 116px tall over two tall tiles, 12px gaps |
| Timeline | collapse at .45s, reopen at 3.2s, loop 4.4s |

## Sound
Silent.

## Adapt it
- `brand`, `user`, `links` and the icon table `ICON`.
- `wOpen`, `wClosed`, `collapseSec`, `expandSec`.
- `events`: when it opens and closes; in a real app this is the hover state.
- The main area is placeholder blocks; replace the `sks` tiles with your content.

## Files
- `code/demo.html` runs on its own and loops. Everything is read from the `CONFIG` object at the top of the script.
- `media/poster.jpg` is one frame of it.

## Credit
Idea: "Sidebar" by manuarora700 on 21st.dev (https://21st.dev/@manuarora700/components/sidebar), MIT. This demo is an original recreation written from the public preview.
