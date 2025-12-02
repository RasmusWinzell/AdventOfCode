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
    counts = []
    for line, goal in zip(lines, goals):
        res = check_spring(line, 0, goal)
        # print(res)
        count += res
        counts.append(res)
    return count, counts


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


from itertools import product, zip_longest


def goal_solotions(goal, length):
    min_length = sum(goal) + len(goal) - 1
    diff = length - min_length
    # print(diff)
    msplit = (0,) + (1,) * (len(goal) - 1) + (0,)
    if diff > 0:
        bin_assignments = list(product(range(diff + 1), repeat=len(goal) + 1))
        # Filter out combinations where the sum of bin assignments is equal to N
        # print(bin_assignments)
        valid_splits = [split for split in bin_assignments if sum(split) == diff]
    else:
        valid_splits = [()]
    # print(valid_splits)
    solutions = []
    test = []
    for split in sorted(valid_splits):
        full_split = [s1 + s2 for s1, s2 in zip_longest(msplit, split, fillvalue=0)]
        res = ""
        # print(split, full_split, goal)
        for a, b in zip_longest(full_split, goal, fillvalue=0):
            res += "0" * a + "1" * b
        # print(res)
        test.append((int(res, 2), full_split))
        solutions.append(int(res, 2))
    t10 = -1
    t20 = -1
    for t1, t2 in sorted(test):
        if t1 == t10:
            # print(t1, t2, t20)
            pass
        t10 = t1
        t20 = t2
    return sorted(test)


def partC(input: str):
    _, costs = partA(input)
    data = [line.split() for line in input.splitlines()]
    lines = [line[0] for line in data]
    goals = [list(map(int, line[1].split(","))) for line in data]
    res = 0
    # lines = lines[2:3]
    # goals = goals[2:3]
    for i, (line, goal, c) in enumerate(zip(lines, goals, costs)):
        print(i)
        # if i != 992:
        #     continue
        line = "?".join([line] * 5)
        goal = goal * 5

        damaged = int("".join("1" if c == "#" else "0" for c in line), 2)
        mask = int("".join("0" if c == "?" else "1" for c in line), 2)
        # print(line, goal)
        # print(bin(damaged), bin(mask))
        solutions = goal_solotions(goal, len(line))
        count = 0
        for solution, split in solutions:
            diff = solution ^ damaged
            masked_diff = diff & mask
            # print(bin(solution)[2:])
            if masked_diff == 0:
                count += 1
                # print(bin(solution), split)
        if count != c:
            print("Not correct", i, line, goal, count, c)
        res += count
        # print(count)

    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=12)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         answer = partA(example.input_data)
    #         assert (
    #             str(answer) == example.answer_a
    #         ), f"Part A: Expected {example.answer_a}, got {answer}"

    #     print(
    #         partC(
    #             """???.### 1,1,3
    # .??..??...?##. 1,1,3
    # ?#?#?#?#?#?#?#? 1,3,1,6
    # ????.#...#... 4,1,1
    # ????.######..#####. 1,6,5
    # ?###???????? 3,2,1"""
    #         )
    #     )
    import time

    t0 = time.perf_counter()
    print(partB(puzzle.input_data))
    t1 = time.perf_counter()
    print(t1 - t0)
    exit()
    if puzzle.answered_a:
        answer = partC(puzzle.input_data)
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
