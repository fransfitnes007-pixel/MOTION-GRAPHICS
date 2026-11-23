---
name: dark-message-input-bar-send-stop-button-states
description: "A compact dark chat input: rounded box, grey placeholder, round arrow button at the bottom right. Use it as the composer in a chat or messaging panel."
---

# Dark message input bar

**Code name:** Send stop button states.

## What you see
The preview clip is 1.9s and nothing moves in it. It shows a near-black page with a dark grey rounded box, about 420 by 90 px in the poster, with the grey placeholder "Send a message..." at the top left and a small dark circle with a dim grey up arrow at the bottom right. That is the ready state with no text, so the send button is disabled. The usage example passes `status="ready"`, `onSend` and `onStop`.

The demo adds the states the props point to, and these are my reading of them, not something seen in the clip: typing a message at 14 characters a second, the button turning white once there is text, a press and send at 3.9s, then a white button with a stop square for 1.8s (status streaming), then back to the resting state.

## When to use it
The message field of a chat panel, support inbox, or internal messaging screen. Plain on purpose; pick it when you want the quiet version. For toolbar modes see the AI prompt box skill.

## How it works
Presentation only. The button colour is a mix between dark grey (no text) and near-white (has text), `eo` over 0.15s, and a scale dip to 86% for 0.14s when sent. While `status` is streaming the arrow cross-fades to a stop square. The caret is a 2px bar placed after the measured text width and blinks every 0.5s.

```js
on = hasText ? eo(clamp((t - typeStart)/.15)) : streaming ? 1 : 0
send.background = mix(#262626, #e8e8ea, on)
```

A caption under the box names the current status; it is a demo label and not part of the component.

## Numbers that matter
| | |
|---|---|
| Box | 672x144 here, `#171717`, 1px `#2a2a2a`, 24px radius |
| Placeholder | 23px, `#8f8f95` |
| Button | 52px circle, 20px from the corner, dim `#262626` with `#555` arrow, active `#e8e8ea` with `#111` arrow |
| Timing | type from 1.1s at 14 chars/s, send 3.9s, stop state 1.8s, loop 8s |

## Sound
Silent.

## Adapt it
- `placeholder` and `message`.
- `bar` size; at a narrow width reduce the text size in the CSS.
- `typeStart`, `charsPerSec`, `sendAt`, `streamSec`.
- Swap the colours in the CSS block for a light version.

## Files
- `code/demo.html` runs on its own and loops. Everything is read from the `CONFIG` object at the top of the script.
- `media/poster.jpg` is one frame of it.

## Credit
Idea: "Input Bar" by 21st on 21st.dev (https://21st.dev/@21st/components/input-bar), MIT. This demo is an original recreation written from the public preview.
