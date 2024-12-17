# Advent of Code 2024 Day 17, https://adventofcode.com/2024/day/17
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day17.py
# This is the cleaned solution
import re
from itertools import starmap, zip_longest
from operator import eq

from aocd.models import Puzzle

digits = re.compile(r"-?\d+")


def run(program, A, B, C):
    def literal(x):
        return x

    def combo(x):
        return x if x < 4 else [A, B, C][x - 4]

    out_buf = []
    i = 0
    while i < len(program):
        opcode, operand = program[i], program[i + 1]
        match opcode:
            case 0:  # adv
                A = A // 2 ** combo(operand)
            case 1:  # bxl
                B = B ^ literal(operand)
            case 2:  # bst
                B = combo(operand) % 8
            case 3:  # jnz
                if A != 0:
                    i = literal(operand)
                    continue
            case 4:  # bxc
                B = B ^ C
            case 5:  # out
                out_buf.append(combo(operand) % 8)
            case 6:  # bdv
                B = A // 2 ** combo(operand)
            case 7:  # cdv
                C = A // 2 ** combo(operand)
        i += 2

    return out_buf


# Solved in 0:27:12
def partA(input):
    A, B, C, *p = map(int, digits.findall(input))
    output = ",".join(map(str, run(p, A, B, C)))
    return output


# Solved in 2:17:20
def partB(input):
    _, B, C, *p = map(int, digits.findall(input))
    A, o = 0, []
    while (c := [0, *starmap(eq, zip_longest(p, o))][::-1].index(0)) < len(p):
        o = run(p, A := A + 8 ** (len(p) - c - 1), B, C)
    return A


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=17)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    