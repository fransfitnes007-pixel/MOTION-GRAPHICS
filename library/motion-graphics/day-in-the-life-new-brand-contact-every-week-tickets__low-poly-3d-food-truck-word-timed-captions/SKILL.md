---
name: day-in-the-life-new-brand-contact-every-week-tickets-low-poly-3d-food-truck-word-timed-captions
description: Part thirty two of the low-poly "day in the life of a UGC creator" reels. A food truck creator's brand contact changes every week: Monday Jess, Wednesday Tom, Friday "Brand Inbox", and each one asks for his handle (and the brief, again). He has sent it eleven times, so he paints it on the truck. Then YourBrand: questions go in a ticket, the whole conversation stays in one thread and the team answers there. Nothing gets lost. Jess is back; she asks for his handle. Reach for it when a reel needs the "new contact, same question" story, a food truck with a serving window, an order-ticket rail that fills up, text painted letter by letter onto a surface, name-badge props, a customer at a window, or phone sheets for a support ticket and its thread.
---

# Day in the life, part thirty two: Jess is back (low-poly 3D)

**Code name:** three.js street corner (asphalt, a kerb, buildings, two trees) with a teal food truck: a front wall built round an open serving window, a striped awning, a counter, a menu board, string lights along the top, a grill and fryer inside, and an order-ticket rail on the back wall; a handle painted on the lower panel; box-built cook in a red bandana and black apron; a box-built customer (Jess) with a BRAND name tag; floating phone sheets; hard cuts on voiceover word times. **From:** original build, part 32 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-new-brand-contact-every-week-tickets__low-poly-3d-food-truck-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.2 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 5.0s.** WHEELS & MEALS on an overcast street corner; he leans on the counter. "Part thirty two." FOOD TRUCK CHANNEL.
2. **5.0 to 7.4s.** His phone: BRAND CONTACT: NEW.
3. **7.4 to 17.4s.** Jess ("Hi! I'm your new contact :) What's your handle?"), Tom ("Hey, new here! What's your handle?"), Brand Inbox, no-reply ("Please resend your handle." "And the brief. Thanks!"); his @wheelsandmeals reply each time; HANDLE SENT ×1, ×2, ×3. An order ticket marked HANDLE? clips onto the rail behind him each time.
4. **17.4 to 20.5s.** AGAIN. The rail full: eleven HANDLE? tickets (HANDLE SENT ×11).
5. **20.5 to 22.4s.** Outside with a roller, he paints @WHEELSANDMEALS across the truck, drips and all. ON THE TRUCK.
6. **22.4 to 24.2s.** Paint on his face; the chrome monogram; golden evening, the string lights come on.
7. **24.2 to 29.1s.** YourBrand, Support tickets ("Questions about a campaign, a payout or your account. The team answers here."): subject "Brand keeps asking for my handle", Ticket opened ✓ (1 TICKET). The thread: Mon, Wed, Fri, then the YourBrand team, "One thread · 4 messages" (ONE THREAD, TEAM ANSWERS HERE).
8. **29.1 to 30.2s.** Hands behind his head: RAIL: CLEAR.
9. **30.2 to 33.1s.** He swats away a JESS badge and a TOM badge, then crosses his arms: "No bullshit."
10. **33.1 to 35.2s.** Jess walks up to the window (JESS: BACK) and asks: HANDLE? He points at the truck.
11. **35.2 to 40.2s.** Black end card: chrome monogram, wordmark, "One ticket. One thread. Nothing gets lost.", yourbrand.com.

## How it works
Same structure as parts one to thirty one. New here:

- **The truck front** is four boxes round an open window, so the cook stands inside and the cameras see in. The order-ticket rail inside holds eleven canvas tickets that switch on one per ask (all eleven on "eleven") and clear after the turn.
- **Painting the handle:** `drawPaint(k)` reveals @WHEELSANDMEALS letter by letter with drips on a transparent canvas over the lower panel; it is only redrawn when the amount changes. The roller sits on his right forearm and yellow paint shows on his apron and face until the reveal.
- **Jess** is a separate box figure that walks up for the callback.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), take 1 of 2 (raw 40.0 s), sped 1.1x. `code/recipe.py` lays a sizzling grill under everything, then a whoosh and pop per message, a send blip and a ticket clip per handle, a stamp for AGAIN, a rattle of clips for eleven, a paint roller and a stamp for the truck, the reveal chord, dings for the ticket, the thread and the team, swats, and a low tone for Jess's last question. No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
