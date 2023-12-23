# Advent of Code 2023 Day 23, https://adventofcode.com/2023/day/23
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day23.py
# This is the original solution
import sys

from aocd.models import Puzzle

sys.setrecursionlimit(10000)

directions = {
    ".": [(0, 1), (0, -1), (1, 0), (-1, 0)],
    "^": [(-1, 0)],
    "v": [(1, 0)],
    ">": [(0, 1)],
    "<": [(0, -1)],
}


def dfs(sy, sx, ey, ex, lines, visited, dirs):
    res = 0
    if (sy, sx) == (ey, ex):
        res = len(visited)
    if (sy, sx) in visited:
        return 0
    visited.add((sy, sx))
    for dy, dx in dirs[lines[sy][sx]]:
        if 0 <= sy + dy < len(lines) and 0 <= sx + dx < len(lines[0]):
            if lines[sy + dy][sx + dx] == "#":
                continue
            res = max(res, dfs(sy + dy, sx + dx, ey, ex, lines, visited.copy(), dirs))
    return res


# Solved in 0:13:30 (Answer: 2042)
def partA(input):
    lines = input.splitlines()
    sy, sx = (0, lines[0].index("."))
    ey, ex = (len(lines) - 1, lines[-1].index("."))

    res = dfs(sy, sx, ey, ex, lines, set(), directions)
    print(res)
    return res


directions2 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
arrows = ["^", "v", ">", "<"]


def find_paths_dfs(y, x, ey, ex, lines, visited, dist, py, px):
    res = []
    if (y, x) in visited:
        return res
    visited.add((y, x))
    next_pos = []
    for dy, dx in directions[lines[y][x]]:
        if 0 <= y + dy < len(lines) and 0 <= x + dx < len(lines[0]):
            if lines[y + dy][x + dx] == "#":
                continue
            next_pos.append((y + dy, x + dx))

    if len(next_pos) > 2 or (y, x) == (ey, ex):
        res.append((dist, (py, px), (y, x)))
        py, px = y, x
        dist = 0

    for ny, nx in next_pos:
        res += find_paths_dfs(ny, nx, ey, ex, lines, visited.copy(), dist + 1, py, px)

    return res


from collections import defaultdict


def path_dfs(y, x, ey, ex, paths, visited, dist):
    if (y, x) == (ey, ex):
        return dist
    if (y, x) in visited:
        return 0
    visited.add((y, x))
    res = 0
    for d, (ny, nx) in paths[(y, x)]:
        res = max(res, path_dfs(ny, nx, ey, ex, paths, visited.copy(), dist + d))
    return res


# Solved in 1:04:28 (Answer: 6466)
def partB(input):
    lines = input.splitlines()
    sy, sx = (0, lines[0].index("."))
    ey, ex = (len(lines) - 1, lines[-1].index("."))

    res = find_paths_dfs(sy, sx, ey, ex, lines, set(), 0, sy, sx)
    print(res[0])

    paths = defaultdict(set)
    for dist, start, end in res:
        paths[start].add((dist, end))
        paths[end].add((dist, start))

    res = path_dfs(sy, sx, ey, ex, paths, set(), 0)
    print(res)
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=23)
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
    # exit()
    if puzzle.answered_b:
        answer = partB(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_b
        ), f"Part B: Expected {puzzle.answer_b}, got {answer}"
    else:
        puzzle.answer_b = partB(puzzle.input_data)
        assert puzzle.answered_b, "Answer B not correct"
