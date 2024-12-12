# Advent of Code 2024 Day 6, https://adventofcode.com/2024/day/6
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day06.py
# This is the original solution
import math
from collections import defaultdict

from aocd.models import Puzzle


# Solved in 0:20:25
def partA(input):
    print(input)
    m = input.split("\n")
    yp, xp = [(i, line.index("^")) for i, line in enumerate(m) if "^" in line][0]
    m = [list(line) for line in m]
    dir = -90
    dx, dy = int(math.cos(math.radians(dir))), int(math.sin(math.radians(dir)))

    visited = set()
    visited.add((yp, xp))

    while True:
        if yp + dy < 0 or yp + dy >= len(m) or xp + dx < 0 or xp + dx >= len(m[0]):
            break
        if m[yp + dy][xp + dx] == "#":
            # rot 90
            dir = (dir + 90) % 360
            dx, dy = int(math.cos(math.radians(dir))), int(math.sin(math.radians(dir)))

        yp += dy
        xp += dx
        m[yp][xp] = "X"
        # print("\n".join(["".join(line) for line in m]))
        visited.add((yp, xp))

    print(len(visited))
    return len(visited)


t = 80


def find_loop(m, yp, xp, dir):
    print("find_loop")
    visited2 = set()
    dx, dy = int(math.cos(math.radians(dir))), int(math.sin(math.radians(dir)))
    # print(dy, dx)
    print(yp, xp)
    while True:

        if yp + dy < 0 or yp + dy >= len(m) or xp + dx < 0 or xp + dx >= len(m[0]):
            break
        while m[yp + dy][xp + dx] == "#":
            # rot 90
            dir = (dir + 90) % 360
            dx, dy = int(math.cos(math.radians(dir))), int(math.sin(math.radians(dir)))

        yp += dy
        xp += dx
        if (yp, xp, dir) in visited2:

            return True
        visited2.add((yp, xp, dir))
        # print(yp, xp)
    return False


def calc(grid, startpos):
    print("calc")
    r, c = startpos
    dr, dc = -1, 0
    seen = set()

    while 1:
        if len(seen) > t:
            break
        # oob?
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
            break

        # hit a wall?
        if grid[r][c] == "#":
            r -= dr
            c -= dc
            dr, dc = dc, -dr
            continue

        k = (r, c, dr, dc)
        if k in seen:

            return True

        seen.add(k)
        print(r, c)
        r += dr
        c += dc

    return False


# Solved in 1:58:28
def partB(input):
    m = input.split("\n")
    syp, sxp = [(i, line.index("^")) for i, line in enumerate(m) if "^" in line][0]
    m = [list(line) for line in m]
    dir = -90 % 360
    dx, dy = int(math.cos(math.radians(dir))), int(math.sin(math.radians(dir)))
    yp, xp = syp, sxp

    visited = set()
    visited.add((yp, xp))

    while True:
        if yp + dy < 0 or yp + dy >= len(m) or xp + dx < 0 or xp + dx >= len(m[0]):
            break
        if m[yp + dy][xp + dx] == "#":
            # rot 90
            dir = (dir + 90) % 360
            dx, dy = int(math.cos(math.radians(dir))), int(math.sin(math.radians(dir)))

        yp += dy
        xp += dx
        # m[yp][xp] = "X"
        # print("\n".join(["".join(line) for line in m]))
        visited.add((yp, xp))

    print(len(visited))

    loops = 0
    for yp2, xp2 in visited:
        if yp2 == syp and xp2 == sxp:
            continue
        old_val = m[yp2][xp2]
        m[yp2][xp2] = "#"
        dir = -90 % 360
        # v1 = set((a, b) for a, b, c in find_loop(m, syp, sxp, dir))
        # v2 = set((a, b) for a, b, c, d in calc(m, (syp, sxp)))

        # v2 = calc(m, (syp, sxp))
        # v1 = find_loop(m, syp, sxp, dir)

        # # print(sorted(list(v1)))
        # # print(sorted(list(v2)))
        # print(v1, v2)
        # assert v1 == v2

        if find_loop(m, syp, sxp, dir):
            # if calc(m, (syp, sxp)):
            loops += 1
            m[yp2][xp2] = "O"
        else:
            m[yp2][xp2] = old_val
    print("\n".join(["".join(line) for line in m]))
    print(loops)
    return loops


# Solved in 1:58:28
def partB2(input):

    m = input.split("\n")
    startpos = [(i, line.index("^")) for i, line in enumerate(m) if "^" in line][0]
    grid = [list(line) for line in m]

    r, c = startpos
    dr, dc = -1, 0
    seen = set()
    history = []

    while 1:
        seen.add((r, c))
        history.append((r, c, dr, dc))

        if not (0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0])):
            break

        if grid[r + dr][c + dc] == "#":
            dr, dc = dc, -dr

        r += dr
        c += dc

    ans1 = len(seen)
    print(ans1)

    prev = None
    ans2 = 0
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if (r, c) not in seen or (r, c) == startpos:
                continue

            if prev is not None:
                grid[prev[0]][prev[1]] = "."

            grid[r][c] = "#"
            prev = r, c
            ans2 += calc(grid, startpos)
            # ans2 += find_loop(grid, startpos[0], startpos[1], -90)
    print(ans2)


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=6)
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

    # for example in puzzle.examples:
    #     if example.answer_b:
    #         answer = partB(example.input_data)
    #         assert (
    #             str(answer) == example.answer_b
    #         ), f"Part B: Expected {example.answer_b}, got {answer}"
    # exit()
    if False and puzzle.answered_b:
        answer = partB(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_b
        ), f"Part B: Expected {puzzle.answer_b}, got {answer}"
    else:
        partB(puzzle.input_data)
        # puzzle.answer_b = partB(puzzle.input_data)
        assert puzzle.answered_b, "Answer B not correct"
