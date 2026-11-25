---
name: ask-bar-greeting-composer-word-blur-in-dock-drop
description: Dark navy page with a breathing blue glow: a greeting blurs in word by word above a pill ask bar; picking a model, typing and sending drops the bar to the bottom and an answer arrives under a spinning sparkle. Use for ai search bar, prompt bar and ask ai beats in app promos.
---

# Ask bar greeting composer

**Code name:** Word blur-in, dock drop.

## What you see
A #0e0f14 page with a deep blue oval glow in the middle that slowly breathes. The words "What shall we look into today?" blur in one at a time (each 0.6s, 70ms apart: 8px up, 4px blur to sharp). Below, a grey #1f1f1f pill bar: plus, placeholder "Ask Qalam", the model name "Swift" with a chevron, a mic. At 1.9s the model chip opens a rounded menu above the bar (Swift ticked, Deep, Scholar, each with a grey one-line description); at 3.3s Deep is picked and the chip reads Deep. From 3.9s "Plan my week" types in, the mic becomes a white circle with an up arrow (pops in with a small overshoot). At 5.4s it sends: the greeting vanishes, the bar jumps to the bottom, the question sits top right in a grey bubble, a blue four-point spark spins beside three bouncing dots, the arrow is now a stop square. The reply fills in, the spark stops and "Deep" appears under it. 11s loop.

## When to use it
The "ask anything" home screen of an AI app, and the beat where the first question is sent. The blur-in greeting is also useful by itself as a heading reveal on dark. Pair with a real answer card afterwards.

## How it works
Greeting word i: `e = cubic-bezier(.2,.7,.2,1)(seg(t, .12 + .07i, .72 + .07i))`, then `opacity = e`, `translateY(8px * (1 - e))`, `blur(4px * (1 - e))`. The glow is a radial gradient (`46% 44% at 53% 56%`, #1b2b6e to transparent at 74%) on a layer bigger than the page. Menu: `opacity` 0 to 1 plus a 6px rise over 0.16s. Send button: scale from .6 with `cubic-bezier(.3,.7,.3,1.4)` over 0.2s. Dots: 7px, 5px apart, 1s loop with 0.15s stagger, lift 3px and drop to 30% opacity. Spark: `rotate` one turn per 2.4s while the reply is pending. Bar position switches the moment a message is sent, as in the source.

## Numbers that matter
| | |
|---|---|
| Page / bar | #0e0f14 / #1f1f1f, bar 64px high, radius 32 |
| Ink / muted / accent | #e8eaed / #9aa0a6 / #8ab4f8 |
| Greeting | 28px, letter-spacing -0.01em, bottom margin 48px |
| Menu | #282a2c, radius 18, padding 8, 288px wide, title 15px/500 + 13px muted line |
| Glow | breathes 14s: scale 1.06, up 1.5%, opacity .86 |
| User bubble | #2b2c30, radius 22 22 6 22, padding 12 18 |

## Sound
A faint swell as the greeting resolves; a short "send" tick; nothing during the stream.

## Adapt it
- `CONFIG.greeting`, `placeholder`, `ask`, `reply`
- `CONFIG.models` names and descriptions, `pickAt`
- Glow colours in the `.ab-glow` gradient for a brand tint
- `cps` for reply speed (a guess, not measured)

## Files
- `code/demo.html` self-contained, loops, `?w=1080&h=1920` for 9:16 (a 540-wide phone column), `?w=1280&h=800` for wide.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Ask Bar" by ham7a311 (https://21st.dev/@ham7a311/components/ask-bar), MIT. Recreated by eye from the public preview; this demo is original code. Full notices: `THIRD_PARTY_NOTICES.md`.
