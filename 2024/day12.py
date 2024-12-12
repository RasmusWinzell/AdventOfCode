# Advent of Code 2024 Day 12, https://adventofcode.com/2024/day/12
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day12.py
# This is the cleaned solution
import itertools
from collections import deque

from aocd.models import Puzzle


def neighbors(x, y):
    return [(x + dx, y + dy, dx, dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))]


def in_bounds(m, x, y):
    return 0 <= x < len(m[0]) and 0 <= y < len(m)


def find_groups(m):
    unvisited = set(itertools.product(range(len(m[0])), range(len(m))))
    q = deque()
    while unvisited:
        sx, sy = unvisited.pop()
        q.append((sx, sy))
        area = 0
        perimeter = set()
        while q:
            x, y = q.popleft()
            area += 1
            for nx, ny, dx, dy in neighbors(x, y):
                if in_bounds(m, nx, ny) and m[ny][nx] == m[sy][sx]:
                    if (nx, ny) in unvisited:
                        unvisited.remove((nx, ny))
                        q.append((nx, ny))
                else:
                    perimeter.add((nx, ny, dx, dy))
        yield area, perimeter


def remove_edge(perimeter):
    q = deque()
    q.append(perimeter.pop())
    while q:
        x, y, dx0, dy0 = q.popleft()
        for nx, ny, dx, dy in neighbors(x, y):
            if (nx, ny, dx0, dy0) in perimeter:
                perimeter.remove((nx, ny, dx0, dy0))
                q.append((nx, ny, dx0, dy0))
    return perimeter


# Solved in 0:14:13
def partA(input):
    m = input.splitlines()
    res = sum(a * len(p) for a, p in find_groups(m))
    return res


# Solved in 0:59:29
def partB(input):
    m = input.splitlines()
    s = 0
    for area, perimeter in find_groups(m):
        edges = 1
        while remove_edge(perimeter):
            edges += 1
        s += area * edges
    print(s)
    return 0


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=12)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    