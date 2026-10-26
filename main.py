# Code Girls United — Advanced+ 2026
# Prints the names in CONTRIBUTORS.md.
# In Visual Studio Code: Terminal → New Terminal, then:  py main.py

from pathlib import Path


def read_contributors(path):
    names = []
    in_names = False
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.lower() == "## names":
            in_names = True
            continue
        if in_names and stripped.startswith("## "):
            break
        if in_names and stripped.startswith("- "):
            name = stripped[2:].strip()
            if name:
                names.append(name)
    return names


def main():
    here = Path(__file__).resolve().parent
    names = read_contributors(here / "CONTRIBUTORS.md")
    print("Code Girls United — Advanced+ 2026")
    print("People on this project:")
    for name in names:
        print(f"- {name}")
    print(f"{len(names)} contributor(s)")


if __name__ == "__main__":
    main()
