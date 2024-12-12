# Advent of Code 2024 Day 9, https://adventofcode.com/2024/day/9
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day09.py
# This is the original solution
from aocd.models import Puzzle


# Solved in 0:16:14
def partA(input):
    spaces = []
    file = True
    curr_id = 0
    for i, digit in enumerate(input):
        if file:
            spaces += [curr_id] * int(digit)
            curr_id += 1
        else:
            spaces += ["."] * int(digit)
        file = not file
    print("".join(map(str, spaces)))

    i = 0
    while i < len(spaces):
        if spaces[i] == ".":
            while spaces[-1] == ".":
                spaces.pop()
            if i >= len(spaces):
                break
            spaces[i] = spaces.pop()
        i += 1

    print("".join(map(str, spaces)))

    checksum = 0
    for i, digit in enumerate(spaces):
        checksum += i * int(digit)
    print(checksum)
    return checksum


# Solved in 0:41:01
def partB(input):
    spaces = []
    files_lens = []
    free_lens = []
    file = True
    curr_id = 0
    for i, digit in enumerate(input):
        if file:
            files_lens.append([int(digit), len(spaces)])
            spaces += [curr_id] * int(digit)
            curr_id += 1
        else:
            free_lens.append([int(digit), len(spaces)])
            spaces += ["."] * int(digit)
        file = not file
    print("".join(map(str, spaces)))

    for i in range(len(files_lens) - 1, -1, -1):
        curr_id = []
        for j in range(len(free_lens)):
            if (
                free_lens[j][0] >= files_lens[i][0]
                and free_lens[j][1] < files_lens[i][1]
            ):
                for x in range(files_lens[i][0]):
                    spaces[free_lens[j][1] + x] = spaces[files_lens[i][1] + x]
                    curr_id.append(str(spaces[files_lens[i][1] + x]))
                    spaces[files_lens[i][1] + x] = "."
                free_lens[j][0] -= files_lens[i][0]
                free_lens[j][1] += files_lens[i][0]
                break
        # print("".join(curr_id))
        # print("".join(map(str, spaces)))

    checksum = 0
    for i, digit in enumerate(spaces):
        if digit != ".":
            checksum += i * int(digit)
    print(checksum)
    return checksum


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=9)
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
