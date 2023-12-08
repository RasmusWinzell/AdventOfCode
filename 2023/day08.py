# Advent of Code 2023 Day 8, https://adventofcode.com/2023/day/8
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day08.py
# This is the original solution
import math
import re
from collections import defaultdict
from functools import reduce

from aocd.models import Puzzle


# Solved in 0:09:58 (Answer: 13771)
def partA(input: str):
    print(input)
    instructions = input.split("\n")[0]
    words = [re.findall(r"[A-Z]+", line) for line in input.split("\n")[2:]]
    dirs = {k: {"L": l, "R": r} for k, l, r in words}
    current = "AAA"
    steps = 0
    i = 0
    while current != "ZZZ":
        current = dirs[current][instructions[i]]
        i = (i + 1) % len(instructions)
        steps += 1
    print(steps)
    return steps


# Solved in 1:07:32 (Answer: 13129439557681)
def partB(input: str):
    instructions = input.split("\n")[0]
    words = [re.findall(r"\d*[A-Z]+", line) for line in input.split("\n")[2:]]
    dirs = {k: {"L": l, "R": r} for k, l, r in words}
    currents = [k for k in dirs.keys() if k[-1] == "A"]
    cycle_end = {}
    cycle_start = {}
    cycles = []
    steps = 0
    jump = 1
    i = 0
    while len(cycles) < len(currents):
        steps += 1
        instr = instructions[i]
        for j, current in enumerate(currents):
            if current in cycle_end:
                continue
            dir = dirs[current]
            currents[j] = curr = dir[instr]
            if curr[-1] == "Z":
                if curr not in cycle_start:
                    cycle_start[curr] = steps
                elif curr not in cycle_end:
                    cycle_end[curr] = steps
                    cycles.append(cycle_end[curr] - cycle_start[curr])
                    print(cycles, len(currents))
        i = (i + 1) % len(instructions)
    starts = [cycle_start[c] % cycles[i] for i, c in enumerate(cycle_start)]
    print(starts, reduce(math.lcm, cycles))
    steps = starts[0] + cycles[0]
    i = 1
    jump = cycles[0]
    while True:
        if steps % cycles[i] == starts[i]:
            jump = math.lcm(jump, cycles[i])
            i += 1

        if i == len(cycles):
            break

        steps += jump

    print(steps)

    return steps


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=8)

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
    #     if example.answer_b:
    #         answer = partB(example.input_data)
    #         assert (
    #             str(answer) == example.answer_b
    #         ), f"Part B: Expected {example.answer_b}, got {answer}"

    if puzzle.answered_b:
        answer = partB(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_b
        ), f"Part B: Expected {puzzle.answer_b}, got {answer}"
    else:
        puzzle.answer_b = partB(puzzle.input_data)
        assert puzzle.answered_b, "Answer B not correct"
