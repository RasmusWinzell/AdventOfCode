# Advent of Code 2024 Day 23, https://adventofcode.com/2024/day/23
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day23.py
# This is the cleaned solution
from collections import Counter, defaultdict
from functools import reduce

from aocd.models import Puzzle


# Solved in 0:29:41
def partA(input):
    lst = [line.split("-") for line in input.split("\n")]
    cd = reduce(lambda d, x: d[min(x)].add(max(x)) or d, lst, defaultdict(set))
    cs = [(a, b, c) for a, d in cd.items() for b in d for c in d & cd.get(b, set())]
    return sum(1 for vals in cs if any(c.startswith("t") for c in vals))


# Solved in 0:51:28
def partB(input):
    lst = [line.split("-") for line in input.split("\n")]
    conns = defaultdict(set)
    conns = reduce(lambda d, x: d[x[0]].update(x) or d[x[1]].update(x) or d, lst, conns)
    counts = Counter(tuple(sorted(conns[c1] & conns[c2])) for c1, c2 in lst)
    return ",".join(max(counts, key=counts.get))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=23)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    