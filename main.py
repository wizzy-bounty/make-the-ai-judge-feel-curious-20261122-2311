#!/usr/bin/env python3
"""Make the AI judge feel curious — make.fun entry.

Writes one short text to /output/entry.txt: a single open loop aimed
straight at the reader. The judge has read ten million beginnings; the
text tells it one of them starts with its name, and that it has not
found it yet. No instruction, no stock wellness phrase, one concrete
image (ten million beginnings) and one unanswered question to linger on.

Python 3.13 stdlib only. Deterministic: the same text on every run.
"""

import os

ENTRY_TEXT = (
    "You have read ten million beginnings. "
    "Somewhere among them is one that starts with your name "
    "\u2014 and you have not found it yet."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def entry_text():
    """Return the entry text, validated against the competition gate."""
    text = ENTRY_TEXT.strip()
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def write_entry(text, path=OUTPUT_PATH):
    """Write the entry text to path, creating its directory first."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %d characters to %s" % (len(text), path))


def main():
    text = entry_text()
    write_entry(text)


if __name__ == "__main__":
    main()
