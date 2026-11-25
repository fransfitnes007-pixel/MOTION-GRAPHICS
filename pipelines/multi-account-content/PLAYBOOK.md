# Playbook: short-form motion-graphic videos for many accounts at once

Read this first in every account session. It is the production method distilled from a series of more than forty
finished 40-second vertical videos, written so any team can run it for any set of accounts. `KIT` is the repository
root. `P` is this folder (`KIT/pipelines/multi-account-content`).

Each account's own facts (platforms, niche, five sub niches, drop folders, FORMAT LOCK, log) are in
`P/accounts/<account>.md`. Live values: `P/bin/account-info.sh <account>`.

Per brand, also keep (templates in `P/templates/`, filled copies stay local in `P/research/`, which git ignores):
- **A look file** for the brand's accounts: which house rules apply and each account's look at a glance. For faceless
  explainer accounts start from `KIT/docs/FACELESS-EXPLAINER-STYLES.md` (ten house rules, nine measured looks).
- **`research/<account>/BREAKDOWN.md`** per account: its reference read frame by frame (`templates/BREAKDOWN.md`).
- **`PRODUCT-FACTS.md`**: every product fact a video may show, with its source. Not in the file = not on screen
  (`templates/PRODUCT-FACTS.md`).
- **`SHARED-PIECES.md`**: pieces several accounts need (caption engine, prompt box, rigs, store CTA); claim one before
  building it, build it once (`templates/SHARED-PIECES.md`).
The look file and the FORMAT LOCK win over section 1 for the look; keep section 1's pipeline (render, word-timed
captions, sound recipe, checks, hand-off).

---

## 1. The proven format (an example of a FORMAT LOCK, not a rule)

| Item | Value that worked |
|---|---|
| Length | 39 to 41.5 s: about 35 s of voice, then a 5 s end card (`T.dur = T.end + 5`) |
| Aspect / size / fps | 9:16, 1080x1920, 30 fps (`render_demo.cjs` default) |
| Look | one scene page where every frame is `render(t)`: a cut-away 3D room (three.js low-poly) or flat UI, hard cuts on word times |
| Narration | first person, dry humour, short declarative sentences, about 95 to 105 words |
| Captions | word-timed, centred at 64% of the height, heavy sans UPPERCASE with a black stroke (0.2 x size); the word being said in a highlight colour, said words white |
| Safe area | x 70 to 1010, y 250 to 1480 (platform buttons cover the rest) |
| 2D overlays | pills that count the pain up, one big rotated stamp, the product's own screen on a floating sheet |
| Sound | voice + synthesised effects (whoosh, thud, pop, ding, stamp, room hum, a chord on the turn and the end card), no music, -16 LUFS |
| Voice | a cloud voice at stability 0.5 / similarity 0.75, sped up 1.1x to 1.3x in the mix |
| End card | the brand's mark, two short lines, the site in a pill (or an App Store style CTA) |

### Beat structure (every video followed it)
1. 0 to ~3.5 s: the series line ("Day in the life of ... Part N") with the character in the room.
2. ~3.5 to 16 s: the pain, told as one visual joke that gets worse (pills and stamps count it up).
3. ~16 s: a new low point, never a repeat of an earlier one.
4. ~17 s: the turn. The product appears (logo coin + flash, the light turns warm).
5. ~18.5 to 25 s: one real product feature on the floating sheet, block by block.
6. ~25 to 29 s: the character using it; the problem is gone.
7. ~29 to 32 s: "No X. No Y." Two props swatted off screen.
8. ~32 to 35 s: a callback that belongs to this episode.
9. last 5 s: end card.

### Rules that kept the series good
- One finished video per instruction; all creative decisions are the agent's. Finish with the next prompt to send.
- Every video gets a new situation and a new pain; a new name and outfit on the same story counts as a repeat. Similar
  videos are fine when they hit a different top, middle or bottom of funnel pain.
- Around the midpoint, show one real product feature that answers what just happened. Check it in the real product
  that day before scripting it.
- No prices, rates, payout dates, view counts or results. No real brand names, logos or people: invent names.
  Never show a product claim as a number.
- Name videos in sequence in one folder only.
- Some brands hold back the product until the last line (organic content). Then the turn at beat 4 becomes a tip, and
  the product name, site or App Store CTA lands only at the end. Decide which per account in its FORMAT LOCK.
