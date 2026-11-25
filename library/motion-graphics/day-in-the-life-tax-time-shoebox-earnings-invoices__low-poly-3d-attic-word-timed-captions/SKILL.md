---
name: day-in-the-life-tax-time-shoebox-earnings-invoices-low-poly-3d-attic-word-timed-captions
description: Part twenty nine of the low-poly "day in the life of a UGC creator" reels. Tax time in an attic: her accountant wants one number, what she earned this year. Brand one paid by bank transfer (the statement just says TRANSFER), brand two through an app (it says Kevin), brand three in candles, which light up all over the attic. The shoebox of receipts is shoes, and she sinks behind the desk. Then YourBrand: every campaign on one earnings page, every payout request makes an invoice, marked paid. She turns the laptop round to show her accountant one page. He writes back: great. Now do last year. Reach for it when a reel needs the tax-time or "what did I earn" story, an attic, rain on a round window, candles lighting one by one, a shoebox that opens on a sneaker, a laptop turned round to the viewer, or phone sheets for a bank statement, a payment app, an earnings page or an invoice list.
---

# Day in the life, part twenty nine: now do last year (low-poly 3D)

**Code name:** three.js attic (pitched roof with rafters and a ridge beam, a round window in the gable with rain streaks, labelled cardboard boxes, a rocking horse, a trunk, a dress form, a hanging bulb with its own point light), an old desk and chair, a laptop that turns round, twenty candles, a crate that lands, a shoebox with a hinged lid and a sneaker, box-built creator with a platinum pixie cut, a mustard hoodie and a pencil behind her ear, floating phone sheets, hard cuts on voiceover word times. **From:** original build, part 29 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-tax-time-shoebox-earnings-invoices__low-poly-3d-attic-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.85 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 4.8s.** A grey, rainy attic. A woman at an old desk with taxes_FINAL_v3.xlsx open (every cell ???). "Part twenty nine." Hands on her head: TAX SEASON.
2. **4.8 to 8.4s.** Her accountant: "Hi! For your taxes I need one number: what did you earn this year?" EARNED: ???
3. **8.4 to 15.9s.** Her bank statement: TRANSFER, TRANSFER, TRANSFER, "From: ?" (FROM: ???). A payment app: "Kevin paid you +$300.00, note: for the thing" (WHO IS KEVIN?).
4. **15.9 to 18.1s.** A crate marked WICK&CO lands; twenty candles light up around the attic: PAID IN: CANDLES.
5. **18.1 to 20.9s.** She lifts a shoebox marked RECEIPTS (RECEIPTS: FOUND). It opens on a sneaker: SHOES, RECEIPTS: 0. She sinks behind the desk.
6. **20.9 to 22.6s.** She sits up; the chrome monogram on her laptop; the rain stops and low sun fills the round window.
7. **22.6 to 28.5s.** YourBrand, Earnings: "Live numbers from every campaign you are in.", three campaigns (EVERY CAMPAIGN). Invoices: INV-1041, INV-1052, INV-1063, "Every payout request creates an invoice to YourBrand.", the chips flip from Approved to Paid (MARKED PAID).
8. **28.5 to 30.5s.** She turns the laptop round to the camera: Earnings, three campaigns, Paid. ONE PAGE.
9. **30.5 to 33.3s.** She swats away a shoebox (✕ SHOEBOX) and a candle (✕ CANDLES), then crosses her arms: "No bullshit."
10. **33.3 to 35.85s.** The accountant chat: her screenshot of the earnings page, "Great.", then "Now do last year." Her face: LAST YEAR: ???
11. **35.85 to 40.85s.** Black end card: chrome monogram, wordmark, "Every campaign. Every invoice. One page.", yourbrand.com.

## How it works
Same structure as parts one to twenty eight. New here:

- **Candles:** `CANDLE_AT` places twenty candles; from `T.candHit` they switch on one by one (22 a second) with flickering flame cones, and the warm point light `glow` follows how many are lit. The crate falls on the same beat.
- **The shoebox:** `shoeBox` arcs from the box stack to beside her face, `shoeLid` swings open, `shoe` pops up with the stamp, then everything sinks with the `SLUMP` pose (seen from the side camera `low` so the laptop lid does not hide it).
- **The laptop turns round:** `laptop.rotation.y = turn * PI`; the screen mesh that faced her now faces the camera (the lid's G is hidden while turned). `drawLaptop` shows the spreadsheet, then the G, then the Earnings list.
- **Rain** on the round window is ten thin boxes falling until the turn; the sky in the window goes from grey to low sun.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice A (see `_engine/VOICES.md`), take 2 of 2 (raw 45.1 s), sped 1.219x. `code/recipe.py` lays rain on the roof until the turn, then a whoosh and pop per phone sheet, clicks as the statement rows land, low tones for TRANSFER and Kevin, a thud for the crate and tiny rising blips as the candles light, paper rustles and a stamp for the shoebox, the reveal chord, pops per campaign row and invoice, three dings as the invoices flip to Paid, swats, pops for the replies and a low tone for "last year". No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
