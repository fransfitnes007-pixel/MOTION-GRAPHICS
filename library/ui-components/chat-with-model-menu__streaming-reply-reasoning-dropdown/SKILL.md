---
name: chat-with-model-menu-streaming-reply-reasoning-dropdown
description: White full-screen AI chat: a question is typed into the pill composer and sent, "Thinking..." shimmers, the answer streams in at about 160 characters a second, then the reasoning-level dropdown opens and a new level is picked. Use for ai chat, chatgpt and chat screen beats in app promos.
---

# Chat with model menu

**Code name:** Streaming reply, reasoning dropdown.

## What you see
White page, 540 wide in the source preview. Three earlier exchanges sit on screen: grey user pills on the right (18px radius, 15px text) each with copy and pencil icons under them, plain unboxed assistant text on the left with copy and regenerate icons. At 0.5s a question starts typing into the pill composer at the bottom ("Ask anything", plus on the left, mic and "Extra High" with a chevron on the right); the mic becomes a black send arrow. At 2.3s it sends: the question lands as a new grey pill (fades in 0.22s, rises 8px) and a grey "Thinking..." with a light sweep appears where the answer will go. At 3.1s the answer streams in, about 160 characters a second, two paragraphs, and the copy/regenerate icons fade in when it ends (4.9s). At 5.7s the "Extra High" button opens a small white menu above it (Intelligence: Instant, Medium, High, Extra High with a tick, Pro, then GPT-5.6 Sol with an arrow); at 6.5s High is hovered, at 7.1s it is picked, the menu fades and the button now reads High. 9.5s loop.

## When to use it
Any "ask the AI" beat in an app promo: the whole conversation fits one phone screen. The typing, send, thinking and streaming beats carry the shot; the model menu at the end is the proof that the app lets you choose how hard it thinks. Wrong for dark or colourful brands unless you re-tint the tokens: it is deliberately plain white and grey.

## How it works
Everything is a function of `t`. The conversation is real DOM flow; the new question and answer are measured and the list is scrolled with `translateY` so it follows the bottom (a 0.45s `eo5` ease when the question lands). The stream is `slice(0, floor((t - start) * cps))` over both paragraphs. "Thinking..." is grey text with a moving gradient clipped to the letters. The menu is `opacity` and `scale(.95 -> 1)` over 0.15s with its origin at the bottom right, like the Radix dropdown it was read from.

## Numbers that matter
| | |
|---|---|
| User pill | bg #f5f5f5, radius 18, padding 7 14, 15px / 22px |
| Assistant text | 15px / 24px, paragraphs 10px apart |
| Spacing | 18px between messages, 36px before a new question |
| Composer | 46px high pill, radius 23, 1px #e5e5e5, shadow 0 1px 2px .05 |
| Menu | radius 14, padding 6, rows 13px with radius 10, 0.15s enter |
| Stream speed | ~164 characters/s (measured 52 mutations in 1.7s), first token 0.69s after send |
| Icon / muted colour | #737373 |

## Sound
A soft tick per sent message; a very quiet keyboard texture under the typing. No sound in the source.

## Adapt it
- `CONFIG.ask`, `CONFIG.reply`, `CONFIG.prior` for the words
- `CONFIG.levels`, `from`, `to` for the dropdown rows
- `CONFIG.cps` for stream speed, `sendAt`, `menuAt`, `pickAt` for the beats
- Shorten `prior` to one exchange if the reel needs bigger type

## Files
- `code/demo.html` self-contained, loops, `?w=1080&h=1920` for 9:16 (a 540-wide phone column), `?w=1280&h=800` for wide.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Chat with Model Menu" by ephraimduncan (https://21st.dev/@ephraimduncan/components/chat-02), MIT. Recreated by eye from the public preview; this demo is original code. Full notices: `THIRD_PARTY_NOTICES.md`.
