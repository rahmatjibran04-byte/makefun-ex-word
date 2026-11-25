#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun bounty entry.

Writes a single-word verdict on an ex to /output/entry.txt.
The word: "Recalled" — like a defective product the manufacturer
pulled from circulation: the fault was in the unit all along.
No network, no arguments, no side effects beyond the output file.
"""

import os

WORD = "Recalled"
OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """Enforce the competition gate before writing anything.

    Exactly one word, 1-111 characters, not only whitespace.
    """
    if not word or word != word.strip():
        raise ValueError("word must be non-empty with no surrounding whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not 1 <= len(word) <= 111:
        raise ValueError("entry must be 1-111 characters")


def main() -> None:
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read back and confirm the file holds exactly the chosen word.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != WORD:
        raise RuntimeError(f"read-back mismatch: {written!r} != {WORD!r}")


if __name__ == "__main__":
    main()
