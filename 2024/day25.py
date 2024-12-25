# Advent of Code 2024 Day 25, https://adventofcode.com/2024/day/25
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day25.py
# This is the original solution
from aocd.models import Puzzle

V = {"#": 1, ".": 0}


# Solved in 1:08:45
def partA(input):
    print(input)
    schems = [
        line.split("\n")
        for line in input.replace("#", "1").replace(".", "0").split("\n\n")
    ]
    print(schems)
    locks = [[6 - sum(map(int, r)) for r in zip(*s)] for s in schems if "1" in s[0]]
    keys = [[sum(map(int, r)) - 1 for r in zip(*s)] for s in schems if "1" in s[-1]]
    assert len(locks) + len(keys) == len(schems)
    locks2 = [[] for _ in range(5 * 5)]
    for lock in locks:
        locks2[sum(lock)].append(lock)

    res = 0
    for key in keys:
        size = sum(key)
        for ls in range(size, 5 * 5):
            for lock in locks2[ls]:
                if all(k <= l for k, l in zip(key, lock)):
                    res += 1
    print(res)
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=25)
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
