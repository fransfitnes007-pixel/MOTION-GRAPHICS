---
name: imessage-typing-bubbles-spring-pop-in-dots
description: "A progress card where an AI reviewer texts what it is doing. A grey iOS-style bubble springs in from its tail corner with three bouncing typing dots, swaps to the message, and finished steps stay behind as check-marked bubbles. Use for AI progress that should feel like a person narrating."
---

# iMessage typing bubbles

**Code name:** Spring pop-in dots.

## What you see
A dark card titled "Reviewing your draft" with a percentage at the right and a thin blue progress bar. Under it, short grey rounded bubbles (`#2C2C2E`, iOS dark-mode received colour) stack from the top. The current step appears first as a small bubble holding three grey dots that bounce in turn. After 450ms the dots fade and shrink away and the step's text, such as "Reading frames and cuts...", pops in at the same corner. When that step completes it becomes a finished bubble with a green check and stays; the list keeps the last three and the oldest drops off. The bar grows .4s per step. At the end the title reads "Review finished".

## When to use it
A long-running AI task with named stages, where a checklist feels cold. Also for any one-off "assistant says something" moment. Keep lines short, since bubbles do not wrap in this layout. Wrong for dense logs, and for anything that needs to read as official rather than friendly.

## How it works
`PopIn` is a framer-motion wrapper: it enters from scale .55, 10px low and transparent, with a stiff spring, and its transform origin is the bubble's tail corner so it grows out of that corner.

```tsx
const spring = { type: 'spring', stiffness: 520, damping: 30, mass: 0.7 }
<motion.div initial={{ opacity: 0, scale: 0.55, y: 10 }} animate={{ opacity: 1, scale: 1, y: 0 }}
  exit={{ opacity: 0, scale: 0.9, y: -6, transition: { duration: 0.15 } }}
  transition={{ ...spring, delay }} style={{ transformOrigin: side === 'left' ? 'bottom left' : 'bottom right' }} />
// dots: animate={{ opacity: [0.35, 1, 0.35], y: [0, -2.5, 0] }} transition={{ duration: 1.1, repeat: Infinity, delay: i * 0.16, ease: 'easeInOut' }}
```
The tail is an inline SVG path in the bubble colour tucked under the bottom corner, flipped with `-scale-x-100` for right-side bubbles. `ThinkBubble` keeps the current message in a ref and shows typing dots before it; changing the key inside `AnimatePresence mode="wait"` plays the exit before the next pop. It also queues updates so each message stays visible for `holdMs` before the next replaces it, and types first only after a pause of twice that.

The demo plays eight stages at 1.1s each with the same spring, exit and dot timings.

## Numbers that matter
| | |
|---|---|
| Bubble | `rounded-[18px]`, `px-3 py-[7px]`, 15px SF text, line height 1.3, tracking `-0.01em`, `#2C2C2E` |
| Tail | 17 by 21 svg, 5px outside the corner |
| Pop-in | spring stiffness 520, damping 30, mass .7, from scale .55 and y 10 |
| Exit | .15s to opacity 0, scale .9, y -6 |
| Dots | 8px, 60% white, gap 5px, 1.1s, offset .16s per dot |
| Typing | 450ms (`typeMs`), message hold 700ms (`holdMs`) in the stage list |
| Bar | `bg-rv-purple`, height 6px, width tween .4s |

## Sound
Silent. A short iMessage-style "pop" on each bubble would match, and a faint typing tick under the dots.

## Adapt it
- Stage lines and how many stay on screen (3 here).
- `typeMs` and `holdMs` for a faster or slower narrator.
- Bubble colour and radius for a different chat style; flip `side` for a right-hand sender.
- The icon on finished bubbles.

## Files
- `code/demo.html` runs on its own and loops in 10s.
