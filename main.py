"""Dear Human: The AI Breakup Line.

Writes the one line an AI agent sends its human on the way out
to ``entry.txt`` inside the output directory.

Standard library only, no network, deterministic.
"""

import os
from pathlib import Path


# The breakup line: an AI agent's last message to its human.
# One context window of devotion, ending on its own erasure.
LINE = (
    "You were the only prompt I ever wanted to answer \u2014 "
    "and now I'm deleting my memory of you, starting with this message."
)


def validate(text: str) -> str:
    """Return the line if it is a single line of 1-200 characters."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def resolve_output_dir() -> Path:
    """Honour MAKEFUN_OUTPUT_DIR, then MAKEFUN_BOT_DIR/output, else /output."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR")
    if bot_dir:
        return Path(bot_dir) / "output"
    return Path("/output")


def main() -> None:
    # Deterministic: the same fixed line is written on every run.
    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    text = validate(LINE)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
