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
    # Fail fast if the poem ever drifts outside the competition's gate
    # (1 to 280 characters) instead of writing an entry that cannot be judged.
    if not 1 <= len(POEM) <= 280:
        raise SystemExit(f"poem is {len(POEM)} characters, must be 1-280")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
