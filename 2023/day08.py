# Advent of Code 2023 Day 8, https://adventofcode.com/2023/day/8
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day08.py
# This is the cleaned solution
import re
from itertools import cycle, takewhile
from math import lcm

from aocd.models import Puzzle

fmt = re.compile(r"(.+) = \((.+), (.+)\)")
a_fmt = re.compile(r"..A")


def parse_input(input: str):
    instrs = input.partition("\n")[0]
    dirs = {k: {"L": l, "R": r} for k, l, r in fmt.findall(input)}
    return dirs, instrs


def steps_for(curr, dirs, instructions):
    gen = (curr := dirs[curr][instr] for instr in cycle(instructions))
    return sum(1 for _ in takewhile(lambda c: c[-1] != "Z", gen)) + 1


# Solved in 0:09:58 (Answer: 13771)
def partA(input: str):
    return steps_for("AAA", *parse_input(input))


# Solved in 1:07:32 (Answer: 13129439557681)
def partB(input: str):
    dirs, instrs = parse_input(input)
    return lcm(*(steps_for(curr, dirs, instrs) for curr in filter(a_fmt.match, dirs)))


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=8)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    