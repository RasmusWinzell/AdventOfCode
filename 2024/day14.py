# Advent of Code 2024 Day 14, https://adventofcode.com/2024/day/14
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day14.py
# This is the cleaned solution
import math
import re
from itertools import product

import numpy as np
from aocd.models import Puzzle

digits = re.compile(r"-?\d+")


def print_grid(bots, iterations, width, height):
    print("Iterations:", iterations)
    grid = [["." for _ in range(width)] for _ in range(height)]
    for px, py, vx, vy in bots:
        x = (px + vx * iterations) % width
        y = (py + vy * iterations) % height
        grid[y][x] = "#"

    print("\n".join("".join(row) for row in grid))


# Solved in 0:15:31
def partA(input):
    size = np.array([101, 103])

    bots = np.array([list(map(int, digits.findall(l))) for l in input.splitlines()])
    coords = (bots[:, :2] + bots[:, 2:] * 100) % size[None, :]

    l, t = (coords < np.floor(size / 2)).T
    r, b = (coords >= np.ceil(size / 2)).T

    res = np.prod([np.sum(a & b) for a, b in product([t, b], [l, r])])

    print(res)
    return res


# Solved in 1:02:03
def partB(input):
    size = np.array([101, 103])

    bots = np.array([list(map(int, digits.findall(l))) for l in input.splitlines()])
    pos, vel = bots[:, :2, None], bots[:, 2:, None]
    coords = (pos + vel * np.arange(103)[None, None, :]) % size[None, :, None]
    start = np.argmin(np.std(coords, axis=0), axis=1)

    N0 = np.prod(size) // size
    m = np.array([pow(int(Ni), int(s) - 2, int(s)) for Ni, s in zip(N0, size)])
    t = np.sum(start * N0 * m) % np.prod(size)

    print_grid(bots, t, *size)
    print(t)
    return t


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=14)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    