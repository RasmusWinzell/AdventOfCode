# Advent of Code 2024 Day 22, https://adventofcode.com/2024/day/22
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day22.py
# This is the original solution
from collections import defaultdict

from aocd.models import Puzzle


# Solved in 0:25:07
def partA(input):
    input = input.split("\n")
    res = 0
    for sec in input:
        print()
        secret = int(sec)
        for i in range(1, 2001):

            val = secret * 64
            val = val ^ secret
            val = val % 16777216
            secret = val

            val = secret // 32
            val = val ^ secret
            val = val % 16777216
            secret = val

            val = secret * 2048
            val = val ^ secret
            val = val % 16777216
            secret = val

        print(sec, secret)
        res += secret
    print(res)
    return res


# Solved in 1:17:30
def partB(input):
    #     input = """1
    # 2
    # 3
    # 2024"""
    input = input.split("\n")
    res = 0
    changes = defaultdict(int)
    for sec in input:
        print(sec)
        secret = int(sec)
        change_list = tuple()
        visited = set()
        old_price = int(str(secret)[-1])
        for i in range(1, 2001):

            val = secret * 64
            val = val ^ secret
            val = val % 16777216
            secret = val

            val = secret // 32
            val = val ^ secret
            val = val % 16777216
            secret = val

            val = secret * 2048
            val = val ^ secret
            val = val % 16777216
            secret = val

            new_price = int(str(secret)[-1])
            change = new_price - old_price
            change_list = (change_list + (change,))[-4:]

            if change_list not in visited and len(change_list) == 4:
                visited.add(change_list)
                changes[change_list] += new_price

            old_price = new_price

    # changes = sorted(changes.items(), key=lambda x: x[1], reverse=True)
    # print(changes[:10])
    res = max(changes.values())
    print(res)
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=22)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         answer = partA(example.input_data)
    #         assert (
    #             str(answer) == example.answer_a
    #         ), f"Part A: Expected {example.answer_a}, got {answer}"

    # if puzzle.answered_a:
    #     answer = partA(puzzle.input_data)
    #     assert (
    #         str(answer) == puzzle.answer_a
    #     ), f"Part A: Expected {puzzle.answer_a}, got {answer}"
    # else:
    #     puzzle.answer_a = partA(puzzle.input_data)
    #     assert puzzle.answered_a, "Answer A not correct"

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
