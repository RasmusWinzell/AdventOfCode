# Advent of Code 2024 Day 19, https://adventofcode.com/2024/day/19
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day19.py
# This is the cleaned solution
from collections import defaultdict as dd
from functools import cache, reduce

from aocd.models import Puzzle


def check_design(pattern, tmap, op):
    @cache
    def run(p):
        return op(run(p[len(t) :]) for t in tmap[p[0]] if t == p[: len(t)]) if p else 1

    return run(pattern)


def parse(input):
    t, _, *ps = input.split("\n")
    return reduce(lambda d, i: d[i[0]].append(i) or d, t.split(", "), dd(list)), ps


# Solved in 0:10:43
def partA(input):
    tmap, patterns = parse(input)
    return sum(check_design(d, tmap, any) for d in patterns)


# Solved in 0:48:57
def partB(input):
    tmap, patterns = parse(input)
    return sum(check_design(d, tmap, sum) for d in patterns)


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=19)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    