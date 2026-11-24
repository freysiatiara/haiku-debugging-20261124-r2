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


def resolve_output_path() -> str:
    """Resolve the output file path (mirrors the round-1 pattern).

    Honors OUTPUT_DIR when set, otherwise /output. The directory is
    created here so callers never write into a missing folder.
    """
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def validate_haiku() -> str:
    """Join the haiku lines and enforce the competition's shape rules.

    Exactly three lines, at most 200 characters in total. Any drift is
    caught here, before anything is written to disk.
    """
    if len(HAIKU) != 3:
        raise ValueError(f"haiku must have exactly 3 lines, got {len(HAIKU)}")
    text = "\n".join(HAIKU) + "\n"
    if len(text) > 200:
        raise ValueError(f"haiku exceeds 200 characters: {len(text)}")
    return text


def main() -> None:
    path = resolve_output_path()
    text = validate_haiku()
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
