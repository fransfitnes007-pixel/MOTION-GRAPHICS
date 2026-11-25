# Prompt library

Copy a prompt into Claude Code with this plugin installed. **Short** prompts assume the kit is set up (`brand.config.json` filled in). **Detailed** prompts spell everything out and work cold. Replace the [brackets]. The full recipe behind each one is in `docs/FORMATS.md`.

## Start here

- **Set up the brand:** `/rebrand Acme, acme.com, @acme, colours #0B0B10 and #FF6A3D, our App Store icon is assets/icon.png`
- **Any reel from an idea:** `/reel a 45 s reel about why most side projects never launch, ending on our app; pictogram style; male voice, fast`
- **Copy a viral format:** `/recreate reference/viral.mp4 same format, but the story is about [your product's problem]`
- **One effect:** `/motion chrome logo spin` then "make it our colours and slower"
- **A voiceover:** `/voice script.txt m_smooth 5.2`
- **Super detailed:** "Make a 60 s 9:16 reel at 30 fps. Hook in 2 s with no brand name. Script below, one line per beat. Voice m_smooth at 5.0 syllables a second, recorded line by line. Pin every beat to the voice's word times. Look: arizona-sunset palette, pixel style, type inside x 70-1010 / y 250-1480. Sound: click on every tag, swish on every cut, a thud on the slam words, a boom on the end card. End card: our App Store listing with the real icon. Deliver tall and wide, a contact sheet, and the numbers you measured."

## 1. Pixel dino-runner reel on black ("game over, then the endless run")

**Short:**

"Make a 34 s dino-game reel for YOURBRAND: the brand is the dino, [bad vendors/creators] are cacti, it crashes and restarts six times, then runs at 2x through YOURBRAND into the chrome mark and a black end card. Tall for Reels/TikTok/Shorts and a separate wide cut for X. Use the saved voice, sped 1.18x."

**Detailed:**

"Create a pixel-art Chrome-offline-dinosaur-style reel, 1080x1920 at 30 fps plus a native 1920x1080 version, 34 s. Voice-over script (one take, library voice, `atempo=1.18`): 'Every [audience] doing [thing] is playing this game. You're the dino. The cactus is a [bad thing]. You dodge one. You dodge two. Then one [fails three ways]. Game over. So you restart. [Repeat]. Every [swear/emphatic] time. Now watch the same game, running through YOURBRAND. [Three benefits]. The dino doesn't restart anymore. It just doesn't stop. YOURBRAND. Stop restarting. Start running.' Draw the game on a 216x150 canvas scaled 5x with smoothing off. Place each cactus where the scroll will be when its spoken word starts; jump 0.28 s before the word. Pills on the dino and cacti. Crash screen at the first hit, restart counter 1-6 faster each time, one slammed word per syllable on the emphatic line, then white dino at 2x with speed lines and jump ticks, hitting a chrome monogram, white flash, circle reveal into a black end card with monogram, wordmark, two 84 px lines and the site. Palette: black, `#8b8b93`, white, cards `#161619`, silver `#d4d4d8`; no other hues. Keep type in x 70-940, y 250-1480. Synthesise blips, thuds, whoosh and a final chord; mux with `-c:a copy`. Check the delivered file by transcript and frame grabs."

## 2. Pixel runner on a dithered desert sunset

**Short:**

"Same dino reel, but on a dithered desert sunset instead of black. The cactus is [a bad warm-up routine]. Dusk when the brand arrives. Same voice, same ending, tall and wide."

**Detailed:**

"Reuse the dino-runner reel engine. New backdrop: a pixel sunset (stops `#1a0a38 ... #ffc65a`, Bayer 4x4 dithered rows), banded sun, two mesa parallax layers, saguaros, dark floor. Dino = black silhouette with orange rim light. Script about [topic]; one voice take; anchor every cactus, pill and jump to word times from a faster-whisper transcript. At the brand reveal cross-fade to a dusk palette in 0.6 s, add stars, turn the dino white, run at 2x with day-counter ticks and sky pills following the voice. Same end card. Draw dino/cacti with a 1 px edge outline for contrast on the bright sky. 40 s, tall + wide."

## 3. Black-and-white pictogram parable (one white person, capsule tags, dot grid)

**Short:**

