---
name: collapsible-glass-sidebar-shell-spring-width-collapse
description: "A dark purple dashboard frame with a sidebar that animates between full width and an icon rail, a round chevron toggle on its edge, and a mobile slide-in drawer. Reach for it when you need to show an app shell that feels responsive, with chart panels inside."
---

# Collapsible glass sidebar shell

**Code name:** Spring width collapse.

## What you see
Two frames. On the left a desktop app: a 240px sidebar with a gradient logo tile, five nav items (the active one has a purple fill and border) and a user card at the bottom. A small purple round button sits on the sidebar's right edge. Inside, a page with two tab pills, four stat tiles, a radar chart and a follower-growth line chart. On the right, a phone frame with a hamburger button.

- 0 to 1.5s: the radar grows from the centre and the line draws left to right.
- 1.9s: a cursor clicks the edge toggle. The sidebar narrows to 68px over 0.3s (easeInOut), the chevron turns 180 degrees, the labels vanish at once, and the page area widens, so the cards and the line chart reflow to the new width.
- 4.2s: it clicks again and the sidebar widens, labels return.
- 5.8s: the cursor taps the phone hamburger. A black 60% backdrop fades in (the source also blurs it by 4px, which the demo leaves out, because a backdrop blur renders slightly differently between two draws of the same frame) while a 256px drawer springs in from the left.
- 8.0s: the drawer springs back out.

## When to use it
Product tours, feature videos for dashboards, or as the frame for any other panel in this library. Collapse to a rail is a good "this app respects your screen space" beat. It does not suit an app with a top nav.

## How it works
Sidebar width is a framer-motion `animate` on `width`, with the nav labels rendered conditionally (`{sidebarOpen && ...}`), which is why the labels disappear instantly instead of fading while the rail narrows.

```tsx
<motion.aside animate={{ width: sidebarOpen ? 240 : 68 }}
  transition={{ duration: 0.3, ease: "easeInOut" }} ...>
<button className="absolute top-5 -right-3 w-6 h-6 rounded-full bg-primary ...">
  <motion.div animate={{ rotate: sidebarOpen ? 180 : 0 }} transition={{ duration: 0.3 }}>
```

The mobile drawer is a spring, not a tween: `initial={{ x: -280 }} animate={{ x: 0 }} exit={{ x: -280 }} transition={{ type: "spring", damping: 25, stiffness: 200 }}` over a `bg-black/60 backdrop-blur-sm` overlay. The demo uses the same damping and stiffness, with `fmSpring(t, 200, 25)`.

The demo reads the main area's real width every frame and redraws the line chart's path to fit, which is what Recharts' `ResponsiveContainer` does when the sidebar moves.

## Numbers that matter
| | |
|---|---|
| Sidebar | 240px open, 68px closed, 0.3s easeInOut |
| Toggle | 24px circle, `top-5 -right-3`, rotates 0 to 180 degrees |
| Drawer | 256px wide, spring stiffness 200, damping 25 |
| Backdrop | black at 60%, blur 4px in the source (omitted in the demo) |
| Page fade | opacity 0 to 1 and y 8 to 0 in 0.4s |
| Radar and line | Recharts default 1.5s ease |

## Sound
Silent. A soft click on each toggle would fit.

## Adapt it
- `T_COLLAPSE`, `T_EXPAND`, `T_OPEN`, `T_CLOSE` set the beats.
- Primary hue (290) for the toggle, active nav and chart strokes.
- The nav list `NAV`, and the cards inside the page.

## Files
- `code/demo.html`: runs on its own.
