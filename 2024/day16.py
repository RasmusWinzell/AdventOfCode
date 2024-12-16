# Advent of Code 2024 Day 16, https://adventofcode.com/2024/day/16
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day16.py
# This is the original solution
from collections import defaultdict
from queue import PriorityQueue

from aocd.models import Puzzle


# Solved in 2:52:31
def partA(input):
    print(input)
    m = input.splitlines()
    s = [(x, y) for y, l in enumerate(m) for x, c in enumerate(l) if c == "S"][0]
    e = [(x, y) for y, l in enumerate(m) for x, c in enumerate(l) if c == "E"][0]

    print(s, e)

    q = PriorityQueue()
    q.put((0, s, (1, 0)))
    visited = set()
    while q:
        d, (x, y), (dx, dy) = q.get()
        if (x, y, dx, dy) in visited:
            continue
        visited.add((x, y, dx, dy))
        if (x, y) == e:
            print(d)
            return d
        for dx2, dy2 in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx2, y + dy2
            if 0 <= nx < len(m[0]) and 0 <= ny < len(m) and m[ny][nx] != "#":
                if (dx, dy) == (dx2, dy2):
                    q.put((d + 1, (nx, ny), (dx2, dy2)))
                else:
                    q.put((d + 1000 + 1, (nx, ny), (dx2, dy2)))


def print_map(m, path):
    print()
    for y, line in enumerate(m):
        for x, c in enumerate(line):
            if (x, y) in path:
                print("O", end="")
            else:
                print(c, end="")
        print()


def find_paths(prev, state, path, m):
    path.add(state[:2])
    # print(state)
    # print_map(m, path)
    for p in prev[state]:
        find_paths(prev, p, path, m)


# Solved in 11:58:23
def partB(input):
    print(input)
    m = input.splitlines()
    s = [(x, y) for y, l in enumerate(m) for x, c in enumerate(l) if c == "S"][0]
    e = [(x, y) for y, l in enumerate(m) for x, c in enumerate(l) if c == "E"][0]

    print(s, e)

    q = PriorityQueue()
    q.put((0, *s, 1, 0, None, None))
    visited = {}
    prev = defaultdict(set)
    best = float("inf")
    while q:
        d, x, y, x2, y2, x3, y3 = q.get()
        if x == 6 and y == 7:
            pass
        if d > best:
            break
        if d <= visited.get((x, y, x2, y2), float("inf")) and (x, y) != s:
            prev[(x, y, x2, y2)].add((x2, y2, x3, y3))
        if (x, y, x2, y2) in visited:
            continue
        visited[(x, y, x2, y2)] = d
        if (x, y) == e:
            best = d
            continue
        for dx2, dy2 in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx2, y + dy2
            if 0 <= nx < len(m[0]) and 0 <= ny < len(m) and m[ny][nx] != "#":
                if (x - x2, y - y2) == (dx2, dy2):
                    q.put((d + 1, nx, ny, x, y, x2, y2))
                else:
                    q.put((d + 1000 + 1, nx, ny, x, y, x2, y2))
    print(best)
    path = set()
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ss = e + (e[0] + dx, e[1] + dy)
        find_paths(prev, ss, path, m)
    print(len(path))
    return len(path)


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=16)
    for example in puzzle.examples:
        if False and example.answer_a:
            inp = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
            answer = partA(inp)
            assert (
                str(answer) == example.answer_a
            ), f"Part A: Expected {example.answer_a}, got {answer}"

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
