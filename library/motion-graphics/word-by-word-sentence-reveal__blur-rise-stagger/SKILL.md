---
name: word-by-word-sentence-reveal-blur-rise-stagger
description: "A sentence that builds one word at a time, each word rising 24px out of a 6px blur, where a word can also be a gradient bold phrase or a notification card sitting in the line. Reach for it for voiceover sentences in an explainer."
---

# Word-by-word sentence reveal

**Code name:** Blur-rise stagger with inline elements.

## What you see
A one-line sentence in regular weight builds itself. Each word starts 24px low, fully transparent and blurred by 6px, and settles into place over 0.4s, so the words arrive at the pace of a voice. The last phrase is bold, and in one sentence it is filled with a blue to cyan gradient. In the other sentence a white notification card (dark app icon, two lines of text, soft shadow) is one of the words and arrives with the same rise and blur. On the tall layout each sentence breaks over two or three centred lines, and each line is built the same way.

## When to use it
Spoken sentences that carry the argument, in a video where the text has to follow the voice word for word. The inline card form is for a sentence that has an object in it ("... [your app] ..."). It is a plain, small, quiet text treatment, so pair it with a bigger moment before and after, not another text effect. It is wrong for headlines (use a heavy slam word) and for long sentences.

## How it works
`line(parts, size)` builds one flex row. Strings become inline-block spans; elements (cards, bold phrases) are appended as they are. The gap between words is `size * .32`, which keeps the spacing natural at any size. `lineAt(e, t, x, y, times)` positions the row (centre anchored with `translate(-50%,-50%)`) and, for each word, computes its own progress:

```js
const q = eo(seg(t, times[i], times[i] + .4))
w.style.opacity = q
w.style.transform = `translateY(${(1 - q) * 24}px)`
w.style.filter = `blur(${(1 - q) * 6}px)`
```
Because the row is laid out as if all words were present, nothing reflows when a word appears and the sentence stays centred on its final width.

## Numbers that matter
| | |
|---|---|
| Rise | 24px, blur 6px, `eo` over .4s |
| Gap | `size * .32` |
| Sizes | 78px (64 on tall) for the question line, 60px (50 on tall) for the sentence with a card, weight 500 and 700 |
| Letter spacing | -.02em, line height 1.1 |
| Card | font 34px, icon square 2.4em, radius 1em, shadow `0 30px 70px -25px rgba(0,0,0,.45)` |
| Voice offsets | words at 0, +.46, +.86 (sentence 1); +0, +.46, +.56, +.9 (sentence 2) |

## Sound
A soft pop on each word, high and short (about 900 to 1100Hz, 0.11s), panned slightly left and right in turn. Under the voice, so keep them quiet.

## Adapt it
- The words and which one is bold or gradient.
- Per-word times from your voice track.
- Size: the whole row scales from one number.
- What the inline element is (card, logo, avatar stack).

## Files
- `code/demo.html` runs on its own. It plays both sentences one after the other; the card icon is a placeholder glyph.
