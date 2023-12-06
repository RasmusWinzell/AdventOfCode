# Advent of Code 2023 Day 6, https://adventofcode.com/2023/day/6
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day06.py
# This is the cleaned solution
import re
from math import ceil, floor, prod, sqrt

from aocd.models import Puzzle


# Solved in 0:10:05 (Answer: 5133600)
def partA(input: str):
    numbers = list(map(int, re.findall("\d+", input)))
    half = len(numbers) // 2
    times, dists = numbers[:half], numbers[half:]
    # Components in the quadratic formula
    quad_comps = [(t / 2, sqrt(-d + t**2 / 4)) for t, d in zip(times, dists)]
    res = prod(ceil(mid + diff) - floor(mid - diff) - 1 for mid, diff in quad_comps)
    return res


# Solved in 0:13:24 (Answer: 40651271)
def partB(input):
    numbers = re.findall("\d+", input)
    half = len(numbers) // 2
    time, dist = int("".join(numbers[:half])), int("".join(numbers[half:]))
    # Use quadratic formula
    mid = time / 2
    diff = sqrt(-dist + time**2 / 4)
    start = floor(mid - diff)
    end = ceil(mid + diff)
    records = end - start - 1
    return records


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=6)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")