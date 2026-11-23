---
name: checklist-steps-tick-in-spring-dot-blur-slide
description: "A left-aligned stack of three huge one-word steps, each with a violet tick dot that springs in as the word slides in from the left through a blur, followed by a smaller sentence that builds word by word underneath."
---

# Checklist steps tick-in

**Code name:** Spring dot, blur slide.

## What you see
Three rows at x=120: a 74px violet gradient circle holding a white check, then a 128px word. Each row slides in 60px from the left while it unblurs over 0.44s; its check dot springs from 0 with a small overshoot. The rows land 0.38s and 0.7s apart, on the spoken words. A 60px sentence starts at 6.56s below the stack and builds word by word with the last word in gradient. At 8.2s everything slides 200px left and blurs out.

## When to use it
A three-step process, a promise in three verbs, or any list the voice reads one item at a time. The dots make each item read as done, so it suits "how it works" more than "problems". Keep it to three rows; four starts to crowd a 1080 frame at this size.

## How it works
Each row is a flex group. Row progress is `p = eo5(seg(t, at-.06, at+.38))` for position, opacity and blur; the dot has its own spring so it pops slightly after the text begins.

```js
const p = eo5(seg(t, g.at - .06, g.at + .38)), pd = spring(seg(t, g.at - .02, g.at + .5), 8, 14)
S(g, { opacity: p * (1 - out), transform: `translate(${(1 - p) * -60 - out * 200}px, 0)`, filter: `blur(${(1 - p) * 12 + out * 10}px)` })
g.dot.style.transform = `scale(${pd})`
```
The group exit shares one `out = eio5(seg(t, 8.2, 8.62))`, so all rows leave together. The right half of the frame can hold a product window; the text column works alone too.

## Numbers that matter
| | |
|---|---|
| Rows | y centres 300, 455, 610 (155px pitch); word 128px weight 800, letter-spacing -.05em |
| Dot | 74px circle, `linear-gradient(180deg,#8b5cf6,#6d3cff)`, 40px check, spring k=8 f=14 over 0.52s |
| Slide in | 60px from the left, 0.44s `eo5`, blur 12px to 0 |
| Sentence | 60px weight 700, words at +0.38s `eo5`, rise 18px |
| Exit | 8.2s to 8.62s `eio5`, 200px left, blur 10px |

## Sound
A whoosh can peak as this scene enters. Nothing per row.

## Adapt it
- The three words and their `at` times.
- Row pitch (`y` values) and word size if you have more than three.
- Dot colours: the gradient and shadow.
- The `out` time.

## Files
- `code/demo.html` runs alone (copy is placeholder).
