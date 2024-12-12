# Advent of Code 2024 Day 12, https://adventofcode.com/2024/day/12
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day12.py
# This is the original solution
from collections import deque

from aocd.models import Puzzle


# Solved in 0:14:13
def partA(input):
    print(input)
    m = input.splitlines()
    print(m)
    total = 0
    visited = set()
    q = deque()
    for ys in range(len(m)):
        for xs in range(len(m[ys])):
            # Run BFS from each unvisited cell (for each garden region)
            if (xs, ys) in visited:
                continue
            visited.add((xs, ys))
            group = m[ys][xs]
            q.append((xs, ys))
            area = 0
            perimeter = 0
            while q:
                x, y = q.popleft()
                area += 1
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(m[0]) and 0 <= ny < len(m) and m[ny][nx] == group:
                        if (nx, ny) in visited:
                            continue
                        visited.add((nx, ny))
                        q.append((nx, ny))
                    else:
                        # all neightbors that are not in the group are part of the perimeter
                        perimeter += 1
            print(f"Group {group} has area {area} and perimeter {perimeter}")
            total += area * perimeter
    print(total)
    return total


# Solved in 0:59:29
def partB(input):
    print(input)
    m = input.splitlines()
    print(m)
    total = 0
    visited = set()
    q = deque()
    for ys in range(len(m)):
        for xs in range(len(m[ys])):
            if (xs, ys) in visited:
                continue
            visited.add((xs, ys))
            group = m[ys][xs]
            q.append((xs, ys))
            area = 0
            perimeter = set()
            while q:
                x, y = q.popleft()
                area += 1
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(m[0]) and 0 <= ny < len(m) and m[ny][nx] == group:
                        if (nx, ny) in visited:
                            continue
                        visited.add((nx, ny))
                        q.append((nx, ny))
                    else:
                        perimeter.add(
                            (nx, ny, dx, dy)
                        )  # add coordinates and direction to perimeter

            # walk around permimeter to find edges
            edges = 0
            q = deque()
            while perimeter:
                # pick a random start point on the perimeter
                edges += 1
                x, y, dx, dy = perimeter.pop()
                q.append((x, y, dx, dy))
                dir = (dx, dy)
                # explore the edge using BFS
                while q:
                    x, y, dx0, dy0 = q.popleft()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if (nx, ny, dx0, dy0) in perimeter:
                            if dir == (dx0, dy0):
                                perimeter.remove((nx, ny, dx0, dy0))
                                q.append((nx, ny, dx0, dy0))

            print(f"Group {group} has area {area} and edges {edges}")

            total += area * edges
    print(total)
    return total


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=12)
    for example in puzzle.examples:
        if example.answer_a:
            inp = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
            answer = partA(inp)
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
            inp = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
            answer = partB(inp)
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
