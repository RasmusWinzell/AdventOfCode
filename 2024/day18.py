# Advent of Code 2024 Day 18, https://adventofcode.com/2024/day/18
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day18.py
# This is the original solution
from collections import deque

from aocd.models import Puzzle


def solve(input, size, fallen):
    bytes = set(tuple(map(int, l.split(","))) for l in input.split("\n")[:fallen])
    visited = set()
    q = deque([(0, 0, 0)])
    while q:
        d, x, y = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if (x, y) == (size - 1, size - 1):
            return d
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in bytes and 0 <= nx < size and 0 <= ny < size:
                q.append((d + 1, nx, ny))
    return None


# Solved in 0:19:37
def partA(input):
    res = solve(input, size=71, fallen=1024)
    return res


# Solved in 0:31:22
def partB(input):
    size = 71
    low, high = 0, input.count("\n")
    while low < high:
        mid = (low + high) // 2
        if solve(input, size, mid) is None:
            high = mid
        else:
            low = mid + 1
    res = input.splitlines()[low - 1]
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=18)
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

    if puzzle.answered_b:
        answer = partB(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_b
        ), f"Part B: Expected {puzzle.answer_b}, got {answer}"
    else:
        puzzle.answer_b = partB(puzzle.input_data)
        assert puzzle.answered_b, "Answer B not correct"
