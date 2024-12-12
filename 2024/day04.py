# Advent of Code 2024 Day 4, https://adventofcode.com/2024/day/4
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day04.py
# This is the original solution
import regex as re
from aocd.models import Puzzle


# Solved in 0:25:32
def partA(input):
    print(input)
    lines = input.split("\n")
    l = len(lines[0])
    text = input.replace("\n", "_")
    count = 0
    count += len(re.findall(rf"XMAS", text, overlapped=True))
    print(count)
    count += len(re.findall(rf"SAMX", text, overlapped=True))
    print(count)

    count += len(re.findall(rf"S{'.'*(l)}A{'.'*(l)}M{'.'*(l)}X", text, overlapped=True))
    print(count)
    count += len(re.findall(rf"X{'.'*(l)}M{'.'*(l)}A{'.'*(l)}S", text, overlapped=True))
    print(count)

    count += len(
        re.findall(rf"X{'.'*(l+1)}M{'.'*(l+1)}A{'.'*(l+1)}S", text, overlapped=True)
    )
    print(count)
    count += len(
        re.findall(rf"S{'.'*(l+1)}A{'.'*(l+1)}M{'.'*(l+1)}X", text, overlapped=True)
    )
    print(count)

    count += len(
        re.findall(
            rf"X{'.'*(l-2+1)}M{'.'*(l-2+1)}A{'.'*(l-2+1)}S", text, overlapped=True
        )
    )
    print(count)
    count += len(
        re.findall(
            rf"S{'.'*(l-2+1)}A{'.'*(l-2+1)}M{'.'*(l-2+1)}X", text, overlapped=True
        )
    )

    print(count)
    return count


# Solved in 0:44:50
def partB(input):
    print(input)
    lines = input.split("\n")
    l = len(lines[0])
    text = input.replace("\n", "_")
    count = 0
    count += len(
        re.findall(rf"M[^_]S{'.'*(l+1-2)}A{'.'*(l+1-2)}M[^_]S", text, overlapped=True)
    )
    count += len(
        re.findall(rf"M[^_]M{'.'*(l+1-2)}A{'.'*(l+1-2)}S[^_]S", text, overlapped=True)
    )
    count += len(
        re.findall(
            rf"M[^_]S{'.'*(l+1-2)}A{'.'*(l+1-2)}M[^_]S", text[::-1], overlapped=True
        )
    )
    count += len(
        re.findall(
            rf"M[^_]M{'.'*(l+1-2)}A{'.'*(l+1-2)}S[^_]S", text[::-1], overlapped=True
        )
    )
    print(count)
    return count


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=4)
    #     for example in puzzle.examples:
    #         if example.answer_a:
    #             id = """MMMSXXMASM
    # MSAMXMSMSA
    # AMXSXMAAMM
    # MSAMASMSMX
    # XMASAMXAMM
    # XXAMMXXAMA
    # SMSMSASXSS
    # SAXAMASAAA
    # MAMMMXMMMM
    # MXMXAXMASX"""
    #             answer = partA(id)
    #             assert (
    #                 str(answer) == example.answer_a
    #             ), f"Part A: Expected {example.answer_a}, got {answer}"

    #     if puzzle.answered_a:
    #         answer = partA(puzzle.input_data)
    #         assert (
    #             str(answer) == puzzle.answer_a
    #         ), f"Part A: Expected {puzzle.answer_a}, got {answer}"
    #     else:
    #         puzzle.answer_a = partA(puzzle.input_data)
    #         assert puzzle.answered_a, "Answer A not correct"

    #     for example in puzzle.examples:
    #         if example.answer_b:
    #             id = """MMMSXXMASM
    # MSAMXMSMSA
    # AMXSXMAAMM
    # MSAMASMSMX
    # XMASAMXAMM
    # XXAMMXXAMA
    # SMSMSASXSS
    # SAXAMASAAA
    # MAMMMXMMMM
    # MXMXAXMASX"""
    #             answer = partB(id)
    #             assert (
    #                 str(answer) == example.answer_b
    #             ), f"Part B: Expected {example.answer_b}, got {answer}"

    if puzzle.answered_b:
        answer = partB(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_b
        ), f"Part B: Expected {puzzle.answer_b}, got {answer}"
    else:
        puzzle.answer_b = partB(puzzle.input_data)
        assert puzzle.answered_b, "Answer B not correct"
