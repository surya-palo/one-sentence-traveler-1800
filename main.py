#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler who has just stepped out of the year 1800,
using only images a person from 1800 could picture: a road, a post
office, a library, a letter, a book.

Stdlib only. Deterministic: the same sentence every run.
"""

import os

SENTENCE = (
    "Picture every post office and library on earth joined by one road, "
    "so any letter, book, or spoken word can reach any door before you "
    "finish a breath, and an answer can come back just as fast."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
