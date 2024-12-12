# Advent of Code 2024 Day 5, https://adventofcode.com/2024/day/5
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day05.py
# This is the original solution
from collections import defaultdict

from aocd.models import Puzzle


# Solved in 0:19:02
def partA(input):
    print(input)
    befores = defaultdict(set)
    # afters = defaultdict(set)

    mid_sum = 0
    for line in input.split("\n"):
        if "|" in line:
            x1, x2 = map(int, line.split("|"))
            befores[x2].add(x1)
            # afters[x1].add(x2)
        else:
            if not line:
                continue
            pages = list(map(int, line.split(",")))
            correct = True
            for i in range(len(pages) - 1):
                for j in range(i + 1, len(pages)):
                    if pages[j] in befores[pages[i]]:
                        # Incorrect order
                        correct = False
            if correct:
                # Correct order
                print("Correct order:", pages)
                mid_number = pages[len(pages) // 2]
                mid_sum += mid_number
    print(mid_sum)
    return mid_sum


# Solved in 0:24:21
def partB(input):
    print(input)
    befores = defaultdict(set)
    # afters = defaultdict(set)

    mid_sum = 0
    for line in input.split("\n"):
        if "|" in line:
            x1, x2 = map(int, line.split("|"))
            befores[x2].add(x1)
            # afters[x1].add(x2)
        else:
            if not line:
                continue
            pages = list(map(int, line.split(",")))
            correct = True
            for i in range(len(pages) - 1):
                for j in range(i + 1, len(pages)):
                    if pages[j] in befores[pages[i]]:
                        # Incorrect order
                        correct = False
            if not correct:
                # Not correct order
                print("Incorrect order:", pages)
                inc = set(pages)

                sorted_pages = sorted(
                    pages, key=lambda x: len(befores[x].intersection(inc))
                )
                print(pages, "=>", sorted_pages)

                mid_number = sorted_pages[len(sorted_pages) // 2]
                mid_sum += mid_number
    print(mid_sum)
    return mid_sum


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=5)
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
