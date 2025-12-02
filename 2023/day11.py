# Advent of Code 2023 Day 11, https://adventofcode.com/2023/day/11
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day11.py
# This is the cleaned solution
import torch
from aocd.models import Puzzle

char_map = {".": 0, "#": 1}


def solve(input: str, N=1):
    grid = torch.tensor([[char_map[c] for c in line] for line in input.splitlines()])
    galaxies = torch.tensor(torch.nonzero(grid))
    for i in (0, 1):
        expands = torch.where(~grid.any(axis=1 - i))[0]
        galaxies[i, :] += torch.sum(galaxies[i, :, None] > expands[None, :], axis=1) * N
    return torch.sum(torch.abs(galaxies[:, :, None] - galaxies[:, None, :])) // 2


# Solved in 0:28:11 (Answer: 10276166)
def partA(input: str):
    return solve(input)


# Solved in 1:16:03 (Answer: 598693078798)
def partB(input: str):
    return solve(input, N=1000000 - 1)


if __name__ == "__main__":
    import time

    puzzle = Puzzle(year=2023, day=11)

    puzzle_input = puzzle.input_data

    t1 = time.perf_counter()
    answer_a = partA(puzzle_input)
    t2 = time.perf_counter()
    answer_b = partB(puzzle_input)
    t3 = time.perf_counter()

    print("Time A:", t2 - t1)
    print("Time B:", t3 - t2)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
