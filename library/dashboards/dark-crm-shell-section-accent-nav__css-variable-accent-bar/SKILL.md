---
name: dark-crm-shell-section-accent-nav-css-variable-accent-bar
description: "A near-black CRM app shell where each sidebar section has its own accent colour, shown as coloured active text and a small left bar. Inside it cycles a stat-card dashboard, a kanban pipeline and a bar funnel. Reach for it for a dense internal tool that should feel calm and colour-coded."
---

# Dark CRM shell with section accent nav

**Code name:** CSS variable accent bar.

## What you see
A zinc-black app (`#09090b`) with two faint ambient glows, violet top right and blue bottom left. A 236px translucent sidebar has a white logo tile, a search box with a `K` key hint, grouped nav with tiny caps headings, and a profile row with a green status dot. The active item gets a lighter fill, a hairline border, coloured text and a 3px bar on its left edge. Colours are per section: Dashboard white, Analytics yellow, Pipeline green, Contacts blue, Calendar pink, Inbox purple, Campaigns orange, Automations teal, AI violet.

Over 11 seconds the demo moves through three views, with the nav following:
- 0 to 3.8s Dashboard (white): five stat cards fade up 10px, 60ms apart, with numbers counting up over 0.9s. Activity feed, tasks, a per-business bar list and appointment tiles.
- 3.8 to 7.4s Pipeline (green): four stage columns with a count chip and cards.
- 7.4 to 11s Analytics (yellow): a funnel where each bar widens to its share over 0.8s, then revenue bars.

Each view change fades in over 0.18s with an 8px rise.

## When to use it
Internal tools, CRMs, admin consoles, any app with many sections where colour can help orientation without painting the whole page. It would be wrong for a marketing page: the contrast is deliberately low and the type is small.

## How it works
One attribute per nav item drives two rules, and the page content never uses these colours for chrome.

```css
.nav-item.active { background: var(--surface-2); border-color: var(--border); }
.nav-item[data-view="analytics"].active { color: var(--c-analytics); }
.nav-item.active::before { content:''; position:absolute; left:-1px; top:50%; transform:translateY(-50%);
  width:3px; height:14px; border-radius:0 3px 3px 0; }
.nav-item[data-view="analytics"].active::before { background: var(--c-analytics); }
```

Surfaces are translucent white over the black: `rgba(255,255,255,.032)` for cards, `.055` for hover and active, `.08` for chips, with borders at `.075`. A card has an inner top highlight, `0 1px 0 rgba(255,255,255,.04) inset`, plus `0 4px 24px rgba(0,0,0,.35)`.

Counters use `countUp`, `1 - (1 - p)^3` over 900ms, started 80ms apart. Stat cards use `statEnter .4s ease both` with `animation-delay` of 0, .06, .12, .18 and .24s. The demo reproduces both as functions of `t`.

## Numbers that matter
| | |
|---|---|
| Ground | `#09090b`, sidebar `rgba(11,11,15,.95)` with a 24px backdrop blur in the source (omitted in the demo) |
| Radii | cards 10px, controls 6px, chips 4 to 20px |
| Sidebar | 236px, nav text 13.5px, group labels 10px caps at .08em |
| Stat value | 32px, weight 700, tracking -0.05em |
| Section accents | `#facc15 #60a5fa #4ade80 #f472b6 #c084fc #fb923c #2dd4bf #a78bfa` |
| Motion | stat enter .4s ease, view fade .18s ease, funnel .8s ease, count-up 900ms |

## Sound
Silent.

## Adapt it
- The accent table: one colour per section.
- Sidebar groups and items.
- Page content: the shell works with any view, only the first three are drawn.
- Swap the white primary button for a brand colour if you want colour in the chrome.

## Files
- `code/demo.html`: runs on its own, with an invented workspace and people.
