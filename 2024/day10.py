# Advent of Code 2024 Day 10, https://adventofcode.com/2024/day/10
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day10.py
# This is the original solution
from collections import deque

from aocd.models import Puzzle


def find_score(m, x, y):
    queue = deque([(x, y, 0)])
    visited = set()
    score = 0
    while queue:
        x, y, height = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if m[y][x] == "9":
            score += 1
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(m[0])
                and 0 <= ny < len(m)
                and m[ny][nx] != "."
                and int(m[ny][nx]) == int(height) + 1
            ):
                queue.append((nx, ny, m[ny][nx]))
    return score


def find_rating(m, x, y, visited=None):

    if visited is None:
        visited = set()

    if m[y][x] == "9":
        print("Visited:")
        for l, line in enumerate(m):
            for c, ch in enumerate(line):
                if (c, l) not in visited:
                    print(ch, end="")
                else:
                    print("#", end="")
            print("")
        print(visited)
        print("")
        return 1

    visited.add((x, y))

    rating = 0
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if (
            0 <= nx < len(m[0])
            and 0 <= ny < len(m)
            and m[ny][nx] != "."
            and int(m[ny][nx]) == int(m[y][x]) + 1
            and (nx, ny) not in visited
        ):
            rating += find_rating(m, nx, ny, visited.copy())
    return rating


# Solved in 0:17:02
def partA(input):
    m = [list(line) for line in input.splitlines()]
    # print(m)

    scoresum = 0
    for y, line in enumerate(m):
        for x, c in enumerate(line):
            if c == "0":
                score = find_score(m, x, y)
                print(score)
                scoresum += score

    print(scoresum)
    return scoresum


# Solved in 0:43:33
def partB(input):
    m = [list(line) for line in input.splitlines()]
    # print(m)

    ratingsum = 0
    for y, line in enumerate(m):
        for x, c in enumerate(line):
            if c == "0":
                rating = find_rating(m, x, y)
                print(rating)
                ratingsum += rating

    print(ratingsum)
    return ratingsum


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=10)
    #     for example in puzzle.examples:
    #         if example.answer_a:
    #             inp = """.....0.
    # ..4321.
    # ..5..2.
    # ..6543.
    # ..7..4.
    # ..8765.
    # ..9...."""
    #             answer = partA(inp)
    #             assert (
    #                 str(answer) == example.answer_a
    #             ), f"Part A: Expected {example.answer_a}, got {answer}"

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
            inp = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
            answer = partB(inp)
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
