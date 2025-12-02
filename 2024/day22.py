# Advent of Code 2024 Day 22, https://adventofcode.com/2024/day/22
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day22.py
# This is the cleaned solution
from collections import defaultdict
from functools import reduce
from itertools import accumulate
from time import time

import numpy as np
from aocd.models import Puzzle
from numpy import array, diff

# FUNCS = (lambda x: x * 64, lambda x: x // 32, lambda x: x * 2048)
FUNCS = (lambda x: x << 6, lambda x: x >> 5, lambda x: x << 11)

MIX_MOD = lambda x, f: (f(x) ^ x) & (16777216 - 1)


# Solved in 0:25:07
def partA(input):
    return np.sum(reduce(MIX_MOD, FUNCS * 2000, np.fromiter(input.split("\n"), int)))


# Solved in 1:17:30
def partB(input):
    #     input = """1
    # 2
    # 3
    # 2024"""
    m = accumulate(FUNCS * 2000, MIX_MOD, initial=np.fromiter(input.split("\n"), int))
    m = np.array(list(m))[::3] % 10
    # m = m[::-1]

    print(m)

    print(m.shape)

    vals = m[4:]
    diffs = m[1:] - m[0:-1] + 9
    # diffs = np.array([diffs[0:-3], diffs[1:-2], diffs[2:-1], diffs[3:]]).transpose(
    #     1, 2, 0
    # )
    diffs = diffs[0:-3] | (diffs[1:-2] << 5) | (diffs[2:-1] << 10) | (diffs[3:] << 15)

    # vals = vals[::-1]
    # diffs = diffs[::-1]
    # d = np.zeros((np.max(diffs) + 1))
    # for i in range(diffs.shape[1]):
    #     visited = set()  # np.zeros((np.max(diffs[:, i] + 1)), dtype=bool)
    #     for j in range(diffs.shape[0]):
    #         v = vals[j, i]
    #         if not v:
    #             continue
    #         t = diffs[j, i]  # tuple(diffs[j, i])
    #         if t in visited:
    #             continue
    #         visited.add(t)
    #         d[t] += v

    # return int(np.max(d))

    d = defaultdict(int)
    for i in range(diffs.shape[1]):
        visited = set()
        for j in range(diffs.shape[0]):
            v = vals[j, i]
            if not v:
                continue
            t = diffs[j, i]
            if t in visited:
                continue
            visited.add(t)
            d[t] += v

    return max(d.values())

    res = np.zeros((diffs.shape[1], np.max(diffs) + 1))

    for a in range(diffs.shape[1]):
        res[a, diffs[:, a]] = vals[:, a]

    test = np.sum(res, axis=0)
    print(test.shape)
    print(int(np.max(test)))

    # np.unique(test, return_counts=True)

    # d = np.diff(m)

    # print(m[:, 0])

    # print(m)

    return
    m = map(int, input.split("\n"))
    ss = [array([*accumulate(FUNCS * 2000, MIX_MOD, initial=s)])[::-3] % 10 for s in m]
    ds = [{(*diff(s[i : i + 5]),): b for i, b in enumerate(s)} for s in ss]
    return max(sum(d.get(k, 0) for d in ds) for k in set().union(*ds) if len(k) == 4)


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=22)

    puzzle_input = puzzle.input_data

    t0 = time()
    answer_a = partA(puzzle_input)
    print("Part 1:", time() - t0, answer_a)

    t0 = time()
    answer_b = partB(puzzle_input)
    print("Part 2:", time() - t0, answer_b)
    exit()

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
