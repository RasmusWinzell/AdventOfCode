# Advent of Code 2023 Day 22, https://adventofcode.com/2023/day/22
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day22.py
# This is the original solution
import re
from collections import defaultdict

import numpy as np
from aocd.models import Puzzle


# Solved in 0:31:55 (Answer: 497)
def partA(input):
    bricks = [list(map(int, re.findall(r"\d+", line))) for line in input.splitlines()]
    sbricks = sorted(bricks, key=lambda x: x[2])

    layers = []
    supports = {}

    for id, (x1, y1, z1, x2, y2, z2) in enumerate(sbricks):
        i = len(layers) - 1
        while i >= 0:
            supported = set()
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x, y) in layers[i]:
                        supported.add(layers[i][(x, y)])
            if len(supported) > 0:
                supports[id] = supported
                break
            i -= 1
        i += 1
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(i, i + z2 - z1 + 1):
                    if z == len(layers):
                        layers.append({})
                    layers[z][(x, y)] = id

    keep = set()
    for k, v in supports.items():
        if len(v) == 1:
            keep.add(next(iter(v)))
    remove = len(sbricks) - len(keep)
    print(remove)
    return remove


def let_them_fall(sbricks, ignore=-1):
    layers = []
    supports = {}
    locs = set()
    for id, (x1, y1, z1, x2, y2, z2) in enumerate(sbricks):
        if id == ignore:
            continue
        i = len(layers) - 1
        while i >= 0:
            supported = set()
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x, y) in layers[i]:
                        supported.add(layers[i][(x, y)])
            if len(supported) > 0:
                supports[id] = supported
                break
            i -= 1
        i += 1
        locs.add((id, i))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(i, i + z2 - z1 + 1):
                    if z == len(layers):
                        layers.append({})
                    layers[z][(x, y)] = id
    return locs


# Solved in 1:07:35 (Answer: 67468)
def partB(input):
    bricks = [list(map(int, re.findall(r"\d+", line))) for line in input.splitlines()]
    sbricks = sorted(bricks, key=lambda x: x[2])

    locs = let_them_fall(sbricks)

    res = 0
    for id, i in locs:
        new_locs = let_them_fall(sbricks, id)
        has_falled = locs.difference(new_locs)
        res += len(has_falled) - 1
    print(res)
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=22)
    for example in puzzle.examples:
        if example.answer_a:
            answer = partA(example.input_data)
            assert (
                str(answer) == example.answer_a
            ), f"Part A: Expected {example.answer_a}, got {answer}"

    if puzzle.answered_a:
        answer = partA(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_a
        ), f"Part A: Expected {puzzle.answer_a}, got {answer}"
    else:
        puzzle.answer_a = partA(puzzle.input_data)
        assert puzzle.answered_a, "Answer A not correct"

    for example in puzzle.examples:
        if example.answer_b:
            answer = partB(example.input_data)
            assert (
                str(answer) == example.answer_b
            ), f"Part B: Expected {example.answer_b}, got {answer}"

    if puzzle.answered_b:
        answer = partB(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_b
        ), f"Part B: Expected {puzzle.answer_b}, got {answer}"
    else:
        puzzle.answer_b = partB(puzzle.input_data)
        assert puzzle.answered_b, "Answer B not correct"
