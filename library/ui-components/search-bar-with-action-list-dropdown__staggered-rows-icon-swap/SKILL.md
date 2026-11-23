---
name: search-bar-with-action-list-dropdown-staggered-rows-icon-swap
description: A light search bar that opens a short list of actions (icon, name, model, shortcut, tag) with a footer of key hints. Reach for it as a Raycast-style command search or a dashboard quick search.
---

# Search bar with an action list dropdown

**Code name:** Staggered rows, icon swap.

## What you see
On white, a small label `Search Commands` sits over a rounded input (placeholder `What's up?`, magnifier at the right). Focus puts a 2px grey ring on the box. A card drops below with five rows: `Book tickets` (blue plane), `Summarize` (orange bars), `Screen Studio` (purple camera), `Talk to Jarvis` (green waveform), `Translate` (blue globe). Each row shows the name, a lighter sub label (`Operator`, `gpt-4o`) and, right-aligned, a shortcut and a type tag (`Agent`, `Command`, `Application`, `Active`). A footer row reads `Press ⌘K to open commands` and `ESC to cancel`.

In the clip the pointer clicks in, the rows stagger in over about 0.4s, then `Boo` is typed: the magnifier flips to a paper-plane send arrow with the first letter and the list shrinks to the one match, `Book tickets`, in about 0.2s.

The demo runs it as: click at 1.0s, rows slide up 6px and fade with a 0.06s stagger, `B` `o` `o` at 2.7, 2.95 and 3.2s, clear at 5.2s, blur at 5.6s.

## When to use it
A command or quick-search box that should offer something to click before the person types: popular searches, recent actions, agent shortcuts. It sits inside a page, not over it, so it is not a full-screen command palette.

## How it works
The dropdown is a bordered card with one row per action. Row height and opacity are both tied to a visibility value, so filtering collapses rows smoothly instead of popping them out. The icon button holds two SVGs that crossfade and turn as the text box becomes non-empty.

```js
const vis = keep ? 1 : 1 - filt                       // filt: 0 to 1 over .22s
row.height  = 42 * vis;  row.opacity = vis * enter
enter       = eo(seg(t, click + .08 + i * .06, click + .38 + i * .06))
icon: search opacity 1-sw, scale 1-.3sw, rotate -30sw;  send opacity sw, scale .7+.3sw
```

The original filters on a substring of every field; the demo keeps rows whose name starts with the first typed letter.

## Numbers that matter
| | |
|---|---|
| Widget | 470px wide in the demo (1.7x scale), input 46px, rows 42px |
| Colours | ring `#9ca3af`, border `#e5e7eb`, sub text `#9ca3af` |
| Row stagger | 0.06s each, 0.3s rise and fade |
| Filter | 0.22s height and opacity |
| Icon swap | 0.18s |
| Loop | 6.4s |

## Sound
Silent.

## Adapt it
- `CONFIG.actions` for rows: name, sub label, shortcut, tag, colour, icon.
- `CONFIG.typed` for what gets typed.
- `CONFIG.footerL` and `footerR` for the hint line.
- `CONFIG.rowH` and `CONFIG.stagger` for density and rhythm.

## Files
- `code/demo.html` runs on its own and loops; every frame is `render(t)`. Edit the `CONFIG` block at the top of its script.
- `media/poster.jpg` is the page's preview image.
- Similar looks already in the library: `command-palette__icon-swap-staggered-rows`.

## Credit
Idea: "Action Search Bar" by kokonutd on 21st.dev (https://21st.dev/@kokonutd/components/action-search-bar), MIT. This demo is an original recreation written from the public preview.
