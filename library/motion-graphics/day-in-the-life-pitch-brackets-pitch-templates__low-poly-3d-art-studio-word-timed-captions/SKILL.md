---
name: day-in-the-life-pitch-brackets-pitch-templates-low-poly-3d-art-studio-word-timed-captions
description: Part nineteen of the low-poly "day in the life of a UGC creator" reels. In an art studio she is pitching a brand: "hi, I love your brand" took an hour, so she finds a template online ("Hey [BRAND NAME]! I've loved [PRODUCT] since [YEAR]!") and sends it, with the brackets, to eleven brands. Then YourBrand: three pitch templates, or it writes one: give it the brand, your stats and the deliverable; get a subject line, an email, a DM and a follow-up. One brand did reply: "Hi [CREATOR NAME],". Reach for it when a reel needs the pitch-email story, text with highlighted [placeholders], an outbox filling up, or generated output appearing block by block.
---

# Day in the life, part nineteen: with the brackets (low-poly 3D)

**Code name:** three.js art studio with an easel whose canvas is blank until the day turns, box-built character, compose / online template / sent list / pitch templates / personalise form / four outputs / reply on a floating sheet, hard cuts on voiceover word times. **From:** original build, part 19 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-pitch-brackets-pitch-templates__low-poly-3d-art-studio-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.8 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.7s.** An art studio in flat north light: white brick, a big window, a paint-spattered floor, a shelf of paint jars, an easel with a blank canvas. She works at a table. "Part nineteen."
2. **3.7 to 5.1s.** Hands to her chest: PITCH DAY.
3. **5.1 to 9.5s.** New message. "Hi, I love your brand." types itself, slowly; a chip in the corner counts to 1 h 02 min and turns red. 7 WORDS · 1 HOUR.
4. **9.5 to 14.9s.** A pink and yellow page: FREE PITCH TEMPLATE!!! "Hey [BRAND NAME]!" then "I've loved [PRODUCT] since [YEAR]!", each bracket in a yellow box.
5. **14.9 to 15.7s.** She hits a key: SENT.
6. **15.7 to 18.4s.** The sent email; the brackets turn red (BRACKETS: STILL IN). Then the Sent list fills: Brand 1 to Brand 11, each "Hey [BRAND NAME]! · delivered ✓". × 11.
7. **18.4 to 20s.** The chrome monogram; the room warms and the canvas on the easel now has a painting on it.
8. **20 to 23.2s.** Brand Pitch Templates: Cold pitch, Warm follow-up, Rate reply (3 TEMPLATES). A purple "✦ Personalise with AI" button appears and is pressed.
9. **23.2 to 26s.** Three fields light up in turn: Brand (Sunny Soda), Your stats (three small bars), Deliverable (three 30-second videos).
10. **26 to 29.8s.** Four blocks land on the words: SUBJECT, EMAIL, DM, FOLLOW-UP. NO BRACKETS IN IT.
11. **29.8 to 33s.** She swats away a blank canvas and a giant red pair of square brackets: ✕ BLANK PAGE, ✕ BRACKETS. Arms crossed: "No bullshit."
12. **33 to 35.8s.** Callback: Inbox, "1 new reply", from Brand 7. "Hi [CREATOR NAME]," then "Thanks for reaching out to [COMPANY]! We loved your [CONTENT TYPE]."
13. **35.8 to 40.8s.** Black end card: chrome monogram, wordmark, "Three pitch templates. Or one written for you.", yourbrand.com.

## How it works
Same structure as parts one to eighteen. New here:

- **`bline(x, s, X, Y, font, base, hi, hiText)`** draws a line of text and puts a filled box behind anything in `[SQUARE BRACKETS]`. It carries the whole joke: yellow boxes on the template, red on the sent mail, the outbox rows and the reply.
- **One `drawDoc` with seven pages** (0 compose, 1 the template, 2 sent and the list of eleven, 3 YourBrand's three templates, 4 what she gives it, 5 what she gets, 6 the reply). `state` picks the page from the beat times.
- **`drawEasel(state)`** repaints the canvas on the easel when the mood flips: blank, then a small landscape.
- **Props for the finale:** `blankP` (a blank canvas) and `brkP` (a pair of square brackets built from six bars).
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice A (see `_engine/VOICES.md`), sped 1.214x (raw 44.9 s, aimed at 37 s), take 2 of 2. Brackets are not written in the voice script ("Hey, brand name."); "A D M" is spaced so it is spelled out. `code/recipe.py` adds slow, hesitant typing under a ticking clock, a tacky jingle for the template page, a clunk as each bracket lands, a mail swoosh for send and eleven more for the outbox, a ding per template and per output block, a clunk and a thud on "[CREATOR NAME]". No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
