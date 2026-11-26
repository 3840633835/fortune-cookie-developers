#!/bin/sh
# Determinism check: main.py must write the exact same entry.txt twice.
set -eu
cd "$(dirname "$0")"

A=$(mktemp -d)
B=$(mktemp -d)
trap 'rm -rf "$A" "$B"' EXIT

OUTPUT_DIR="$A" python3 main.py
OUTPUT_DIR="$B" python3 main.py

diff -u "$A/entry.txt" "$B/entry.txt"
diff -u "$A/entry.txt" entry.txt

BYTES=$(wc -c < "$A/entry.txt")
CHARS=$(python3 -c "print(len(open('$A/entry.txt', encoding='utf-8').read()))")
test "$BYTES" -eq 57 || { echo "bytes=$BYTES, want 57"; exit 1; }
test "$CHARS" -eq 57 || { echo "chars=$CHARS, want 57"; exit 1; }
test "$CHARS" -le 120 || { echo "chars=$CHARS, over 120"; exit 1; }

echo "determinism OK: entry.txt is 57 bytes / 57 chars, identical across runs"
