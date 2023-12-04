# Advent of Code 2023 Day 4, https://adventofcode.com/2023/day/4
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day4.py
# This is the original solution
import re

from aocd.models import Puzzle


# Solved in 0:10:37 (Answer: 21158)
def partA(input: str):
    points = 0
    for line in input.split("\n"):
        cards = line.split(": ")[1]
        card_a, card_b = cards.split("|")
        num_a = set([int(num) for num in re.findall(r"\d+", card_a)])
        num_b = [int(num) for num in re.findall(r"\d+", card_b)]
        print(num_a, num_b)
        same = sum(1 for num in num_b if num in num_a)
        print(same, 2 ** (same - 1))
        if same:
            points += 2 ** (same - 1)
    return points


# Solved in 0:21:18 (Answer: 6050769)
def partB(input: str):
    lines = input.split("\n")
    card_count = {i: 1 for i in range(len(lines))}
    for i, line in enumerate(lines):
        cards = line.split(": ")[1]
        card_a, card_b = cards.split("|")
        num_a = set([int(num) for num in re.findall(r"\d+", card_a)])
        num_b = [int(num) for num in re.findall(r"\d+", card_b)]
        same = sum(1 for num in num_b if num in num_a)
        for j in range(i + 1, min(i + 1 + same, len(lines))):
            print("Adding", j + 1)
            card_count[j] += card_count[i]
    print(card_count)
    return sum(card_count.values())


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=4)

    example = puzzle.examples[0]
    puzzle_input = example.input_data

    puzzle_input = puzzle.input_data

    # puzzle_input = """input"""

    res = partB(puzzle_input)

    # puzzle_answer = example.answer_a
    # puzzle_answer = example.answer_b
    # # puzzle_answer = answer

    # assert str(res) == str(
    #     puzzle_answer
    # ), f"Part A: Expected {puzzle_answer}, got {res}"

    # puzzle.answer_a = res
    puzzle.answer_b = res
