# Advent of Code 2024 Day 1, https://adventofcode.com/2024/day/1
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day01.py
# This is the original solution
from aocd.models import Puzzle


# Solved in 0:07:20
def partA(input):
    print(input)
    x = [x.split() for x in input.split("\n")]
    print(x)
    a = sorted([int(x[0]) for x in x])
    b = sorted([int(x[1]) for x in x])

    dists = [abs(a[i] - b[i]) for i in range(len(a))]
    return sum(dists)


# Solved in 0:19:34
def partB(input):
    print()
    print(input)
    x = [x.split() for x in input.split("\n")]
    # print(x)
    a = sorted([int(x[0]) for x in x])
    b = sorted([int(x[1]) for x in x])
    # print(a)
    # print(b)

    j = 0
    res = 0
    for i in range(len(a)):
        if i - 1 < 0 or a[i - 1] != a[i]:
            count = 0
        while (j < len(b)) and (a[i] >= b[j]):
            print("herre", a[i], b[j])
            if a[i] == b[j]:
                count += 1
            j += 1
        # print(a[i], count)
        res += a[i] * count
    print(res)
    return res


if __name__ == "__main__":

    puzzle = Puzzle(year=2024, day=1)
    for example in puzzle.examples:
        if example.answer_a:
            answer = partA(example.input_data)
            assert (
                str(answer) == example.answer_a
            ), f"Part A: Expected {example.answer_a}, got {answer}"

    if puzzle.answered_a:
        answer = partA(puzzle.input_data)
        print(answer)
        assert (
            str(answer) == puzzle.answer_a
        ), f"Part A: Expected {puzzle.answer_a}, got {answer}"
    else:
        puzzle.answer_a = partA(puzzle.input_data)
        assert puzzle.answered_a, "Answer A not correct"

    for example in puzzle.examples:
        if example.answer_b:
            answer = partB(example.input_data)
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
