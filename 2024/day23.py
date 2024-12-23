# Advent of Code 2024 Day 23, https://adventofcode.com/2024/day/23
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day23.py
# This is the original solution
from collections import defaultdict

from aocd.models import Puzzle


# Solved in 0:29:41
def partA(input):
    print(input)
    conns = [line.split("-") for line in input.split("\n")]
    connd = defaultdict(set)
    for c in conns:
        c1, c2 = sorted(c)
        connd[c1].add(c2)

    res = 0
    for c1 in connd.keys():
        for c2 in connd.get(c1, []):
            for c3 in connd.get(c2, []):
                if c3 in connd[c1]:
                    if any(c.startswith("t") for c in [c1, c2, c3]):
                        print(c1, c2, c3)
                        res += 1
    print(res)
    return res


# Solved in 0:51:28
def partB(input):
    print(input)
    conns = [line.split("-") for line in input.split("\n")]
    connd = defaultdict(set)
    for c in conns:
        c1, c2 = sorted(c)
        connd[c1].add(c2)
        connd[c2].add(c1)

    def fully_connected(connected, curr):
        for c in connected:
            if c not in connd[curr]:
                return False
        return True

    def find_connected(connected, curr):
        for c in connd[curr]:
            if c not in connected and fully_connected(connected, c):
                connected.add(c)
                find_connected(connected, c)

    best = None
    for c in connd.keys():
        connected = {c}
        find_connected(connected, c)
        if best is None or len(connected) > len(best):
            best = connected
    best = ",".join(sorted(best))
    print(best)
    return best


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=23)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         answer = partA(example.input_data)
    #         assert (
    #             str(answer) == example.answer_a
    #         ), f"Part A: Expected {example.answer_a}, got {answer}"
    # print(puzzle.answer_a)
    if puzzle.answered_a:
        answer = partA(puzzle.input_data)
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
