---
name: hero-stack-fade-up-expo-out-staggered-delays
description: "A landing hero that builds itself in order. The headline, paragraph, buttons and a video card each rise 20 to 32px and fade in on one expo-out curve, 0.1s apart, with a blue gradient second line in the headline. Use for the first screen of a marketing page."
---

# Hero stack fade-up

**Code name:** Expo-out staggered delays.

## What you see
A light page with a faint blue wash behind the top. A chrome wordmark sits at the top. Under it a two-line headline in 60 to 68px bold with tight tracking: the first line in near-black, the second in a left-to-right blue gradient. The headline rises 20px and fades in over .8s, starting .1s in. The paragraph follows .1s later, then the pair of buttons .1s after that: the black metal-rim primary and a clear glass secondary with a building icon. Last, .45s in, a wide video card rises 32px over .9s, with a blue halo above it, a round metal play button with a pinging ring, and a "Watch the film" pill. Everything settles by about 1.4s.

## When to use it
The first screen of a marketing page: one idea, one or two actions, one proof object. The delay steps are small enough that it reads as one build rather than four separate entrances. For lower sections use the `FadeUp` form: `whileInView` with `once` and a -60px margin, delays of .05 to .1s.

## How it works
No orchestration; each block is a `motion` element with the same easing and its own delay:

```tsx
<motion.h1 initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.8, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}>
// p: delay .2, buttons: delay .3, film card: initial y 32, duration .9, delay .45
```
`[0.16, 1, 0.3, 1]` is an expo-out curve: 80% of the move happens in the first quarter of the time, then a long soft settle. That is why 20px feels gentle. The gradient line is plain `background-clip: text` over `linear-gradient(90deg, #1D4ED8, #2563EB 45%, #0EA5E9)` with a transparent text fill. The primary button's rim and the play button use the metal-rim recipe (see `liquid-metal-cta-button__registered-angle-conic-rim`). The secondary uses the stylesheet's `.btn-glass`, a clear glass layer built from nine inset and outer shadows; on the live page it also runs an SVG displacement through `backdrop-filter`, which the demo leaves out.

## Numbers that matter
| | |
|---|---|
| Headline | 40px on phones up to 68px (`lg:text-[4.25rem]`), bold, tracking-tight, leading 1.04 |
| Delays | h1 .1s, paragraph .2s, buttons .3s, video card .45s |
| Durations | .8s for text and buttons, .9s for the card |
| Distance | 20px for text and buttons, 32px for the card |
| Ease | `[0.16, 1, 0.3, 1]` |
| Gradient (light) | `#1D4ED8, #2563EB 45%, #0EA5E9`; dark theme `#D4D4D8, #FFF, #A1A1AA` |
| Paragraph | 16 to 18px, `text-rv-muted`, max width 40rem |

## Sound
Silent.

## Adapt it
- Copy, and which words form the gradient line.
- `--hero-grad` colours.
- Step size between delays (.1s) for a slower or tighter build.
- The proof object: a video, a product screenshot, a stat strip.

## Files
- `code/demo.html` runs on its own and loops in 6s.
