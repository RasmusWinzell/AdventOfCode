# Advent of Code 2024 Day 17, https://adventofcode.com/2024/day/17
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day17.py
# This is the original solution
import re

from aocd.models import Puzzle

digits = re.compile(r"-?\d+")


# Solved in 0:27:12
def partA(input):
    m = input.splitlines()
    A = int(digits.findall(m[0])[0])
    B = int(digits.findall(m[1])[0])
    C = digits.findall(m[2])[0]

    program = list(map(int, digits.findall(m[4])))

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

    output = ",".join(map(str, out_buf))
    print(output)
    return output


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


# Solved in 2:17:20
def partB(input):
    print(input)
    m = input.splitlines()
    B = int(digits.findall(m[1])[0])
    C = digits.findall(m[2])[0]

    program = list(map(int, digits.findall(m[4])))
    print(len(program))

    def check_correct(program, output):
        if len(program) != len(output):
            return 0
        correct = 0
        for i in range(len(program) - 1, -1, -1):
            if program[i] != output[i]:
                break
            correct += 1
        return correct

    A = 0
    minA = 0
    correct = 0
    output = []
    for idx in range(len(program) - 1, -1, -1):
        print(idx, correct)
        while (
            check_correct(program, output) <= correct
        ):  # len(output) < len(program) or output[idx] != program[idx]:
            A += 8**idx
            # print(A)
            output = run(program, A, B, C)
            # print(output)
        correct = min(len(program) - idx, check_correct(program, output))
        minA = A

    print(minA, ",".join(map(str, run(program, minA, B, C))))
    return minA


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=17)
    for example in puzzle.examples:
        if example.answer_a:
            answer = partA(example.input_data)
            assert (
                str(answer) == example.answer_a
            ), f"Part A: Expected {example.answer_a}, got {answer}"

    if puzzle.answered_a:
        answer = partA(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_a
        ), f"Part A: Expected {puzzle.answer_a}, got {answer}"
    else:
        puzzle.answer_a = partA(puzzle.input_data)
        assert puzzle.answered_a, "Answer A not correct"

    for example in puzzle.examples:
        if False and example.answer_b:
            inp = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
            answer = partB(inp)
            assert (
                str(answer) == example.answer_b
            ), f"Part B: Expected {example.answer_b}, got {answer}"

    if puzzle.answered_b:
        answer = partB(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_b
        ), f"Part B: Expected {puzzle.answer_b}, got {answer}"
    else:
        puzzle.answer_b = partB(puzzle.input_data)
        assert puzzle.answered_b, "Answer B not correct"
