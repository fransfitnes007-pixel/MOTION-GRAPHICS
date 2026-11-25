#!/bin/bash
# Account facts for one account, as JSON, read-only.
#
# This is an adapter. Out of the box it reads the account's own file, accounts/<account>.md, and prints the fields the
# GO routine needs. If your accounts live in a database or a CRM, point ACCOUNT_INFO_CMD at your own read-only script:
#   export ACCOUNT_INFO_CMD="/path/to/my-account-lookup"      # called as: $ACCOUNT_INFO_CMD <account>
# It must print one JSON object with (at least) these keys:
#   {
#     "account":     "example-account",
#     "niche":       "Study",
#     "sub_niches":  ["Exam cramming", "Flashcards", "..."],     # one video per sub niche per GO
#     "interests":   ["..."],  "tones": ["..."],
#     "reference_url": "https://... (the reference video the format copies, or null)",
#     "drop_folders": {"Exam cramming": "/path/to/drop/folder", "...": "..."},
#     "platforms":   [{"platform": "tiktok", "handle": "@...", "cleared": false}]
#   }
# Keep credentials out of the output: this is read by agents and may end up in transcripts.
#
# Usage: account-info.sh <account>
set -euo pipefail
A="${1:?account name}"
[[ "$A" =~ ^[A-Za-z0-9._-]+$ ]] || { echo "bad account name" >&2; exit 2; }
if [ -n "${ACCOUNT_INFO_CMD:-}" ]; then exec "$ACCOUNT_INFO_CMD" "$A"; fi
HERE="$(cd "$(dirname "$0")/.." && pwd)"
F="$HERE/accounts/$A.md"
[ -f "$F" ] || { echo "no $F: copy accounts/_TEMPLATE.md to accounts/$A.md and fill it in" >&2; exit 1; }
python3 - "$F" "$A" <<'PY'
import json, re, sys
t = open(sys.argv[1]).read()
def field(name):
    m = re.search(r'^- ' + re.escape(name) + r':[ \t]*(.*)$', t, re.M)
    return (m.group(1).strip() or None) if m else None
rows = re.findall(r'^\|\s*\d+\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|', t, re.M)
subs = [r[0] for r in rows]
print(json.dumps({
    'account': sys.argv[2],
    'niche': field('Niche'),
    'sub_niches': subs,
    'interests': [x.strip() for x in (field('Interests') or '').split(',') if x.strip()],
    'tones': [x.strip() for x in (field('Tone') or '').split(',') if x.strip()],
    'reference_url': field('Reference video'),
    'drop_folders': {r[0]: r[1].strip('`') for r in rows if r[1]},
}, indent=2))
PY
