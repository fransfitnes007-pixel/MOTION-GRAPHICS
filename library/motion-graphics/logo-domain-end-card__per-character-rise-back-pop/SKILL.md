---
name: logo-domain-end-card-per-character-rise-back-pop
description: "A logo mark pops in with a slight overshoot, the web address underneath types itself on letter by letter with each letter rising, then a name and a tagline fade up. Reach for it as the closing frame of a launch or promo video."
---

# Logo and domain end card

**Code name:** Per-character rise, back-ease pop.

## What you see
The button has just been clicked and has swelled away. A black rounded-square logo mark (150px) pops in from 70% with an overshoot over 0.55s. 0.15s later the web address underneath builds letter by letter, each letter rising 40% of its height while fading in, 32ms after the last, 0.4s per letter. A name fades up 18px at 1.25s after the click, and a grey tagline 0.15s after that. Then it holds on the pastel ground.

## When to use it
The final 3 seconds of a launch, promo or tutorial: whatever the viewer should remember (the address) is biggest. It works with any brand mark. Wrong for a very long URL: at 136px, 16 characters is about 1100px wide.

## How it works
Each character is its own span. A character's progress is an ease-out-cubic over 0.4s, offset by 0.032s per character, and it drives opacity and a rise of 0.4 x the font size. The mark uses ease-out-back for its scale. The name and tagline are plain fade-ups. All times are relative to the click on the CTA (0 in the demo).

```js
endChars.forEach((ch, j) => {
  const k = eo(p(t, CTACLICK + 0.55 + j * 0.032, CTACLICK + 0.95 + j * 0.032))
  ch.style.opacity = k; ch.style.transform = `translateY(${(1 - k) * L.end.domain * 0.4}px)`
})
endMark.style.transform = `scale(${lerp(0.7, 1, back(p(t, CTACLICK + 0.4, CTACLICK + 0.95)))})`
```

The demo draws the mark as a black square with the words "your logo" and clears the inline styles once each element has arrived. It also fades the card in and out so the loop is clean.

## Numbers that matter
| | |
|---|---|
| Mark | 150px (170 tall), radius 24%, shadow `0 30px 60px -26px rgba(15,17,26,.5)` |
| Domain | 136px (104 tall), bold, letter-spacing -0.03em, 0.32 x mark height below the mark |
| Name | 44px (46 tall), semibold, 0.36 x domain size below it |
| Tagline | 32px (34 tall), `#5c606b`, 0.4 x its size below the name |
| Timing after the click | mark .4s to .95s; letters from .55s, 32ms apart, .4s each; name 1.25s to 1.7s; tagline 1.4s to 1.85s |

## Sound
Silent; music resolves under it.

## Adapt it
- `DOMAIN`, the name, the tagline, and the mark (an image or SVG instead of the placeholder).
- The per-character delay `0.032` for a faster or slower type-on.
- Ground: the blobs, or a flat colour.
- Sizes in the `E` block.

## Files
- `code/demo.html` runs on its own (4.2s loop).
