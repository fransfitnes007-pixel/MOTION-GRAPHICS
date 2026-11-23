---
name: book-title-buy-button-end-card-slam-pop-cursor-click
description: "A closing card: the 3D book floats in at left, the author line, a two-line title and a yellow shop button appear at right, a cursor clicks the button, a tagline slams in, and the picture fades to black. Use it to end a book, product or app ad."
---

# Book, title and buy-button end card

**Code name:** Slam, pop and cursor click.

## What you see
The book rises 120px into place at left (0.9s) and keeps bobbing and turning 3 degrees. At 0.6s a round avatar and a gold tracked line ("AUTHOR NAME · A TRUE STORY") appear. "The Golden Title" slams in word by word at 0.8s, "on Silver Lane." at 1.3s. At 2.4s a yellow pill button pops in. At 4.7s a cursor, which has glided in since 3.2s, clicks it: the button dips to 95% and a gold ring expands. Then the tagline slams at 5.6s and a small grey URL line fades in at 6.3s. In the last 0.6s the vignette closes to black. On 9:16 everything centres, book above text.

## When to use it
The last 8 to 11 seconds of an ad for something a person can buy. The yellow button reads as a shop button; recolour it to match your shop.

## How it works
`sceneCta()` is one function of time, built from pieces in other skills: `book()` (see the 3D book skill), `slam()` for the three text lines, `cursor()`, and a button animated like a card:

```js
const kb = backS(p(t, bAt, bAt + 0.5), 1.8), pressed = t > click && t < click + 0.18 ? 0.95 : 1
tf(bt, { x: bkx, y: bky, s: lerp(0.7, 1, kb) * pressed, a: p(t, bAt, bAt + 0.2) })
cursor(t, [[click - 1.5, bkx + bw * 1.1, bky + bh * 2.2], [click - 0.3, bkx + bw * 0.62, bky + bh * 0.55], [click + 0.9, ...]], click)
// last 0.6s: vig background rewritten to close to black
```
`bAt = t0 + 2.4`, `click = t0 + 4.7`. The text column sits at `x = 56%` of the width (wide) or the centre (tall); the vertical stack is eyebrow, headline, button, tagline, URL, each offset from the title y. The button is 420 by 92 (wide), `#ffd814` with a dark label, radius 999px, and a soft yellow shadow. The eyebrow, avatar, headline and URL here are placeholders.

## Numbers that matter
| | |
|---|---|
| Book | rises 120px over 0.9s (`eo`), scale .82 wide / .78 tall, bob 6px |
| Title | Playfair 700 at 92px, "Golden Title" in gold italic; words 0.1s apart |
| Button | 420 by 92px, #ffd814, text 30px 600, pop 0.5s `backS(1.8)` from .7 |
| Click | t0 + 4.7s, cursor path starts t0 + 3.2s |
| Tagline | 44px at click + 0.9s; URL 24px at click + 1.6s, opacity .8 |
| End | vignette to black over the last 0.6s |

## Sound

## Adapt it
- Book art, author, title, button label, URL, tagline.
- Button colour (default is a shop-yellow).
- `bAt`, `click` timing to match the voice.
- Drop the avatar or the URL line.

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. Playfair Display (SIL Open Font License, from Google Fonts) is copied into `code/fonts/` because the serif headline is half the look. Small labels use the system font stack. Rye and Great Vibes are copied for the placeholder cover.
- `code/fonts/` holds the fonts the demo loads.
