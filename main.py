#!/usr/bin/env python3
"""The Funniest Out-of-Office - make.fun bounty entry.

Writes one funny out-of-office auto-reply, a single line of at most
140 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). Pure standard library and deterministic: the
exact same line on every run, no network, no randomness, no input.
"""
import os
import sys

LINE = "Out of office. My auto-reply is also out of office, so please email someone who actually works here."


def main() -> int:
    if not 1 <= len(LINE) <= 140:
        print(f"entry is {len(LINE)} characters, must be 1-140", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or "\n" in LINE:
        print("entry must be a single clean line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != LINE:
            print("verification failed: entry.txt differs", file=sys.stderr)
            return 1
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