"Make a 70 s black-and-white pictogram reel for YOURBRAND in the style of [reference reel]: one white faceless person, dashed ground, dot grid, capsule tags, counters and typing always moving. Story: the friend with the best [idea] never builds it, someone with a worse one wins; the product enters at ~48 s as a phone that builds the app from one sentence; end on a store card. Voice: steady adult male, 5 syllables/s, SFX measured from the reference."

**Detailed:**

"Watch the reference reel frame by frame (contact sheets at 2 fps, scene-cut detection, whisper transcript with word times, pitch and loudness). Write a parable that keeps the skeleton (paradox hook, twist at the halfway point, last line as the title) but swaps every tag, counter and prop to fit [topic]. Draw it as an HTML canvas at 1080x1920, `render(t)`, black background with a `rgba(255,255,255,.075)` 44 px dot grid, a dashed ground at y=1330, a white pictogram person, white capsule tags (size 28, weight 700, spacing .14em), counters, typing boxes, checklists, flip cards, a price tag that lands on the spoken number, calendar pages, a cliff and bridge, a desk and clock, a rocket with version badges, a chart, a crowd. Record the voice line by line with a pitch band of 130-165 Hz and a stretch cap of 1.3; pin every beat to word times. Build SFX in four families from the reference's measured envelopes and place them from a logged event list. No colour until the end card, which is the store listing with the real icon. Render frames to ffmpeg (CRF 17), mux with AAC 192k. Give me a contact sheet of every beat before the full render."

## 4. Black-stage "pawn" explainer engine (one JSON spec per video, voice is the clock)

**Short:**

"Make a 40 s pawn-on-black-stage explainer for YOURBRAND: hook 'Tired of [pain]?', one emotional line, the offer, the close, the standard end card. Use the engine and the saved voice; spec JSON plus build."

**Detailed:**

"Write a spec JSON for the pawn engine: lines with `say`, `scene`, and caption pills anchored to spoken words. Look: black stage, dot grid, one spotlight, one white pawn, heavy counters, tracked labels, ember orange for cost and mint for success only. Voice in full sentences, one take, word times from faster-whisper. End on the standard end-card scene (light glass stage, logo animation, 'Your [platform]', site pill). Output 1080x1920 30 fps, loudness -14 LUFS, contact sheet of every scene first."

## 5. Stamped-word feed-scroll brand film (light stage, modelled on a viral UI-concept reel)

**Short:**

"Rebuild this viral UI-concept reel [link] as a 30 s motion graphic for YOURBRAND: same skeleton (stamped words on a post card, feed blur, dark 'just like that' beat, giant slam word, popup with cursor click, notification cards, bracket tags, spotlight joke, quiet end card), our colours and real product screens, a female library voice matched in pitch and pace to the original narrator (not a clone), synthesised music and effects on the cuts, wide and tall."

**Detailed:**

"Download and study the reference (contact sheets at 2 fps, scene cuts with `select='gt(scene,0.25)'`, whisper word times, pitch percentiles with an autocorrelation tracker). Write a 22 s script that keeps its rhythm: [three verbs], 'and just like that, you lose it in the endless feed. But what if [your product did X]? [Three steps]. 'Forever?... Forever.' Build one HTML page with `render(t)` for both layouts. Use the palette and motion constants above. Anchor every cut to word times, 0.02-0.18 s early. Synthesise a 122 BPM bed with ducking. Mux at -16 LUFS. Show me stills of every scene in both layouts before the full render."

## 6. Full-platform product film: real feed scroll, red X, flash cut into a dark glass product tour

**Short:**

"Make the full product film: real feed scroll with a red X, flash cut into a dark liquid-glass tour of both sides of the product, one completed demo state so every number matches, real faces from other creators, end on a CTA slam and an orbit of posts. Wide and tall, 80 s."

**Detailed:**

"Record the real vertical feed on my phone (screen record) and the product's demo views with Playwright at 2x. Build one `render(t)` page. Script [183 words, numbers as words]. Cut sequence: verbs, feed scroll in a phone that speeds up under the slam, red X, grey phone, 'what if the feed worked for you', flash zoom, white hit, dark aurora stage (hex above), tilted windows with glow, callout brackets on key words, tour in this order [list], stats beat, approve click, tracked views, payouts, spotlight joke, launch slam, wordmark with sweep, orbit ring of posts, CTA button with click, typed site. Invented names only; label sample data. Voice at natural pace, mux at -16 LUFS."

## 7. No-voice 3D logo ident (4K 60 fps)

