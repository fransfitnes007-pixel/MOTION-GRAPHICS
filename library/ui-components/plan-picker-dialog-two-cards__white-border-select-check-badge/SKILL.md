---
name: plan-picker-dialog-two-cards-white-border-select-check-badge
description: A dark 'Choose Your Plan' dialog with two plan cards (name, short line, price per month, three checked features each). Selecting a card draws a white 2px outline and a white check badge on its top-right corner and dims the other. Confirm Selection is a white button; Cancel is plain text. Reach for it for upgrade and plan-change flows.
---

# Plan picker dialog with two cards

**Code name:** White border select with check badge.

## What you see
A black page with a white 'Upgrade Plan' button (sparkle icon) in the middle. Click it and over 0.3s a dialog 469 by 657 (960 by 822 frame) scales from 95% to full and fades in over a dimmed page. Header: a bolt icon and 'Choose Your Plan' in 24px semibold, a two-line grey intro, an X top right. Then two cards 415 by 194 and 18px apart: name 16px semibold, grey one-line description, price in 29px bold with a grey '/mo', and three features with check marks. The selected card (Pro at first) has a 2px white border, a slightly lighter fill, full-strength text, and a white circle with a black check hanging half out over its top-right corner. The other card has a 1px grey border and text at 72%. Clicking the other card swaps the two over 0.25s. The white Confirm Selection button (198 by 45) goes light grey on hover; Cancel sits to its right as 16.5px grey text. In the demo the sequence is: open at 0.9s, select Basic at 2.3s, back to Pro at 3.5s, hover and click Confirm at 5.2s, which closes the dialog. The 4s preview video covers the dialog only, from selection to Confirm.

## When to use it
Upgrade, downgrade and tier-change steps, where two or three plans can be compared in one view and one is picked. Two or three cards is the limit; for more, use a pricing page. Put the price and the three strongest features on the card and leave detail to a link.

## How it works
A modal dialog over a dimmed page with a list of selectable cards. Selection state drives three style changes on each card: border colour and width (1px grey to 2px white), the check badge (opacity and scale from 0.4), and text opacity (72% to 100%). In the demo a single `k2` value per card (0 to 1) is eased over 0.25s from the time of the last click, and everything reads from it. The dialog's entrance is `scale(.95 + .05 * open)` plus a 12px rise and a fade, in 0.3s. The component takes a `plans` array of id, name, price, description and features.

## Numbers that matter
- Dialog 469 by 657, radius 16px, fill `#1c1c1e`, border `#2b2b2e`
- Cards 415 by 194, radius 16px; unselected border 1px `#2f2f32`, selected 2px white
- Check badge 19px white circle, hung 11px above the card top, right edge 20px in
- Price 29px bold; names 16px semibold; features 16.5px `#d2d2d5`
- Selection and hover 0.25s ease-out; open 0.3s

## Sound
Silent.

## Adapt it
- `plans`: name, price, desc and features for each card; two or three fit.
- `title`, `intro`, `trigger`, `confirm`, `cancel` copy.
- `panel`, `card`, `cardOn` colours for a light or branded dialog.
- `openAt`, `picks`, `confirmAt` to retime the scripted clicks; `defaultPlan` for the starting selection.

## Files
- `code/demo.html` runs on its own, loops in 7.4s, and has a `CONFIG` block at the top of the script.

## Credit
Idea: "Modal Pricing" by kokonutd on 21st.dev (https://21st.dev/@kokonutd/components/modal-pricing), MIT. This demo is an original recreation written from the public preview.
