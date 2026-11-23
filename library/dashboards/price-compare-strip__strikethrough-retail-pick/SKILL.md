---
name: price-compare-strip-strikethrough-retail-pick
description: "A white strip of small-caps labelled numbers: retail struck through, a resale range, a large green pick, and a typed-price input that turns rust when it is out of range. Reach for it when you need reference, recommended and typed prices side by side."
---

# Price compare strip

**Code name:** Strikethrough retail and pick.

## What you see
Three identical strips stacked, each fading up in turn from 0.2s. Left to right: RETAIL in grey monospace with a hairline strikethrough, RESALE RANGE in black, MY PICK in larger green, then a vertical hairline and YOUR PRICE with an empty green-bordered input and an underlined "use mine" link. A dashed rule closes each strip with a one-line source note. From 2.2s a price types into each input, one digit every .14s. The first value sits inside the range and keeps its green border; the other two exceed the range and the input border turns rust.

## When to use it
Anywhere a reference price, a recommended price and the user's own price need to sit side by side: listing tools, quote builders, price lists, procurement comparisons. It also works as a compact "was / now / suggested" row. Avoid it for more than five or six numbers; it stops reading at a glance.

## How it works
A flex row with wrap. Each block is a column: a 9.5px uppercase label over a mono value. The only styling differences are on the value: retail is muted and struck through, range is full ink, pick is accent-coloured and four points larger. The user's block gets a left hairline.

```css
.pb{display:flex;flex-direction:column;gap:2px}
.pb span{font:600 9.5px/1 Archivo,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--faint)}
.pb b{font:600 15px/1 "IBM Plex Mono",monospace;font-variant-numeric:tabular-nums}
.pb.retail b{color:var(--muted);text-decoration:line-through;text-decoration-thickness:1px}
.pb.pick b{color:var(--accent);font-size:19px}
.pb.mine{border-left:1px solid var(--line);padding-left:14px}
.pin{border:1.5px solid var(--accent);border-radius:8px;font:600 17px/1 "IBM Plex Mono",monospace}
.pin.warn{border-color:var(--urgent)}
```

Tabular numerals keep digits from jumping as values change. On narrow screens the "mine" block loses its hairline and takes a full row (`flex-basis:100%`).

## Numbers that matter
| | |
|---|---|
| Label | 9.5px uppercase, .08em, `#8A9A93` |
| Value | mono 15px, tabular; pick 19px, accent `#0F6E4F` |
| Strip | white, 1px line border, radius 9px, padding 11px 12px, gap 14px |
| Input | 104px wide, 1.5px accent border, radius 8px, mono 17px |
| Warn | border `#A83C14` |
| Demo timing | strips in .2 to 1.2s, typing from 2.2s (.14s per digit), loop 6s |

## Sound
Silent.

## Adapt it
- The three reference numbers and their labels.
- The rule that triggers `.warn` (above range, below cost, over budget).
- Accent and warn colours.
- The source line under the dashed rule, or drop it.

## Files
- `code/demo.html` runs on its own and loops; 6s. All data is placeholder.