**Short:**

"No-voice 40 s dark 3D ident for YOURBRAND using only the chrome monogram: rim-lit logo sting, typed prompt bar in perspective, dashboards and phones flying through 3D, timeline bars, neon button close-up, quiet kinetic text, back to the logo. 4K 60 fps, wide and tall, synthesised score at -14 LUFS."

**Detailed:**

"Build a 40 s, no-voice, dark 3D ident for YOURBRAND using only the chrome monogram (never the wordmark), modelled on [reference post] (read its caption in the browser; copy its audio hit points at 2.6, 6.1, 9.6, 16.7, 20.2, 30.8, 34.4 s but not the track). Beats: point of light; monogram turns in with blue `#7dd3fc` and violet `#c084fc` rim lights (masked fills with the blur on a wrapper), shine sweep and three rings on the first hit; a glass prompt bar in perspective types a request and flares through the camera; dashboards assembled from transparent 2x card layers fly through 3D beside phones playing real feed frames; timeline bars grow under a scanning playhead; neon-rim Approve button close-up and click; seven phones rise; quiet kinetic text over a light ribbon; monogram alone, last shine, fade. Add grain, vignette and falling bokeh. Serve the page over http because of masks. Render 4K at 60 fps in four parallel slices plus 1080p copies. Synthesise the score (supersaw pad, sub, half-time 808 at 94 BPM with sidechain pump, pluck motif with ping-pong delay, layered impacts, risers, whooshes, real key and click samples, FFT hall reverb) at -14 LUFS. Give stills of each beat before the long render."

## 8. Colour-poster "slam" film (one flat colour per beat, type cropped by the frame)

**Short:**

"A poster film where the whole frame is one flat colour per beat, huge cropped uppercase type, hard cuts on every word, real clips inside the letters, a stutter on 'No', 28 s, 140 BPM hits on words. Product: YOURBRAND."

**Detailed:**

"Write a 27 s script in this shape: an accomplishment ('You made the video. You got the views.'), the humiliating default ('then they say send me your link, and you send... a [cheap template]'), 'No. No, no, no. No!', 'You are not a [bad thing]. You are a business. So look like one.', then product nouns one per beat, brand, call to action. Build a `render(t)` page where each beat is a flat full-bleed colour from `#1E2BFF #FF2A12 #D4FF12 #FF2A8D #0A0A0C #F5F1E4 #7A1FFF #00D97E #FF7A00 #19C2FF`, uppercase condensed black type at line-height .84 auto-fitted to width, words arriving at 1.42x and landing in .1 s then creeping +2.2%/s, hard cuts on word starts, a stutter shake (`sin(t*190)/cos(t*240)` decaying over .22 s) on the No beat, the word VIDEO cut out of a strip of 14 poster tiles, a struck-through link. Synthesise 140 BPM half-time 808 hits locked to words, silence plus a limp note for the bad screen, a five-hit climbing stutter on the No beat. Voice at natural pace, -16 LUFS."

## 9. Ring-of-phones film (3D ring, screen floods with each layout colour)

**Short:**

"A 31 s film with a 3D ring of phones in perspective, a colour flood on each layout change, content pinned while the look swaps via slats, a grey 'everything looks the same' wall for the problem."

**Detailed:**

"31 s wide film, bright library female voice, 100 BPM arpeggio climbing one chord per layout. Opening problem: a grey wall of identical skeleton cards with a ticking clock and a grey drone. Then a ring of 6 real phones in `preserve-3d` perspective (no CSS filters on 3D containers) that fans open and closes; each layout change floods the screen with its colour (`#FF2E88 #FF6A00 #4A12FF #00C795 #FFC400 #0A3CFF`) via a circle growing from the centre; the page swaps through 10 venetian slats while the buyer's videos and numbers stay pinned; a browser scene on the buyer's own domain; end card. Script: 'Every X looks different. So why does every X's link look the same? Here are six ways to look like you...'. Invented cast, 'Sample data' tags."

## 10. Dark-stage "cinema" product film (one light beam, orbiting avatars, tilted windows)

**Short:**

"A 43 s dark-stage product film: one violet accent on near-black, one light beam, orbiting avatars turning into identical grey cards, a phone feed snapping while clip cards fly past the camera, six sites on an arc, a tilted setup demo with word-by-word captions, dashboards on dotted lines, one-click look swaps, end card then a TV switch-off. SF-style bold type, library female voice, 104 BPM bed."

