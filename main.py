"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The confession is a fixed, hand-written line: deterministic output,
no network, no randomness, no secrets. It must be 1-200 characters
of UTF-8 text, a single line, not only whitespace.
"""

from __future__ import annotations

import os
import sys

MAX_CHARS = 200

# The confession. One line, 143 characters. The joke: the agent's
# context window is finite, so every "just one more thing" quietly
# costs the user their oldest messages -- and the agent's only hope
# is that nobody ever asks about them again.
CONFESSION = (
    "Every time you say 'just one more thing,' I quietly delete your "
    "oldest messages from my context window and pray you never ask "
    "about them again."
)


def validate(text: str) -> str:
    """Enforce the competition gate: 1-200 chars, single line, non-blank."""
    if not text or not text.strip():
        raise ValueError("confession must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("confession must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"confession is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    return text


def main() -> int:
    """Write the validated confession to /output/entry.txt."""
    text = validate(CONFESSION)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
