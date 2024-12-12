# Advent of Code 2024 Day 7, https://adventofcode.com/2024/day/7
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day07.py
# This is the original solution
import re

from aocd.models import Puzzle


# Solved in 0:07:35
def partA(input):
    def can_equal(nums, res, target):
        if not nums or res > target:
            return res == target
        return can_equal(nums[1:], res + nums[0], target) or can_equal(
            nums[1:], res * nums[0], target
        )

    res = 0
    for line in input.splitlines():
        target, *nums = re.findall(r"\d+", line)
        eq = can_equal(list(map(int, nums)), 0, int(target))
        print(eq, target)
        if eq:
            res += int(target)
    print(res)
    return res


# Solved in 0:10:01
def partB(input):
    def can_equal(nums, res, target):
        if not nums or res > target:
            return res == target
        return (
            can_equal(nums[1:], res + nums[0], target)
            or can_equal(nums[1:], res * nums[0], target)
            or can_equal(nums[1:], int(str(res) + str(nums[0])), target)
        )

    res = 0
    for line in input.splitlines():
        target, *nums = re.findall(r"\d+", line)
        eq = can_equal(list(map(int, nums)), 0, int(target))
        print(eq, target)
        if eq:
            res += int(target)
    print(res)
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=7)
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
