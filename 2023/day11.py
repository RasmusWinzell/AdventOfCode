# Advent of Code 2023 Day 11, https://adventofcode.com/2023/day/11
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day11.py
# This is the original solution
from aocd.models import Puzzle


def bfs(grid, ys, xs):
    queue = [(0, ys, xs)]
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dists = []
    while queue:
        dist, y, x = queue.pop(0)
        if grid[y][x] == "#" and (y, x) != (ys, xs):
            dists.append((dist - 2, (y, x), (ys, xs)))
        if visited[y][x]:
            continue
        visited[y][x] = True
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]):
                queue.append((dist + 1, new_y, new_x))
    return dists


# Solved in 0:28:11 (Answer: 10276166)
def partA(input: str):
    grid = [list(line) for line in input.splitlines()]

    y = 0
    while y < len(grid):
        if not any(cell == "#" for cell in grid[y]):
            grid.insert(y, ["." for _ in range(len(grid[0]))])
            y += 1
        y += 1

    x = 0
    while x < len(grid[0]):
        if not any(row[x] == "#" for row in grid):
            for row in grid:
                row.insert(x, ".")
            x += 1
        x += 1

    print("\n".join("".join(row) for row in grid))

    dists = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "#":
                for dist, n1, n2 in bfs(grid, y, x):
                    key = tuple(sorted([n1, n2]))
                    dists[key] = dist

    for k, v in dists.items():
        print(k, v)
    print(len(dists), sum(dists.values()))
    return sum(dists.values())


# Solved in 1:16:03 (Answer: 598693078798)
def partB(input):
    grid = [list(line) for line in input.splitlines()]

    horizontals = set()

    y = 0
    while y < len(grid):
        if not any(cell == "#" for cell in grid[y]):
            horizontals.add(y)
        y += 1

    verticals = set()

    x = 0
    while x < len(grid[0]):
        if not any(row[x] == "#" for row in grid):
            verticals.add(x)
        x += 1

    print("vert", verticals)
    print("hor", horizontals)

    print("\n".join("".join(row) for row in grid))

    galaxies = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "#":
                galaxies.append((y, x))

    total_dist = 0
    expand = 1e6
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            y1, x1 = galaxies[i]
            y2, x2 = galaxies[j]
            dist = 0
            for y in range(min(y1, y2) + 1, max(y1, y2) + 1):
                if y in horizontals:
                    dist += expand
                else:
                    dist += 1

            for x in range(min(x1, x2) + 1, max(x1, x2) + 1):
                if x in verticals:
                    dist += expand
                else:
                    dist += 1

            print(galaxies[i], galaxies[j], dist)

            total_dist += dist

    print(total_dist)
    return total_dist


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=11)
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
