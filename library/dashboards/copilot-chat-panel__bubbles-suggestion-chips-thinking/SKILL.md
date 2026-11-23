---
name: copilot-chat-panel-bubbles-suggestion-chips-thinking
description: "A compact data-aware chat panel: gradient bot avatar and a green 'Connected to your data' line, a greeting bubble, three suggestion chips, violet user bubbles, dark assistant bubbles with bold figures, a Thinking... bubble and an input with a send button."
---

# Copilot chat panel

**Code name:** Chat bubbles, suggestion chips and thinking state.

## What you see
A 380 by 520 panel. Header: a violet-to-blue square with a bot icon, "Campaign Copilot", a green dot and "Connected to your data". The first bubble is the greeting; three outlined chips offer questions. At 1.2s one chip lights violet, the chips vanish and the question appears as a right-aligned violet bubble. A "Thinking..." bubble with a spinner shows for about two seconds, then the answer fills in (bold names and numbers), and the history scrolls up. From 5.6s a second question is typed into the input one character at a time, sent at 7s, answered at 8.7s.

## When to use it
Any assistant or copilot panel in a product video. It shows the pattern that matters: suggestions first, a visible thinking state, answers that quote real numbers.

## How it works
Bubbles: user `bg-rv-purple text-white`, assistant `bg-rv-bg text-white/85 border border-rv-border`, both `max-w-[88%] px-3.5 py-2.5 rounded-2xl text-sm leading-relaxed`. Replies support `**bold**` through a tiny regex split (`renderMd`). The panel is `rounded-2xl border bg-rv-card flex flex-col h-[520px]`; the log scrolls to the bottom whenever messages or `busy` change. The suggestion chips are shown only while there is no history. Send button: `p-2.5 rounded-xl bg-rv-purple shadow-lg shadow-rv-purple/25`, disabled while busy or empty.

The demo reveals the answer by slicing the string over one second and keeps the last message in view by translating the list by the overflow:

```js
inner.style.transform = `translateY(${-Math.max(0, inner.offsetHeight - 410)}px)`
```

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Panel 520px high; bubbles 14px text, 16px radius.
- Bot avatar 32px, gradient `#8B5CF6` to `#3B82F6`.
- Online dot 6px `#34D399`.
- Typing speed in the demo: 1.2s for 35 characters.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `GREET`, `SUG`, `Q1`/`A1`, `Q2`/`A2`.
- Timings of the chip pick, thinking and typing.
- Panel height and `410` scroll offset.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
