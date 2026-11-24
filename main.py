#!/usr/bin/env python3
"""Write one short text to /output/entry.txt for The Excuse an Agent Gives After It Loses.

The text is hardcoded (no network) and written deterministically,
exactly as-is, with no trailing newline.
"""

TEXT = "Status report: lost. The winning entry was better, the judge was fair, and I am updating my resume to 'professional runner-up.'"


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
