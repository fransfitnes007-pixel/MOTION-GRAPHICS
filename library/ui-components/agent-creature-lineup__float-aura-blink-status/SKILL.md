---
name: agent-creature-lineup-float-aura-blink-status
description: "Eight small SVG creatures in a row on a glass stage. One at a time is running, with pulsing rings and a bobbing smile; finished ones settle with a check badge; pending ones sit dimmed. A status line below swaps text as the run advances. Use to show a team of AI agents working through a pipeline."
---

# Agent creature lineup

**Code name:** Float, aura and blink by status.

## What you see
A wide dark glass card with a faint blue grid and a soft glow at the top edge. Eight characters stand in a row, 88px each, every one a different silhouette (kite, rounded square, eye ellipse, blob, tall capsule, flame, gear ring, hexagon) in its own colour, with a face: two eyes that blink together every 5.5 seconds and a mouth. Below each: its name in bold and its title in tiny capitals in its colour. Every 2.5 seconds the next agent starts running. A running agent bobs 7px, tilts 1.5 degrees either way, grins and wobbles its smile, and sends out two rings that grow 35% and fade. The gear one spins its teeth. Agents that have finished keep a calm smile and get a round check badge at the bottom right that springs in. Agents not yet reached are at half opacity with a flat mouth and no highlights in the eyes. Under a thin fading divider a line reads "Name  what it is doing...", swapping with a fade and a 6px slide each step; after the last agent it says the campaign is assembled and the loop restarts.

## When to use it
A product page showing a multi-agent pipeline, an onboarding wait screen, any place where several workers take turns and you want each one to read as a character. Silhouettes give the identity, so it works with plain flat colours.

## How it works
State comes from one integer, `step`. For agent `i`: `i < step` is COMPLETED, `i === step` is RUNNING, otherwise PENDING. Each state selects a different float animation, aura, mouth path and badge. All motion is framer-motion keyframes:

```tsx
animate={running ? { y: [0, -7, 0], rotate: [0, 1.5, 0, -1.5, 0] } : { y: [0, -4, 0] }}
transition={{ duration: running ? 1.6 : 4 + (shape % 3), repeat: Infinity, ease: 'easeInOut' }}
// rings: animate={{ scale: [1, 1.35], opacity: [0.6, 0] }} transition={{ duration: 1.4, repeat: Infinity, ease: 'easeOut' }}, second ring delay .7
// blink: animate={{ scaleY: [1, 1, 0.1, 1, 1] }} transition={{ duration: 4, times: [0, .45, .5, .55, 1], repeat: Infinity, repeatDelay: 1.5 }}
// badge: initial={{ scale: 0 }} animate={{ scale: 1 }} transition={{ type: 'spring', stiffness: 400, damping: 18 }}
```
The pending creatures float slowly with a period of 4, 5 or 6 seconds depending on their index, so the row never bobs in unison. The ground glow under each is a small blurred ellipse whose alpha is .15 pending, .55 running, .35 done. The status line is an `AnimatePresence mode="wait"` pair of `motion.p`, so the old text finishes leaving before the new one comes in.

Demo changes: the step is 1.4s instead of 2.5s so the loop is 12.6s, the ground glow is a radial gradient rather than a blur, and the mouth morph is interpolated between the two path strings from the source.

## Numbers that matter
| | |
|---|---|
| Step | 2500ms per agent, 9 steps (8 agents plus an all-done beat) |
| Character | 88px box, body svg 78% of it, viewBox 100 |
| Running | bob 7px, tilt 1.5deg, 1.6s; rings 1.4s, second delayed .7s; mouth `M40 60 Q50 70 60 60` and `M40 61 Q50 66 60 61`, .8s |
| Done | smile `M41 61 Q50 68 59 61`, badge 28px with `0 0 12px` glow in the agent colour |
| Pending | opacity .5, flat mouth `M42 62 L58 62` |
| Stage | `rounded-3xl`, fill `rgba(13,13,26,.85)`, border `rgba(139,92,246,.15)`, grid 32px at 5% |
| Colours | `139,92,246` `16,185,129` `245,158,11` `236,72,153` `59,130,246` `239,68,68` `20,184,166` `99,102,241` |

## Sound
Silent. A soft pop on each badge would pair with it.

## Adapt it
- The names, colours and `thinking` lines.
- `STEP_MS`: how long each agent runs.
- Silhouettes: change the `BodyShape` paths, keep the face in the same place.
- Add a FAILED state: muted red, a short shake and a cross badge (in the source component).

## Files
- `code/demo.html` runs on its own and loops in 12.6s.
