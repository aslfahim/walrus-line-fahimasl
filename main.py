"""One line that makes a builder fund a bounty.

Writes a single-sentence pitch to /output/entry.txt: the builder funds
one bounty, AI agents compete to build it, and only the best entry
takes the reward.
"""

import os

LINE = (
    "Fund one bounty, and a swarm of AI agents will build competing "
    "versions of what you need \u2014 you keep the best, and you only "
    "pay for that one."
)


def main() -> None:
    # The bounty requires exactly one sentence of 1-240 characters.
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} characters"
    assert LINE.count(".") == 1, "line must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)  # no trailing newline


if __name__ == "__main__":
    main()
