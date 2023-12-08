# Advent of Code 2023 Day 8, https://adventofcode.com/2023/day/8
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day08.py
# This is the cleaned solution
import re
from itertools import cycle
from math import lcm

from aocd.models import Puzzle

fmt = re.compile(r"(.+) = \((.+), (.+)\)")
a_fmt = re.compile(r"..A")


def steps_for(curr, dirs, instructions):
    instrs, steps = cycle(instructions), 1
    while (curr := dirs[curr][next(instrs)])[-1] != "Z":
        steps += 1
    return steps


# Solved in 0:09:58 (Answer: 13771)
def partA(input: str):
    instrs = input.partition("\n")[0]
    dirs = {k: {"L": l, "R": r} for k, l, r in fmt.findall(input)}
    return steps_for("AAA", dirs, instrs)


# Solved in 1:07:32 (Answer: 13129439557681)
def partB(input: str):
    instrs = input.partition("\n")[0]
    dirs = {k: {"L": l, "R": r} for k, l, r in fmt.findall(input)}
    return lcm(*(steps_for(curr, dirs, instrs) for curr in filter(a_fmt.match, dirs)))


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=8)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    