# Advent of Code 2023 Day 2, https://adventofcode.com/2023/day/2
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day02.py
# This is the cleaned solution
import math
import re
from collections import defaultdict

from aocd.models import Puzzle

max_cubes = {"red": 12, "green": 13, "blue": 14}


# Solved in 0:14:05 (Answer: 2006)
def partA(input: str):
    id_sum = 0
    for i, line in enumerate(input.split("\n")):
        cubes = [cube.split() for cube in re.split(r", |; |: ", line)[1:]]
        valid = not any(int(count) > max_cubes[color] for count, color in cubes)
        if valid:
            id_sum += i + 1
    return id_sum


# Solved in 0:18:29 (Answer: 84911)
def partB(input):
    power_sum = 0
    for i, line in enumerate(input.split("\n")):
        req_cubes = defaultdict(int)
        cubes = [cube.split() for cube in re.split(r", |; |: ", line)[1:]]
        for count, color in cubes:
            req_cubes[color] = max(req_cubes[color], int(count))
        power_sum += math.prod(req_cubes.values())
    return power_sum


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=2)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
