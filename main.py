#!/usr/bin/env python3
"""Two Lines to Your Past Self — a warning sent back to one specific night.

Writes the entry text to /output/entry.txt:
  line 1 — a warning to my past self about one specific moment, in one
           sentence: the night in the kitchen when she asked "Are we okay?"
           and I answered "We're fine" just to end the conversation;
  line 2 — one sentence on why it mattered: she believed me and stopped
           asking, so two winters later she left still waiting for the
           honest answer I never gave her.
"""

import os

ENTRY = (
    "That night in the kitchen, when she asks, 'Are we okay?', don't answer 'We're fine' just to end the conversation.\n"
    "She believed you and stopped asking, so two winters later she left still waiting for the honest answer you never gave her.\n"
)


def validate(text):
    """Check the entry against the gate: UTF-8 text of 1 to 280 characters,
    not only white space, exactly two lines, one sentence each."""
    if not text or not text.strip():
        return False
    if len(text) > 280:
        return False
    lines = [ln for ln in text.split("\n") if ln.strip()]
    if len(lines) != 2:
        return False
    return all(ln.strip().endswith(".") and ln.count(".") == 1 for ln in lines)


def main():
    assert validate(ENTRY), "entry fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
