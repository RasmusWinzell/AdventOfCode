# Advent of Code 2023 Day 3, https://adventofcode.com/2023/day/3
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day3.py
# This is the original solution
import math
from collections import defaultdict

from aocd.models import Puzzle


# Solved in 0:16:07 (Answer: 557705)
def partA(input: str):
    engine = input.split("\n")
    visited = set()
    numbers = []
    for i, line in enumerate(engine):
        for j, c in enumerate(line):
            if c != "." and not c.isdigit():
                for i2 in range(i - 1, i + 2):
                    if i2 < 0 or i2 >= len(engine):
                        continue
                    for j2 in range(j - 1, j + 2):
                        if j2 < 0 or j2 >= len(line):
                            continue
                        if (i2, j2) in visited:
                            continue
                        loc = engine[i2][j2]
                        if loc.isdigit():
                            jn = j2
                            number = ""
                            while jn >= 0 and engine[i2][jn].isdigit():
                                jn -= 1
                            jn += 1
                            while jn < len(line) and engine[i2][jn].isdigit():
                                number += engine[i2][jn]
                                visited.add((i2, jn))
                                print(number, i2, jn)
                                jn += 1
                            numbers.append(int(number))
    print(numbers)
    return sum(numbers)


# Solved in 0:22:41 (Answer: 84266818)
def partB(input: str):
    engine = input.split("\n")
    visited = set()
    adjacent = defaultdict(list)
    for i, line in enumerate(engine):
        for j, c in enumerate(line):
            if c != "." and not c.isdigit():
                for i2 in range(i - 1, i + 2):
                    if i2 < 0 or i2 >= len(engine):
                        continue
                    for j2 in range(j - 1, j + 2):
                        if j2 < 0 or j2 >= len(line):
                            continue
                        if (i2, j2) in visited:
                            continue
                        loc = engine[i2][j2]
                        if loc.isdigit():
                            jn = j2
                            number = ""
                            while jn >= 0 and engine[i2][jn].isdigit():
                                jn -= 1
                            jn += 1
                            while jn < len(line) and engine[i2][jn].isdigit():
                                number += engine[i2][jn]
                                visited.add((i2, jn))
                                print(number, i2, jn)
                                jn += 1
                            if c == "*":
                                adjacent[(i, j)].append(int(number))
    print(adjacent)
    ratios = [math.prod(p) for p in adjacent.values() if len(p) > 1]
    print(ratios)
    return sum(ratios)


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=3)

    example = puzzle.examples[0]
    puzzle_input = example.input_data

    puzzle_input = puzzle.input_data

    # puzzle_input = """input"""

    res = partB(puzzle_input)

    puzzle.answer_b = res

    puzzle_answer = example.answer_b
    # puzzle_answer = example.answer_b
    # puzzle_answer = answer

    assert str(res) == str(
        puzzle_answer
    ), f"Part A: Expected {puzzle_answer}, got {res}"

    # puzzle.answer_a = resA
    # puzzle.answer_b = res
