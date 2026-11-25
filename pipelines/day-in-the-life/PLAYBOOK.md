# Day in the Life: how a part is made

`KIT` is the repository root. `P` is `KIT/pipelines/day-in-the-life`. When the owner says **go**: pick the next story
yourself, deliver one finished video, and end the message with `Say "go" for Part N.` One video per go. Ask only when
something is truly blocked (a feature you cannot confirm exists, a voice you cannot reach).

## 1. The story
- **A new creator each time** (alternate women and men, a new look), a new day, and a pain point that is not in
  `P/EPISODE-LOG.md`. A new name and outfit on the same story counts as a repeat. Rotate beginner, intermediate and
  veteran without saying the level out loud, and cover the whole funnel over time (finding deals, pitching, briefs,
  filming, delivering, approvals, posting, tracking, getting paid, growing).
- **First person, the creator's own day:** what they tried to do today, what went sideways, the thought they would only
  admit to another creator. One visual joke that gets worse beat by beat, ending on a new low point (check the Gags list
  so the low point is new).
- **Around the midpoint:** "Then I found YourBrand." One real feature that answers that exact problem. Once every clean
  feature has been used, do second passes: pair a used feature with a pain point that has not been shown.
- **The closer:** "No X. No Y. No bullshit." (he or she swats two chips away, then crosses their arms), then a callback
  that belongs to the episode: the pain-era habit kept fondly, the unlikely fan converting, the low point framed in the
  hallway. Then the end card: monogram, wordmark, two or three short lines, the domain.
- **Length:** about 95 to 105 words, about 540 characters, about 40 seconds. A 640-character script ran 55 s raw and
  could not be saved by speeding up.

## 2. Claim rules (product half)
- Check every feature exists in your product before you write the line (read the app's own pages or code). The sheet
  copies the real screen: real titles, real button labels, real step names. Leave out any step that names another
  company's app.
- No prices, rates, payout dates, view counts or results for the product. Views are bars, never numbers. Never say the
  product is free unless the owner has said so in writing. Nothing from a client brief that is not public yet.
- No real brand names, logos, platforms or people anywhere: say "DM", "the group chat", "socials". Made-up brands,
  handles and numbers belong only to the pain half.
- Features that touch money (rate calculators, bonuses, rate templates) need the owner's OK first.

## 3. Voice
- Two voices that alternate: voice A (a woman) on odd parts, voice B (a man) on even parts. Any TTS works; the series
  used a web text-to-speech app: pick the voice, paste the script as one paragraph of short sentences ending with the
  domain spelled for speech ("Your Brand dot com"), generate two takes, keep the better one. If the app is shared with
  other people, note what was in the text box and which voice was selected, and put both back when you are done.
- Speed rule: `python3 P/tools/prep_voice.py take1.mp3 <episode>/code/voiceover.wav`. Speed = raw seconds / 37, kept
  between 1.1 and 1.3, 48 kHz mono. If the raw take is over about 48 s, shorten the script.
- Word times on the machine: `python3 P/tools/words.py voiceover.wav --script script.txt`, then
  `python3 P/tools/tidy.py voiceover.words.json words.json` (joins split tokens, drops the spoken URL, no word starts
  before the last one ends). The printout gives every word with its index: you pin beats to those indexes.

## 4. Build
1. New folder `<episode>/` with `code/` and `media/`. Copy `_shared_ui.js`, `three.min.js`, `brand-assets.js` and
   `recipe.py` from the last part's `code/`.
2. Write `middle.js` for this part, starting from the last part's scene section (everything between its helpers and
   `/*SHARED_UI*/`): the room, `makePerson()` with the new outfit, poses, props, `drawDoc()` sheets, `CAM`, `state(t)`.
   See `P/SCENE-KIT.md`.
3. Write `spec.json` (title, top comment, script, end lines, outfit colours, beats as word indexes, caption groups) and
   assemble: `python3 P/tools/fill.py --base <last part>/code/demo.src.html --episode <episode> --words words.json
   --spec spec.json --middle middle.js`. It reports any word that does not match the script.
4. **Stills before video.** `node KIT/engine/tools/render_demo.cjs still <episode>/code/demo.html <dir> "t1,t2,..." 1080 1920`
   on every beat, then `python3 P/tools/sheet.py <dir> 6` and look at the sheet. Fix framing, anything under the caption
   (it sits at 64% of the height), props blocking the face, small sheet text, pills over sheet titles.
5. Sound: edit `code/recipe.py` (voice plus synthesised effects on the T times, no music; mirror T from `T.json`).
6. Render, mix and check: `bash P/tools/mux.sh <episode> <out.mp4>`. It renders, mixes, muxes with
   `scale=in_range=pc:out_range=tv,format=yuv420p`, libx264 crf 17, `loudnorm=I=-16`, AAC 192k, re-muxes with a
   limiter if the peak reads 0.0 dB, prints loudness, and writes a poster and two frame sheets. Look at both sheets.
7. Write `SKILL.md` and `meta.json` for the part (same shape as the published pieces), add the part to
   `P/EPISODE-LOG.md` and to the "already used" lists, and rebuild the index once: `python3 KIT/engine/tools/build_index.py`.
8. Report: what happens in it, the choices the owner may want changed, whether anyone has listened to the mix, and the
   last line `Say "go" for Part N+1.`

To publish a part made for a real brand in a public copy of this kit, run
`python3 P/tools/port_episode.py <episode> --part N --brand "RealName"`: it swaps the brand for the placeholders,
removes platform names and voice names, drops voice audio and clips, and renders a new poster.

## 5. Layout facts that save time
- Desk or table top at (2.0, 1.5, -1.2); seated hips at (2.0, 1.2, -2.4); a standing spot at (0.3, 1.1, 1.9).
- The floating phone or page sits at (0, 3.0, 2.6) and fills the frame from the `phone` camera.
- Cameras that have worked: `front`, `frontR`, `face`, `shoulder` (laptop over the shoulder), `phone`, `film`, `center`
  (the swat finale), `slump` (table from above), `wide`.
- Pills and cards live in the top band, y 250 to about 700. Captions at 64% of the height. Never show a product claim
  as a number.
