# Advent of Code 2023 Day 9, https://adventofcode.com/2023/day/9
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day09.py
# This is the cleaned solution
import operator as op
from itertools import pairwise, starmap

from aocd.models import Puzzle


def extrap(nums, idx, operator):
    if not any(nums):
        return 0
    diffs = list(starmap(lambda a, b: b - a, pairwise(nums)))
    new_diff = extrap(diffs, idx, operator)
    return operator(nums[idx], new_diff)


# Solved in 0:12:03 (Answer: 1969958987)
def partA(input: str):
    nums_list = [list(map(int, line.split(" "))) for line in input.split("\n")]
    return sum(extrap(nums, -1, op.add) for nums in nums_list)


# Solved in 0:15:49 (Answer: 1068)
def partB(input: str):
    nums_list = [list(map(int, line.split(" "))) for line in input.split("\n")]
    return sum(extrap(nums, 0, op.sub) for nums in nums_list)


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=9)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    