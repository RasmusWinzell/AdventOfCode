# Advent of Code 2023 Day 6, https://adventofcode.com/2023/day/6
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day06.py
# This is the original solution
from aocd.models import Puzzle


# Solved in 0:10:05 (Answer: 5133600)
def partA(input: str):
    print(input)
    lines = input.split("\n")
    times = list(map(int, lines[0].split()[1:]))
    dists = list(map(int, lines[1].split()[1:]))
    res = 1
    for i in range(len(times)):
        wins = 0
        for hold in range(times[i]):
            dist = (times[i] - hold) * hold
            if dist > dists[i]:
                wins += 1
        print(wins)
        res *= wins
    return res


# Solved in 0:13:24 (Answer: 40651271)
def partB(input):
    lines = input.split("\n")
    time = int(lines[0].split(" ", 1)[1].replace(" ", ""))
    record_dist = int(lines[1].split(" ", 1)[1].replace(" ", ""))
    wins = 0
    for hold in range(time):
        dist = (time - hold) * hold
        if dist > record_dist:
            wins += 1
    return wins


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=6)
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
