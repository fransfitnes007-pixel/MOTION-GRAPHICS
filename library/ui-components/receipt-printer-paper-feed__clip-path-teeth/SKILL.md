---
name: receipt-printer-paper-feed-clip-path-teeth
description: "A small dark receipt-printer machine with a status display and a Pay now button, from whose slot a paper slip with a zigzag torn edge feeds out. The slip is the invoice before payment and the receipt after. Reach for it for a payment or confirmation screen."
---

# Receipt printer paper feed

**Code name:** Clip-path teeth.

## What you see
A rounded dark machine with a gradient face: a small logo plate at top left, a white "Pay now" button at top right, a black display showing the title, the amount due and a pulsing indigo "Ready to pay" line, and a dark slot. A paper slip slides down out of the slot over 1.6 seconds with a long ease-out, showing a mark, seller, order line, items, "TOTAL DUE", order details and a barcode. The paper's bottom edge is a fine zigzag. A pointer taps Pay now; the button shows a spinner, then the machine shows a green "Paid" pill and "Payment received". On the receipt page the paper prints again, now reading "TOTAL PAID".

## When to use it
Payment, order confirmation or invoice screens where a deal has states (locked, ready, paid) and the page should show them physically. The paper is plain text, so it prints and screenshots well. Wrong for multi-step carts, or when the amount must be editable.

## How it works
Two blocks: the machine and the paper box. The paper box is `overflow-hidden` with `-mt-3` so it tucks under the machine. The article inside animates `y` from `"-100%"` to 0 with `duration: 1.6, ease: [0.23, 1, 0.32, 1], delay: 0.25`, so it appears from behind the slot and falls into place. The zigzag is a `clip-path` polygon built in JS:

```tsx
const TEETH = 36
const teeth = Array.from({ length: TEETH * 2 + 1 }, (_, i) => `${(i * 100) / (TEETH * 2)}% ${i % 2 === 0 ? "100%" : "calc(100% - 5px)"}`).join(", ")
const PAPER_CLIP = `polygon(0 0, 100% 0, ${teeth.split(", ").reverse().join(", ")})`
```

The barcode is not random: `bars(code)` runs an FNV-style hash over the order code (`h ^= charCode + i; h = Math.imul(h, 16777619)`) to get 46 bar widths of 1 to 3px, so the same order always prints the same bars, and every seventh bar is blanked. The stage prop is `locked | ready | paid`: locked shows a dim "Locked" chip, ready shows the white Pay button and a pulsing dot (`animate-pulse`), paid shows a green chip. Reduced motion skips the feed.

## Numbers that matter
| | |
|---|---|
| Machine | rounded-[28px], gradient #2a2a31 to #17171c, 14px padding, 340px wide |
| Display | bg #0c0c10, rounded-2xl, inset shadow, amount 24px bold |
| Paper | 84% of the machine width, bg #fbfbf9, 11.5px monospace, 28px / 20px / 32px padding |
| Feed | y -100% to 0, 1.6s, ease [.23, 1, .32, 1], delay .25s |
| Edge | 36 teeth, 5px deep, clip-path polygon |
| Barcode | 46 bars, 1 to 3px wide, 44px high, gap 2px |
| Pay button | gradient white, #f3efff, #dcd3ff; text #14101f; h-10, rounded-xl |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The lines, rows and seller on the slip; the stage and `statusText` from your payment state.
- Feed time (1.6s) and delay; shorter feels like a thermal printer, longer like a ticket.
- Tooth count and depth for a finer or coarser tear.
- Paper colour and font: monospace sells it.

## Files
- `code/demo.html` runs on its own and loops. Order, seller and buyer are placeholders. The slip is the "Receipt Printer" idea from dqnamo.com credited in the source comment.