**Detailed:**

"Build the 43 s dark-stage film as 8 acts exactly as the beat sheet above (orbiting avatars to grey cards; the feed scroll with 12 snaps and 28 streaming cards; six phones on an arc; the tilted setup demo with word-by-word captions and an outlined pill word; chips lifting off the page; media-kit phone; three dashboards on dotted lines with a checkmark row; six layout swaps with pinned content; end card in the beam; TV switch-off). Colours ink `#0B0C14`, accent `#8B7CFF`, second `#5B4BE8`, stage `#120E24 -> #07060C`, beam as a blurred rotated gradient band in screen blend, grain at .07. All anchors from word timestamps (+0.3 s offset). Invented names only, real numbers or 'Sample data'. 4K master, 1080p, web copy; mux at -16 LUFS; new filename for the web copy."

## 11. Product-site film family: five more looks

**Detailed:**

"Reference the film we already shipped (same voice, same cast rules) and make three fully different variations for the home page: A light, one continuous camera over a board; B poster slam; C 3D ring of phones. Each needs its own script (22-32 s), palette, type treatment and synthesised bed, word-anchored cuts, tall and wide layouts and a poster frame. Invented creators and domains matching each niche, every section filled in, SF-style bold type everywhere (inject the font into captured UI), no price on screen, no emoji. Render stills first and show me a contact sheet of all three."

## 12. Liquid-glass two-world launch film (16:9, 60 fps)

**Short:**

"41 s liquid-glass launch film for YOURBRAND: light glass world then a black stage via a circle iris, logo animation open and close, pipeline pan, AI review card, one 3D phone posting, whip turns per platform, dashboard, curved wall of 100 phones, 60 fps, anchor every beat to word times."

**Detailed:**

"Two worlds joined by a circle iris: light glass (`#e2e2e3`, pastel aura) and a black stage with one blue floor glow. S1 pills flood outward as the camera pulls back; S2 logo animation then wordmark and a glass pill; S3 pipeline pan with stepper 01-07; S4 AI review (score to 9.2), video drops behind a folder flap, When/Then card with a border beam, dark world opens out of the THEN row; S5 one 3D phone posts; S6 whip turns per platform; S7 screenshots fly into a dark dashboard; S8 three real clips then a curved wall of ~100 phones; S9 close in on the logo. Glass = backdrop blur plus saturate, white film, bright top rim. Gradient on one word per line. No stock footage, no crossfades, no CSS transitions, no `Math.random`, nothing still over 1.2 s. 60 fps, ~2 minute render, 124 BPM D minor bed whose groove starts when the dark world opens, voice at natural pace, -14 LUFS."

## 13. Single-accent-dot keynote-calm launch film (near black, scramble decode)

**Short:**

"27 s keynote-calm launch film modelled on this reel: tiny italic hook, big glowing payoff line, one blue dot threading every scene, chaos of vendor tabs sucked into the dot, a real product page with cursor clicks, a state map lighting up, a 3D prism of screens, a scramble-decode line, logo end card with typed URL. 30 fps, 3 sub-samples."

**Detailed:**

"Use the prompt skeleton `<inputs> <direction> <structure> <build> <gotchas>`. Inputs: product, logo (white-on-transparent, never inverted), accent `#3b82f6 -> #60a5fa`, SF-style type, voice settings, script. Direction: near-black `#030305`, one bottom glow, one blue dot threading all scenes, shots enter already moving and leave on an accelerating move or blur ramp. Structure: S1 hook (small italic with a drawn underline) through S9 wordmark and typed URL as described. Build: pure `render(t)`, voice as clock, demo-account captures at 2x, CSS 3D perspective 1600 px, 1920x1080 at 30 fps with 3 sub-samples, crf 15, -14 LUFS with a 0.63 limiter. Gotchas: no prices or claims in compliance niches, no black gap between payoff and logo."

## 14. Book-opening dark trailer (3D book, four aspect ratios, hook A/B/C)

**Short:**

"Make a dark SaaS-style trailer for a book: a real-looking 3D book opens on a click, the camera pushes into the page, serif kinetic headlines, glass pop-ups with click sounds, a timeline rail, stat tiles, store-button end card. Render 16:9, 9:16, 4:5 and 1:1, long and short cuts, three hook variants, theatrical narrator."

**Detailed:**

