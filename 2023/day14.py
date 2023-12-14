# Advent of Code 2023 Day 14, https://adventofcode.com/2023/day/14
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day14.py
# This is the original solution
from aocd.models import Puzzle


# Solved in 0:07:58 (Answer: 103333)
def partA(input):
    lines = [list(line) for line in input.splitlines()]

    # tilt
    for i in range(1, len(lines)):
        for j in range(i, 0, -1):
            for k in range(len(lines[j])):
                if lines[j][k] == "O" and lines[j - 1][k] == ".":
                    lines[j][k] = "."
                    lines[j - 1][k] = "O"
    for line in lines:
        print("".join(line))

    load = sum(
        (len(lines) - i) * "".join(line).count("O") for i, line in enumerate(lines)
    )
    print(load)
    return load


def spin_cycle(lines):
    for i in range(1, len(lines)):
        # for j in range(i, 0, -1):
        for k in range(len(lines[0])):
            if lines[i][k] == "O":
                j = i
                while (j := j - 1) >= 0 and lines[j][k] == ".":
                    pass
                lines[i][k] = "."
                lines[j + 1][k] = "O"

    for i in range(1, len(lines[0])):
        # for j in range(i, 0, -1):
        for k in range(len(lines)):
            if lines[k][i] == "O":
                j = i
                while (j := j - 1) >= 0 and lines[k][j] == ".":
                    pass
                lines[k][i] = "."
                lines[k][j + 1] = "O"

    for i in range(len(lines) - 2, -1, -1):
        # for j in range(i, len(lines) - 1):
        for k in range(len(lines[0])):
            if lines[i][k] == "O":
                j = i
                while (j := j + 1) < len(lines) and lines[j][k] == ".":
                    pass
                lines[i][k] = "."
                lines[j - 1][k] = "O"
    for i in range(len(lines[0]) - 2, -1, -1):
        # for j in range(i, len(lines[0]) - 1):
        for k in range(len(lines)):
            if lines[k][i] == "O":
                j = i
                while (j := j + 1) < len(lines[0]) and lines[k][j] == ".":
                    pass
                lines[k][i] = "."
                lines[k][j - 1] = "O"


# Solved in 1:49:30 (Answer: 97241)
def partB(input):
    lines = [list(line) for line in input.splitlines()]
    configs = {}
    cycles = 1000000000
    for x in range(cycles):
        if (x + 1) % 1000 == 0:
            print(f"Cycle {x+1}")
        spin_cycle(lines)
        # for line in lines:
        #     print("".join(line))
        # load = sum(
        #     (len(lines) - i) * "".join(line).count("O") for i, line in enumerate(lines)
        # )
        # print(load)

        l = tuple(tuple(line) for line in lines)
        if l in configs:
            start = 1 + configs[l]
            period = x - configs[l]
            rest = (cycles - start) % period
            print(start, x, period, rest)
            for x2 in range(rest):
                spin_cycle(lines)
                for line in lines:
                    print("".join(line))
                load = sum(
                    (len(lines) - i) * "".join(line).count("O")
                    for i, line in enumerate(lines)
                )
                print(load)
            load = sum(
                (len(lines) - i) * "".join(line).count("O")
                for i, line in enumerate(lines)
            )
            print(load)
            return load
        else:
            configs[l] = x


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=14)
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

    # partB(puzzle.input_data)
    # exit()

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
