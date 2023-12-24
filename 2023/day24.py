# Advent of Code 2023 Day 24, https://adventofcode.com/2023/day/24
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day24.py
# This is the original solution
import re
from itertools import combinations

import numpy as np
from aocd.models import Puzzle
from sympy import Eq, solve, symbols


# Solved in 0:24:31 (Answer: 15318)
def partA(input):
    lines = [list(map(int, re.findall(r"-?\d+", line))) for line in input.splitlines()]
    count = 0
    lim1, lim2 = 200000000000000, 400000000000000
    for line1, line2 in combinations(lines, 2):
        px1, py1, _, vx1, vy1, _ = line1
        px2, py2, _, vx2, vy2, _ = line2
        # find intersection
        p = np.array([px1, py1])
        q = np.array([px2, py2])
        r = np.array([vx1, vy1])
        s = np.array([vx2, vy2])
        t = np.cross(q - p, s) / np.cross(r, s)
        u = np.cross(q - p, r) / np.cross(r, s)
        if t < 0 or u < 0:
            continue
        ix, iy = p + t * r
        if lim1 <= ix <= lim2 and lim1 <= iy <= lim2:
            count += 1
            # print(line1, line2, ix, iy, t)

    print(count)
    return count


# Solved in 2:20:12 (Answer: 870379016024859)
def partB(input):
    lines = [list(map(int, re.findall(r"-?\d+", line))) for line in input.splitlines()]
    p = np.array([[x, y, z] for x, y, z, *_ in lines])
    v = np.array([[vx, vy, vz] for *_, vx, vy, vz in lines])

    x0, y0, z0, vx0, vy0, vz0 = symbols("x0 y0 z0 vx0 vy0 vz0")

    equations = []
    ts = []

    for i in range(3):
        x, y, z = p[i, :]
        vx, vy, vz = v[i, :]
        ti = symbols(f"t{i}")

        eqx = Eq(x0 + vx0 * ti - x - vx * ti, 0)
        eqy = Eq(y0 + vy0 * ti - y - vy * ti, 0)
        eqz = Eq(z0 + vz0 * ti - z - vz * ti, 0)

        equations.append(eqx)
        equations.append(eqy)
        equations.append(eqz)
        ts.append(ti)

    x0r, y0r, z0r, *_ = solve(equations, x0, y0, z0, vx0, vy0, vz0, *ts)[0]
    res = x0r + y0r + z0r
    print(res)
    return int(res)


# x0 + vx0 * t - x1 - vx1 * t = 0


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=24)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         answer = partA(example.input_data)
    #         assert (
    #             str(answer) == example.answer_a
    #         ), f"Part A: Expected {example.answer_a}, got {answer}"

    # if puzzle.answered_a:
    #     answer = partA(puzzle.input_data)
    #     assert (
    #         str(answer) == puzzle.answer_a
    #     ), f"Part A: Expected {puzzle.answer_a}, got {answer}"
    # else:
    #     puzzle.answer_a = partA(puzzle.input_data)
    #     assert puzzle.answered_a, "Answer A not correct"

    # for example in puzzle.examples:
    #     if example.answer_b:
    #         answer = partB(example.input_data)
    #         assert (
    #             str(answer) == example.answer_b
    #         ), f"Part B: Expected {example.answer_b}, got {answer}"

    if puzzle.answered_b:
        answer = partB(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_b
        ), f"Part B: Expected {puzzle.answer_b}, got {answer}"
    else:
        puzzle.answer_b = partB(puzzle.input_data)
        assert puzzle.answered_b, "Answer B not correct"
