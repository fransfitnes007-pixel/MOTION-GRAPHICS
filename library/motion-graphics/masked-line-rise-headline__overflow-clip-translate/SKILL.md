---
name: masked-line-rise-headline-overflow-clip-translate
description: "Editorial headline reveal on a dark stage: every line is a mask and each word rises 110% of its height into it. Use it for chapter headlines and statements in explainers with a strong left-aligned layout."
---

# Masked line rise headline

**Code name:** Words sliding up out of an overflow-hidden line.

## What you see
On a near-black stage a headline sits at the left, 100px, weight 800, tight letter-spacing. Nothing is blurred and nothing fades: each word starts 110% of its own height below the baseline, hidden because each line clips its overflow, and slides up into place with a strong ease-out over 0.36s. "Your content deserves" is three words down the first line, then "more than a plain link." on the second, with the last two words in light lavender. At 3.05s every word slides back up and out through the top of its line in 0.3s, ease in and out.

## When to use it
Editorial, left-aligned title cards and chapter lines on a dark stage, where the viewer should read each word as it is spoken. It is cleaner than a blur or fade and works on mixed backgrounds, as long as the line is allowed room above it to hide in. It does not suit centred type unless you change the alignment.

## How it works
Each line is a block with `overflow:hidden` and a little bottom padding so descenders are not clipped. Each word is an inline-block child; moving a word down by 110% of its height simply puts it under the clip.

```css
.hl .ln { display:block; overflow:hidden; padding:0 0 .08em }
.hl .w  { display:inline-block }
```
```js
const p = eo5(seg(t, s.at - .06, s.at + .3)), q = eio(seg(t, out, out + .3))
s.style.transform = `translateY(${(1 - p) * 110 - q * 110}%)`
```

Because the move is in percent of the word's own height, the same code works at any size. A word marked accent gets `#a5b4fc`.

## Numbers that matter
- Entry: `eo5` from 0.06s before the word to 0.3s after (0.36s), translateY 110% to 0.
- Exit: `eio` over 0.3s, 110% upward; all words together.
- Type: 92 to 100px, weight 800, line-height 1.04, letter-spacing -.045em, word gap .24em, left 112px.
- Accent colour `#a5b4fc`; text `#fff` on `#07070c`.

## Sound

## Adapt it
- The words, the `at` times and which words are accent.
- `top` and `size` of the headline; the left margin (112px).
- Entry curve (`eo5`) and length, for a faster or slower rise.
- Add a second block with `sub()` underneath for a small grey subtitle.

## Files
- `code/demo.html` runs on its own and loops. The demo uses the system font stack.