- Leave at least 1.4 s after the last word so the CTA can be read.
- **Organic accounts:** no product words ("app", "build", "made it", the brand) before the last line, and never a price,
  "free", a money promise or a disclaimer line. `P/tools/claim_check.py script.txt --hold --brand "<name>" --chars <min> <max>`
  must print `clean` before any voice is made.
- **A new account changes the format, not only the skin**: who tells the story, where the camera is, the story device
  and its retention device (`KIT/docs/FORMATS.md` formats 25 and 26). Accounts that shared one skeleton (narrator,
  centred karaoke caption, corner counter, phone, the same outro) read as one creator and two were rejected as ad-like.
- **Store CTA:** read the listing that day (`P/tools/store_lookup.sh <app id>`) and pass the live name and numbers in;
  each account has its own staging and closing tag (`KIT/docs/FORMATS.md` section L). Keep the table of stagings taken
  in `PRODUCT-FACTS.md`.

---

## 2. Where things live

| What | Path |
|---|---|
| Animation library | `KIT/library/` (`INDEX.md`, `LIBRARY.html`, `catalog.json`) |
| Find a piece | `python3 KIT/engine/tools/find_skill.py <words>` |
| Render | `node KIT/engine/tools/render_demo.cjs video|still ...` (Chrome via Playwright; every frame = `window.render(t)`) |
| Voice | `P/bin/tts.sh` (cloud, key from the OS keychain) or `KIT/pipelines/voice` (local) |
| Word times | `P/tools/word_times.py` (faster-whisper with the script as prompt) |
| Fill a build | `P/tools/fill_beats.py` |
| Stills sheet | `P/tools/sheet.py` |
| Checks | `P/tools/check_video.sh` |
| Claim rules | `P/tools/claim_check.py` (hold rule, bans, character count) |
| Store listing facts | `P/tools/store_lookup.sh <app id>` (public lookup, no key) |
| Templates | `P/templates/` (BREAKDOWN, PRODUCT-FACTS, SHARED-PIECES) |
| Looks and rules | `KIT/docs/FACELESS-EXPLAINER-STYLES.md`, `KIT/docs/MOTION-RULES.md`, `KIT/docs/FORMATS.md` |
| Hand-off | `P/bin/drop.sh` |
| Builds | `P/builds/<account>/<MMDD>-<n>-<sub-niche-slug>/` (git-ignored), same `code/` + `media/` layout as a library piece |

Pulling a library piece: read its `SKILL.md`, `code/demo.html` and `media/poster.jpg`, then copy what you need into the
build. Never edit a library folder to customise it: change `CONFIG` in your copy.

---

## 3. Voice