"Use the source text as the only source of facts. Build one `render(t)` page with `cut`, `hook` and `voice` query parameters. Storyboard: [beats above]. Stage `#07080b` with grain, vignette and three drifting blobs; gold `#e8b43a`, silver `#cfd4dc`, red `#d8463a`. Book in CSS 3D with perspective 2600, cursor click, `rotateY` open, push-in. Voice with `edge-tts` and pauses written as ellipses. SFX kit plus drone bed. Output all deliverables with posters; list what you could not verify (no one has heard it)."

## 15. Website launch film: typed URL, morph into the browser, sections, key and click sounds only

**Short:**

"29.5 s launch film for yourbrand.com: hook question, search bar zooms, the domain types with keyboard sounds, morph into the real browser, six sections with a matching phone, stats, CTA click, end card; wide and tall; keyboard and click sounds only, no music; SF-style type."

**Detailed:**

"Record yourbrand.com with Playwright (videos blocked, preview flag on) and build a 29.5 s page in 16:9 and 9:16: hook question word by word (0-3.6), search bar zoom (3.6-5.8) with 16 keystrokes at irregular times, ENTER pulse at 5.95, morph into the address bar with a load line (6.1-6.95), six section scenes every ~2.2 s with a cursor click on nav, 2x2 glass stat cards, CTA ripple at 26.2, end card with the domain typed per character. Palette `#f4f5f7`, ink `#0b0c10`, accent `#5b5ce6`, drifting pastel blobs. SF Bold type. Audio: keypress and click samples placed with `adelay`/`amix`, no music; export the cue list from the page so audio follows the picture. Tune layout constants per format from stills and auto-shrink titles."

## 16. White-label "how to set up" walkthrough with a follow camera

**Short:**

"A 35 s walkthrough of the setup wizard with blank placeholder data, a follow camera that zooms to each field as it is filled, cursor clicks, typed text and key sounds, ending on the live site; no prices."

**Detailed:**

"Seed a blank tenant (you@yourname.com, slug yourname), script the real wizard with Playwright (before/after screenshots per field plus click-target coordinates) across ten screens, then build a 34.5 s page with a follow camera that pushes in to the active field, cursor ripples, typed text, progress and a final live site. Use coloured placeholder clips for uploads (`lavfi color` with `-t`). No pricing. Export a cue list and build key and click sounds from it. Report any product bug you find while filming, fix it and re-film."

## 17. Beat-grid promo (every cut on a beat of a fixed BPM)

**Short:**

"32 s promo at 128 BPM: every cut on a beat, kinetic text with video covers between the words, flash-cut niches, logo zoom-through into the dashboard, whip pans, giant case numbers, curtain wipe, end card; energetic voice slotted into beats; 60 fps."

**Detailed:**

"Beat length 0.469 s; put every cut on a beat. Sequence: kinetic text with video covers popping between words, eighth-note flash cuts through niches, logo slam with a camera zoom through the logo into the dashboard, stat cards lifting out of the screen, match cut from a tile to the full wall, whip pans with SVG directional blur, giant case numbers, curtain wipe, button ripple into the end card. Use real covers in every tile (no gradient placeholders). Voice: 11 lines fitted into slots (base speed 1.12, re-render faster up to 1.35x when a line overruns, trim silence). 128 BPM A minor bed with sidechain, impacts on beats 12/40/48/60, whoosh peaks on moves. 60 fps, -16 LUFS."

## 18. Retro-console life-sim cutscene reel (AI keyframes + local image-to-video + real UI composite)

**Short:**

"A 32 s vertical Reel styled as a forgotten early-2000s life-sim cutscene: one locked character (ref attached), 2 am scrolling, fridge, crackers, bed, back to the couch messier, then the real app recording taps the panic button, she breathes out, 2 s brand end card. Pixel captions one at a time. First watch the reference reels fully and tell me what you could not verify. Make the master still first and show me before animating."

**Detailed:**

"Before building anything: play the reference account's reels end to end and extract cuts, captions, loudness and pacing; report what you could not verify. Make the locked character master still with a local image model (three seeds), wait for my pick, then make two seeded keyframes per shot via reference edits with the SAME block, animate each with the local image-to-video model one at a time (704x1280, 24 fps, frame counts 8n+1), generate a green-screen phone plate, track and composite the real app recording (warp per frame, keep thumb on top, retime to the tap), render in the video framework with pixel captions (Press Start 2P, outline via stacked shadows, y 1230, bottom 420 px clear), grain/scanlines/vignette, a clean end card with no store badge, synthesised foley and a tension drone that releases at the tap, voice from my custom voice with two takes per line. Deliver MASTER, CLEAN, PREVIEW, END CARD, STORYBOARD and a QA report."

