#!/bin/bash
# Hand a finished, checked video to the poster: copy it (and its caption) into the sub niche's drop folder.
#
# The drop folder is any folder your posting system watches: a synced Google Drive / Dropbox / OneDrive folder, a
# network share, or a plain local folder. This script only copies files; it never posts, logs in or touches devices.
# Being in the folder is the approval, so drop only videos that passed the checks in PLAYBOOK.md section 7.
#
# Usage: drop.sh <clip.mp4> <drop folder> <name> [caption.txt]
#   <name>  a plain file name without extension, e.g. example-account-exam-cramming-1124-1
# Conventions most watchers follow (and this script respects):
#   - the caption is written first, then the video, so the watcher never sees a video without its caption;
#   - names starting with "." or "_" are ignored by watchers: the copy goes to "_<name>.part" then is renamed;
#   - copy in the order the videos should post.
set -euo pipefail
CLIP="${1:?clip.mp4}"; DIR="${2:?drop folder}"; NAME="${3:?name}"; CAP="${4:-}"
[[ "$NAME" =~ ^[A-Za-z0-9._-]+$ ]] || { echo "name: letters, digits, . _ - only" >&2; exit 2; }
[ -d "$DIR" ] || { echo "drop folder not found: $DIR" >&2; exit 1; }
[ -f "$CLIP" ] || { echo "clip not found: $CLIP" >&2; exit 1; }
EXT="${CLIP##*.}"
[ -e "$DIR/$NAME.$EXT" ] && { echo "already there: $DIR/$NAME.$EXT" >&2; exit 1; }
if [ -n "$CAP" ]; then cp "$CAP" "$DIR/_$NAME.txt.part" && mv "$DIR/_$NAME.txt.part" "$DIR/$NAME.txt"; fi
cp "$CLIP" "$DIR/_$NAME.$EXT.part" && mv "$DIR/_$NAME.$EXT.part" "$DIR/$NAME.$EXT"
echo "dropped $DIR/$NAME.$EXT${CAP:+ (+ caption)}"
