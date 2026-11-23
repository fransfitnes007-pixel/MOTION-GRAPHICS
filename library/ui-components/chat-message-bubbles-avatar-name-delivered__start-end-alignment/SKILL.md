---
name: chat-message-bubbles-avatar-name-delivered-start-end-alignment
description: A chat thread with incoming grey rounded bubbles (avatar left, name above) and an outgoing black bubble on the right with "Delivered" under it. Reach for it for a message list, comments or a chat mock-up. It has no animation of its own; the demo reveals the messages one by one.
---

# Chat message bubbles with avatar, name and Delivered

**Code name:** Start and end aligned message parts.

## What you see
White page, three messages, 96px apart. Incoming messages: a 57 px round avatar at the left, the sender name above the bubble in 22 px medium weight, and a light grey (`#f4f4f5`) bubble with 31px corners except a 10px square corner at the bottom left, where the tail would be. The outgoing message is a near-black bubble aligned to the right edge with a white text and a 10px square corner at the bottom right, and "Delivered" in grey 19px under it, right-aligned.

The 21st.dev page has a still image and no video, so the original does not move. The demo makes each message fade up 14px over 0.4s, 0.8s apart, and "Delivered" fades in just after the second bubble, then the whole thread fades out so it loops.

## When to use it
A support chat, an in-app messenger preview, comments under a post, or the conversation inside a product screenshot. It stops at the bubbles: there is no input, typing indicator or timestamps. For an iMessage-style typing animation see the sibling.

## How it works
A small compound component: `Message` (with `align="end"` to flip it), `MessageAvatar`, `MessageContent`, `MessageHeader` for the name and `MessageFooter` for the status line. The bubble itself is a plain div in the usage example:

```tsx
<div className="w-fit rounded-2xl rounded-bl-md bg-muted px-4 py-2 text-sm text-foreground">...</div>   // incoming
<div className="w-fit rounded-2xl rounded-br-md bg-primary px-4 py-2 text-sm text-primary-foreground">...</div>   // outgoing
```

So the shape is one rounded box with the corner nearest the speaker made square (`rounded-bl-md` or `rounded-br-md`). The demo measures each text, adds 28px each side, and places incoming bubbles from the left edge of the text column and outgoing ones from the right edge. Names are placeholders; the original handles are replaced.

## Numbers that matter
| | |
|---|---|
| Canvas | 960 by 720 |
| Bubble | 62px tall, 31px radius, 10px at the speaker corner, 28px side padding |
| Text | 26.5px, incoming `#111` on `#f4f4f5`, outgoing white on `#171717` |
| Avatar | 57px circle, 14px gap to the bubble column at x 199 |
| Name | 22px medium, 36px above the bubble |
| Caption | 19px `#76767c`, 9px below the outgoing bubble |
| Demo reveal | starts 0.35s, 0.8s apart, 14px rise over 0.4s |

## Sound
Silent.

## Adapt it
- `messages`: side, name, text and avatar for each line; add or remove entries and update the `Y` anchors.
- `incomingBg`, `incomingText`, `outgoingBg`, `outgoingText` for the palette (a blue outgoing bubble gives an iMessage look).
- `firstAt`, `gap`, `riseMs`, `rise` for the reveal, or set `riseMs` to 0 for a static thread.

## Files
- `code/demo.html` runs on its own and loops. All imagery is CSS or SVG placeholder.
- `media/poster.jpg` is a preview image showing the component.

## Credit
Idea: "Message" by shadcn on 21st.dev (https://21st.dev/@shadcn/components/message), MIT. This demo is an original recreation written from the public preview.
