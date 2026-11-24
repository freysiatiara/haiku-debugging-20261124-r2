#!/usr/bin/env python3
"""Round 2 entry for make.fun's "Seventeen Syllables of Debugging".

Writes one fresh haiku about debugging -- three lines in the 5-7-5
syllable shape, at most 200 characters -- as plain text to
/output/entry.txt. Standard library only and fully deterministic:
the same bytes on every run.
"""

import os

HAIKU = (
    "the cursor blinks twice",
    "then the stack trace laughs at me",
    "it was a typo",
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = "\n".join(HAIKU) + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
