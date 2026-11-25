---
name: multi-account-content
description: "Run several social accounts from the kit: one session per account, a locked format per account, and a GO that makes one finished vertical video per sub niche with parallel subagents, checks each, and drops caption and video into the folder the posting system watches. Use when the user manages many accounts, says GO in an account session, or asks to batch videos per niche."
---

# Multi-account content

`KIT` is the repository root, two folders up from this skill. Everything lives in
`KIT/pipelines/multi-account-content/` (call it `P`). Read `P/PLAYBOOK.md` once per session; it is the method.

## In an account session
1. Read `P/accounts/<account>.md` (FORMAT LOCK and Log). If it does not exist, copy `P/accounts/_TEMPLATE.md` and fill
   it in with the owner. `P/bin/account-info.sh <account>` prints the account's facts as JSON.
2. **No FORMAT LOCK yet:** read the reference video with eyes and scrapey (`KIT/docs/EYES-AND-SCRAPEY.md`), make ONE test
   video (PLAYBOOK section 4), take corrections until the owner approves, then write the lock.
3. **GO:** follow PLAYBOOK section 7: scripts in the main session, voices, one subagent per video on a cheaper model
   (at most one per sub niche, 2 or 3 full renders at once per machine), check every contact sheet yourself, drop
   with `P/bin/drop.sh`, log, report, end with `Say "GO" for the next batch.`

## Rules
- Voices: `P/bin/tts.sh` reads the key from the OS keychain or the environment inside the command. Never write a key to
  a file, prompt, commit or log; never print it. Local voices first when the owner has not chosen a cloud voice.
- Never post directly, never touch accounts' logins or devices. Being in the drop folder is the approval.
- Never edit a library piece in place: copy it into the build.
- Several account sessions may run at once: follow `KIT/AGENTS.md` (own build folder, locks for shared resources,
  one index rebuild at the end).
- Motion: `KIT/docs/MOTION-RULES.md` for timings, easing, cut rates and the 15-second recipe.
- Anything new and reusable goes back into `KIT/library` white-labelled (`engine/SKILL-SPEC.md`).
