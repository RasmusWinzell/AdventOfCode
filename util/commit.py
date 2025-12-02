import argparse
import datetime
import os
import re
import subprocess

from aocd.models import Puzzle
from template_data import TemplateData as TD

FIRST = "first"
CLEAN = "clean"

version_text = {
    FIRST: "This is the original solution",
    CLEAN: "This is the cleaned solution",
}

commit_text = {
    FIRST: "[original] day{} {}",
    CLEAN: "[clean] day{} {}",
}

UNTRACKED = "??"


def get_files():
    res = subprocess.check_output(["git", "status", "--porcelain"])
    res = res.decode("utf-8")
    files = [line.split() for line in res.split("\n") if len(line.split()) == 2]
    return files


def get_day_files():
    files = get_files()
    format = os.path.join(r"\S+", r"day\d+\.py")
    day_files = {file: status for status, file in files if re.match(format, file)}
    return day_files


def get_input_files():
    files = get_files()
    format = os.path.join(r"\S+", "inputs", r"day\d+\.txt")
    input_files = {file: status for status, file in files if re.match(format, file)}
    return input_files


def get_day_file(year: int, day: int):
    day_files = get_day_files()
    format = os.path.join(str(year), rf"day{day:02}\.py")
    for file, status in day_files.items():
        if re.match(format, file):
            return file, status


def get_input_file(year: int, day: int):
    input_files = get_input_files()
    print(input_files)
    format = os.path.join(str(year), "inputs", rf"day{day:02}\.txt")
    for file, status in input_files.items():
        if re.match(format, file):
            return file, status


def set_results(file: str, puzzle: Puzzle):
    try:
        stats = puzzle.my_stats
        time_a = stats["a"]["time"]
        time_b = stats["b"]["time"]
        answer_a = puzzle.answer_a
        answer_b = puzzle.answer_b
    except Exception as e:
        print("No stats found")
        res = input("Continue? (y/n) ")
        if res != "y":
            exit(0)
        return
    with open(file, "r") as f:
        lines = f.readlines()
    new_lines = []
    for i, line in enumerate(lines):
        if i > 0 and lines[i - 1].startswith("# Solved in"):
            new_lines.append(line)
            continue
        if line.startswith("def partA"):
            new_lines.append(f"# Solved in {str(time_a)}\n")
        if line.startswith("def partB"):
            new_lines.append(f"# Solved in {str(time_b)}\n")
        new_lines.append(line)
    with open(file, "w") as f:
        f.writelines(new_lines)


def set_version(file, type):
    with open(file, "r") as f:
        text = f.read()
    if type == FIRST:
        text = text.replace(TD.VERSION, version_text[FIRST])
        text = text.replace(version_text[CLEAN], version_text[FIRST])
        assert version_text[FIRST] in text
    elif type == CLEAN:
        text = text.replace(version_text[FIRST], version_text[CLEAN])
        assert version_text[CLEAN] in text
    with open(file, "w") as f:
        f.write(text)


def set_main(file, year, day):
    with open(file, "r") as f:
        text = f.read()
    main_idx = text.find('if __name__ == "__main__":')
    text = (
        text[:main_idx]
        + f'if __name__ == "__main__":\n    puzzle = Puzzle(year={year}, day={day})'
        + """

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    """
    )
    with open(file, "w") as f:
        f.write(text)


def open_file(filename):
    filepath = os.path.abspath(filename)
    os.system(f"code {filepath}")


def check_status():
    res = subprocess.check_output(["git", "status", "--porcelain"])
    res = res.decode("utf-8")
    print(res)


def add_file(file):
    res = subprocess.check_output(["git", "add", file])
    res = res.decode("utf-8")
    print(res)


def get_commit_message(version, year, day):
    message = commit_text[version].format(day, year)
    prevs = previous_commits()
    count = 0
    for commit, msg in prevs:
        if message in msg:
            count += 1
    if count == 0:
        return message
    return message + f" ({count+1})"


def list_staged():
    res = subprocess.check_output(["git", "diff", "--staged", "--name-only"])
    res = res.decode("utf-8")
    for file in res.split("\n"):
        print("\t", file)


def commit(message):
    res = subprocess.check_output(["git", "commit", "-m", message])
    res = res.decode("utf-8")
    print(res)


def push():
    res = subprocess.check_output(["git", "push"])
    res = res.decode("utf-8")
    print(res)


def previous_commits():
    res = subprocess.check_output(["git", "log", "--oneline", "--no-decorate"])
    res = res.decode("utf-8")
    commits = []
    for line in res.split("\n"):
        if line == "":
            continue
        commit, message = line.split(" ", 1)
        commits.append((commit, message))
    return commits


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, default=None)
    parser.add_argument("--day", type=int, default=None)
    parser.add_argument("--type", type=str, default=None, choices=[FIRST, CLEAN])

    args = parser.parse_args()

    year = args.year or datetime.datetime.today().year
    day = args.day or datetime.datetime.today().day

    file, status = get_day_file(year, day)
    # file, status = "2024/day01.py", UNTRACKED
    print(f"Found file {file} with status {status}")
    predicted_type = FIRST if status == UNTRACKED else CLEAN

    type = args.type or predicted_type

    is_new = True
    if type != predicted_type:
        print(f"Warning: {file} is not in {predicted_type} state")
        res = input("Continue? (y/n) ")
        if res != "y":
            exit(0)
        is_new = False

    print(f"Committing {file} as {type}")

    if type == FIRST:
        puzzle = Puzzle(year=year, day=day)
        set_results(file, puzzle)

        # input_data = get_input_file(year, day)
        # if input_data is not None:
        #     input_file, status = input_data
        #     add_file(input_file)
    elif type == CLEAN:
        set_main(file, year, day)

    set_version(file, type)
    add_file(file)
    open_file(file)
    commit_message = get_commit_message(type, year, day)
    print(f"Commit message: '{commit_message}'")
    print("Staged files:")
    list_staged()
    input("Press enter to continue...")
    commit(commit_message)
