# Advent of Code 2024 Day 8, https://adventofcode.com/2024/day/8
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day08.py
# This is the original solution
from aocd.models import Puzzle


# Solved in 0:15:54
def partA(input):
    antennas = {}
    m = [list(line) for line in input.splitlines()]
    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            if char != ".":
                antennas[(x, y)] = char

    count = 0
    keys = list(antennas.keys())
    for i, k1 in enumerate(keys):
        for j, k2 in enumerate(keys[i + 1 :]):
            if not antennas[k1] == antennas[k2]:
                continue
            x1, y1 = k1
            x2, y2 = k2

            x3 = x2 + (x2 - x1)
            y3 = y2 + (y2 - y1)

            if (
                0 <= x3 < len(line)
                and 0 <= y3 < len(input.splitlines())
                and m[y3][x3] != "#"
            ):
                m[y3][x3] = "#"
                count += 1

            x4 = x1 + (x1 - x2)
            y4 = y1 + (y1 - y2)

            if (
                0 <= x4 < len(line)
                and 0 <= y4 < len(input.splitlines())
                and m[y4][x4] != "#"
            ):
                m[y4][x4] = "#"
                count += 1

    for line in m:
        print("".join(line))

    print(count)
    return count


# Solved in 0:22:52
def partB(input):
    antennas = {}
    m = [list(line) for line in input.splitlines()]
    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            if char != ".":
                antennas[(x, y)] = char

    count = 0
    keys = list(antennas.keys())
    for i, k1 in enumerate(keys):
        for j, k2 in enumerate(keys[i + 1 :]):
            if not antennas[k1] == antennas[k2]:
                continue
            x1, y1 = k1
            x2, y2 = k2

            a = 0
            while True:
                x3 = x2 + (x2 - x1) * a
                y3 = y2 + (y2 - y1) * a
                a += 1

                if 0 <= x3 < len(line) and 0 <= y3 < len(input.splitlines()):
                    if m[y3][x3] != "#":
                        m[y3][x3] = "#"
                        count += 1
                else:
                    break

            b = 0
            while True:
                x4 = x1 + (x1 - x2) * b
                y4 = y1 + (y1 - y2) * b
                b += 1

                if 0 <= x4 < len(line) and 0 <= y4 < len(input.splitlines()):
                    if m[y4][x4] != "#":
                        m[y4][x4] = "#"
                        count += 1
                else:
                    break

    for line in m:
        print("".join(line))

    print(count)
    return count


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=8)
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

    if puzzle.answered_b:
        answer = partB(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_b
        ), f"Part B: Expected {puzzle.answer_b}, got {answer}"
    else:
        puzzle.answer_b = partB(puzzle.input_data)
        assert puzzle.answered_b, "Answer B not correct"
