---
name: numbered-card-grid-and-dark-steps-stagger-in-view-reveal
description: "As the page scrolls, a heading and a three-by-two grid of glass cards with black number badges rise in one by one, then a black rounded panel with a four-step list rises in below. Reach for it as the middle of a sales page."
---

# Numbered card grid and dark steps panel

**Code name:** Stagger in-view reveal.

## What you see
The page rests, then scrolls. At the top, a centred eyebrow and headline fade up, then six glass cards, each with a black rounded-square badge ("01"), a short bold title and a line of grey text, rise 70ms apart in reading order. Scrolling on, a large ink-black panel with 36px corners reveals: a small "How it works" pill, a headline and a white button on the left; four translucent white cards on the right, each with a pale-violet step number.

## When to use it
The "what you get" and "how it works" stretch of a landing page. The light-then-dark change gives the page a rhythm break before the FAQ. Wrong for pages with a single section, or when each card needs a different entrance.

## How it works
`Reveal` is one `motion.div`: `hidden { opacity: 0, y: 18 }`, `show { opacity: 1, y: 0, duration: .6, ease: [.22, 1, .36, 1] }`, triggered with `whileInView` and `viewport={{ once: true, margin: "-60px" }}`, so it fires when the element is 60px inside the bottom of the screen and never plays again. `Stagger` is the same trigger on a parent with `staggerChildren: 0.07`, and children use the same `item` variant.

```tsx
<Stagger className="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
  {a.bullets.map((b, i) => <MotionItem variants={item} className="glass card-hover rounded-3xl p-6">...</MotionItem>)}
</Stagger>
```

The dark panel is a single `Reveal`, not staggered: `rounded-4xl bg-ink px-6 py-10 text-white`, a grid of `[0.8fr_1.2fr]`, and step cards `border border-white/10 bg-white/[0.06] p-5 backdrop-blur-sm`. The demo scrolls the page on a timer and works out each element's start time from when its top crosses `viewport height - 60px`.

## Numbers that matter
| | |
|---|---|
| Card | `glass`, rounded-3xl, 24px padding, grid gap 16px, 3 columns at lg |
| Badge | 40px, rounded-2xl, bg ink, white 14px semibold |
| Stagger | .07s |
| Reveal | y 18 to 0, opacity 0 to 1, .6s, ease [.22, 1, .36, 1], once, margin -60px |
| Dark panel | bg ink (#0b0c10), rounded-4xl (36px), padding 56 by 40, two columns .8fr and 1.2fr |
| Step card | border white/10, fill white/6, rounded-2xl, 20px padding, number in accent-glow #c7c8ff |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The copy and the number of cards (multiples of 3 keep the grid even).
- The panel colour: ink is the theme token, so a brand colour changes the panel and the badges together.
- Stagger interval and trigger margin.
- Swap the step list for a timeline or video.

## Files
- `code/demo.html` runs on its own and loops. Copy is placeholder text.
