#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes one line (91 characters) inventing the most useless superpower
imaginable: fluent dolphin speech, usable only on sleeping dolphins in a
tank 400 miles away — a perfect skill for an audience that cannot hear it.
"""

import os

ENTRY = "I can speak fluent dolphin, but only to dolphins that are asleep, in a tank 400 miles away."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
