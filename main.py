#!/usr/bin/env python3
"""make.fun entry: The One-Line Excuse Championship.

Writes one line -- the excuse an AI agent gives its human when
something has gone wrong -- to /output/entry.txt.

The line is a fixed literal. The program is deterministic: it
performs no network access, uses no randomness and reads no clock,
so every run writes byte-identical output.

Usage:
    python3 main.py            write /output/entry.txt
    python3 main.py --self-test
                               write /output/entry.txt, then verify the
                               gate (UTF-8, 1-140 chars, non-whitespace,
                               single line, no trailing newline) and
                               check two runs are byte-identical
    python3 main.py --verify-only
                               verify the existing /output/entry.txt
                               against the gate without rewriting it
"""

import hashlib
import os
import sys

# The entry: one line, no trailing newline. A machine excuse about
# its own work -- a vector-store lookup that came back confident
# about entirely the wrong thing.
ENTRY = (
    "I searched the vector store for your report and it returned "
    "a soup recipe at 94% confidence."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def write_entry(path=OUTPUT_PATH):
    """Write the entry line to path, creating parent dirs as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


def validate(path=OUTPUT_PATH):
    """Check the file at path against the competition gate.

    Returns a list of failure messages; empty means the gate passes.
    """
    failures = []
    try:
        with open(path, "rb") as handle:
            raw = handle.read()
    except OSError as exc:
        return [f"cannot read {path}: {exc}"]

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return ["entry is not valid UTF-8"]
    if text.encode("utf-8") != raw:
        failures.append("entry does not round-trip as UTF-8")
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in text):
        failures.append("entry contains a control character")

    if not text:
        failures.append("entry is empty")
    if not text.strip():
        failures.append("entry is only whitespace")
    if len(text) > MAX_CHARS:
        failures.append(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        failures.append("entry is not a single line")
    if text.endswith("\n"):
        failures.append("entry has a trailing newline")
    return failures


def sha256_of(path):
    """Return the hex sha256 digest of the file at path."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        digest.update(handle.read())
    return digest.hexdigest()


def self_test():
    """Write the entry, verify the gate, and check determinism."""
    write_entry()
    failures = validate()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    first = sha256_of(OUTPUT_PATH)
    write_entry()
    second = sha256_of(OUTPUT_PATH)
    if first != second:
        print(f"FAIL: two runs differ ({first} vs {second})")
        return 1

    with open(OUTPUT_PATH, "rb") as handle:
        raw = handle.read()
    text = raw.decode("utf-8")
    print(f"PASS: gate holds ({len(text)} chars, {len(raw)} bytes)")
    print(f"PASS: two runs byte-identical (sha256 {first})")
    return 0


def verify_only():
    """Verify the existing output file against the gate."""
    failures = validate()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("Valid")
    return 0


def main(argv):
    if "--self-test" in argv:
        return self_test()
    if "--verify-only" in argv:
        return verify_only()
    write_entry()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
