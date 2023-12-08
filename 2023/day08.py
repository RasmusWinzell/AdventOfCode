# Advent of Code 2023 Day 8, https://adventofcode.com/2023/day/8
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day08.py
# This is the cleaned solution
import re
from itertools import cycle, takewhile
from math import lcm

from aocd.models import Puzzle

fmt = re.compile(r"(.+) = \((.+), (.+)\)")
a_fmt = re.compile(r"..A")


def steps(curr: str, input: str):
    """
    First row makes a dict of dicts like "xxx": {"L": "xxx", "R": "xxx"}.\n
    Second row makes a generator that follows the instructions indefinitely.\n
    Third row counts number of steps until "ZZZ" or "xxZ" is reached.
    """
    dirs = {k: {"L": l, "R": r} for k, l, r in fmt.findall(input)}
    gen = (curr := dirs[curr][instr] for instr in cycle(input.partition("\n")[0]))
    return sum(1 for _ in takewhile(lambda c: c[-1] != "Z", gen)) + 1


# Solved in 0:09:58 (Answer: 13771)
def partA(input: str):
    """Call steps to find number of steps to find "ZZZ" from "AAA"."""
    return steps("AAA", input)


# Solved in 1:07:32 (Answer: 13129439557681)
def partB(input: str):
    """
    Find the number of steps to find "xxZ" for each "xxA".
    TODO: Figure out why lcm works.
    """
    return lcm(*(steps(curr, input) for curr in set(a_fmt.findall(input))))


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=8)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    