---
name: serif-word-slam-headline-staggered-word-scale-fade
description: "Big bold serif headline that lands one word at a time, each word dropping in from 1.3x scale, with a gold italic or red accent word. Reach for it for hook lines and reveals in a dark, cinematic video."
---

# Serif word slam headline

**Code name:** Staggered word scale-fade.

## What you see
Black stage with a slow red glow. "Every October," builds word by word at 0.25s, then "the blood came back." at 1.25s with "blood" in red. Each word starts 30% too big and 35% of the font size below its place, fades in as it settles, and the next word follows 0.1s later. After the hold the lines lift 40px and shrink to 96% as they fade (0.35s). The "true story" reveal reuses the same call: "This is not fiction." with "not" in red, then "This is a true story." with "true story." in gold Playfair italic.

## When to use it
Opening hooks, a one-line claim, a reveal that follows a spoken line. It suits serif, literary or documentary tone and a dark stage. Keep it to two short lines; long lines slam slowly because each word costs 0.1s. For a different entrance (blur, rise) see the sibling skills listed in meta.json.

## How it works
`slam()` splits the HTML string into words while keeping the inline tags that were open around each word (`tokenize`), wraps each word in `<span class="w">` (inline-block, `white-space:pre`) and animates the spans independently:

```js
const k = eo(p(t, t0 + i * w, t0 + i * w + d))      // w = .1 stagger, d = .45 per word
sp.style.opacity = k
sp.style.transform = `translateY(${(1 - k) * 0.35 * fs}px) scale(${lerp(1.3, 1, k)})`
// exit: ko = p(t, out, out + outD); whole line opacity 1-ko, scale lerp(1,.96,ko), translateY(-40*SC*ko)
```
Emphasis is markup: `<span class="red">` for #d8463a and `<i>` for gold #e8b43a in Playfair Display italic (the italic is a separate font file, `PFI`). `slam()` re-tokenizes only when the text or size changes, so calling it every frame is cheap. Centre alignment measures `el.offsetWidth`, so the fonts must be loaded before the first frame; the demo calls `document.fonts.load` for that.

If two scenes reuse the same element, only call `slam()` for the scene that is active: it hides the element whenever `t` is outside its own window.

## Numbers that matter
| | |
|---|---|
| Font | Playfair Display 700, line-height 1.02, letter-spacing -0.01em |
| Size | 128px on 1920 wide, 100px on 1080 wide (times the layout scale) |
| Word stagger / duration | 0.1s / 0.45s, `eo` (cubic ease-out) |
| Word start | scale 1.3, translateY 35% of font size |
| Exit | 0.35s, scale 0.96, up 40px |
| Colours | text #f3f1ea, red #d8463a, gold #e8b43a |
| Timing | line 1 at 0.25s, line 2 at 1.25s, out at 4.15s; "not fiction" at 4.8s, "true story" at 6.75s |

## Sound

## Adapt it
- The text and which word is red or gold.
- `HF`, the headline size; a longer hook drops it to 0.78x (wide) or 0.64x (tall) for a longer line.
- `w` (stagger) and `d` (word duration) for a faster or slower build.
- The colour classes `.h .red` and `.h i`.

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. Playfair Display (SIL Open Font License, from Google Fonts) is copied into `code/fonts/` because the serif headline is half the look. The demo uses the system font stack.
- `code/fonts/` holds the fonts the demo loads.
