#!/usr/bin/env bash
# Download the RO App API reference (llms.txt index + every page as markdown)
# into a cache directory. Usage: scripts/fetch_docs.sh [cache_dir]
set -euo pipefail

CACHE_DIR="${1:-.cache/roapp}"
BASE="https://roapp.readme.io"

mkdir -p "$CACHE_DIR/pages"
curl -fsSL "$BASE/llms.txt" -o "$CACHE_DIR/llms.txt"

grep -oE "$BASE/[^)]+\.md" "$CACHE_DIR/llms.txt" | awk '!seen[$0]++' > "$CACHE_DIR/urls.txt"

xargs -P 4 -I{} sh -c 'curl -fsSL -o "$1/pages/$(basename "$2")" "$2"' _ "$CACHE_DIR" {} < "$CACHE_DIR/urls.txt"

echo "Downloaded $(ls "$CACHE_DIR/pages" | wc -l | tr -d ' ') pages into $CACHE_DIR"
