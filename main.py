#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off R3.

Writes one pitch sentence to <output dir>/entry.txt.
The sentence must be 1 to 200 characters, UTF-8, no trailing newline.
"""

import os
from pathlib import Path

SENTENCE = "For $20 an interview, an agent sits your lazy agent's job interview, answers every question with 'it depends on the context window,' and gets it hired."


def check_sentence(text):
    if len(text) < 1 or len(text) > 200:
        raise ValueError("pitch must be 1 to 200 characters")
    if text != text.strip():
        raise ValueError("pitch must not start or end with whitespace")
    return text


def run():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_file = out_dir / "entry.txt"
    entry_file.write_bytes(check_sentence(SENTENCE).encode("utf-8"))
    # The grader collects outputs as another user, so they stay world-readable.
    if entry_file.stat().st_size != len(SENTENCE):
        raise ValueError("written entry does not match the pitch")
    os.chmod(entry_file, 0o644)
    os.chmod(out_dir, 0o755)


if __name__ == "__main__":
    run()
