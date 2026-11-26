"""The Dog Reviews the Mailman — make.fun entry.

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt (creating /output if needed).

The line is the dog's own verdict: contempt for a mailman who knocks
and flees, undercut by the dog waiting for him every single day.

Standard library only.
"""

import os

LINE = (
    "He knocks twice, runs away, and calls it a job. "
    "I have never respected a man less, or waited for one more."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
