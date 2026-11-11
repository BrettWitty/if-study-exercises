#!/usr/bin/python3

# This makes a quick template of files for the exercises.

from pathlib import Path
import argparse
import re
import sys
import unicodedata

EXERCISE_BASE_URL = "https://games.brettwitty.net/ifcourse/exercises"
DIR_PATTERN = re.compile(r"^(\d+)-(.+)$")

def existing_exercises(root: Path) -> dict[int,Path]:
    found : dict[int, Path] = {}

    for entry in root.iterdir():
        if entry.is_dir():
            m = DIR_PATTERN.match(entry.name)
            if m:
                found[int(m.group(1))] = entry
    return found

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower().replace("'","")
    text = re.sub(r"[^a-z0-9]+","-", text)
    return text.strip("-")

def ask(prompt: str, default: str | None = None) -> str:
    suffix = f" [{default}]" if default else ""
    while True:
        answer = input(f"{prompt}{suffix}: ").strip()
        if answer:
            return answer
        if default is not None:
            return default
        print("  (required)")

def ask_number(suggested: int, taken: dict[int, Path]) -> int:
    while True:
        raw = ask("Exercise number", f"{suggested:02d}")
        if not raw.isdigit():
            print("  Please enter a whole number.")
            continue
        n = int(raw)
        if n in taken:
            print(f"  {n:02d} is already used by {taken[n].name}/")
            continue
        return n

def render_files(title: str, game: str, exercise_url: str) -> dict[str, str]:
    game_ref = f'"{game}"' if game else "TODO"
    game_md = f'*{game}*' if game else "TODO"

    readme = f"""\
# {title}

[(Exercise page)]({exercise_url})

We look at {game_md}, focussing on TODO.

- [Slow play](./slow-play.md). [(Raw notes)](./slow-play-raw-notes.md)
- [Writing exercise](./writing.md): TODO
- [Design exercise](./design.md): TODO
- [Implementation exercise](./implementation.md): TODO
"""

    slow_play = f"""\
# Slow play of {game_ref}

"""

    raw_notes = f"""\
# Slow play notes for {game_md}

## Goals

## Tasks

1.

## Notes


"""

    def exercise(kind: str) -> str:
        return f"""\
# {kind} exercise in "{title}"

## Exercise


## Answer

"""

    return {
        "README.md" : readme,
        "slow-play.md" : slow_play,
        "slow-play-raw-notes.md" : raw_notes,
        "writing.md" : exercise("Writing"),
        "design.md" : exercise("Design"),
        "implementation.md" : exercise("Implementation")
    }

def main() -> int:

    parser = argparse.ArgumentParser(description="Template creator")
    parser.add_argument("-n", "--number", type=int, help="Exercise number (default: next free)")
    parser.add_argument("-t", "--title", help="Exercise title (eg. Straightjackets for Comedy)")
    parser.add_argument("-s", "--slug", help="Folder slug (default: from title)")
    parser.add_argument("-g", "--game", help="Game being played")
    parser.add_argument("-e", "--exercise", metavar="SLUG_OR_URL", help="Course exercise page")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent, help="Project root (default: this folder)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be created")

    args = parser.parse_args()

    root: Path = args.root.resolve()
    taken = existing_exercises(root)
    latest = max(taken,default=0)

    if taken:
        print(f"Latest exercise: {taken[latest].name}/")
    else:
        print("No exercises found.")

    try:
        number = args.number if args.number is not None else ask_number(latest+1, taken)
        title = args.title or ask("Title")
        slug = slugify(args.slug or ask("Directory slug", slugify(title)))
        game = args.game if args.game is not None else ask("Game title (optional)", "")
        exercise = args.exercise or ask("Exercise page slug or URL", slug)
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        return 1

    if not slug:
        print("Error: slug is empty", file=sys.stderr)
        return 1
    if number in taken:
        print(f"Error: {number:02d} is already used by {taken[number].name}/", file=sys.stderr)
        return 1

    exercise_url = exercise if exercise.startswith("http") else f"{EXERCISE_BASE_URL}/{exercise.strip('/')}/"
    target = Path(f"./{number:02d}-{slug}")

    if target.exists():
        print(f"Error: {target} already exists.", file=sys.stderr)
        return 1

    files = render_files(title, game, exercise_url)

    if args.dry_run:
        print(f"\nWould create {target.name}/")
        for name, content in files.items():
            print(f"\n--- {name} ---\n{content}", end="")
        return 0

    target.mkdir()
    for name, content in files.items():
        (target / name).write_text(content, encoding="utf-8")

    print(f"Created {target.name}/")
    for name in files:
        print(f"   {name}")

    print("\nREADME table row:\n")
    print(f"| [{title}](./{target.name}/) | [:green_book:]({exercise_url}) "
          f"| [Link](./target.name/slow-play.md) | TBD | TBD | TBD |")

    return 0


if __name__ == "__main__":
    sys.exit( main() )