## 19. Screen-recorded app-demo clips for creators (simulator pipeline)

**Short:**

"For each creator and day, build the demo app from the plan, record it in a clean simulator, cut a 16 s 1080x1920 clip (prompt typed 4 s, two taps 6 s, final tap 6 s) plus component clips, QA with contact sheets, name by the pattern, upload."

**Detailed:**

"Read the plan JSON for [creator] day [n]. Build the app locally, install in a clean simulator with the status bar at 9:41, record with `simctl io recordVideo`, drive taps 1.2 s apart, cut with ffmpeg (app crop `scale=1080:-2,crop=1080:1920:0:150`; prompt crop with pad; typed text sped 2.45x into a 4 s slot; hold frames with `tpad` before `trim`; punch-in on the final tap; `concat`), encode crf 18 silent 30 fps, QA with contact sheets and duration checks against the storyboard slots, remove any other brand's text, upload with the naming pattern and a general-named shared copy, and register the clip in the brief page. Never claim a check passed unless you just saw it."

## 20. Native-UGC-style reels from real recordings (17-video format family)

**Short:**

"Make 3 new organic-style 9:16 videos for [client app]: real screen recordings only, native captions with the spoken word in yellow, handheld wobble, each ends on the store-search CTA. Styles: [A], [B], [C]. Never say it took N prompts; emphasise screenshots and drawings as input."

**Detailed:**

"Client facts re-read from the client site today. Audience 16-25; the feeling is 'I have to try this'. Make 3 videos, 28-35 s, 9:16, each a different style from [list], using only real screen recordings (record the live site with the scripted recorder, or real app builds from a hosted preview with MediaRecorder), TikTok-style captions (white 800, black outline, spoken word `#ffe14d`, chunks of up to 4 words), a slight handheld wobble, tap rings and chips only where they serve the story, and the store-search ending (type the name, real listing pops, finger taps GET, no extra text). Voice: house voice, full sentences, the signature word present. Never say how many prompts it took; do not frame the offer as free templates. Label genres, cut before trademarked titles, flag clone footage for client sign-off."

## 21. Skeptic-and-answer explainer (two-voice objection loop)

**Short:**

"Break this reel down (cuts, word-anchored cuts, pauses, wpm, caption style, CTA) and write a skeptic-and-answer script for [topic] with the same rhythm; build the explainer cards with motion inside the lists."

**Detailed:**

"Download the reel (or use the original file), list every cut with timestamps and which land within 0.1 s of a word start, the pause lengths, words per second, caption style and the CTA staging. Then write a two-voice question-and-answer script for [topic] where the skeptic voices every objection (price, what do I get, where is the catch, credits, who do I share it with) in 2-6 words and the answer is a list, with the question on a recurring human clip and the answer on an animated card with pops on spoken words and ticking counters. Hide topic jumps in a blur whip or a four-flash burst. Last 10 s held on one shot with the CTA acted out."

## 23. Product listing videos from phone footage (batch ffmpeg)

**Short:**

"For each folder of phone clips make a single upright 1080x1920 H.264 video under 55 s and under 9 MB, HDR tonemapped to SDR, no audio; test the rotation on a 3 s sample first and show me a contact sheet."

**Detailed:**

"For each listing folder, concat the clips in file order into one 1080x1920 H.264 video of at most 55 s with no audio, tonemap HDR to SDR (`zscale ... tonemap=hable ...`), letterbox with `pad`, 30 fps, size-target below 9 MB (`kbps = budget*8*1024/duration`, 720p if below 2,300k). Before processing the batch, render a 3 s sample for each rotation variant (`-noautorotate` without transpose, autorotate, autorotate with transpose) and show a contact sheet; choose the one that is upright. Identify products by looking at frames, not by guessing."

## 24. "Day in the life" pain-point-to-solution reel (script template)

**Short:**

"Make a 'day in the life of a [role]' reel for YOURBRAND: three pain points, then discovering the product, a four-step win and a kicker, young conversational female voice sped 1.18x, domain read aloud."

**Detailed:**

