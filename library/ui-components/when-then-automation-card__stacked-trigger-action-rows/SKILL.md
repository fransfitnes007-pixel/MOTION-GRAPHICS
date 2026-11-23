---
name: when-then-automation-card-stacked-trigger-action-rows
description: A light card with two stacked rows, a WHEN trigger and a THEN action, each with a coloured app tile, joined by a down arrow. Reach for it to show a simple automation recipe in a settings or integrations screen.
---

# When-Then automation card

**Code name:** Stacked trigger and action rows.

## What you see
A white card with a soft grey border and a light shadow, 784 by 405 at the poster scale. Inside sit two rows, each 722 by 132, with a 2px light grey outline and 20px corners. The top row has a rounded purple tile with a white slanted slab, then "WHEN" in bold grey beside the app name in black, and the event ("Payment received") in grey below. A 48px grey circle with a down arrow sits between the rows. The bottom row repeats the layout with a pale grey tile holding a four-colour hash, "THEN" and the action ("Send #revenue alert").

The original on 21st.dev is static. The demo adds a 5s loop: the card fades up, the rows spring in 0.18s apart, then the arrow nudges down 7px at 1.9s and the bottom row picks up a purple outline for a moment, to show the flow from trigger to action.

## When to use it
An integrations page, an automation builder's recipe list, or an onboarding step that explains "when this happens, do that". It reads well in lists of several cards. It is too plain for a hero.

## How it works
Two identical row components stacked in a card, with a small circular connector between them.

```tsx
<Automation1 triggerLabel="When" actionLabel="Then"
  trigger={{ src, alt: "Stripe", event: "Payment received" }}
  action={{ src, alt: "Slack", event: "Send #revenue alert" }} />
```

Each row is an icon tile (88px, 22px radius) plus two text lines. The label word ("WHEN", "THEN") is a semibold uppercase span in grey with the app name beside it in black. The tile takes either a brand colour or a neutral grey behind the logo image. The demo replaces the two logos with a plain slab and a hash drawn in SVG.

## Numbers that matter
| | |
|---|---|
| Card | 784 x 405 at poster scale, 26px radius, 1.5px border `#e4e4e6`, soft shadow |
| Row | 722 x 132, 20px radius, 2px border `#e8e8ea`, 30px side margin |
| Icon tile | 88 x 88, 22px radius, purple `#5433ff` or grey `#f3f3f4` |
| Type | 28px; label word bold `#6b6b70`, app name `#0a0a0a`, event `#707076` |
| Connector | 48px circle, `#f3f3f4` fill, 2px `#e3e3e5` border, 22px arrow |
| Demo loop | 5s, spring k=8 f=10 on rows, arrow nudge at 1.9s |

## Sound
Silent.

## Adapt it
- `CONFIG.trigger` and `CONFIG.action`: app name, event text and tile colour.
- `triggerLabel` and `actionLabel` if you want "IF" and "DO" or "On" and "Then".
- `pulseAt`: when the arrow nudges, or 99 to keep it still like the original.
- Add a third row by copying `mkRow` and a second arrow.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Trigger To Action" by ziegfiroyt on 21st.dev (https://21st.dev/@ziegfiroyt/components/automation1), MIT. This demo is an original recreation written from the public preview.
