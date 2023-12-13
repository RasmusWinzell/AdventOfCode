# Advent of Code 2023 Day 13, https://adventofcode.com/2023/day/13
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day13.py
# This is the original solution
from aocd.models import Puzzle


def find_split(lines):
    possible_split = None
    split_length = 0
    for i in range(1, len(lines)):
        # print(lines[i], "-", lines[i - 1], lines[i] == lines[i - 1], possible_split)

        if possible_split is not None and (i - 1 - 2 * split_length) < 0:
            # print(f"Split done at {i}")
            break
        elif possible_split is not None and (
            lines[i] == lines[i - 1 - 2 * split_length]
        ):
            # print(f"Continued split at {i} with {i-1-2*split_length}")
            split_length += 1
        else:
            # print(f"Reset split at {i}")
            possible_split = None
            split_length = 0
        if possible_split is None and lines[i] == lines[i - 1]:
            # print(f"Found split at {i}")
            possible_split = i
            split_length = 1
    return possible_split


def find_other_split(lines):
    bit_lines = [int(line.replace(".", "0").replace("#", "1"), 2) for line in lines]
    for split in range(1, len(lines)):
        diff = 0
        for offset in range(min(split, len(lines) - split)):
            # print(
            #     bin(bit_lines[split - offset - 1]),
            #     bin(bit_lines[split + offset]),
            #     split - offset - 1,
            #     split + offset,
            # )
            diff += (
                bit_lines[split - offset - 1] ^ bit_lines[split + offset]
            ).bit_count()
            if diff > 1:
                break
        # print(split, diff)
        if diff == 1:
            return split
    return None


# Solved in 0:39:04 (Answer: 37975)
def partA(input):
    patterns = input.split("\n\n")
    res = 0
    # patterns = patterns[47:48]
    for i, pattern in enumerate(patterns):
        lines = pattern.splitlines()
        lines_transposed = ["".join(x) for x in zip(*lines)]

        # print("Horizontal:")
        horizontal_split = find_split(lines)
        # print("Vertical:")
        vertical_split = find_split(lines_transposed)

        res += (vertical_split or 0) + (horizontal_split or 0) * 100
    print(res)
    return res


# Solved in 1:09:30 (Answer: 32497)
def partB(input):
    patterns = input.split("\n\n")
    res = 0
    # patterns = patterns[95:96]
    for i, pattern in enumerate(patterns):
        lines = pattern.splitlines()
        lines_transposed = ["".join(x) for x in zip(*lines)]

        # print("Original:", find_split(lines), find_split(lines_transposed))

        # print("Horizontal:")
        horizontal_split = find_other_split(lines)
        # print("Vertical:")
        vertical_split = find_other_split(lines_transposed)

        res += (vertical_split or 0) + (horizontal_split or 0) * 100
    print(res)
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=13)
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
