#!/usr/bin/env bash
# Submit a job to a queue-style generation API, poll, and print the result JSON.
# Example provider: fal.ai queue. Bring your own key: export FAL_KEY=...
# Usage: queue_job.sh <model-path> <input.json> [out.json]
#   e.g. queue_job.sh <vendor>/<model> input.json result.json
set -euo pipefail
: "${FAL_KEY:?set FAL_KEY in your environment (never commit it)}"
BASE="https://queue.fal.run/"
model="$1"; input="$2"; out="${3:-result.json}"
if [[ ! "$model" =~ ^[A-Za-z0-9._/-]+$ || "$model" == *..* ]]; then echo "bad model path: $model" >&2; exit 1; fi
[[ -f "$input" ]] || { echo "no such input file: $input" >&2; exit 1; }
resp=$(curl -sS -X POST "${BASE}${model}" \
  -H "Authorization: Key $FAL_KEY" -H "Content-Type: application/json" -d @"$input")
status_url=$(printf '%s' "$resp" | python3 -c 'import sys,json;print(json.load(sys.stdin)["status_url"])')
result_url=$(printf '%s' "$resp" | python3 -c 'import sys,json;print(json.load(sys.stdin)["response_url"])')
# never send the key anywhere but the provider's own queue host
for u in "$status_url" "$result_url"; do
  [[ "$u" == "$BASE"* ]] || { echo "refusing to send the key to unexpected URL: $u" >&2; exit 1; }
done
echo "submitted; polling $status_url" >&2
while :; do
  s=$(curl -sS "$status_url" -H "Authorization: Key $FAL_KEY" | python3 -c 'import sys,json;print(json.load(sys.stdin).get("status",""))')
  echo "status: $s" >&2
  [[ "$s" == "COMPLETED" ]] && break
  [[ "$s" == "FAILED" || "$s" == "ERROR" ]] && { echo "job failed" >&2; exit 1; }
  sleep 10
done
curl -sS "$result_url" -H "Authorization: Key $FAL_KEY" > "$out"
echo "saved $out" >&2
