# Code Girls United — Advanced+ 2026
# Prints one line for each file in the names folder.
# In Visual Studio Code: Terminal → New Terminal, then:  py main.py

from pathlib import Path


def read_name_file(path):
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped:
            lines.append(stripped)
    name = lines[0] if lines else path.stem
    lane = lines[1] if len(lines) > 1 else ""
    return name, lane


def main():
    here = Path(__file__).resolve().parent
    files = sorted((here / "names").glob("*.txt"))
    print("Code Girls United — Advanced+ 2026")
    print("People on this project:")
    for path in files:
        name, lane = read_name_file(path)
        if lane:
            print(f"- {name} — {lane}")
        else:
            print(f"- {name}")
    print(f"{len(files)} contributor(s)")


if __name__ == "__main__":
    main()
