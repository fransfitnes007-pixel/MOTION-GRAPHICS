# Agents: how to work in this repository, several at once

This kit is built to be driven by agents (Claude Code sessions, subagents, other coding agents), many at the same time.
Read this before you change anything.

## What to load
- The skills in `skills/` (they load automatically when the kit is installed as a plugin). Start from `reel-maker` for
  one video, `multi-account-content` for batches across accounts, `motion-library` to find a piece, `eyes-and-scrapey`
  before reading any reference.
- Rules: `docs/MOTION-RULES.md` (timings, easing, cut rates, the 15-second recipe) and `docs/EYES-AND-SCRAPEY.md`.
- The library: `python3 engine/tools/find_skill.py <words>`, or `library/INDEX.md`.

## Working in parallel
1. **One build folder per agent.** Every video is built in its own folder (for example
   `pipelines/multi-account-content/builds/<account>/<MMDD>-<n>-<slug>/`). Two agents never write the same folder.
2. **The library is read-only during builds.** Copy a piece into your build and change its `CONFIG` there. Adding a new
   piece is a separate, single-agent step (below).
3. **Shared resources take a lock.** Anything only one agent can use at a time (a shared browser tab, a web app's text
   box, a physical device) is guarded by a directory lock: `mkdir <dir>/.<name>.lock` succeeds for one agent only;
   `rmdir` it when done. While it is held, do other work (scripts, scenes, stills) and try again later. To wait, use a
   until-loop on the condition, never a timer that wakes a model.
4. **Cap heavy renders.** A full `render_demo.cjs video` runs a headless Chrome for minutes. Keep 2 or 3 at once per
   machine; stills are cheap and can run freely.
5. **APIs are parallel-safe.** `pipelines/multi-account-content/bin/tts.sh` and other API calls have no shared state.
6. **Subagents get a full brief.** Their build folder, inputs, the steps to follow (by file and section), what not to
   touch, and exactly what to return (paths to stills and contact sheets, length, loudness, anything unfixed). The lead
   agent checks every result itself before calling it done.
7. **Use the cheaper model for mechanical steps** (filling beats, rendering, muxing, checks); keep writing and judging
   on the main session.

## Adding to the library (one agent at a time)
Follow `engine/SKILL-SPEC.md`, then:
```bash
node engine/tools/make_posters.cjs <slug>
node engine/tools/verify_library.cjs <slug>
python3 engine/tools/build_index.py        # one agent rebuilds the index, at the end
```
White-label always: placeholder copy (`YourBrand`, `yourbrand.com`, `@yourbrand`), no client or person names, no
footage you do not own. Credit outside authors in `meta.json` (`credit`) and `THIRD_PARTY_NOTICES.md`. Pieces derived
from a source with no licence shown, or from a site whose terms forbid building a library from it, stay out.

## Before a commit
- Scan the staged diff for brand, client and person names, handles, ids, hostnames, emails and keys; fix any hit.
- No video files in `library/` (`*.mp4` is git-ignored); posters only. Keep large media out unless the README needs it.
- Never commit `.env` files, `voices.local.json`, account files or builds.
