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


def _outer_endings(line):
    """Count sentence-ending marks (. ! ?) that sit outside quoted speech.

    A mark inside quotes belongs to the quoted sentence, not to the
    line's own sentence: line 1 quotes "Are we okay?" yet is a single
    sentence. An apostrophe between two letters is a contraction
    ("don't"), never a quote.
    """
    endings = 0
    quote = None
    for i, ch in enumerate(line):
        prev = line[i - 1] if i else ""
        nxt = line[i + 1] if i + 1 < len(line) else ""
        contraction = ch == "'" and prev.isalpha() and nxt.isalpha()
        if quote:
            if ch == quote and not contraction:
                quote = None
        elif ch in "'\"" and not contraction:
            quote = ch
        elif ch in ".!?":
            endings += 1
    return endings


def validate(text):
    """Check the entry against the gate: UTF-8 text of 1 to 280 characters,
    not only white space, exactly two lines, one sentence each.

    One sentence per line is checked with _outer_endings, so "Stop!
    Think." now fails as the two sentences it is (counting periods
    alone let it pass) and a line ending in "!" or "?" passes (the
    old check demanded a period). Blank lines are not skipped: apart
    from one trailing newline the text must split into exactly two
    non-blank lines.
    """
    if not isinstance(text, str) or not text.strip():
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    if not 1 <= len(text) <= 280:
        return False
    body = text[:-1] if text.endswith("\n") else text
    lines = body.split("\n")
    if len(lines) != 2 or any(not ln.strip() for ln in lines):
        return False
    for ln in lines:
        line = ln.strip()
        tail = line.rstrip("'\"")
        if _outer_endings(line) != 1 or not tail or tail[-1] not in ".!?":
            return False
    return True


def main():
    assert validate(ENTRY), "entry fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
