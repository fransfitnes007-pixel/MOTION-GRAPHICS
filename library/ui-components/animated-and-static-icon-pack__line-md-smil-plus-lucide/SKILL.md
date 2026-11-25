---
name: animated-and-static-icon-pack-line-md-smil-plus-lucide
description: A pack of 18 self-animating SVG icons (line-md) and 36 static Lucide icons, with a demo grid. Reach for it whenever a video needs a better icon than a plain glyph: a bell that rings, a check that draws, a loader, a download arrow.
---

# Animated and static icon pack

**Code name:** Line-md SMIL plus Lucide.

## What you see
Dark page. A heading Animated, then a grid of line icons in four accent colours, each one moving on its own: the bell swings, the loader spins, the check-all draws its ticks, download and upload arrows loop, the heart and star fill in. Below, a heading Static and 36 calm Lucide icons. Each cell pops in with a small spring, one after another. 6s loop.

## When to use it
Icon beats in app-promo reels: a notification bell, a payment tick, a loading ring, a share arrow. Pick the animated ones when the icon should do something, the static ones when it should just sit and read. They are single-colour (`currentColor`), so set `color` and they take any brand colour.

## How it works
The animated icons are plain SVG with SMIL (`<animate>`, `<animateTransform>`). SMIL can be driven by hand, which is what keeps the demo a pure function of time:

```js
svg.pauseAnimations(); svg.setCurrentTime(t)   // t in seconds; same t, same frame
```

Loop lengths are 0.2s to 6s depending on the icon; `DUR = 6` covers the longest. Drop the files in `code/svg/animated/` into any page, or inline them as the demo does.

## Numbers that matter
| | |
|---|---|
| Viewbox | 24 x 24, stroke 2, round caps |
| Colour | `currentColor`; demo cycles 4 accents |
| Pop-in | spring(7, 11), 35ms stagger |
| Animated set | line-md, 18 icons, MIT, Vjacheslav Trushkin |
| Static set | Lucide, 36 icons, ISC |

## Sound
Silent. A soft tick on the check, a short bell on bell-loop.

## Adapt it
- Add icons: `https://api.iconify.design/line-md/<name>.svg` or `/lucide/<name>.svg`.
- `size` and `cols` in the demo script set the grid.
- For a hero icon at 9:16, inline one SVG at 400px and call `setCurrentTime`.
- Not included: Lottie. These sets are SVG; the page's other animated sets (Lucide Animated, AnimateIcons, Heroicons Animated) are React hover components, not files.

## Files
- `code/demo.html` runs the grid and loops.
- `code/svg/animated/*.svg` 18 animated icons. `code/svg/static/*.svg` 36 static icons.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Material Line Icons (line-md, animated)" by Vjacheslav Trushkin (https://21st.dev/community/icons), MIT. "Lucide (static)" by Lucide Contributors (https://21st.dev/community/icons), ISC. Formulas follow the original MIT component; the demo is rewritten as render(t). Full notices: `THIRD_PARTY_NOTICES.md`.
