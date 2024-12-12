# Advent of Code 2024 Day 2, https://adventofcode.com/2024/day/2
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day02.py
# This is the original solution
from aocd.models import Puzzle


# Solved in 0:22:06
def partA(input):
    reports = [list(map(int, line.split())) for line in input.split("\n")]
    safe = 0
    for report in reports:
        ok = True
        sign = None
        for i in range(len(report) - 1):
            # print(report[i], report[i + 1])
            if 1 <= abs(report[i] - report[i + 1]) <= 3 and (
                sign is None or (sign == (report[i] < report[i + 1]))
            ):
                sign = report[i] < report[i + 1]
            else:
                ok = False
        if ok:
            safe += 1
            print("ok", report)
    print(safe)
    return safe

    # print(reports)


# Solved in 0:44:37
def partB(input):
    reports = [list(map(int, line.split())) for line in input.split("\n")]
    safe = 0
    for report in reports:
        for sign in [True, False]:
            for skip in range(len(report)):
                bad = 0
                rep = report[:skip] + report[skip + 1 :]
                for i in range(len(rep) - 1):
                    print(rep[i], rep[i + 1])
                    if 1 <= abs(rep[i] - rep[i + 1]) <= 3 and (
                        sign == (rep[i] < rep[i + 1])
                    ):
                        pass
                    else:
                        bad += 1
                if bad == 0:
                    safe += 1
                    print("ok", rep, bad, sign)
                    break
    print(safe)
    return safe


if __name__ == "__main__":

    # partB("0 5 6 7")

    # exit()
    puzzle = Puzzle(year=2024, day=2)
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
