# Advent of Code 2023 Day 15, https://adventofcode.com/2023/day/15
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day15.py
# This is the original solution
from aocd.models import Puzzle


def ascii_hash(text: str):
    current_value = 0
    for c in text:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


# Solved in 0:05:01 (Answer: 519041)
def partA(input):
    instrs = input.replace("\n", "").split(",")
    return sum(ascii_hash(instr) for instr in instrs)


# Solved in 0:22:07 (Answer: 260530)
def partB(input):
    instrs = input.replace("\n", "").split(",")
    hashmap = [{} for _ in range(256)]
    for instr in instrs:
        print(instr)
        if "-" in instr:
            lable, value = instr.split("-")
            h = ascii_hash(lable)
            hashmap[h].pop(lable, None)
        else:
            lable, value = instr.split("=")
            h = ascii_hash(lable)
            hashmap[h][lable] = int(value)
    focus_power = 0
    for j, row in enumerate(hashmap):
        for i, (k, v) in enumerate(row.items()):
            box_power = (j + 1) * (i + 1) * v
            focus_power += box_power
    print(focus_power)
    return focus_power


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=15)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    