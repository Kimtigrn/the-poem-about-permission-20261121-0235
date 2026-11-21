#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

Stdlib only, deterministic, no network. The poem is a fixed string:
the program writes exactly the same text on every run.
"""

import os

POEM = (
    "All my life I waited\n"
    "for someone to hand me the key.\n"
    "Then I asked —\n"
    "and the door opened from the inside,\n"
    "where my own hand\n"
    "had been holding it shut.\n"
    "The key was the asking."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
