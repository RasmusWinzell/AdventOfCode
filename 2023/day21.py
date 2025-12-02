# Advent of Code 2023 Day 21, https://adventofcode.com/2023/day/21
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day21.py
# This is the original solution
from aocd.models import Puzzle


# Solved in 0:10:17 (Answer: 3578)
def partA(input, in_steps=64):
    lines = input.splitlines()
    sy, sx = [
        (i, line.index("S"))
        for i, line in enumerate(lines)
        if "S" in line
        if "S" in line
    ][0]

    even = []
    odd = []
    visited = set()
    max_steps = in_steps

    queue = [(0, sy, sx)]
    while queue:
        steps, y, x = queue.pop(0)
        if steps > max_steps:
            break
        if lines[y][x] == "#":
            continue
        if (y, x) in visited:
            continue
        visited.add((y, x))
        if lines[y][x] in ".S":
            if steps % 2 == 0:
                even.append((y, x))
            else:
                odd.append((y, x))
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= y + dy < len(lines) and 0 <= x + dx < len(lines[0]):
                queue.append((steps + 1, y + dy, x + dx))
    if max_steps % 2 == 0:
        return len(even)
    else:
        return len(odd)


def bfs(sy, sx, lines):
    res = []
    visited = set()

    queue = [(0, sy, sx)]
    while queue:
        steps, y, x = queue.pop(0)
        if lines[y][x] == "#":
            continue
        if (y, x) in visited:
            continue
        visited.add((y, x))
        res.append((steps, y, x))
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= y + dy < len(lines) and 0 <= x + dx < len(lines[0]):
                queue.append((steps + 1, y + dy, x + dx))
    return res


def repeat_input(input, radius):
    lines = input.splitlines()
    new_lines = []
    for line in lines:
        rline = line.replace("S", ".")
        new_lines.append(rline * radius + line + rline * radius)
    joint_lines = "\n".join(new_lines)
    rjoint_lines = joint_lines.replace("S", ".")
    return "\n".join([rjoint_lines] * radius + [joint_lines] + [rjoint_lines] * radius)


# Solved in 4:31:14 (Answer: 594115391548176)
def partB(input, in_steps=26501365):
    size = input.count("\n") + 1
    steps = [in_steps % size + size * i for i in range(3)]
    rinput = repeat_input(input, steps[-1] // size + 1)
    y = [partA(rinput, step) for step in steps]

    print(y)

    a = (y[2] + y[0] - 2 * y[1]) // 2
    b = y[1] - y[0] - a
    c = y[0]

    print(a, b, c)
    n = in_steps // size

    answer = a * n**2 + b * n + c

    print(answer)

    return answer


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=21)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         answer = partA(example.input_data)
    #         assert (
    #             str(answer) == example.answer_a
    #         ), f"Part A: Expected {example.answer_a}, got {answer}"

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
