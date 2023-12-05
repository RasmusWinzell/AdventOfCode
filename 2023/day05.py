# Advent of Code 2023 Day 5, https://adventofcode.com/2023/day/5
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day05.py
# This is the original solution
from aocd.models import Puzzle


# Solved in 0:33:56 (Answer: 551761867)
def partA(input):
    lines = input.split("\n")
    seeds = list(map(int, lines[0].split()[1:]))
    maps = []
    current_map = None
    map_type = None
    for line in lines[1:]:
        if not line.strip():
            continue
        if ":" in line:
            if map_type is not None:
                maps.append(current_map)
            current_map = []
            map_type = line.split()[0]
            print(map_type)
        else:
            ss, ds, l = map(int, line.split())
            current_map.append((ss, ds, l))
            print(ss, ds, l)
    maps.append(current_map)

    def traverse(value, i):
        if i >= len(maps):
            print(value)
            return value
        for ds, ss, l in maps[i]:
            if ss <= value and ss + l > value:
                res = traverse(value + ds - ss, i + 1)
                return res
        res = traverse(value, i + 1)
        return res

    lowest = float("inf")
    for seed in seeds:
        print("seed", seed)
        loc = traverse(seed, 0)
        lowest = min(lowest, loc)
    return lowest


# Solved in 1:17:00 (Answer: 57451709)
def partB(input):
    lines = input.split("\n")
    seeds = list(map(int, lines[0].split()[1:]))
    maps = []
    current_map = None
    map_type = None
    for line in lines[1:]:
        if not line.strip():
            continue
        if ":" in line:
            if map_type is not None:
                maps.append(current_map)
            current_map = []
            map_type = line.split()[0]
            print(map_type)
        else:
            ss, ds, l = map(int, line.split())
            current_map.append((ss, ds, l))
            print(ss, ds, l)
    maps.append(current_map)

    def traverse(start, length, i):
        if length <= 0:
            return float("inf")
        if i >= len(maps):
            return start
        lowest = float("inf")
        tested = []
        for ds, ss, l in maps[i]:
            print(start, length, ss, l)
            new_start = max(ss, start)
            new_end = min(ss + l, start + length)
            new_length = new_end - new_start
            if new_length > 0:
                print("yay", new_start, new_length)
                res = traverse(new_start + ds - ss, new_length, i + 1)
                lowest = min(lowest, res)
                tested.append((new_start, new_end))
        print(tested, "lowest", lowest)
        tested = sorted(tested)
        if not tested:
            print("not tested")
            res = traverse(start, length, i + 1)
            lowest = min(lowest, res)
        else:
            ss, _ = tested[0]
            res = traverse(start, min(length, ss - start), i + 1)
            lowest = min(lowest, res)
            print("lowest", lowest)
            for i in range(len(tested) - 1):
                ss1, se1 = tested[i]
                ss2, se2 = tested[i + 1]
                new_start = max(se1, start)
                new_end = min(ss2, start + length)
                new_length = new_end - new_start
                if new_length > 0:
                    res = traverse(new_start, new_length, i + 1)
                    lowest = min(lowest, res)
                    print("lowest", lowest)
            _, se = tested[-1]
            new_start = max(start, se)
            res = traverse(new_start, min(length, length - new_start + start), i + 1)
            lowest = min(lowest, res)
            print("lowest", lowest)
        print("   " * i, "lowest", i, lowest)
        return lowest

    lowest = float("inf")
    for seed_start, length in zip(seeds[0:-1:2], seeds[1::2]):
        print("seed", seed_start, length)
        loc = traverse(seed_start, length, 0)
        print(loc)
        lowest = min(lowest, loc)
    return lowest


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=5)
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
