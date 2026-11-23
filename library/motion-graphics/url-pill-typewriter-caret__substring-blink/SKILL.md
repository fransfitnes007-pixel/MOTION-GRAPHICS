---
name: url-pill-typewriter-caret-substring-blink
description: "A big address bar that types its text and blinks a caret. Use it to land a website address as a call to action, with keystroke sounds underneath."
---

# URL pill typewriter with caret

**Code name:** Substring slice with a blinking caret.

## What you see
A pill 800 by 120 with fully round ends, in frosted dark glass with a hairline outline, fades up 30px into place. A grey lock icon sits at its left. After a beat, white 56px bold text types out "yourname.com" at about 12 characters in 0.54s, with a lavender caret, 5px wide and 58px high, trailing it. Once the text is complete the caret blinks at 3Hz and does not go away. A light-stage version is the same pill in frosted white with dark text and an indigo caret.

## When to use it
Landing a URL as the last thing a viewer has to remember. Time the typing to the spoken address, and use keyboard samples. Keep the address short: the typing is a straight line, so more than 15 characters starts to drag.

## How it works
Like every typed element in this library, the text is a slice of the final string chosen by progress.

```js
const n = Math.round(clamp(seg(t, YOUR - .05, DOMAIN + .1)) * dom.length)
text.textContent = dom.slice(0, n)
caret.style.opacity = (Math.floor(t * 3) % 2 || n < dom.length) ? 1 : 0   // always on while typing, then blinks at 3Hz
```

The caret is a real element, so its blink is a function of `t` too, and the loop shows it. The pill itself is `rgba(255,255,255,.07)` with `backdrop-filter: blur(24px)`; it needs the dot grid or glow behind it to look like glass.

## Numbers that matter
- Pill: 800 by 120, radius 60, padding 0 44px, gap 22px; text 56px weight 700, letter-spacing -.02em.
- Fade-in: `eo5` over 0.4s, 30px rise, scale .94 to 1.
- Typing: 12 characters over 0.54s (for example 19.0s to 19.59s).
- Caret: 5 by 58px, `#a5b4fc` on dark, `#5b5ce6` on light, blink `floor(t*3) % 2`.

## Sound
Keystroke samples under the typing work well.

## Adapt it
- The string and the typing window.
- Pill size, text size and colours; flip to the light version by swapping the glass class and text colour.
- Caret blink rate (`t * 3`).
- Lock icon: remove it for non-URL text.

## Files
- `code/demo.html` runs on its own and loops. The address is a neutral placeholder.
