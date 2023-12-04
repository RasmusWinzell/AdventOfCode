import datetime
import os
import time

import template
from aocd.models import Puzzle
from template_data import TemplateData as TD


def get_today_puzzle():
    today = datetime.datetime.today()
    return Puzzle(year=today.year, day=today.day)


def get_day_file(year: int, day: int):
    return os.path.join(str(year), f"day{day:02}.py")


def get_input_file(year: int, day: int):
    return os.path.join(str(year), "inputs", f"day{day}.txt")


def wait_for_puzzle(puzzle: Puzzle):
    unlock_time = puzzle.unlock_time()
    # check if puzzle unlocks in the future
    now = datetime.datetime.now().replace(tzinfo=unlock_time.tzinfo)
    if unlock_time <= now:
        # Puzzle already unlcoked
        print("Puzzle already unlocked")
        return

    # wait for puzzle to unlock
    wait_time = unlock_time - now
    print(f"Waiting for puzzle to unlock in {wait_time}")
    time.sleep(wait_time.total_seconds() - 10)
    for i in range(10, 0, -1):
        print(f"\rWaiting for puzzle to unlock in {i}", end="")
        time.sleep(1)


def display_puzzle(puzzle: Puzzle):
    print(f"Advent of Code {puzzle.year} Day {puzzle.day}, {puzzle.url}")
    try:
        puzzle.view()
        print("Puzzle displayed")
    except Exception:
        pass


def summerize_puzzle(puzzle: Puzzle):
    print(f"Title: {puzzle.title}")
    print(f"Number of examples: {len(puzzle.examples)}")


def create_file(puzzle: Puzzle):
    filename = get_day_file(puzzle.year, puzzle.day)

    # check if file already exists
    if os.path.exists(filename):
        print(f"File {filename} already exists")
        return

    # ensure directory exists
    dir = os.path.dirname(filename)
    if dir != "" and not os.path.exists(dir):
        os.makedirs(dir, exist_ok=True)

    # read template
    template_text = ""
    with open(template.__file__, "r") as f:
        template_text = f.read()

    # replace template placeholders
    template_text = template_text.replace(TD.YEAR, str(puzzle.year))
    template_text = template_text.replace(TD.DAY, str(puzzle.day))
    template_text = template_text.replace(TD.PUZZLE_LINK, puzzle.url)
    template_text = template_text.replace(TD.FILENAME, filename)

    # create file
    with open(filename, "w") as f:
        f.write(template_text)


def save_input_file(puzzle: Puzzle):
    filename = get_input_file(puzzle.year, puzzle.day)

    # check if file already exists
    if os.path.exists(filename):
        print(f"File {filename} already exists")
        return

    # ensure directory exists
    dir = os.path.dirname(filename)
    if dir != "" and not os.path.exists(dir):
        os.makedirs(dir, exist_ok=True)

    # create file
    with open(filename, "w") as f:
        f.write(puzzle.input_data)


def open_file(puzzle: Puzzle):
    filename = get_day_file(puzzle.year, puzzle.day)
    filepath = os.path.abspath(filename)
    os.system(f"code {filepath}")


if __name__ == "__main__":
    puzzle = get_today_puzzle()
    wait_for_puzzle(puzzle)
    display_puzzle(puzzle)
    summerize_puzzle(puzzle)
    create_file(puzzle)
    save_input_file(puzzle)
    open_file(puzzle)
