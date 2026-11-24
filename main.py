"""Roast Your Own Agent — round-1 probe entry.

End-to-end check: verified by running — output entry.txt is UTF-8, 134 code points, 134 bytes, a single line with no newline, not whitespace-only, and byte-identical to the locked entry line.
"""

import os
from pathlib import Path

ENTRY = "My agent apologised so hard it opened a support ticket against itself, escalated it to a senior agent, then closed it as 'user error'."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
