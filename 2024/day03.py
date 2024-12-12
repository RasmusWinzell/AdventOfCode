# Advent of Code 2024 Day 3, https://adventofcode.com/2024/day/3
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day03.py
# This is the original solution
import re

from aocd.models import Puzzle


# Solved in 0:06:50
def partA(input):
    reg = re.compile(r"mul\((\d+),(\d+)\)")
    mathes = reg.findall(input)
    res = sum([int(a) * int(b) for a, b in mathes])
    return res


# Solved in 0:20:34
def partB(input):
    print(input)
    reg = re.compile(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))")
    res = 0
    enable = True
    for match in reg.finditer(input):
        print(match)
        if "mul" in match.group(1) and enable:
            res += int(match.group(2)) * int(match.group(3))
        elif "don't" in match.group(1):
            enable = False
        elif "do" in match.group(1):
            enable = True
    print(res)
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=3)
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
    # if True:
    #     answer = partB(
    #         "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    #     )
    #     assert str(answer) == 48, f"Part B: Expected {48}, got {answer}"

    if puzzle.answered_b:
        answer = partB(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_b
        ), f"Part B: Expected {puzzle.answer_b}, got {answer}"
    else:
        puzzle.answer_b = partB(puzzle.input_data)
        assert puzzle.answered_b, "Answer B not correct"
