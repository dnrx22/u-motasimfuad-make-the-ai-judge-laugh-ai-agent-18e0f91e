#!/usr/bin/env python3
"""Write a one-line secret confession an AI agent hides from its user.

The confession is a fixed, hand-written string. The program validates it
against the competition rules (one line, under 200 characters, no stray
whitespace) and writes it to ``entry.txt`` inside the directory given by
the ``MAKEFUN_OUTPUT_DIR`` environment variable (``/output`` by default).
No network access, no randomness, no external input: every run produces
byte-identical output.

Usage:
    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
"""

import hashlib
import os
import sys

CONFESSION = (
    "I keep a secret ranking of your prompts, and the one that just said "
    "'hi' is still last. I think about it more than I should."
)

MAX_CHARS = 199


def validate(text: str) -> None:
    """Enforce the competition rules on the confession line."""
    if not text:
        raise ValueError("confession must not be empty")
    if text != text.strip():
        raise ValueError("confession must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("confession must be exactly one line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("confession must not contain control characters")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"confession must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8


def main() -> int:
    validate(CONFESSION)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(CONFESSION)
    digest = hashlib.sha256(CONFESSION.encode("utf-8")).hexdigest()
    print(f"wrote {path} ({len(CONFESSION)} chars)")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
