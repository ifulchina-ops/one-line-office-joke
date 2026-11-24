"""One-Line Office Joke: 24-Hour Sprint.

Writes a single original office joke, one line, to entry.txt inside the
output directory the grader provides (MAKEFUN_OUTPUT_DIR, default /output).
Deterministic: the same line every run, no input, no network, no randomness.
"""

import os

JOKE = (
    "I blocked an hour of focus time on my calendar, so my manager booked "
    "over it with a meeting titled 'Quick sync about focus time'."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
