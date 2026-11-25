# Multi-account content pipeline

Run many social accounts from one kit: each account has its own agent session, its own locked format and five sub
niches; one word ("GO") makes one finished vertical video per sub niche, built by parallel subagents, checked, and
dropped into the folder your posting system watches. White-label: nothing here names a brand, a person or a service
account. Your accounts, voices and folders stay in git-ignored local files.

## How it works
1. **One session per account.** Name the session after the account. It reads `PLAYBOOK.md`, its own
   `accounts/<account>.md`, `KIT/docs/MOTION-RULES.md`, and the library index.
2. **Dial in one test video.** Give it the specifics: the reference video, the voice, the formats, each sub niche's idea
   and hook. It reads the reference with eyes and scrapey (`KIT/docs/EYES-AND-SCRAPEY.md`), makes ONE test video, and
   you correct it until it is right.
3. **Lock it.** It writes what you approved into the FORMAT LOCK of `accounts/<account>.md`.
4. **GO.** It writes one script per sub niche, makes the voices, sends one subagent per video to build in parallel,
   checks every contact sheet itself, drops caption + video into each sub niche's folder, logs them, and reports.
   Then move to the next account's session. Several account sessions can run at the same time (see `KIT/AGENTS.md`).

## Files
| Path | What it is |
|---|---|
| `PLAYBOOK.md` | The production method: proven format, voice, build steps, hand-off, checks, the GO routine, pitfalls |
| `accounts/_TEMPLATE.md` | The account pack: platforms, niche, five sub niches with drop folders, FORMAT LOCK, Log |
| `accounts/order.example.json` | The order to work through accounts in |
| `voices.example.json` | Voice aliases for `tts.sh`; copy to `voices.local.json` |
| `bin/tts.sh` | ElevenLabs voice with timestamps; key read from the OS keychain or the environment, never from a file |
| `bin/account-info.sh` | Account facts as JSON: reads the account file, or your own lookup via `ACCOUNT_INFO_CMD` |
| `bin/drop.sh` | Copy caption then video into a drop folder, safely named, never overwriting |
| `tools/word_times.py` | Script-guided word times (faster-whisper), tidied for captions, with a mismatch check |
| `tools/fill_beats.py` | Pin a scene page to a new take: words, caption groups, beat times, scene, end lines |
| `tools/sheet.py` | Tile render stills into one sheet to look at |
| `tools/check_video.sh` | Duration, loudness, black frames, 1 fps contact sheets |

## Set up
```bash
cd pipelines/multi-account-content
cp accounts/_TEMPLATE.md accounts/my-account.md            # one per account; fill it in
cp voices.example.json voices.local.json                    # optional, for the cloud voice
security add-generic-password -s motion-kit-elevenlabs -a ELEVENLABS_API_KEY -w   # macOS, optional; Linux: secret-tool
bin/account-info.sh my-account                               # check the account file parses
```
Requirements: the kit's own (Node 18+, Python 3.9+, ffmpeg, Chrome), plus `pip install faster-whisper pillow` for the
tools. The cloud voice is optional; `KIT/pipelines/voice` is the free local route.

## Then
In the account's session: `/go my-account` (or just "GO" once the FORMAT LOCK is filled in).

## Privacy
`accounts/*.md` (except the template), `voices.local.json` and `builds/` are git-ignored. Keep logins, device ids,
phone numbers, keys and folder ids out of every committed file. `bin/account-info.sh` output is read by agents, so
it must never contain credentials.
