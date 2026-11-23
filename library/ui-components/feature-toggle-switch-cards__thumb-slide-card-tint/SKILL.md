---
name: feature-toggle-switch-cards-thumb-slide-card-tint
description: A two-column grid of settings cards, each with an icon, title, short description and an on/off pill switch. Switched-on cards pick up a light grey fill. Reach for it on a settings or feature-flags screen.
---

# Feature toggle switch cards

**Code name:** Thumb slide with card tint.

## What you see
Four white cards in two columns on a white page, each 360 by 115 with 24px corners and a 1px light grey border. Left in each card is a 42px rounded icon tile (chart, bug, globe, database), then a 22px semibold title and a 19px grey description wrapping to two lines. A 44 by 26 pill switch sits top right.

Off cards stay white with a pale grey track and the thumb on the left. On cards get a `#fafafa` fill, the icon tile turns grey `#e6e6e8`, the track goes near-black and the thumb slides 18px right.

The clip is 7.9s. A cursor turns Analytics on at about 1.1s and off at 1.8s, flips CDN Caching off at 2.5s and on at 3.1s, Auto Backup on at 4.5s and off at 5.1s, then Error Logging off at 5.7s. The demo adds a click at 7.0s to put Error Logging back so it loops.

## When to use it
Settings pages with a few independent options that each need a sentence of explanation. The card tint gives a second signal of state, so a column of them reads at a glance. For long lists use plain rows.

## How it works
One card component with the switch as a controlled boolean. State changes the background of three things together: card, icon tile and track. In the demo each of those is interpolated by one value `m` (0 off, 1 on) over 0.22s, and the thumb's left offset is `3 + 18 * m`.

```js
S(card, { background: mixc(cardOff, cardOn, m) })
S(tile, { background: mixc(tileOff, tileOn, m) })
S(thumb, { left: px(3 + 18 * m) })
```

The 21st.dev usage is `<Pattern />` with no props; titles and icons are inside the component.

## Numbers that matter
| | |
|---|---|
| Card | 360 x 115, 24px radius, 1px border `#e6e6e8`, gap 23px across and 23px down |
| Icon tile | 42px, 11px radius, off `#ffffff`, on `#e6e6e8` |
| Type | title 22px/600 `#0c0c0c`; text 19px `#777` |
| Switch | 44 x 26, thumb 20px white; track on `#1b1b1d`, off `#e7e7e9` |
| Card fill | on `#fafafa`, off `#ffffff` |
| Timing | 0.22s ease-out for tint and thumb; demo loop 8s |

## Sound
Silent.

## Adapt it
- `CONFIG.cards`: titles, descriptions, icons and starting states.
- `switchOn` for the brand accent instead of near-black.
- `clicks`: which switch flips and when.
- Change `box` width and the `i % 2` column logic for a single column or three.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Feature Toggle Switch Cards" by cnippet-dev on 21st.dev (https://21st.dev/@cnippet-dev/components/v-switch-8), MIT. This demo is an original recreation written from the public preview.
