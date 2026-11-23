---
name: email-link-strikethrough-scalex-red-bar
description: "A pitch-email card whose link is crossed out by a red line that draws itself. Use it to reject the old way of sending work, with the dark editorial look."
---

# Email with struck-out link

**Code name:** ScaleX red bar and tinted link chip.

## What you see
A dark email composer, 690 by 470 with a traffic-light header, slides up 80px and swings in from the right (rotated 14 degrees about the vertical axis, easing to 6 degrees) between 0.2s and 0.9s. The message reads "To", "Subject", a greeting and a link in a rounded grey chip. As the link is spoken (2.3s) a 4px red bar draws from the left edge of the chip to the right over 0.76s with ease in and out, and the chip's background turns from 6% white to 12% red. At 3.1s the whole card swells 30%, blurs and fades.

## When to use it
A beat that rejects the usual way of doing something (the link nobody clicks, the PDF, the attachment). The red bar is a hand-drawn "no" that is more tasteful than a cross. Best on the dark stage; on light backgrounds, use the crossed-out document skill instead.

## How it works
The bar is a child of the link chip, always present, with `transform-origin: 0 50%` and a scaleX driven by time:

```js
strike.style.transform = `scaleX(${eio(seg(t, LINK_A, LINK_B + .25))})`
chip.style.background = t > LINK_A ? `rgba(239,68,68,${.12 * seg(t, LINK_A, LINK_A + .3)})` : 'rgba(255,255,255,.06)'
card: perspective(1800px) translateY((1 - mi) * 80px) rotateY((-14 + 8 * mi)deg) scale(1 + mo * .3)
```

The card's entry and exit share the same `opacity` multiplication, so there is no separate in and out state. The bar spans the word from the start of the link text to just after its last word, so it finishes with the voice.

## Numbers that matter
- Card: 690 by 470, radius 24, `#12121c`, 1px outline at 9%; header 58px.
- Entry: `eo5` over 0.7s, 80px, rotateY -14 to -6.
- Strike: 4px `#ef4444`, `eio` over 0.76s; chip tint 12% red over 0.3s.
- Exit: `eio` over 0.45s, scale 1.3, blur 10px.

## Sound

## Adapt it
- The email text, subject and the link text (neutral placeholders here).
- `LINK_A`, `LINK_B`: the two words the bar should draw between.
- Bar colour (red = reject; swap it for a tick colour to approve).
- Card position and tilt direction.

## Files
- `code/demo.html` runs on its own and loops. The demo uses the system font stack; SF Pro Display is a good match. The email text is neutral placeholder copy.
