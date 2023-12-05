# Advent of Code 2023 Day 5, https://adventofcode.com/2023/day/5
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day05.py
# This is the cleaned solution
from aocd.models import Puzzle

inf = float("inf")


def parse(input: str):
    seeds = list(map(int, input.split("\n", 1)[0].split()[1:]))
    map_lines = [sec.split("\n")[1:] for sec in input.split("\n\n")[1:]]
    maps = [[tuple(map(int, line.split())) for line in sec] for sec in map_lines]
    return seeds, maps


# Solved in 0:33:56 (Answer: 551761867)
def partA(input):
    seeds, maps = parse(input)
    best_location = inf
    for seed in seeds:
        value = seed
        for range in maps:  # Loop through each map (ie seed-to-soil)
            for dst, src, length in range:  # Loop through each range in map
                if src <= value < src + length:
                    value += dst - src
                    break
        best_location = min(best_location, value)
    return best_location


# Solved in 1:17:00 (Answer: 57451709)
def partB(input):
    seeds, maps = parse(input)

    prev_ranges = zip(seeds[:-1:2], seeds[1::2])  # Set seeds as initial ranges
    for range_map in maps:
        range_dict = {src + l: 0 for _, src, l in range_map}  # Add ends
        range_dict.update({src: dst - src for dst, src, _ in range_map})  # Add starts
        range_list = [(-inf, 0)] + sorted(range_dict.items()) + [(inf, 0)]

        new_ranges = []
        # Loop through ranges from previous iteration
        for prev_start, prev_length in prev_ranges:
            # Loop through all ranges in the map (ie seed-to-soil)
            for (start, diff), (end, _) in zip(range_list[:-1], range_list[1:]):
                new_start = max(prev_start, start)
                new_end = min(prev_start + prev_length, end)
                if (new_length := new_end - new_start) > 0:
                    new_ranges.append((new_start + diff, new_length))
        prev_ranges = new_ranges

    return min(start for start, _ in prev_ranges)


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=5)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")