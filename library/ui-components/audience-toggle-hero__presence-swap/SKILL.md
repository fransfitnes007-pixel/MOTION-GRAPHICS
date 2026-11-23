---
name: audience-toggle-hero-presence-swap
description: "A two-option pill toggle in the nav that swaps the whole hero (eyebrow, headline, sub, video, buttons) between two audiences with a quick fade-up. Reach for it when one page has to speak to two buyers, such as teams and individuals."
---

# Audience toggle hero

**Code name:** Presence swap.

## What you see
A frosted segmented control sits in the middle of the nav: "For teams" is selected (black pill, white text). Under it a centred eyebrow, a 60px headline and a lede. A pointer moves to "For individuals" and taps. The current copy fades out while moving up 8px (.3s), then the new copy fades in from 10px below (.3s). The black pill jumps to the other segment a beat after the tap, the video frame gets a new tint because the player is remounted, and the two buttons and the small reassurance line change. A second tap swaps it back.

## When to use it
One landing page, two audiences, one URL. A video sales page is the natural fit. Wrong when the audiences need different pages for search, or when there are more than three options (use tabs or a menu).

## How it works
State holds the audience key. A `key` on the copy block makes React treat each audience as a new element, and `AnimatePresence mode="wait"` plays the exit before the enter:

```tsx
<AnimatePresence mode="wait">
  <motion.div key={a.key} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }}
    exit={{ opacity: 0, y: -8 }} transition={{ duration: 0.3 }}>
```

The toggle itself has no sliding indicator: the active button just gets `bg-ink text-white shadow-pill` and the others `text-ink-2`. Picking an option also calls `history.replaceState` to `/teams` or `/individuals`, and the page reads the path on load, so each audience has a shareable link. The `VslPlayer` has `key={audience + video.src}` so switching audiences restarts the video.

The demo cannot reproduce the router, so it draws the pointer and the swap as a function of time. The demo hero video box is narrowed to 768px (the live one is up to 1024) so the buttons below it fit in the frame.

## Numbers that matter
| | |
|---|---|
| Toggle | rounded-full bg-white/70 p-1, buttons px-4 py-1.5 text-sm font-medium |
| Exit | opacity 1 to 0, y 0 to -8, .3s |
| Enter | opacity 0 to 1, y 10 to 0, .3s, starts after the exit finishes |
| Headline | 60px / 1.05, semibold, -.02em, `text-balance` |
| Default audience | set in config; path `/teams` or `/individuals` overrides it |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The two audiences: tab labels, eyebrow, headline, sub, CTA labels and links.
- Swap time and distance (.3s, 10 and -8px) for a faster or slower feel.
- Add a third audience by adding an item; the segmented control grows by itself.
- Give each audience its own video through the optional `video` field.

## Files
- `code/demo.html` runs on its own and loops. Photos and logos are CSS placeholders; copy is placeholder text.
