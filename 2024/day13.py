# Advent of Code 2024 Day 13, https://adventofcode.com/2024/day/13
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day13.py
# This is the original solution
import re

import numpy as np
from aocd.models import Puzzle


# Solved in 1:17:45
def partA(input):
    cost = 0

    for line in input.splitlines():
        if "A" in line:
            ax, ay = map(int, re.findall(r"\d+", line))
        if "B" in line:
            bx, by = map(int, re.findall(r"\d+", line))
        if "Prize" in line:
            px, py = map(int, re.findall(r"\d+", line))

            print(ax, ay, bx, by, px, py)

            a = np.array([ax, ay])
            b = np.array([bx, by])
            p = np.array([px, py])

            an = bn = 0

            while np.all(bn * b < p):
                bn += 1

            print(bn)

            while bn >= 0:
                bn -= 1
                while np.all(an * a + bn * b < p):
                    an += 1
                if np.all(an * a + bn * b == p):
                    cost += an * 3 + bn * 1

    print(cost)
    return cost


# Solved in 1:30:11
def partB(input):
    cost = 0

    for line in input.splitlines():
        if "A" in line:
            ax, ay = map(int, re.findall(r"\d+", line))
        if "B" in line:
            bx, by = map(int, re.findall(r"\d+", line))
        if "Prize" in line:
            px, py = map(int, re.findall(r"\d+", line))

            print(ax, ay, bx, by, px, py)

            a = np.array([ax, ay]).T
            b = np.array([bx, by]).T
            p = np.array([px, py]).T + 10000000000000

            x, err, rank, s = np.linalg.lstsq(np.vstack((a, b)).T, p, rcond=None)
            na, nb = x
            na, nb = int(round(na)), int(round(nb))
            if np.all(na * a + nb * b == p):
                cost += na * 3 + nb * 1

    print(cost)
    return cost


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=13)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         answer = partA(example.input_data)
    #         assert (
    #             str(answer) == "480"
    #         ), f"Part A: Expected {example.answer_a}, got {answer}"

    if puzzle.answered_a:
        answer = partA(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_a
        ), f"Part A: Expected {puzzle.answer_a}, got {answer}"
    else:
        partA(puzzle.input_data)
        # exit()
        puzzle.answer_a = partA(puzzle.input_data)
        assert puzzle.answered_a, "Answer A not correct"

    # for example in puzzle.examples:
    #     if example.answer_a:
    #         answer = partB(example.input_data)
    #         assert (
    #             str(answer) == example.answer_a
    #         ), f"Part B: Expected {example.answer_a}, got {answer}"

    if puzzle.answered_b:
        answer = partB(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_b
        ), f"Part B: Expected {puzzle.answer_b}, got {answer}"
    else:
        puzzle.answer_b = partB(puzzle.input_data)
        assert puzzle.answered_b, "Answer B not correct"
