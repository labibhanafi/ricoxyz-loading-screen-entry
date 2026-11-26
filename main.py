#!/usr/bin/env python3
"""Loading Screen Gold entry: writes one loading-screen tip to /output/entry.txt.

Deterministic: the entry text is a fixed constant; the program writes it
unchanged on every run.
"""

import os

ENTRY = "Tip: if your agent had a loading screen, it would say: 'Waiting for human to stop rewriting my prompt.' So - stop rewriting the prompt."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check against the competition gate: 1-200 chars, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
