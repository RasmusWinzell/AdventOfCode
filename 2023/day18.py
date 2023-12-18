# Advent of Code 2023 Day 18, https://adventofcode.com/2023/day/18
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day18.py
# This is the original solution
from aocd.models import Puzzle

dirs = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


# Solved in 0:28:05 (Answer: 52035)
def partA(input):
    lines = input.splitlines()
    instructions = [line.split() for line in lines]

    xmin, xmax = 0, 0
    ymin, ymax = 0, 0
    visited = set()
    x, y = 0, 0
    for i, instruction in enumerate(instructions):
        dir, dist, _ = instruction
        dx, dy = dirs[dir]
        for _ in range(int(dist)):
            x += dx
            y += dy
            visited.add((x, y))
            xmin = min(xmin, x)
            xmax = max(xmax, x)
            ymin = min(ymin, y)
            ymax = max(ymax, y)

    for j in range(ymin, ymax + 1):
        for i in range(xmin, xmax + 1):
            if (i, j) in visited:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

    queue = [(xmin - 1, ymin - 1)]
    bfs_visited = set()
    while queue:
        x, y = queue.pop(0)
        if (x, y) in visited:
            continue
        if xmin - 1 <= x <= xmax + 1 and ymin - 1 <= y <= ymax + 1:
            if (x, y) in bfs_visited:
                continue
            bfs_visited.add((x, y))
            for dir in dirs.values():
                queue.append((x + dir[0], y + dir[1]))

    area = (xmax - xmin + 3) * (ymax - ymin + 3)
    count = area - len(bfs_visited)
    return count


hex_dirs = ["R", "D", "L", "U"]


# Solved in 1:11:03 (Answer: 60612092439765)
def partB(input):
    lines = input.splitlines()
    instructions = [line.split() for line in lines]

    coordinates = []
    edges = 0
    x, y = 0, 0
    coordinates.append((x, y))
    for i, instruction in enumerate(instructions):
        dir, dist, _ = instruction
        dist = int(dist)
        _, _, hex_instr = instruction
        dist = int(hex_instr[2 : 2 + 5], 16)
        dir = hex_dirs[int(hex_instr[-2])]

        print(dir, dist)
        edges += dist
        dx, dy = dirs[dir]
        x += dx * dist
        y += dy * dist
        coordinates.append((x, y))
    print(coordinates)

    # trapezoid area formula
    area = 0
    for i in range(len(coordinates)):
        j = (i + 1) % len(coordinates)
        area += (coordinates[i][0] + coordinates[j][0]) * (
            coordinates[i][1] - coordinates[j][1]
        )
    area = abs(area) / 2
    extra = 3 + (edges - 4) / 2

    return int(area + extra)


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=18)
    # partA(puzzle.input_data)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         answer = partB(example.input_data)
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
