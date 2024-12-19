# Advent of Code 2024 Day 19, https://adventofcode.com/2024/day/19
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day19.py
# This is the original solution
from collections import defaultdict
from functools import cache

from aocd.models import Puzzle

tmap = None


@cache
def check_design(design):
    # print(design)
    if not design:
        return 1
    sols = 0
    for towel in tmap[design[0]]:
        for i in range(len(towel)):
            if i == len(design) or towel[i] != design[i]:
                break
        else:
            sols += check_design(design[i + 1 :])
    return sols


# Solved in 0:10:43
def partA(input):
    check_design.cache_clear()
    global tmap
    towels, designs = input.split("\n\n")
    towels = towels.split(", ")
    tmap = defaultdict(list)
    for towel in towels:
        tmap[towel[0]].append(towel)

    res = 0
    for design in designs.split("\n"):
        possible = check_design(design)
        # print(possible)
        if possible:
            res += 1

    print(res)
    return res


# Solved in 0:48:57
def partB(input):
    print("Part B")
    check_design.cache_clear()
    global tmap
    towels, designs = input.split("\n\n")
    towels = towels.split(", ")
    assert len(towels) == len(set(towels))
    tmap = defaultdict(list)
    for towel in towels:
        tmap[towel[0]].append(towel)

    res = 0
    for design in designs.split("\n"):
        possible = check_design(design)

        res += possible

    print(res)
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=19)
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
