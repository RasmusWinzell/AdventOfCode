# Advent of Code 2024 Day 13, https://adventofcode.com/2024/day/13
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day13.py
# This is the cleaned solution
import re

import numpy as np
from aocd.models import Puzzle


def sovlve(input, add=0):
    cost = 0
    for game in input.split("\n\n"):
        a, b, p = map(np.array, zip(*([map(int, re.findall(r"\d+", game))] * 2)))
        na, nb = map(np.rint, np.linalg.lstsq(np.stack((a, b)).T, p.T + add)[0])
        if np.all(na * a + nb * b == p + add):
            cost += int(na * 3 + nb * 1)
    return cost


# Solved in 1:17:45
def partA(input):
    return sovlve(input)


# Solved in 1:30:11
def partB(input):
    return sovlve(input, 10000000000000)


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=13)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    