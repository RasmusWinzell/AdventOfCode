# Advent of Code 2023 Day 9, https://adventofcode.com/2023/day/9
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day09.py
# This is the original solution
from aocd.models import Puzzle


# Solved in 0:12:03 (Answer: 1969958987)
def partA(input: str):
    lines = input.split("\n")
    res = 0
    for line in lines:
        nums = [list(map(int, line.split(" ")))]
        i = 0
        while any(
            diffs := [nums[i][j + 1] - nums[i][j] for j in range(len(nums[i]) - 1)]
        ):
            nums.append(diffs)
            i += 1
        nums.append(diffs + [0])

        for i in range(len(nums) - 1, 0, -1):
            nums[i - 1] += [nums[i][-1] + nums[i - 1][-1]]

        res += nums[0][-1]

    return res


# Solved in 0:15:49 (Answer: 1068)
def partB(input):
    lines = input.split("\n")
    res = 0
    for line in lines:
        nums = [list(map(int, line.split(" ")))]
        i = 0
        while any(
            diffs := [nums[i][j + 1] - nums[i][j] for j in range(len(nums[i]) - 1)]
        ):
            nums.append(diffs)
            i += 1
        nums.append([0] + diffs + [0])

        for i in range(len(nums) - 1, 0, -1):
            nums[i - 1] = [nums[i - 1][0] - nums[i][0]] + nums[i - 1]
            nums[i - 1] = nums[i - 1] + [nums[i][-1] + nums[i - 1][-1]]

        print(nums[0][0])
        res += nums[0][0]

    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=9)
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
