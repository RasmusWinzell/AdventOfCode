# Advent of Code 2024 Day 22, https://adventofcode.com/2024/day/22
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day22.py
# This is the cleaned solution
from functools import reduce
from itertools import accumulate

from aocd.models import Puzzle
from numpy import array, diff

FUNCS = (lambda x: x * 64, lambda x: x // 32, lambda x: x * 2048)
MIX_MOD = lambda x, f: (f(x) ^ x) % 16777216


# Solved in 0:25:07
def partA(input):
    return sum(reduce(MIX_MOD, FUNCS * 2000, s) for s in map(int, input.split("\n")))


# Solved in 1:17:30
def partB(input):
    m = map(int, input.split("\n"))
    ss = [array([*accumulate(FUNCS * 2000, MIX_MOD, initial=s)])[::-3] % 10 for s in m]
    ds = [{(*diff(s[i : i + 5]),): b for i, b in enumerate(s)} for s in ss]
    return max(sum(d.get(k, 0) for d in ds) for k in set().union(*ds) if len(k) == 4)


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=22)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    