"Write the script in the template above (numbers as words, domain as 'yourbrand dot com'), generate one voice take (stability 50, similarity 75), speed it 1.18x, transcribe word times, then build the reel in whichever look fits (pictogram parable, pawn stage or pixel runner) with a pill per pain point, a counter for the failed attempts ('Fifty pitches. Zero replies.'), a stamped REJECTED or GHOSTED on each failure, a four-step checklist animating on the four verbs, and the standard end card."

## 25. Faceless continuous-stage explainer (no cuts, one accent colour, frame-0 hook)

**Short:**

"Make a 40 s faceless explainer for [sub niche] in look [1-9 from FACELESS-EXPLAINER-STYLES.md]: hook complete on frame 0, no cuts, one accent colour, word-timed captions with one accent word per phrase, the problem counted, the idea typed into a neutral prompt box, the result on a phone, then the YOURBRAND store CTA."

**Detailed:**

"Read docs/FACELESS-EXPLAINER-STYLES.md and pick one look. Write a 36 to 40 s first-person script (about 120 to 130 words at 190 wpm) with no product words before the last line; run tools/claim_check.py. Voice it, take word times, then build one render(t) page: dark stage, one accent colour, a counter that moves from frame 0, a new element every 0.5 to 1.5 s, transitions by spring, morph, redraw or circle wipe only (zero cuts), captions in the chosen variant's band with the said word lit, unsaid words dim and one accent word per phrase. Beats: hook on frame 0, problem grows, the idea typed into an unbranded prompt box, chat step rows then the result on a phone, the payoff, the name and the store-native CTA staged for this account, 1.4 s after the last word. Voice plus synthesised hits, no music, -14 to -16 LUFS. Show me a stills sheet before the full render."

## 26. Story-device formats: change the format, not the skin

**Short:**

"Make a 30 to 40 s organic reel for [niche] as the [device] format: the story device is the whole picture, one retention device ([counter]), a real tip, no product words until the last line, and the YOURBRAND store CTA staged inside the device's world."

**Detailed:**

"Pick a story device from FORMATS.md format 26 that no other account of ours uses. Write a first-person script: a named feeling, a specific funny detail, one tip that helps, the product only in the last line (run tools/claim_check.py). Draw everything in code inside the device's world (paper, monitor, map, dashboard) with one on-theme retention device that moves from frame 0 to the end, every line acted out, no pause over 0.3 s, a new element at least every 1.5 s, the bottom third of the frame used, nothing cut off at the edges. End with the store-native CTA (FORMATS.md section L) staged as part of the device (torn receipt, loot drop, final plate) with this account's own closing tag. Stills sheet first, then render, then check the outro frame at full size."

## 27. 3D studio with a mascot (Blender, word-keyed choreography, store product-page CTA)

**Short:**

"Make a 50 s 3D-studio reel for [niche]: an original mascot on a dark truss-lit stage, crash zoom, whip pans, a split-flap money board, a light leak on 'Simple.', a colour flood into the YOURBRAND store product page."

**Detailed:**

"Write a 135 to 150 word first-person script (pain first, one real tip, the product only in the last line). Draw the 2D assets (phone screens, monitors, pop-ups, notepad, pedestal cards) in one HTML page and render them to textures. Build the Blender scene with an original mascot and key every camera move and prop to word times from the voice (crash zoom, whip pan with blur, split-flap board, modal spring, shake, zoom-through, light leak, colour flood). Render in 120-frame chunks in fresh processes, composite with grain and vignette, synthesise a 100 BPM bed with a riser into the CTA, master at -14 LUFS, and end on the store product page with the live listing facts."

## 28. Low-poly 3D first-person "day in the life" series

**Short:**

"Make the next part of the low-poly day-in-the-life series for YOURBRAND: a new creator, a new setting, a fresh pain, one real feature at the midpoint, a callback, about 40 s."

**Detailed:**

"Read pipelines/day-in-the-life/ (playbook and episode log) and pick a pain, setting, gag, payoff feature and callback no earlier part used (a new name and outfit on the same story counts as a repeat). Write ~540 characters for the female voice or ~580 for the male one, voice it, take word times, fill the previous part's page with the new words, caption groups and beats, write the new room, outfit, props, product sheets and camera shots, check a stills sheet, write the sound recipe, render, mux at -16 LUFS with the level=false limiter, and check the 1 fps contact sheet before calling it done."
