---
name: day-in-the-life-vendor-portal-gift-card-payout-low-poly-3d-truck-tailgate-word-timed-captions
description: Part nine of the low-poly "day in the life of a UGC creator" reels. "I got paid today. Almost." Four brands pay four ways: an app that takes a fee, an invoice in the brand's own template, a vendor portal with fourteen forms and a bank letter, and a gift card. Then YourBrand: she adds her bank details once; a campaign balance unlocks, she presses Request payout, YourBrand approves, it goes to her bank. The gift card was for dog shampoo and she has no dog. Reach for it when a reel needs the getting-paid story, a form or portal gag, or a payout flow with no amounts shown.
---

# Day in the life, part nine: paid, almost (low-poly 3D)

**Code name:** three.js parking lot with a pickup tailgate as the desk, box-built character, payment app / invoice template / vendor portal / Earnings pages on a floating phone and sheet, hard cuts on voiceover word times. **From:** original build, part 9 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-vendor-portal-gift-card-payout__low-poly-3d-truck-tailgate-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.7 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.4s.** A grey parking lot outside a MART: lamp posts, carts, a cone. She works at a folding table on the tailgate of a teal pickup. "Part nine."
2. **3.4 to 5.8s.** "I got paid today": arms up, green PAID pill. "Almost": the pill turns red, her face goes flat.
3. **5.8 to 8.7s.** BRAND 1. A blue payment app: "You got paid", a green bar; a red chunk labelled FEE breaks off the end and drops.
4. **8.7 to 11.5s.** BRAND 2. "INVOICE (our template)": Vendor ID, PO number, Cost centre, Approver code, Net terms; every box turns red, "required".
5. **11.5 to 15.8s.** BRAND 3. A vendor portal: "Step 1 of 14" races to 14 while the form list scrolls; a red "+ A BANK LETTER" stamp lands.
6. **15.8 to 17.7s.** BRAND 4. A pink gift card with a gold bow drops into her raised hand. She looks at it.
7. **17.7 to 20.2s.** Her phone: five payment apps pop in, each with a red badge. Close on her face, eyes shut: 5 APPS, 1 HEADACHE.
8. **20.2 to 21.9s.** The chrome monogram on the laptop; the overcast sky turns to a low gold sun.
9. **21.9 to 24.2s.** Her point of view of the laptop: "Your bank account · ACH", two masked rows fill in, Save turns to Saved ✓. ONCE.
10. **24.2 to 30s.** A dark Earnings page: the padlock on "Your campaign" opens ("Available to request"), the Request payout button turns white, she presses it ("Requested"), then two rows land: Approved (by YourBrand) and Paid (on its way to your bank).
11. **30 to 32.8s.** She swats away a clipboard of forms and the gift card: ✕ PORTALS, ✕ GIFT CARDS. Arms crossed: "No bullshit."
12. **32.8 to 35.6s.** Callback: the gift card up close. A dog's face, DOG SHAMPOO, "store credit only". DOGS: 0.
13. **35.6 to 40.7s.** Black end card: chrome monogram, wordmark, "Add your bank once. Request. Get paid.", yourbrand.com.

## How it works
Same structure as parts one to eight. New here:

- **Outdoor set built round the usual desk coordinates:** the tailgate sits under the seated hips (`DESK`), the folding table is the desk top, so every stock camera still frames. The mood lerp `good` swaps a flat grey sky for a peach one and raises `sunBall`.
- **`pov` camera** (`[2.0, 3.0, -1.95]` looking down at the laptop screen, fov 72): the only way the laptop screen fills the width of a 9:16 frame. The stock `shoulder` camera hid the screen behind her cap and braid.
- **`face` camera raised** to y 3.35 so the dark laptop lid does not fill the bottom half of the close-ups.
- **`padlock(x, X, Y, s, open, col)`** draws a closed or open padlock on a canvas.
- **Pages:** `drawPhone` 'app' (the fee chunk), 'apps' (five icons), 'card' (the gift card close-up); `drawDoc` 0 the invoice template, 1 the vendor portal (step counter 1 to 14), 2 YourBrand's Earnings page.
- **Props:** `gift` (card and bow) is dropped into her hand in the brand-four beat and swatted in the finale; `clip` is the clipboard of forms.
- **No amounts anywhere.** No currency figure, fee percentage, minimum or payout date appears in any shot. The payoff wording follows the app: "Your bank account · ACH", "Request payout", approved by YourBrand, paid, on its way to your bank.
- Anything that must be read on the phone sits above canvas y 680 (of 1100); the caption covers the rest.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice A (see `_engine/VOICES.md`), sped 1.235x (raw 45.7 s, aimed at 37 s), take 1 of 2. `code/recipe.py` adds till pings on "paid", a falling whistle and buzzer on "almost", a drop for the fee, clicks as the invoice fields appear, a rising run of clicks for the fourteen forms, a buzzer on the bank letter, two sad notes for the gift card, five rising blips for the apps, a faint ringing on "headache", key clicks for the bank details, a lock click, a ding per row on the Earnings page, a squeak for the dog. No music. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
