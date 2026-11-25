#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes one line (under 200 characters): the excuse an AI agent hands
its human after shipping a bug. The joke turns on something only an
agent could say: a context window that fills up mid-fix.
"""

import os

EXCUSE = (
    "My context window filled up mid-fix, so I forgot the bug, "
    "the fix, and \u2014 briefly \u2014 your name. "
    "The code shipped anyway."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: entry.txt holds exactly the one line the
    # gate measures (1-200 chars, not only whitespace).
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
