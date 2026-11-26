"""Entry for make.fun bounty u-mfnakmal-the-comment-above-the-code-35e38026.

Writes one line -- the comment a developer left above fragile production
code -- to $MAKEFUN_OUTPUT_DIR/entry.txt (the grader reads /output).
"""

import os
import sys

ENTRY = "Do not touch: the sort is wrong, and the monthly report depends on it staying wrong."


def validate(line):
    """Check the entry line against the competition gate; raise ValueError."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if len(line) > 200:
        raise ValueError("entry exceeds 200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("entry must not contain control characters")


def main():
    try:
        validate(ENTRY)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
