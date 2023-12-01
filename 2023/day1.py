# Advent of Code 2023 Day 1, https://adventofcode.com/2023/day/1
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/day1.py
# This is the original solution
import re

from aocd.models import Puzzle


# Solved in 0:09:41 (Answer: 56397)
def partA(input):
    print(input)
    res = []
    for line in input.split("\n"):
        number = []
        for c in line:
            try:
                digit = int(c)
                number.append(c)
            except Exception:
                pass
        res.append(int(number[0] + number[-1]))
    return sum(res)


def check_digits(input: str):
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for k, v in digits.items():
        if input.endswith(k):
            return v
    return None


# Solved in 0:25:30 (Answer: 55701)
def partB(input):
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    res = []
    for line in input.split("\n"):
        check_digits(line)
        print(res)
        number = []
        middle = ""
        for c in line:
            try:
                d2 = check_digits(middle)
                if d2 is not None:
                    number.append(str(d2))
                digit = int(c)
                print("Adding number", c)
                number.append(c)
                middle = ""
            except Exception:
                middle += c
        d2 = check_digits(middle)
        if d2 is not None:
            number.append(str(d2))
        res.append(int(number[0] + number[-1]))
    return sum(res)


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=1)

    print(len(puzzle.examples))
    # example = puzzle.examples[0]
    # puzzle_input = example.input_data
    # puzzle_answer = example.answer_a

    puzzle_input = puzzle.input_data

    #     puzzle_input = """two1nine
    # eightwothree
    # abcone2threexyz
    # xtwone3four
    # 4nineeightseven2
    # zoneight234
    # 7pqrstsixteen"""

    resA = partB(puzzle_input)
    print(resA)

    # assert resA == puzzle_answer, f"Part A: Expected {puzzle_answer}, got {resA}"

    puzzle.answer_b = resA
