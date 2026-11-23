---
name: giant-number-count-up-accent-eo5-colour-flip
description: "A huge headline number on a dark stage counting up as the voice says \"real numbers\". Use it for the one metric that matters most."
---

# Giant count-up number

**Code name:** Eo5 count with accent colour flip beside a phone.

## What you see
A headline reads "Your results, in real numbers." with the first line's second word in lavender. Under it a 210px heavy white number starts at 0 and counts up quickly, through tens of thousands to 995,885, slowing to a crawl, over 1.3s from the word "results" to just after "numbers". When it reaches 1,000,000 it turns lavender. A grey spaced caption fades in under it, and a phone leans in at the right.

## When to use it
The key proof number in a dark video, spoken once. The steep ease-out gives the feeling of an accelerating thing that has "arrived". Use one per video; the glass-card version suits a lighter, quieter moment.

## How it works
As with the glass card, the number is text re-set every frame, with tabular numerals so it does not jitter:

```js
big.textContent = Math.round(lerp(0, 1000000, eo5(seg(t, RESULTS, NUMBERS + .2)))).toLocaleString('en-US')
big.style.color = t > NUMBERS + .2 ? '#a5b4fc' : '#fff'
```

The caption's opacity is a plain `eo5` on the word "real". The strip and the phone are the same as in the other laptop and phone scenes. Because the curve is a quintic ease-out, after half the time the number is already at 97% of its final value; if that is too fast, use `eo` (cubic).

## Numbers that matter
- Number: 210px, weight 800, letter-spacing -.06em, line-height 1; at (104, 560).
- Count: `eo5`, 0 to 1,000,000 over 1.34s; flip to `#a5b4fc` at the end.
- Caption: 30px bold, letter-spacing .14em, `#9b9bb3`, at y 790.
- Phone 280px, rotate (1 - pp) * -6 - 3 degrees.

## Sound

## Adapt it
- The target number and the caption.
- The count curve (`eo5` to `eo`).
- Accent colour at the end.
- The phone or other visual on the right.

## Files
- `code/demo.html` runs on its own and loops. The caption is neutral placeholder text. The demo uses the system font stack; SF Pro Display is a good match.
