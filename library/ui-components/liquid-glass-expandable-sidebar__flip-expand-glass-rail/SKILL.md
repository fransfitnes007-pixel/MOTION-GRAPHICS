---
name: liquid-glass-expandable-sidebar-flip-expand-glass-rail
description: A frosted-glass app sidebar over a photo that expands from an icon rail into grouped, searchable navigation, with a glass pill that glides to the selected page. Reach for it for app tours, nav and menu beats on a phone-shaped frame.
---

# Liquid glass expandable sidebar

**Code name:** Flip expand, glass refraction rail.

## What you see
A sandy and sea-blue scene with a tall rounded frosted-glass panel on the left: a small mark and Studio workspace with a collapse arrow, a Find a page search field, grouped links (Workspace: Home, Projects, Studio website and Client portal nested under it, Create, Inbox; More: Calendar, Settings, Help) and a Studio Member account row at the bottom. A lighter glass pill sits behind Studio website. At 1.3s it glides to Inbox (0.4s, power2.out). At 2.5s the panel collapses over 0.5s to a 68px rail: labels fade, search and group titles go, the nested pages fold into Projects, the arrow flips. At 3.7s Calendar shows a white tooltip. At 5.0s it expands again. 7.5s loop.

## When to use it
Navigation in an app promo, the "everything in one place" beat, a settings or workspace tour. At 9:16 it fills the height of the phone nicely. The glass needs something colourful or photographic behind it.

## How it works
- Open and close is GSAP Flip: capture state, change `data-expanded`, `Flip.from(snapshot, { duration: .5/speed, ease: 'power2.inOut', scale: false })`. The demo replicates it as a 0.5s power2.inOut width change, 260px to 68px, radius 26px to 32px.
- The selection light is one absolutely-positioned marker moved with `gsap.to(light, { y: top, height, duration: .4/speed, ease: 'power2.out' })`; the demo moves it the same way.
- The glass material is stacked backgrounds plus `backdrop-filter: blur(var(--gn-blur)) saturate(1.3)` and inset edge highlights. In Chromium it also builds an SVG displacement map (`feImage` + `feDisplacementMap`, scale 20 to 28) from the panel's rounded-rect distance field and applies it as a second backdrop filter, so the edge bends the picture. The demo keeps blur, saturation and edge light only: the displacement map is a canvas data URI built from live element size, which is not a pure function of time.
- Rail labels become tooltips on hover or focus; scroll edges fade with a CSS mask.

## Numbers that matter
| | |
|---|---|
| Width | 260px open, 68px rail |
| Radius | 26px open, 32px rail |
| Expand | 0.5s power2.inOut (Flip) |
| Marker | 0.4s power2.out |
| Row | 44px high, 15px radius links |
| Glass defaults | blur 2, opacity .08, saturation 1.3, edge .85, distortion 28 |
| Demo settings | frost 2, edgeLight .85, refraction 20, selectionLight .8 |

## Sound
Silent. A soft whoosh on expand.

## Adapt it
- `CONFIG.groups` (id, label, icon, child flag), `brand`, `account`.
- `CONFIG.timeline`: `select` [time, id], `collapse` [[collapse at, 0], [expand at, 1]], tooltip time and row.
- Replace the gradient scene with a real photo or a screen recording; the glass reads it live.
- For the real behaviour (search filtering, scroll fades, keyboard) install the original MIT component from its page (credited below); it needs `gsap`, `@gsap/react`, `lucide-react`.

## Files
- `code/demo.html` runs on its own and loops; the values to change are in its `CONFIG` block.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Liquid Glass Expandable Sidebar" by automateflows (Troy Lorents / Automate Flows) (https://21st.dev/@automateflows/components/liquid-glass-expandable-sidebar), MIT. Rebuilt as render(t) from the published code. Full notices: `THIRD_PARTY_NOTICES.md`.
