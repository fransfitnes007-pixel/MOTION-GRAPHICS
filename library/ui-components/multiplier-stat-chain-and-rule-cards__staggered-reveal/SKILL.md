---
name: multiplier-stat-chain-and-rule-cards-staggered-reveal
description: "A left-to-right chain of stat cards joined by arrows that rise in one after another while counting up, the last one tinted green as the result, followed by a row of white cards that each draw an indigo rule across their top edge. Reach for it to show how a result was built up from smaller numbers."
---

# Multiplier stat chain and rule cards

**Code name:** Staggered reveal.

## What you see
Inside a white glass panel, five bordered cards sit in a row with a small arrow between each: partners, posts, views, link taps, sales. They rise 16px and fade in 140ms apart, each arrow fading in a beat after its card, and each figure counts up over 1.1s. The last card has a green border and tint with green text, the result. Below a heading, three white cards rise 22px; as each lands, a 3px indigo-to-lilac line sweeps across its top edge from left to right and a pale indigo number badge sits above the title.

## When to use it
A case study, funnel or "how the maths works" block where the viewer should follow one figure into the next. Stacks vertically on phones, with the arrows hidden. Wrong for unrelated stats (use the stat band) or more than six steps.

## How it works
`ScaleStrip` is a flex row; each node is `flex flex-1 items-center gap-2.5` holding a `motion.div` and, unless last, an arrow `motion.span` hidden below `sm`. A shared `useRevealed` hook starts everything at once.

```tsx
<motion.div initial={{ opacity: 0, y: 16 }} animate={inView ? { opacity: 1, y: 0 } : {}}
  transition={{ duration: 0.5, delay: i * 0.14, ease: [0.22, 1, 0.36, 1] }}
  className={cn("flex-1 rounded-2xl border px-4 py-4", last ? "border-success/30 bg-success/10" : "border-ink/8 bg-white/75")}>
```

`ApproachCard` uses `whileInView` with `delay: (i % 3) * 0.09`, plus an `absolute inset-x-6 top-0 h-[3px] origin-left` gradient `motion.span` animating `scaleX` from 0 to 1 over .7s with an extra .15s delay.

## Numbers that matter
| | |
|---|---|
| Node card | rounded-2xl, border ink/8, fill white/75, 16px padding; figure 30px semibold; label 11px uppercase tracking-wider |
| Result card | border success/30, fill success/10, text #166534 |
| Strip reveal | y 16, .5s, delay i x .14s, ease [.22, 1, .36, 1]; arrow opacity delay + .1s |
| CountUp | 1100ms in the strip |
| Rule card | rounded-3xl, border ink/5, fill white/75, 24px padding; y 22, .55s, delay (i % 3) x .09s |
| Top rule | 3px, gradient accent #5b5ce6 to #8b8cf0, scaleX .7s, origin left |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The nodes: value, label and optional sub line; the last node is always styled as the result.
- The 140ms per-node delay.
- The rule gradient: it reads from the accent and accent-soft tokens.
- Use two or three card columns for fewer cards.

## Files
- `code/demo.html` runs on its own and loops. All figures and copy are invented.
