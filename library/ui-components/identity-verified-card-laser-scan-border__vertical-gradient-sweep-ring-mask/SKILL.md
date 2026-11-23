---
name: identity-verified-card-laser-scan-border-vertical-gradient-sweep-ring-mask
description: "A white security card: fingerprint tile, 'Identity Verified', teal Secure badge, an avatar with name and ID, four small fact tiles, a green 'Scan complete' bar and a 'View Access Log' button. A band of lavender, pink, red and teal light slides down its border. Use for verification or access screens."
---

# Identity verified card with laser-scan border

**Code name:** Vertical gradient sweep, ring mask.

## What you see
A white card, 384 x 461 in the demo (shown 1.55x), radius 22, a 1px grey border and a very soft shadow. Header: a 40px light grey tile with a fingerprint icon, 'Identity Verified' in 15px semibold over 'Biometric Scan' in 12.5px grey, and a teal 'Secure' pill with a dot on the right. Then a 60px round avatar, 'Albert' in 17px semibold, 'Senior Engineer' and 'ID: #EMP-00421' in grey. A 2 x 2 grid of 160 x 62 tiles on `#fafafa` (Access Level / Level 4, Clearance / Top Secret, Last Scan / Just now, Location / HQ — Floor 3). A mint bar with a teal shield and 'Scan complete — Access granted'. A full-width outlined button with a lock and 'View Access Log'. The border is a 2px ring that is plain grey except where a tall gradient band passes: lavender at the top edge of the band, then pink, rose, then teal at the bottom. The band, about three quarters of the card tall, enters above the card, slides down it in 2.4s and leaves below, so the side borders colour in from top to bottom while the top and bottom edges only light at the ends. Names and numbers are placeholders.

## When to use it
A verification, access-granted, KYC or security screen, or any card that should feel like it is being scanned. The light edge is faint on purpose, so it works best on a white page with plenty of space round the card.

## How it works
The border is a separate ring layer that sits on top of the card. It has 2px padding and a two-layer mask (a `content-box` layer and a full layer combined with `exclude`), so only the border strip is visible. The ring's background is a vertical linear gradient sized to 75 percent of the card's height with no repeat, and the demo moves `background-position-y` from above the card to below it on a loop.

```js
const bh = cardH * .75
ring.style.backgroundSize = `100% ${bh}px`
ring.style.backgroundPosition = `0 ${lerp(-bh, cardH, (t / 2.4) % 1)}px`
```

Stops from the clip: lavender `#a9b8ff` 18 percent, `#cbb3f0` 32, pink `#f4a3b8` 50, rose `#f08f98` 62, teal `#4fdcc6` 86, transparent at both ends. The real component's source is locked, so the sweep period is read from the video frames and is approximate.

## Numbers that matter
| | |
|---|---|
| Card | 384 x 461, radius 22, border `#e9e9ec` |
| Ring | 2px, mask exclude |
| Band | 75 percent of card height, one pass per 2.4s, no repeat |
| Colours | `#a9b8ff` `#cbb3f0` `#f4a3b8` `#f08f98` `#4fdcc6` |
| Teal | text `#10cdb0`, bar `#f0fdfa`, border `#a9f1e4` |
| Tiles | 160 x 62, `#fafafa`, radius 11 |
| Loop | 4.8s, two passes |

## Sound
Silent.

## Adapt it
- `band` stops: swap the colours for a brand palette, or use one hue and transparent for a single laser line.
- `period` and `bandHeight`: speed and how much of the border is lit.
- `borderWidth`: 1 for subtle, 3 for obvious.
- All the text and the four `stats`.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Shine Border Security Card" by shadcnspace on 21st.dev (https://21st.dev/@shadcnspace/components/shine-border-02), MIT. This demo is an original recreation written from the public preview.
