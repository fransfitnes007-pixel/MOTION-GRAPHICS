---
name: phone-fan-spring-spread-rotate-translate-stagger
description: "A set of phones spreading like a hand of cards, one after another, to show several options at once. Use it for a \"six layouts\" or \"six themes\" moment."
---

# Phone fan spring spread

**Code name:** Six phones springing into a rotated fan, staggered.

## What you see
A headline, "Start with a look." then "Six layouts.", sits on the left. As the second line is spoken, six phones, 220px wide, all start stacked at the same spot (1270, 250), 200px low and invisible. Each one in turn, 0.07s apart from left to right, springs up while shifting sideways by 110px times its distance from the centre, dipping 18px times that distance and tilting 7 degrees times it. At rest the fan runs from -17.5 to +17.5 degrees, with the two middle phones highest and in front. After 1.0s of hold the fan slides 900px right as the scene ends.

## When to use it
A set of alternatives you want the viewer to see at once before looking at them one at a time: themes, layouts, colourways, templates. It reads as "six" without any counting. The fan works from 3 to 7 items; more than that crowds the screen.

## How it works
Each phone carries its index `i` and the same formula. `d = i - 2.5` is its signed distance from the middle of six.

```js
const f = spring(seg(t, SIX - .1 + p.i * .07, SIX + .7 + p.i * .07), 7, 11), d = p.i - 2.5
p.transform = `translateX(${d * 110 * f}px) translateY(${Math.abs(d) * 18 * f + (1 - f) * 200}px) rotate(${d * 7 * f}deg) scale(${.9 + .1 * f})`
p.zIndex = 10 - Math.round(Math.abs(d))              // centre phones on top
```

Because every term is multiplied by the spring `f`, the fan opens and closes along one path, and the overshoot of the spring opens it a little too far before settling. The exit translates the whole fan to the right by 900px with `eio5`.

## Numbers that matter
- Phone: 220px wide, 2.16 aspect, corner 52px, bezel 10px, notch 34% by 28px.
- Fan: 110px per step sideways, 18px per step down, 7 degrees per step; stagger .07s; `spring(k=7, f=11)` over 0.8s.
- Exit: `eio5` over 0.45s, 900px right.
- Headline 92px, subtitle 30px `#9b9bb3` at 540px.

## Sound

## Adapt it
- The phones' screens; here they are CSS placeholders.
- The number of phones; recompute `d` as `i - (n - 1) / 2`.
- Spread (110px), rotation (7 degrees) and drop (18px) per step.
- The headline words.

## Files
- `code/demo.html` runs on its own and loops. The phone screens are CSS placeholders. The demo uses the system font stack.
