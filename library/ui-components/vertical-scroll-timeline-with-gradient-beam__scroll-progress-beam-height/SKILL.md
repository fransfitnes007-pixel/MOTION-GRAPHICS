---
name: vertical-scroll-timeline-with-gradient-beam-scroll-progress-beam-height
description: "A scrolling timeline: a faint rail with grey dots, big grey entry titles (2024, Early 2023, Changelog), a line of text and a 2 by 2 image grid under each, and a gradient beam on the rail that lengthens as the page scrolls. Reach for it for about pages, changelogs and company histories."
---

# Vertical timeline with a scroll-following gradient beam

**Code name:** Scroll-progress beam height on a rail.

## What you see
A white page. At the top, a small heading "Changelog from my journey" and two grey lines of intro. Below it a vertical rail 2 px wide at x 164 that fades out at both ends, with a 34 px grey dot for each entry. Each entry has a 52 px bold grey title beside its dot, one or two paragraphs (22 px, near black), sometimes a checklist with green tick emojis, and a 2 by 2 grid of 443 by 148 px image cards with rounded corners and a soft ring shadow.

On the rail sits a beam, 2 px wide: its lower end is purple (`#a855f7`), 10% of the way up it is blue (`#3b82f6`), and above that it fades to nothing. Its lower end stays about halfway down the screen, so the beam lengthens as you scroll down and shortens as you scroll back up. In the preview the page scrolls down for 4.6s, stops at the end for about a second, then scrolls back to the top, with easing at both ends.

## When to use it
A company history, a personal about page, a product changelog, a roadmap. It needs a tall page and scrolling, so it does not suit short content. The beam gives a sense of reading progress without a separate progress bar.

## How it works
The beam is a div whose height comes from scroll position, with the gradient pointing upward so the bright end is at the bottom:

```js
lead  = scrollY + viewportH * 0.5              // page y the beam reaches
h     = clamp(lead - railTop, 0, railHeight)
beam.style.height  = h + 'px'
beam.style.opacity = clamp(h / (railHeight * 0.1))      // fades in over the first 10%
background: linear-gradient(to top, #a855f7 0%, #3b82f6 10%, transparent 100%)
```

The original does this with framer-motion's `useScroll` and `useTransform`, and in its wide layout the titles are sticky next to the dots. The usage example passes an array of `{ title, content }` items where content is any JSX, so entries can hold anything. In the demo the page position is keyframed in `CONFIG.scroll` instead of following a real scroll, and the dot and title sit on the same line.

The demo's images are drawn placeholders (a light and a dark UI mock-up), and the name in the copy is replaced with "Acme".

## Numbers that matter
| | |
|---|---|
| Stage | 1280 by 1070 box; page is about 2540px tall, so 1473px of scroll |
| Rail | x 164, 2px, grey `#e4e4e7`, fades to transparent over the first and last 10% |
| Dots | 34px, `#e9e9ec` with a 1px `#d6d6da` ring |
| Titles | 52px bold `#6b6b6b`, text starts at x 251 |
| Images | 443 by 148, 13px radius, 28px column gap, 29px row gap |
| Beam | 2px, purple to blue to transparent, lower end at 50% of the viewport height |
| Scroll | down 0.8 to 5.4s, hold, up 6.6 to 9.4s |

## Sound
Silent.

## Adapt it
- `entries`: titles, paragraphs, optional `list`, and the image style; edit `TY` for each entry's vertical position.
- `beamFrom`, `beamVia`, `beamLead` for the beam colours and how far ahead of the scroll it runs.
- `titleColor`, `railX` for the rail look.
- `scroll` keyframes to set the scroll story; the demo needs real images in `mock()` for a finished look.

## Files
- `code/demo.html` runs on its own and loops. All imagery is CSS or SVG placeholder.
- `media/poster.jpg` is a preview image showing the component.

## Credit
Idea: "Timeline" by manuarora700 on 21st.dev (https://21st.dev/@manuarora700/components/timeline), MIT. This demo is an original recreation written from the public preview.
