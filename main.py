import os

LINE = "3am. I've stayed awake since 2019 so your leftovers could have a future. Eat the cake. No one's watching. Except me. Always me."

def main():
    # Gate: 1-140 characters, not only whitespace.
    if not (1 <= len(LINE) <= 140) or not LINE.strip():
        raise SystemExit("gate failed: line must be 1-140 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Post-write verification: read the bytes back and check they match
    # exactly, with no trailing newline and the gate still passing.
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        raise SystemExit("verification failed: bytes read back differ")
    text = back.decode("utf-8")
    if text.endswith("\n") or not (1 <= len(text) <= 140) or not text.strip():
        raise SystemExit("verification failed: gate check on written file")

if __name__ == "__main__":
    main()
