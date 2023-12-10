# Advent of Code 2023 Day 10, https://adventofcode.com/2023/day/10
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day10.py
# This is the original solution
from collections import defaultdict

from aocd.models import Puzzle

dirs = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
    "S": [(1, 0), (0, 1), (-1, 0), (0, -1)],
}


# Solved in 0:37:16 (Answer: 6842)
def partA(input):
    grid = [list(line) for line in input.splitlines()]
    start = [
        (0, y, x, 0, 0)
        for y, row in enumerate(grid)
        for x, c in enumerate(row)
        if c == "S"
    ][0]

    queue = [start]
    visited = defaultdict(int)
    m = {}

    def show():
        print()
        for y in range(len(grid)):
            line = ""
            for x in range(len(grid[0])):
                dig = m.get((y, x), None)
                if dig is None:
                    line += "."
                else:
                    line += str(dig % 10)
            print(line)

    while queue:
        s, y, x, dy0, dx0 = queue.pop(0)
        # print(s, y, x)
        # print(visited)
        if (dy0, dx0) not in dirs[grid[y][x]] and s > 0:
            continue
        if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
            visited[(y, x)] += 1
            if visited[(y, x)] > 1:
                return s
            m[(y, x)] = s
            for dy, dx in dirs[grid[y][x]]:
                if dy == dy0 and dx == dx0:
                    continue
                queue.append((s + 1, y + dy, x + dx, -dy, -dx))


# Solved in 1:40:59 (Answer: 393)
def partB(input):
    grid = [list(line) for line in input.splitlines()]
    start = [
        (0, y, x, 0, 0)
        for y, row in enumerate(grid)
        for x, c in enumerate(row)
        if c == "S"
    ][0]

    m = {}

    def show():
        print()
        for y in range(len(grid)):
            line = ""
            for x in range(len(grid[0])):
                dig = m.get((y, x), None)
                if dig is None:
                    line += "."
                else:
                    line += dig
            print(line)

    for i in range(2):
        queue = [start]
        visited = defaultdict(int)
        m = {}
        while queue:
            s, y, x, dy0, dx0 = queue.pop(0)
            # print(s, y, x)
            # print(visited)
            if (dy0, dx0) not in dirs[grid[y][x]] and s > 0:
                continue
            if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
                visited[(y, x)] += 1
                m[(y * 2, x * 2)] = grid[y][x]
                m[(y * 2 + dy0, x * 2 + dx0)] = "O"
                if visited[(y, x)] > 1:
                    start = (0, y, x, 0, 0)
                    break
                for dy, dx in dirs[grid[y][x]]:
                    if dy == dy0 and dx == dx0:
                        continue
                    queue.append((s + 1, y + dy, x + dx, -dy, -dx))
        print()

    queue = [(-1, -1)]
    visited = set()
    while queue:
        y, x = queue.pop(0)
        if (y, x) in visited or m.get((y, x), None) is not None:
            continue
        if -1 <= y <= len(grid) * 2 and -1 <= x <= len(grid[0]) * 2:
            visited.add((y, x))
            m[(y, x)] = "x"
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                queue.append((y + dy, x + dx))

    lines = []
    for y in range(-1, len(grid) * 2 + 1):
        line = ""
        for x in range(-1, len(grid[0]) * 2 + 1):
            dig = m.get((y, x), None)
            if dig is None:
                line += "."
            else:
                line += dig
        lines.append(line)
        print(line)

    count = 0
    for y in range(0, len(grid) * 2, 2):
        for x in range(0, len(grid[0]) * 2, 2):
            if m.get((y, x), None) is None:
                count += 1

    print(count)
    return count


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=10)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         answer = partA(example.input_data)
    #         assert (
    #             str(answer) == example.answer_a
    #         ), f"Part A: Expected {example.answer_a}, got {answer}"

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

    res = partB(
        """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""
    )

    if puzzle.answered_b:
        answer = partB(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_b
        ), f"Part B: Expected {puzzle.answer_b}, got {answer}"
    else:
        puzzle.answer_b = partB(puzzle.input_data)
        assert puzzle.answered_b, "Answer B not correct"
