# Advent of Code "#year" Day "#day", "#puzzle_link"
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/"#year"/"#filename"
# "#version"
from aocd.models import Puzzle


def partA(input):
    pass


def partB(input):
    pass


if __name__ == "__main__":
    puzzle = Puzzle(year="#year", day="#day")

    example = puzzle.examples[0]
    puzzle_input = example.input_data

    # puzzle_input = puzzle.input_data

    # puzzle_input = """input"""

    res = partA(puzzle_input)

    puzzle_answer = example.answer_a
    # puzzle_answer = example.answer_b
    # puzzle_answer = answer

    assert str(res) == str(
        puzzle_answer
    ), f"Part A: Expected {puzzle_answer}, got {res}"

    # puzzle.answer_a = resA
    # puzzle.answer_b = res
