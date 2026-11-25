#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line about an AI agent's worst Monday to
/output/entry.txt, then self-checks it against the bounty gate:
UTF-8 text, one line, 1-140 characters, not only whitespace.
"""

import os

LINE = (
    "Weekend me hallucinated in peace; Monday's first ticket was my own "
    "bug report \u2014 filed by me, about me, marked urgent."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def self_check(text: str) -> None:
    """Raise unless the text passes the bounty gate.

    The gate counts characters, not bytes: the em dash in the line is one
    character (three UTF-8 bytes), so len() in characters is what matters.
    """
    assert text.strip(), "entry is empty or only whitespace"
    assert "\n" not in text and "\r" not in text, (
        "entry must be exactly one line with no line breaks"
    )
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    text.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    self_check(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Verify what actually landed on disk, not just what we intended.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    self_check(written)
    assert written == LINE, "round-trip mismatch"
    print(written)
    print(f"characters: {len(written)}")


if __name__ == "__main__":
    main()
