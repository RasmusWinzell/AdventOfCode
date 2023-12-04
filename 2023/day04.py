# Advent of Code 2023 Day 4, https://adventofcode.com/2023/day/4
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day04.py
# This is the cleaned solution
import re

from aocd.models import Puzzle


# Solved in 0:10:37 (Answer: 21158)
def partA(input: str):
    points = 0
    for line in input.split("\n"):
        numbers = list(map(int, re.findall(r"\d+", line.split(":")[1])))
        wins = len(numbers) - len(set(numbers))  # Difference is number of wins
        if wins:
            points += 2 ** (wins - 1)
    return points


# Solved in 0:21:18 (Answer: 6050769)
def partB(input: str):
    lines = input.split("\n")
    card_count = {i: 1 for i in range(len(lines))}
    for i, line in enumerate(lines):
        numbers = list(map(int, re.findall(r"\d+", line.split(":")[1])))
        wins = len(numbers) - len(set(numbers))  # Difference is number of wins
        for j in range(i + 1, min(i + 1 + wins, len(lines))):
            card_count[j] += card_count[i]
    return sum(card_count.values())


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=4)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
