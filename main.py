#!/usr/bin/env python3
"""One-Star Review of Something Essential — make.fun entry.

Writes a single-line one-star review of an essential thing to
/output/entry.txt. Stdlib only, fully deterministic.
"""

import os

REVIEW = (
    "One star. Slept eight hours, woke up tired. No refund, no explanation. "
    "Would not recommend to anyone who enjoys functioning."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
