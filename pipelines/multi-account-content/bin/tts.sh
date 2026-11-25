#!/bin/bash
# ElevenLabs text-to-speech for the multi-account pipeline (optional cloud voice; local voices live in pipelines/voice).
#
# The API key is never stored in this repo, a file, a prompt or a log. It is read at run time from, in order:
#   1. the OS keychain:  macOS `security` (service $TTS_KEYCHAIN_SERVICE, account $TTS_KEYCHAIN_ACCOUNT)
#                        Linux `secret-tool` (service $TTS_KEYCHAIN_SERVICE, account $TTS_KEYCHAIN_ACCOUNT)
#   2. the environment:  ELEVENLABS_API_KEY
# Store it once, outside any chat:
#   macOS:  security add-generic-password -s motion-kit-elevenlabs -a ELEVENLABS_API_KEY -w
#   Linux:  secret-tool store --label="ElevenLabs" service motion-kit-elevenlabs account ELEVENLABS_API_KEY
#
# Usage: tts.sh <voice alias | VOICE_ID> <script.txt> <out.mp3> [model]
#   Voice aliases come from voices.local.json next to this pipeline (git-ignored; copy voices.example.json).
#   Model defaults to $TTS_MODEL or eleven_multilingual_v2; check the provider's docs for current model ids.
#   Settings: $TTS_STABILITY (0.5) and $TTS_SIMILARITY (0.75). Speed-up is done afterwards in the mix (ffmpeg atempo).
# Also writes <out>.timestamps.json (character timings), usable instead of a transcription for word-timed captions.
# Several agents can call this at once: it is a plain HTTPS request with no shared state.
set -euo pipefail
V="${1:?voice alias or id}"; IN="${2:?script.txt}"; OUT="${3:?out.mp3}"
MODEL="${4:-${TTS_MODEL:-eleven_multilingual_v2}}"
SERVICE="${TTS_KEYCHAIN_SERVICE:-motion-kit-elevenlabs}"; ACCOUNT="${TTS_KEYCHAIN_ACCOUNT:-ELEVENLABS_API_KEY}"
HERE="$(cd "$(dirname "$0")/.." && pwd)"

# alias -> voice id
if [ -f "$HERE/voices.local.json" ]; then
  ID=$(python3 -c 'import json,sys;d=json.load(open(sys.argv[1]));v=d.get(sys.argv[2]);print(v["id"] if isinstance(v,dict) else (v or ""))' "$HERE/voices.local.json" "$V")
  [ -n "$ID" ] && V="$ID"
fi

K=""
if command -v security >/dev/null 2>&1; then K=$(security find-generic-password -s "$SERVICE" -a "$ACCOUNT" -w 2>/dev/null || true); fi
if [ -z "$K" ] && command -v secret-tool >/dev/null 2>&1; then K=$(secret-tool lookup service "$SERVICE" account "$ACCOUNT" 2>/dev/null || true); fi
[ -z "$K" ] && K="${ELEVENLABS_API_KEY:-}"
[ -z "$K" ] && { echo "No ElevenLabs key: store one in the keychain (see the header of this file) or set ELEVENLABS_API_KEY." >&2; exit 1; }

BODY=$(python3 -c 'import json,sys,os;print(json.dumps({"text":open(sys.argv[1]).read().strip(),"model_id":sys.argv[2],"voice_settings":{"stability":float(os.environ.get("TTS_STABILITY","0.5")),"similarity_boost":float(os.environ.get("TTS_SIMILARITY","0.75"))}}))' "$IN" "$MODEL")
RESP=$(mktemp)
code=$(curl -s -o "$RESP" -w "%{http_code}" -X POST "https://api.elevenlabs.io/v1/text-to-speech/$V/with-timestamps?output_format=mp3_44100_128" \
  -H "xi-api-key: $K" -H "Content-Type: application/json" --data-binary "$BODY")
unset K
[ "$code" = 200 ] || { echo "ElevenLabs HTTP $code: $(head -c 300 "$RESP")" >&2; rm -f "$RESP"; exit 1; }
python3 - "$RESP" "$OUT" <<'PY'
import json, sys, base64
d = json.load(open(sys.argv[1]))
open(sys.argv[2], 'wb').write(base64.b64decode(d['audio_base64']))
json.dump(d.get('alignment') or {}, open(sys.argv[2] + '.timestamps.json', 'w'))
print('wrote', sys.argv[2])
PY
rm -f "$RESP"
