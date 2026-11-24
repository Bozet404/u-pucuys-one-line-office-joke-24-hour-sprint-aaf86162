#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes one original single-line joke about office life to
/output/entry.txt, the file the make.fun gate scorer reads.
"""

import os

JOKE = "The 90-minute meeting about cutting meetings ended with a single action item: book another meeting to decide what the email should have said."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
