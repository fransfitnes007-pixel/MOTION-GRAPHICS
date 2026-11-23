---
name: add-to-cart-list-with-live-cart-panel-odometer-total
description: A shop list of three shoes with Add buttons next to a Cart card. Add one and a row slides into the cart while the Total rolls up like an odometer; the plus button rolls it again. Reach for it as a mini cart on a product page or a store demo.
---

# Add to cart list with live cart panel

**Code name:** Odometer total.

## What you see
White page, two columns. Left: three bordered rows, each with a grey rounded icon tile holding a black shoe, a name (Air Max 90) with a small grey tag (Running), a grey price and colour line ($129.99 . Black/White) and an outlined + Add button. Right: a Cart (0) card, empty, with a hairline, Total 0 and a full-width black Checkout button with a card icon. In the clip the pointer moves to the first Add (the icon tile darkens on hover) and clicks: the heading becomes Cart (1), a pale grey row opens in the cart with the name, a minus-1-plus stepper, a small x and $129.99, and the Total digits roll from 0 up to 129.99 over about half a second. Clicking plus makes it 2, the price $259.98, and the digits roll again to 259.98 (the changed digits move, the rest stay). The pointer then moves to Checkout and clicks, which darkens the button. About 3.8s in all.

## When to use it
A store or product page where adding something should feel immediate, a pricing or add-ons panel with a running total, an order form that shows its sum as you go. The odometer is the part that sells it; use it where the number matters.

## How it works
Two parts. The list is plain rows with an add handler. The cart keeps `items` in state; the heading counts them and the Total is the sum. The Total is drawn as digit columns: each digit is an overflow-hidden box with a strip of 0 to 9 translated by `-digit * lineHeight`, so a change from 1 to 2 slides the strip up one step. A column only moves when its digit changes, which is why the left digits stay still going from 129.99 to 259.98 apart from the first two.

```js
strip.style.transform = `translateY(${-lerp(oldDigit, newDigit, ease) * LINE}px)`
// ease out cubic over 0.5s; leading zeros hidden; decimals hidden while the total is 0
```

The existing `odometer-number-roll__digit-column-translate` is the stand-alone version of the digit roll. The demo scripts the clicks and replaces the shoe photo with a black SVG shoe. The reset at the end of the loop is instant.

## Numbers that matter
| | |
|---|---|
| Preview size | cards 298 and 257 wide at 640px viewport; the demo draws it at 1.8x |
| Row | 65px high, 10px gap, 10px radius, 1px `#e4e4e7` |
| Add button | 58 by 29, 1px border, 7px radius |
| Cart item | `#f5f5f6`, 8px radius, 47px high; opens over 0.3s |
| Total roll | 0.5s, ease out cubic, 15px line height per digit |
| Demo timing | add 0.95s, plus 2.15s, checkout 3.1s, reset 4.35s, 5s loop |

## Sound
Silent.

## Adapt it
- `CONFIG.products`: name, tag, price, colour.
- `CONFIG.ink`, `line`, `chip`: colours; the Checkout button colour is in the `co` box.
- `CONFIG.rollTime`: digit roll speed.
- `CONFIG.addAt`, `plusAt`, `checkoutAt`: the scripted clicks. The demo always adds the first product; wire your own handler for the rest.

## Files
- `code/demo.html` runs on its own and loops. The shoes are black SVG placeholders; the clicks are scripted and always add the first product.
- `media/poster.jpg` is a still of the component.

## Credit
Idea: "Interactive Checkout" by kokonutd on 21st.dev (https://21st.dev/@kokonutd/components/interactive-checkout), MIT. This demo is an original recreation written from the public preview.
