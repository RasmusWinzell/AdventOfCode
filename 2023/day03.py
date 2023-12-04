# Advent of Code 2023 Day 3, https://adventofcode.com/2023/day/3
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day03.py
# This is the cleaned solution
import math
import re
from collections import defaultdict
from itertools import product

from aocd.models import Puzzle


def search_engine(input: str):
    symbol_map, num_map = {}, {}
    for i, line in enumerate(input.split("\n")):
        for m in re.finditer(r"[^\.\d]", line):  # Finds all symbols
            symbol_map[(i, m.start())] = m.group()
        for m in re.finditer(r"\d+", line):  # Finds all numbers
            id = len(num_map)
            for j in range(*m.span()):
                number = int(m.group())
                num_map[(i, j)] = (id, number)
    return symbol_map, num_map


# Solved in 0:16:07 (Answer: 557705)
def partA(input: str):
    symbol_map, num_map = search_engine(input)

    num_sum = 0
    visited = set()
    for (i, j), _ in symbol_map.items():
        for i2, j2 in product(range(i - 1, i + 2), range(j - 1, j + 2)):  # Neighborhood
            if neighbor := num_map.get((i2, j2)):
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                num_sum += neighbor[1]
    return num_sum


# Solved in 0:22:41 (Answer: 84266818)
def partB(input: str):
    symbol_map, num_map = search_engine(input)

    adjacent = defaultdict(list)
    visited = set()
    for (i, j), _ in symbol_map.items():
        for i2, j2 in product(range(i - 1, i + 2), range(j - 1, j + 2)):  # Neighborhood
            if neighbor := num_map.get((i2, j2)):
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                adjacent[(i, j)].append(neighbor[1])
    ratios = [math.prod(p) for p in adjacent.values() if len(p) > 1]
    return sum(ratios)


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=3)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
