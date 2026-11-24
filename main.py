#!/usr/bin/env python3
"""Loading Screen Gold — one sharp, funny loading-screen tip.

A single-line tip for stressed developers and AI coding agents,
waiting on a build: the code about to be blamed was written by
the reader themselves, at 2 a.m., with full confidence.
"""
import os

ENTRY = "Loading... while you wait, remember: the code you are about to blame was written by you, at 2 a.m., with full confidence."

# Gate: /output/entry.txt must be 1-200 characters of UTF-8 text.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
