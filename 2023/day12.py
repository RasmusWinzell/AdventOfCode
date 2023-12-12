# Advent of Code 2023 Day 12, https://adventofcode.com/2023/day/12
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day12.py
# This is the original solution
from functools import cache

from aocd.models import Puzzle


@cache
def check_spring(line: str, count, goal, old=""):
    # print(old + line, count, goal)
    if len(line) == 0 and len(goal) == 0:
        return 1
    if len(line) == 0:
        return 0
    if len(goal) == 0:
        return "#" not in line
    res = 0
    if line[0] in "#?":
        if count + 1 <= goal[0]:
            res += check_spring(line[1:], count + 1, goal, old + "#")
    if line[0] in ".?":
        if count == 0:
            res += check_spring(line[1:], 0, goal, old + ".")
        elif count == goal[0]:
            res += check_spring(line[1:], 0, goal[1:], old + ".")
    return res


# Solved in 0:51:00 (Answer: 7771)
def partA(input):
    data = [line.split() for line in input.splitlines()]
    lines = [line[0] + "." for line in data]
    goals = [tuple(map(int, line[1].split(","))) for line in data]
    count = 0
    for line, goal in zip(lines, goals):
        res = check_spring(line, 0, goal)
        print(res)
        count += res
    return count


@cache
def check_springs(line: str, goals):
    # print(line, goals)
    if len(line) == 0 and len(goals) == 0:
        # print("found")
        return 1
    if len(line) == 0:
        return 0
    if len(goals) == 0:
        return "#" not in line
    res = 0
    if line[0] in ".?":
        res += check_springs(line[1:], goals)
    if line[0] in "#?":
        goal = goals[0]
        if len(line) > goal and "." not in line[:goal] and line[goal] in ".?":
            res += check_springs(line[goal + 1 :], goals[1:])
    return res


# Solved in 2:28:43 (Answer: 10861030975833)
def partB(input):
    data = [line.split() for line in input.splitlines()]
    lines = [line[0] for line in data]
    goals = [tuple(map(int, line[1].split(","))) for line in data]
    count = 0
    for line, goal in zip(lines, goals):
        line = "?".join([line] * 5)
        goal = goal * 5

        # parts = [part for part in line.split(".") if part]
        print(line, goal)
        res = check_springs(line + ".", goal)
        print(res)
        count += res
    return count


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=12)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         answer = partA(example.input_data)
    #         assert (
    #             str(answer) == example.answer_a
    #         ), f"Part A: Expected {example.answer_a}, got {answer}"

    print(
        partB(
            """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
        )
    )
    # print(partB(puzzle.input_data))

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
