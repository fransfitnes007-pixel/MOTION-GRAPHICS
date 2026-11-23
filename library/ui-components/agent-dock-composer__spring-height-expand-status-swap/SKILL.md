---
name: agent-dock-composer-spring-height-expand-status-swap
description: "A compact dark dock for talking to an AI agent: avatar, name, a status line that slides between Ready, Working and Listening, and Voice and Chat buttons with key hints. Chat opens a text box that grows upward out of the bar. Reach for it as the persistent assistant control in an app."
---

# Agent dock composer

**Code name:** Spring height expand, status swap.

## What you see
A 520px wide, 16px-radius bar, near-black (`neutral-950`) with a hairline white 10% border and a deep shadow, pinned near the bottom of the page over other content. Left: a 36px rounded avatar, the agent's name and a 12px grey status line. Right: two buttons, each an icon, a label and a small square key chip: "Voice  V" and "Chat  C".

- 1.4s: the cursor clicks Chat. The button turns into "Send" with a paper plane. A text area grows upward from the bar (0 to 132px, 0.3s, `cubic-bezier(.22,1,.36,1)`) with a close X, and the bar stays fixed at the bottom.
- 2.1 to 4.6s: text types in.
- 5.4s: Send. The composer collapses back down and the status changes from "Ready" to "Working..." with the old text sliding up 6px and fading while the new one slides in from below in 0.16s.
- 8.6s: back to "Ready". 9.4s: Voice is clicked. The button fills violet and reads "Stop", the status reads "Listening...". 12.0s: it is stopped.

## When to use it
Any app with a persistent assistant that needs one small control, not a chat page. The upward growth is the useful trick: the bar never moves, so it can be fixed to the bottom of a screen. It is the wrong shape for a long conversation. Put the transcript above it, in the `children` slot.

## How it works
```tsx
<div className="flex w-full flex-col-reverse overflow-hidden rounded-2xl border border-white/10 bg-neutral-950 p-2 ...">
  <div className="flex items-center gap-3">{/* avatar, name, status, buttons */}</div>
  <motion.div animate={{ height: mode === "composing" ? 132 : 0, opacity: mode === "composing" ? 1 : 0 }}
    transition={shouldReduceMotion ? { duration: 0 } : { duration: 0.3, ease: [0.22, 1, 0.36, 1] }} className="overflow-hidden">
```
- `flex-col-reverse` puts the bar last in the DOM and first visually at the bottom, so extra height pushes upward.
- Status: `AnimatePresence mode="popLayout"` with `initial {opacity 0, y 6}`, `animate {opacity 1, y 0}`, `exit {opacity 0, y -6}`, `duration 0.16, ease easeOut`, keyed by the status string. `popLayout` takes the leaving line out of flow so the two lines overlap instead of pushing each other.
- Focus follows mode through an effect, and the hidden textarea gets `tabIndex -1` so the first Tab does not land in an invisible box. Enter sends, Shift+Enter is a new line, Escape closes.
- Reduced motion sets the height transition to `duration: 0`.

The demo reproduces the height and status animations from the same curves as functions of time, with a scripted cursor.

## Numbers that matter
| | |
|---|---|
| Dock | 16px radius, padding 8px, border white 10%, bg `#0a0a0a` |
| Composer | 132px open (textarea 112px), 0.3s, `[0.22, 1, 0.36, 1]` |
| Status swap | 0.16s easeOut, 6px in, 6px out |
| Buttons | 36px high, 8px radius, key chip 24px, active fill `#8b5cf6` |
| Avatar | 36px, radius 12px |

## Sound
Silent. A short mic-on tick would go well with the Listening state.

## Adapt it
- Name, avatar and the three status strings.
- Accent for the active (listening) state.
- `132` for composer height, and the dock width.
- Drop the Voice button by omitting the toggle handler, as the source does.

## Files
- `code/demo.html`: runs on its own.
