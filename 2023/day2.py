# Advent of Code 2023 Day 2, https://adventofcode.com/2023/day/2
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day2.py
# This is the original solution
from collections import defaultdict

from aocd.models import Puzzle

max_cubes = {"red": 12, "green": 13, "blue": 14}


# Solved in 0:14:05 (Answer: 2006)
def partA(input: str):
    id_sum = 0
    for i, line in enumerate(input.strip().split("\n")):
        print("Game", i + 1)
        cube_count = defaultdict(int)
        cube_sets = line.split(": ", 1)[1].split("; ")
        for cube_set in cube_sets:
            cubes = cube_set.split(", ")
            print(cubes)
            for cube in cubes:
                count, color = cube.split()
                cube_count[color] = max(cube_count[color], int(count))

        valid = True
        for k in max_cubes.keys():
            if cube_count[k] > max_cubes[k]:
                valid = False
                break

        if valid:
            id_sum += i + 1
            print("Valid", cube_count)
    return id_sum


# Solved in 0:18:29 (Answer: 84911)
def partB(input):
    power_sum = 0
    for i, line in enumerate(input.strip().split("\n")):
        print("Game", i + 1)
        cube_count = defaultdict(int)
        cube_sets = line.split(": ", 1)[1].split("; ")
        for cube_set in cube_sets:
            cubes = cube_set.split(", ")
            print(cubes)
            for cube in cubes:
                count, color = cube.split()
                cube_count[color] = max(cube_count[color], int(count))

        power = 1
        for k in max_cubes.keys():
            power *= cube_count[k]
        power_sum += power
    return power_sum


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=2)

    example = puzzle.examples[0]
    puzzle_input = example.input_data

    puzzle_input = puzzle.input_data

    # puzzle_input = """input"""
    print(puzzle_input)
    res = partB(puzzle_input)
    print(res)

    # puzzle_answer = example.answer_a
    # puzzle_answer = example.answer_b
    # puzzle_answer = answer

    # assert str(res) == str(
    #     puzzle_answer
    # ), f"Part A: Expected {puzzle_answer}, got {res}"

    # uzzle.answer_a = res
    puzzle.answer_b = res
