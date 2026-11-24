#!/usr/bin/env python3
"""Roast Your Own Agent — writes one sharp roast line to /output/entry.txt.

Stdlib only. The line is deterministic so both graded runs produce
identical bytes.
"""

import os

ROAST = (
    "My agent confidently wrote the wrong code, apologized, "
    "fixed it by breaking something else, apologized for the "
    "apology, then cheerfully summarized the whole disaster "
    "as a success."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
