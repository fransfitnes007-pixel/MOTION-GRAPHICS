---
name: contact-card-with-mouse-glow-and-particles-pointer-tour-spotlight
description: "A rounded white call-to-action card: a logo with four grey skill chips around it that light up in turn as a red pointer tours them, a bold 'Any questions about Design?' line, and Book a call, mail and WhatsApp buttons. Moving the mouse over it brings a green spotlight and rising dots. Reach for it for a contact or booking block."
---

# Contact card with mouse glow and drifting dots

**Code name:** Pointer tour and spotlight.

## What you see
A card 704 by 787 in a 1280 by 1092 frame on a faint dotted page, 44px corners, 1px `#e2e8f0` border. In the top half, a small black D-shaped logo in the middle and four pill chips (Branding, Graphic Design, Web Application, UI-UX) in grey at 40 to 50% opacity. A small red arrow pointer moves between them: it sits at Branding (that chip goes to full opacity and dark text), glides 0.5s to Graphic Design, then Web Application, then UI-UX, then back to Branding, each stop 1.15s apart (one lap is 4.6s, two in the demo). Below, a 45px bold title, a 30px grey line, and a black 'Book a call' button next to two outline square buttons (mail, WhatsApp green). When the real mouse enters the card, in about 0.4s a pale green radial glow (340px radius, up to 34% opacity) tracks it, a brighter green rim lights the card border near it, and 200 small grey dots that were at 10% opacity come up to full and drift upward at about 12px a second. When the mouse leaves they fade out over about a second.

## When to use it
A contact, booking or 'ask me' block where the card should feel alive but the buttons stay plain. The glow and dots only appear on hover, so on touch screens it is just the chips and pointer. Keep the tour to four or five chips.

## How it works
Two separate things run. First, the pointer tour is a framer-motion `useAnimate` sequence: the pointer moves with `ease: easeInOut` over 0.5s, starting 0.5s after the previous chip finished lighting, and each chip fades from 0.4 to 1 over 0.3s as the pointer arrives and back to 0.4 over 0.1s as it leaves; the demo copies those times exactly (stops at 0.8s, 1.9s, 3.0s, 4.1s). Second, the highlighter: a group tracks the mouse and each item draws a radial gradient at that point plus a border glow; a particle canvas (200 dots, vy -0.2) switches from 10% to 100% opacity with a 1s transition. The demo scripts a mouse path and works out a smoothed hover value from whether the mouse is inside the card, which drives glow and dots. The pointer label 'Ali' in the source is invisible in the preview (its background class is not defined), so the demo leaves it out.

## Numbers that matter
- Pointer stops (box px): (200,60), (50,102), (224,170), (88,198); lap 4.6s
- Chip: border `#94a3b8`, fill `#e2e8f0`, 12px text, opacity .4/.5 resting, 1 lit
- Glow `rgb(150,225,120)`, radius 340px, 34% at the centre, in 0.35s, out 0.55s
- 200 particles, 0.8 to 2.4px, `#555`, drift about 12px per second
- Card 704 by 787, radius 44px; title 45px bold; buttons 76px

## Sound
Silent.

## Adapt it
- `title`, `sub`, `button` copy and the `tags` chips (each takes left/right/top/bottom).
- `stops`: the pointer's coordinates, one per chip.
- `glow` colour and `glowRadius` for a different spotlight.
- `particles`, `particleColor`, `particleSpeed`; and `cursorPath` to retime the scripted mouse.

## Files
- `code/demo.html` runs on its own, loops in 9.2s, and has a `CONFIG` block at the top of the script.

## Credit
Idea: "Highlighter" by designali-in on 21st.dev (https://21st.dev/@designali-in/components/highlighter), MIT. This demo is an original recreation written from the public preview.
