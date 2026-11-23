---
name: tablet-frame-scroll-flatten-hero-rotate-x-scale-title-drift
description: A marketing hero where a device frame tilts flat as the page scrolls, with the headline moving faster than the page. Use it under a landing page headline to show the product screen.
---

# Tablet frame scroll flatten hero

**Code name:** Rotate X scale title drift.

## What you see
A white page with a faint dot grid. Centred: the small line "Unleash the power of" in 44px semibold, then "Scroll Animations" in 104px bold black over two lines. Under the headline a tablet frame comes up from the bottom of the screen: a thick dark frame with a grey outer rim, a light bezel inside it, and a dark app screen (a sidebar and a list of issues, placeholder copy here). At rest it is tipped back 20 degrees and 5% large, so its top edge is narrower. Scrolling over about 1s lifts it to the top of the screen, rotating it to flat and scaling it to 100%, while the headline moves up about 100px faster than the page and leaves the screen. A heavy layered shadow sits under the tablet, a series of 6 box-shadows growing from 9px to 233px. A thin scrollbar thumb on the right edge moves with the scroll. The demo then scrolls back up and loops.

## When to use it
The top of a landing page, where the product screenshot should arrive on scroll instead of sitting there. It needs page height to scroll through, around 1000px of space above and 500px below in the usage code. It sits close to the container text scroll skill, which keeps the headline on the card; here the headline is above it.

## How it works
The scroll progress `p` runs 0 to 1 over the scroll distance. The page moves up by `p * 480px`; on top of that the headline gets `translateY(p * -100px)`. The tablet is inside a `perspective: 1000px` parent with `transform-origin: 50% 0%` and gets `rotateX(lerp(20, 0, p))` and `scale(lerp(1.05, 1, p))`. The original uses framer-motion `useScroll` with `useTransform` for these three values and different numbers on mobile.

```js
rotate = lerp(20, 0, p);  scale = lerp(1.05, 1, p);  title.y = -100 * p
card shadow: 0 0 #0000004d, 0 9px 20px #0000004a, 0 37px 37px #00000042, 0 84px 50px #00000026, 0 149px 60px #0000000a, 0 233px 65px #00000003
```

In the demo the scroll is scripted with `eio`; wire `p` to your own scroll position. The app screenshot is replaced by HTML placeholders.

## Numbers that matter
| | |
|---|---|
| Tablet | 880 wide, 4px `#6c6c6c` rim, `#222` frame with 22px padding, 34px radius, light bezel 12px, inner screen radius 12px |
| Scroll | 480px of page travel, rotateX 20 to 0, scale 1.05 to 1, headline extra -100px |
| Type | eyebrow 44px semibold, headline 104px bold, line height 1 |
| Timing | rest .2s, scroll down 1.0s, hold 1.6s, scroll up 1.5s, loop 6s |
| Perspective | 1000px, origin 50% 0% |

## Sound
Silent.

## Adapt it
- `eyebrow`, `headline`, and the two type sizes.
- `rotFrom`, `scaleFrom`, `titleExtra`, `scrollDist` for how dramatic the move is.
- Replace the dark placeholder screen with an `<img>` of your product.
- Bind `p` to real scroll progress and drop the scripted timings.

## Files
- `code/demo.html` runs on its own and loops. Everything is read from the `CONFIG` object at the top of the script.
- `media/poster.jpg` is one frame of it.

## Credit
Idea: "Container Scroll Animation" by manuarora700 on 21st.dev (https://21st.dev/@manuarora700/components/container-scroll-animation), MIT. This demo is an original recreation written from the public preview.
