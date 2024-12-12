# Advent of Code 2024 Day 11, https://adventofcode.com/2024/day/11
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day11.py
# This is the original solution
from functools import cache

from aocd.models import Puzzle


# Solved in 0:09:18
def partA(input):
    stones = list(map(int, input.split()))
    print(stones)
    for blink in range(1, 25 + 1):
        print(f"blink {blink}")
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stones.append(int(str(stone)[: len(str(stone)) // 2]))
                new_stones.append(int(str(stone)[len(str(stone)) // 2 :]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
        print(stones)
    print(len(stones))
    return len(stones)


@cache
def get_num_stones(stone, blinks):
    # print(stone, blinks)
    if blinks == 0:
        return 1
    if stone == 0:
        return get_num_stones(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        return get_num_stones(
            int(str(stone)[: len(str(stone)) // 2]), blinks - 1
        ) + get_num_stones(int(str(stone)[len(str(stone)) // 2 :]), blinks - 1)
    else:
        return get_num_stones(stone * 2024, blinks - 1)


# Solved in 0:23:07
def partB(input):
    # input = "125 17"
    stones = list(map(int, input.split()))
    print(stones)
    stone_sum = 0
    for stone in stones:
        stone_sum += get_num_stones(stone, 75)
    print(stone_sum)
    return stone_sum


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=11)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         inp = "125 17"
    #         answer = partA(inp)
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
