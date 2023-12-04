# Advent of Code 2023 Day 1, https://adventofcode.com/2023/day/1
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/day01.py
# This is the cleaned solution
import regex as re
from aocd.models import Puzzle

digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


# Solved in 0:09:41 (Answer: 56397)
def partA(input: str):
    digits = [re.findall(r"\d", line) for line in input.split("\n")]
    sums = [int(digs[0] + digs[-1]) for digs in digits]
    return sum(sums)


# Solved in 0:25:30 (Answer: 55701)
def partB(input):
    format = r"\d|" + "|".join(digit_map.keys())
    digits = [re.findall(format, line, overlapped=True) for line in input.split("\n")]
    converted_digits = [[digit_map.get(d) or d for d in digs] for digs in digits]
    sums = [int(digs[0] + digs[-1]) for digs in converted_digits]
    return sum(sums)


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=1)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