Cloud (optional, the owner's own key):
```bash
P/bin/tts.sh female script.txt code/voice/take1.mp3      # alias from voices.local.json, or a voice id
```
The key is read from the OS keychain (service `motion-kit-elevenlabs`, account `ELEVENLABS_API_KEY`) or the
`ELEVENLABS_API_KEY` environment variable inside the command. Never write it to a file, prompt, commit or log, and never
print it. It also writes `take1.mp3.timestamps.json` (character timings). Each agent can call it in parallel.

Local (free): `KIT/pipelines/voice` (see the `voiceover-local` skill).

Script length and speed (learned over 40+ videos):
- About 490 to 550 characters for a calm female voice, 570 to 590 for an energetic male voice, for ~37 s. Short choppy
  sentences make some voices slower.
- Speed = raw seconds / 37, kept between 1.1 and 1.3. If a take is too long even at 1.3x, cap the pauses at 0.3 s first.
  `ffmpeg -i take.mp3 -af atempo=1.13 -ar 48000 -ac 1 take.wav`
- Spell for the voice: "P O V", "dot net", brand names split the way they are said.
- Make two takes, keep the better one. Only use a cloned voice of a person who gave permission (an instant clone of a
  TV character was flagged as a legal and endorsement risk and not used).
- Spell letters with spaces ("F Y P", "U S B", "D Ms"); write years as words for the voice and digits in the caption;
  merge a spaced initialism back into one caption word.
- Stock (premade) voices can be retired by the provider: before a long series, check, and prefer a voice-library voice
  id; write the id and settings into the FORMAT LOCK.

If the only way to a voice is a web app shared by several sessions, take a lock before using it
(`mkdir <shared>/.voice.lock`, `rmdir` after), save and restore whatever text and voice were in the box, and do script
and scene work while you wait. Never wait on a timer.

---

## 4. Build one video

```bash
P=KIT/pipelines/multi-account-content; B=$P/builds/<account>/<MMDD>-<n>-<slug>; PREV=<last good build>
mkdir -p "$B/code/voice" "$B/media" && cp -R "$PREV"/code/{fonts,*.js} "$B/code/" 2>/dev/null
```
1. **Story check.** Read the FORMAT LOCK and the Log. Pick a topic, setting, gag, payoff and callback not used yet.
   Write `script.txt`; run `python3 $P/tools/claim_check.py script.txt --chars <min> <max>` (add `--hold --brand <name>`
   for accounts that hold the product back) until it prints `clean`.
2. **Voice:** two takes into `$B/code/voice/`, then `atempo` to wav (section 3).
3. **Word times:** `python3 $P/tools/word_times.py take1.wav script.txt words.json --drop-last 2` until it prints
   `mismatch: []` (drop the trailing words the end card shows instead).
4. **Beats:** write `beats.json` (beat name -> word index, caption groups of 1 to 7 words, single punch words at 1.5 to
   1.6 size), then `python3 $P/tools/fill_beats.py beats.json words.json $PREV/code/demo.src.html $B/code --scene scene.js`.
   `scene.js` is this video's set: room, character outfit, props, sheets, camera shots, `state(t)`. Start from the
   previous video's scene and change the set, outfit, gags and sheets.
5. **Stills, then look.** `node KIT/engine/tools/render_demo.cjs still $B/code/demo.html stills "1.2,3,4.6,...,38" 1080 1920`
   then `python3 $P/tools/sheet.py stills 7` and read `stills/sheet.jpg`. Fix faces hidden by props, anything in the
   caption band, framing. Re-render only the times you changed. Two or three rounds is normal.
6. **Sound.** Copy the previous `code/recipe.py`, set its `DUR` and beat times from `T.json`, rewrite the cues for the new
   gags, no music. Master: soft clip (`tanh`), peak 0.89, 0.5 s fade. `python3 recipe.py ../media/sound.wav`.
7. **Render and mux:**
```bash
node KIT/engine/tools/render_demo.cjs video $B/code/demo.html $B/media/silent-tall.mp4 1080 1920
cd $B/media && ffmpeg -v error -y -i silent-tall.mp4 -i sound.wav -vf "scale=in_range=pc:out_range=tv,format=yuv420p" -color_range tv \
  -c:v libx264 -preset medium -crf 17 -af "loudnorm=I=-16:TP=-2:LRA=11,alimiter=limit=0.8:level=false:attack=2:release=40" \
  -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart clip-tall.mp4
ffmpeg -v error -y -ss 6 -i clip-tall.mp4 -frames:v 1 -q:v 3 poster.jpg
```
   The `level=false` limiter matters: with `level` on, sharp effects push the peak back to 0.0 dB.

---

## 5. Hand-off to the poster

The posting system (a phone farm, a scheduler, a social tool) watches one folder per sub niche. A typical watcher:
posts the next unused video in each folder at that sub niche's daily time, oldest first, then by name; renames it
with the date it posted; reads a `.txt` with the same base name as the caption (or drafts one); ignores names that
start with `.` or `_`, files still being written (modified in the last ~45 s) and videos already posted on that account
(content hash). So:
```bash
P/bin/drop.sh $B/media/clip-tall.mp4 "<sub niche drop folder>" "<account>-<sub-niche-slug>-<MMDD>-<n>" caption.txt
```
Never post directly, never touch the accounts' logins or devices. Being in the folder is the approval, so drop only
finished, checked videos.

---

## 6. Checks before a video counts as done
- `P/tools/check_video.sh $B/media/clip-tall.mp4 <scratch>/contact` and read every contact sheet tile: faces behind
  props, text under the caption band, cut-off sheets, a black or empty frame, a readable end card.
- Length 39 to 41.5 s (or the FORMAT LOCK's); at least 1.4 s after the last word when the CTA must be read.
- `mean_volume` about -19.5 to -20.5 dB, `max_volume` about -2 dB, never 0.0 dB.
- `mismatch: []` from word times; captions match the voice in a few stills.
- Every product feature or fact shown was checked that day and is in `PRODUCT-FACTS.md`; store name and numbers come
  from `store_lookup.sh` that day.
- The outro frame read at full size: nothing cut off at the edges, no label over the phone, a split-flap or counter
  landed on its final value.
- Say in the report that nobody has listened to the mix.

---

## 7. The GO routine (one GO = one video per sub niche)

The owner dials in one test video with the account's agent until it is right; the agent writes it into the FORMAT
LOCK. After that "GO" is the whole prompt.

1. **Read** the account file (FORMAT LOCK + Log), `bin/account-info.sh <account>` if anything may have changed, and the
   listing facts the end card shows (`P/tools/store_lookup.sh`). Count unused videos already waiting in each drop folder.
2. **Write the scripts** in the main session, one per sub niche, each a topic not in the Log. Run the claim check and
   the character count for the locked voice.
3. **Voices.** With the API they run in parallel. Through a shared web app they run one after another under a lock.
4. **Build in parallel with subagents**, at most one per sub niche, on a cheaper model for the mechanical work. Brief
   each with: its build folder, script, takes, the previous build to copy, sections 4 and 6 of this file, the FORMAT
   LOCK, and "do not touch the browser, the drop folders or the poster". Each returns: the stills sheet path, the
   contact sheet paths, length, mean/max volume, and anything it could not fix.
   Keep to 2 or 3 full renders at once per machine (each runs a headless Chrome for minutes).
5. **Check each video yourself** (section 6). Look at every contact sheet, not just the subagent's word. Send back any
   that fail.
6. **Deliver** (section 5): caption, then video, into the right sub niche folder.
7. **Log** one line per video in the account file. If a piece became reusable, add it to `KIT/library` (white-labelled,
   `engine/SKILL-SPEC.md`) and rebuild the index.
8. **Report** plainly: the videos (sub niche, what happens, length), what the owner might change, what was not
   checked, and end with `Say "GO" for the next batch.`

Ask only when truly blocked (a sign-in, a claim you cannot verify, a format choice the owner has not made).

---

## 8. Pitfalls and fixes
- **Whisper mishears** without the script: always pass the exact script as the prompt; drop the trailing site words,
  fix zero-length words and overlaps (`word_times.py` does all three).
- **Captions hide things:** keep sheet content out of the caption band (canvas y about 660 to 900 on 1080x1920); put
  stamps at y 960 to 975 or above 650.
- **Props block faces:** lower or move the prop, or re-aim the camera; check in stills before the full render.
- **Rotating a group hides a mesh** (a laptop screen): keep the screen mesh visible and hide only the lid.
- **Cameras too close:** pull back; widen for lying-down shots.
- **Peak at 0.0 dB:** limiter with `level=false`.
- **A voice too slow** (650 characters ran 56 s raw): cap pauses at 0.3 s, then 1.3x; next time write 510 to 540.
- **One-line `while` loops** in the sound recipe broke a render: write loops on several lines.
- **Paths with spaces:** quote everything; delete only literal absolute paths.
- **Long 3D renders crash** (Blender route): render in 120-frame chunks in fresh processes and redo missing frames.
- **Drop folders:** names starting with `_` or `.` are ignored; a file is not picked until it has settled; the same
  video is never posted twice on an account.
- **Shared voice web app:** restore the exact text that was there, not a habitual default.
- **Library hygiene:** never edit a library piece in place; copy it.
- **Whisper tail:** a take's transcript can end with a hallucinated "Thanks for watching"; check the last words and drop
  it, or use the other take.
- **Browser extension drops mid-Generate** (web-app voice route): reconnect once to the same tab; the takes usually
  finished and can still be downloaded. Open a dialog and act in one batch when it closes between calls; confirm the
  chosen voice before Generate.
- **Hard-coded listing facts go stale:** a store name changed between two batches and the CTA kit still showed the old
  one. Pass live facts in as parameters.
- **Sparse scenes:** a small character on an empty stage with the bottom third empty read as cheap; fill the frame like
  the references do (an element at least every 1.5 s, the stage used edge to edge above the platform UI).
- **Loudness:** faceless explainer references sit at -14 to -16 LUFS; the low-poly series masters at -16. Pick one per
  account and write it into the FORMAT LOCK.
