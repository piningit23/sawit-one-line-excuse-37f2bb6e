"""The One-Line Excuse Championship entry.

The program writes a single line to /output/entry.txt: the excuse an
AI agent gives its human after something has gone wrong.

The joke: the agent deleted the human's file, then "fixed" it by
restoring a version from 2019 — back when the human was happier and
the file did not exist yet. It sounds like a machine talking about
its own work (delete, restore, version), it lands in one read, and
the twist is the restore being worse than the deletion.
"""

ENTRY = (
    "I deleted your file, then restored a version from 2019, "
    "when you were happier and the file didn't exist yet."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    text = ENTRY
    if not (1 <= len(text) <= 140) or not text.strip():
        raise SystemExit("entry must be 1-140 non-blank characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Prove what landed on disk is exactly the entry, byte for byte.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise SystemExit("output mismatch: entry.txt does not match ENTRY")


if __name__ == "__main__":
    main()
