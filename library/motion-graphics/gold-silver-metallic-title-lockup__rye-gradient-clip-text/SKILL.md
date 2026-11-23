---
name: gold-silver-metallic-title-lockup-rye-gradient-clip-text
description: "A book-cover title built from gold and silver chrome Rye lettering, script connector words in Great Vibes, and a tracked gold kicker. Use it for a western, gothic or period-piece title, or as the cover inside a 3D book."
---

# Gold and silver metallic title lockup

**Code name:** Rye gradient clip text.

## What you see
A dark dusk-photo cover. At the top the author's name in Great Vibes script, white, with a gold rule and "A TRUE STORY" in tracked Playfair capitals under it. At the bottom the title in a stacked lockup: script "The" in white, "GOLDEN" and "TITLE" in Rye with a gold chrome gradient, script "on", then "SILVER" and "LANE" in the same face with a silver gradient. Each word has a hard offset shadow plus a soft dark shadow, so it reads as embossed metal. A faint gloss band passes across (it can run while a book turns).

## When to use it
Titles for books, whisky, westerns, true-crime, anything period. It needs a dark photo underneath and big sizes: the chrome gradient turns to mud below about 60px.

## How it works
The metal is a vertical gradient with hard colour changes, clipped to the text:

```css
.golden{font-family:Rye;font-size:216px;letter-spacing:.02em;
  background:linear-gradient(180deg,#fff2b3 0%,#f6d35a 22%,#e4a92a 48%,#b67a12 62%,#f7d873 82%,#ffe9a3 100%);
  -webkit-background-clip:text;background-clip:text;color:transparent;
  filter:drop-shadow(0 6px 0 #4a2f06) drop-shadow(0 14px 26px rgba(0,0,0,.75))}
.silver{ /* same, with #ffffff #dfe4ea #a9b1bb #f4f6f8 #c3c9d2 and a #1d2126 hard shadow */ }
```
The two `drop-shadow` filters are the trick: the first, with zero blur, is the extruded edge; the second is the soft lift. The reflective band in the gradient (dark at 62%, light again at 82%) is what makes it look like chrome. Everything else on the cover is script (`Great Vibes`) or tracked Playfair. The demo sizes all type in container units (`cqw`) of the cover so one number scales the lockup. The type itself is never animated; the sliding gloss is a `translateX(lerp(-BW, BW, (sin(t*.9)+1)/2))` band, which this demo applies to the whole plate. The demo's lockup is a rebuild at a different scale with a CSS dusk scene in place of the cover art.

## Numbers that matter
| | |
|---|---|
| Cover | 1800 by 2700px (6 x 9 in at 300 dpi) |
| Type | author 168px, kicker 40px (.42em), "The" 170px, GOLDEN/TITLE and SILVER/LANE 216px, "on" 110px |
| Gold stops | #fff2b3 #f6d35a #e4a92a #b67a12 #f7d873 #ffe9a3 at 0 22 48 62 82 100% |
| Silver stops | #ffffff #dfe4ea #a9b1bb #f4f6f8 #c3c9d2 at 0 30 52 68 100% |
| Shadows | 0 6px 0 dark brown or grey, plus 0 14px 26px rgba(0,0,0,.75) |

## Sound
Silent.

## Adapt it
- The four words and the script connectors.
- Gold and silver stop colours (a copper or blue-steel pair works).
- `font-size` ladder; keep the words as large as the width allows.
- The photo behind and the bottom darkening.

## Files
- `code/demo.html` runs on its own and loops.
- `code/fonts/` holds Playfair Display, Rye and Great Vibes (all SIL OFL, from Google Fonts).
