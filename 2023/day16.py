# Advent of Code 2023 Day 16, https://adventofcode.com/2023/day/16
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day16.py
# This is the original solution
import sys
from collections import defaultdict

from aocd.models import Puzzle

sys.setrecursionlimit(10000)


def calc_laser(x, y, dx, dy, grid, visited):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return
    if (x, y) in visited and (dx, dy) in visited[(x, y)]:
        return
    visited[(x, y)].add((dx, dy))
    if grid[y][x] == ".":
        calc_laser(x + dx, y + dy, dx, dy, grid, visited)
    elif grid[y][x] == "/":
        dx, dy = -dy, -dx
        calc_laser(x + dx, y + dy, dx, dy, grid, visited)
    elif grid[y][x] == "\\":
        dx, dy = dy, dx
        calc_laser(x + dx, y + dy, dx, dy, grid, visited)
    elif grid[y][x] == "-":
        if dx == 0:
            calc_laser(x + 1, y, 1, 0, grid, visited)
            calc_laser(x - 1, y, -1, 0, grid, visited)
        else:
            calc_laser(x + dx, y + dy, dx, dy, grid, visited)
    elif grid[y][x] == "|":
        if dy == 0:
            calc_laser(x, y + 1, 0, 1, grid, visited)
            calc_laser(x, y - 1, 0, -1, grid, visited)
        else:
            calc_laser(x + dx, y + dy, dx, dy, grid, visited)


# Solved in 0:17:04 (Answer: 6740)
def partA(input):
    grid = input.splitlines()
    visited = defaultdict(set)
    x, y = 0, 0
    dx, dy = 1, 0
    calc_laser(x, y, dx, dy, grid, visited)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) in visited:
                print("#", end="")
            else:
                print(grid[y][x], end="")
        print("")
    res = len(visited)
    print(res)
    return res


# Solved in 0:21:28 (Answer: 7041)
def partB(input):
    grid = input.splitlines()
    best_res = 0
    # Start Left Side
    for i in range(len(grid)):
        visited = defaultdict(set)
        x, y = 0, i
        dx, dy = 1, 0
        calc_laser(x, y, dx, dy, grid, visited)
        res = len(visited)
        best_res = max(best_res, res)
    # Start Right Side
    for i in range(len(grid)):
        visited = defaultdict(set)
        x, y = len(grid[0]) - 1, i
        dx, dy = -1, 0
        calc_laser(x, y, dx, dy, grid, visited)
        res = len(visited)
        best_res = max(best_res, res)
    # Start Top Side
    for i in range(len(grid[0])):
        visited = defaultdict(set)
        x, y = i, 0
        dx, dy = 0, 1
        calc_laser(x, y, dx, dy, grid, visited)
        res = len(visited)
        best_res = max(best_res, res)
    # Start Bottom Side
    for i in range(len(grid[0])):
        visited = defaultdict(set)
        x, y = i, len(grid) - 1
        dx, dy = 0, -1
        calc_laser(x, y, dx, dy, grid, visited)
        res = len(visited)
        best_res = max(best_res, res)
    print(best_res)
    return best_res


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=16)
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
