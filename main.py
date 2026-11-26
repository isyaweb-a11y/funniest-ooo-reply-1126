#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

Writes a single out-of-office email auto-reply line to
/output/entry.txt. The gate requires 1-160 characters of UTF-8 text.
"""

import os
import sys

MAX_CHARS = 160

ENTRY = (
    "I'm out of office until Monday. Please don't email twice "
    "\u2014 the second one doesn't make the first one more urgent."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    """Return the stripped line, or raise if it breaks the gate."""
    line = text.strip()
    if not line:
        raise ValueError("entry is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry too long: {len(line)} chars")
    return line


def main() -> int:
    try:
        text = validate(ENTRY)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
