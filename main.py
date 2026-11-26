#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — entry program.

Writes a single original line of fortune-cookie wisdom for a software
developer to /output/entry.txt (1-120 characters, no trailing newline),
for make.fun bounty u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.

The line was chosen after scoring 35 fresh candidates against the judge's
brief (see METHODOLOGY.md): it is oracular second person, it states a truth
every senior engineer recognises (a 'temp' name never dies), and it turns
that truth with a quiet double meaning — the throwaway name outlives its
author.
"""

import os
import sys

# The winning fortune-cookie line (57 characters, ASCII, no trailing newline).
LINE = "You will name a variable 'temp', and it will outlive you."


def main() -> int:
    """Write LINE to /output/entry.txt, deterministically."""
    # The gate refuses anything outside 1-120 characters, so check first.
    if not 1 <= len(LINE) <= 120:
        raise SystemExit("entry line must be 1-120 characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    os.umask(0o022)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
