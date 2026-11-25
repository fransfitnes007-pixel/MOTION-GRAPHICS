# <account> — account pack

Copy this file to `accounts/<account>.md` (one per account; real account files are git-ignored). The agent that runs
this account reads it first on every turn. Never put passwords, session cookies, phone numbers or API keys here.

## Account
- Account: <account>
- Platforms: TikTok <@handle> · Instagram <@handle> · YouTube <@handle> · X <@handle>
- Cleared to post: no            (the poster queues nothing until an account is cleared)
- Wide videos go to: X only       (tall 1080x1920 goes to TikTok, Reels, Shorts, Facebook, Snapchat)

## Niche
- Niche: <Study>
- Interests: <comma separated>
- Tone: <comma separated, e.g. Relatable, Funny, Calm>
- Audience: <who every video is for, in one line>
- Claim rules: <what may never be said, e.g. no money promises, no betting, no real brand names>
- Reference video: <link to the video whose format this account copies, or empty>

| # | Sub niche | Drop folder |
|---|---|---|
| 1 | <Sub niche one> | `<path to its drop folder>` |
| 2 | <Sub niche two> | `<path>` |
| 3 | <Sub niche three> | `<path>` |
| 4 | <Sub niche four> | `<path>` |
| 5 | <Sub niche five> | `<path>` |

`bin/account-info.sh <account>` prints these fields as JSON (or calls your own lookup through `ACCOUNT_INFO_CMD`).

## FORMAT LOCK
Write here only what the owner approved on the test video. This is what makes video N+1 match video N; keep it current.
- Reference look (what to copy one to one, read with eyes and scrapey that day):
- Voice (alias from voices.local.json, model, stability, similarity, speed-up):
- Length / aspect / fps:
- Beat structure with timings (hook, problem, turn, proof, callback, CTA/end card):
- Captions (font, weight, size, position, highlight colour):
- Colours, type, motion rules, library pieces used (slugs):
- Sound (effects only / bed / loudness target):
- Per sub niche: the idea shown, the hook line:
- End card / CTA:
- Caption + hashtag rule:
- Approved example videos (paths):
- Last good build (the folder the next video is copied from):

## Log
One line per video: date · sub niche · topic · setting/gag · voice + speed · dropped file name · what the owner changed.
- 
