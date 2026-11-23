---
name: command-palette-icon-swap-staggered-rows
description: "A dark command palette that drops in from above with its rows fading up one after another. Typing swaps the search icon for a send icon with a vertical slide and narrows the list; the selected row is tinted violet with an enter arrow; a hint footer shows the shortcut. Use for a Cmd-K launcher."
---

# Command palette

**Code name:** Icon swap, staggered rows.

## What you see
The page dims to 60% black with a 2px blur. A 576px dark card (16px radius, deep shadow) drops in from 12px above at 98% scale on a firm spring. Its input row says "What's up?" with a grey magnifier at the right. The list below is grouped under tiny letter-spaced headings (Navigate, Actions, Settings), and each row fades up 8px in turn, .03s apart. A row has a lilac icon, a medium-weight label, a grey hint, then at the right a monospace shortcut chip and the group name. The highlighted row has a 15% violet fill and shows a small return arrow. Type a letter and the magnifier slides down and out while a paper-plane icon slides in from above; the list narrows to matches and drops empty groups. Arrow keys move the highlight, Enter runs the command and the card leaves with a quick fade up. The footer reads "Press ⌘ K to open commands" and "ESC to cancel".

## When to use it
A global launcher for an app with many screens and actions, opened by a hotkey or a search button. The icon swap tells the user "this is now a request", which suits an assistant-style search; for plain navigation search you can drop it. Needs a real fuzzy-search layer behind it (cmdk handles that).

## How it works
`cmdk` provides input, grouping, keyword matching, arrow navigation, wrap-around and Enter. Framer-motion provides the three pieces of motion:

```tsx
// the card
initial={{ opacity: 0, y: -12, scale: 0.98 }} animate={{ opacity: 1, y: 0, scale: 1 }} exit={{ opacity: 0, y: -8, scale: 0.98 }}
transition={{ type: 'spring', stiffness: 400, damping: 32 }}
// the icon swap, AnimatePresence mode="popLayout"
<motion.div key="send"   initial={{ y: -14, opacity: 0 }} animate={{ y: 0, opacity: 1 }} exit={{ y: 14, opacity: 0 }} transition={{ duration: 0.2 }} />
<motion.div key="search" initial={{ y: -14, opacity: 0 }} animate={{ y: 0, opacity: 1 }} exit={{ y: 14, opacity: 0 }} transition={{ duration: 0.2 }} />
// each row's content: variants hidden { opacity: 0, y: 8 } to show { opacity: 1, y: 0, transition: { duration: .2 } }, delay: Math.min(i, 8) * 0.03
```
The scrim and card share an outer `motion.div` that fades in .15s. The selected-row styling comes from cmdk's `data-selected` attribute (`data-[selected=true]:bg-rv-purple/15`), so it needs no state. Page scroll is locked while open and Escape closes. `shouldFilter={false}` lets you pass pre-filtered results for async search.

The demo types "pay" at .22s a key, filters with a simple substring match on label and hint (cmdk's fuzzy match is more forgiving), moves the highlight with ArrowDown and closes on Enter.

## Numbers that matter
| | |
|---|---|
| Card | `max-w-xl` 576px, radius 16px, `bg-rv-card #0d0d1a`, border `#1a1a2e`, shadow `0 28px 56px -24px rgba(0,0,0,.9)`, top offset 12vh |
| Open | spring stiffness 400, damping 32, from y -12 and scale .98 |
| Scrim | `bg-black/60`, `backdrop-blur-[2px]`, .15s |
| Input | height 48px, 14px text, icon 16px at the right |
| Icon swap | .2s, y -14 to 0 in, 0 to 14 out |
| Rows | `px-3 py-2`, 14px, selected `bg-rv-purple/15`, stagger `min(i, 8) * .03s` |
| Group heading | 10px semibold uppercase, tracking `.12em`, muted |

## Sound
Silent. A soft keyboard tick per letter fits.

## Adapt it
- The item list: label, hint, group, icon, shortcut.
- The input icon pair, or remove the swap.
- Placeholder text and footer copy.
- Selected row colour via `--rv-purple`.

## Files
- `code/demo.html` runs on its own and loops in 7s.
