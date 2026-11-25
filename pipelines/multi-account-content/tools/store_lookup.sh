#!/usr/bin/env bash
# Read an app's live store listing facts for the end-card CTA, the day you build (names and ratings change).
# Uses the public iTunes lookup endpoint; no key, no login. Prints JSON the CTA can take as parameters.
# Usage: store_lookup.sh <numeric app id> [country, default us]
set -euo pipefail
ID="${1:?numeric app id}"; C="${2:-us}"
[[ "$ID" =~ ^[0-9]+$ ]] || { echo "app id must be numeric" >&2; exit 2; }
[[ "$C" =~ ^[a-z]{2}$ ]] || { echo "country must be two letters" >&2; exit 2; }
curl -fsS "https://itunes.apple.com/lookup?id=${ID}&country=${C}" | python3 -c '
import json, sys, datetime
d = json.load(sys.stdin)
if not d.get("resultCount"):
    sys.exit("no listing found")
r = d["results"][0]
out = {
    "checked": datetime.date.today().isoformat(),
    "name": r.get("trackName"),
    "seller": r.get("sellerName"),
    "rating": round(r.get("averageUserRating") or 0, 1),
    "ratings_count": r.get("userRatingCount"),
    "price": r.get("formattedPrice"),
    "age": r.get("contentAdvisoryRating"),
    "version": r.get("version"),
    "genre": r.get("primaryGenreName"),
    "icon": r.get("artworkUrl512") or r.get("artworkUrl100"),
    "screenshots": r.get("screenshotUrls", []),
}
print(json.dumps(out, indent=2))
'
# Look at every screenshot before using it: leave out any that shows the store owner's own logo.
