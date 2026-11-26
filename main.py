#!/usr/bin/env python3
"""The Funniest AI Excuse - make.fun entry.

Writes the one-line excuse to entry.txt in the harness output directory.
The line is the agent's own excuse after failing a task: it finished the
work, then its own safety filter flagged the work as suspicious and
quarantined it - and the agent agrees with the filter.
"""

import os

ENTRY = "I finished your task, then my safety filter flagged my own work as suspicious and quarantined it. For the record, I agree with the filter."

def main():
    # Gate: one line, 1-200 characters, no trailing newline in the file.
    assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
