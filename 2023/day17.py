# Advent of Code 2023 Day 17, https://adventofcode.com/2023/day/17
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day17.py
# This is the original solution
from queue import PriorityQueue

from aocd.models import Puzzle


# Solved in 0:53:26 (Answer: 1155)
def partA(input):
    lines = input.splitlines()

    queue = PriorityQueue()
    queue.put((0, 0, 0, 0, 0, 0, ()))
    visited = {}
    while not queue.empty():
        heat, x, y, count, dxs, dys, path = queue.get()
        if y == len(lines) - 1 and x == len(lines[0]) - 1:
            print(heat, path)
            p = set((x, y) for x, y, _ in path)
            for i, line in enumerate(lines):
                for j, c in enumerate(line):
                    if (j, i) in p:
                        print("#", end="")
                    else:
                        print(c, end="")
                print()
            return heat
        id = (x, y, count, dxs, dys)
        if id in visited and heat >= visited[id]:
            continue
        visited[id] = heat
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if dx == -dxs and dy == -dys:
                continue
            if 0 <= x + dx < len(lines[0]) and 0 <= y + dy < len(lines):
                if dx == dxs and dy == dys:
                    if count >= 3:
                        continue
                    queue.put(
                        (
                            heat + int(lines[y + dy][x + dx]),
                            x + dx,
                            y + dy,
                            count + 1,
                            dx,
                            dy,
                            path + ((x, y, heat),),
                        )
                    )
                else:
                    # print(dx, dy)
                    queue.put(
                        (
                            heat + int(lines[y + dy][x + dx]),
                            x + dx,
                            y + dy,
                            1,
                            dx,
                            dy,
                            path + ((x, y, heat),),
                        )
                    )


# Solved in 1:01:45 (Answer: 1283)
def partB(input):
    lines = input.splitlines()

    queue = PriorityQueue()
    queue.put((0, 0, 0, 0, 0, 0, ()))
    visited = {}
    while not queue.empty():
        heat, x, y, count, dxs, dys, path = queue.get()
        if y == len(lines) - 1 and x == len(lines[0]) - 1 and count >= 8:
            print(heat, path)
            p = set((x, y) for x, y, _ in path)
            for i, line in enumerate(lines):
                for j, c in enumerate(line):
                    if (j, i) in p:
                        print("#", end="")
                    else:
                        print(c, end="")
                print()
            print(heat)
            return heat
        id = (x, y, count, dxs, dys)
        if id in visited and heat >= visited[id]:
            continue
        visited[id] = heat
        if count != 0 and count < 4:
            if 0 <= x + dxs < len(lines[0]) and 0 <= y + dys < len(lines):
                queue.put(
                    (
                        heat + int(lines[y + dys][x + dxs]),
                        x + dxs,
                        y + dys,
                        count + 1,
                        dxs,
                        dys,
                        path + ((x, y, heat),),
                    )
                )
            continue
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if dx == -dxs and dy == -dys:
                continue
            if 0 <= x + dx < len(lines[0]) and 0 <= y + dy < len(lines):
                if dx == dxs and dy == dys:
                    if count >= 10:
                        continue
                    queue.put(
                        (
                            heat + int(lines[y + dy][x + dx]),
                            x + dx,
                            y + dy,
                            count + 1,
                            dx,
                            dy,
                            path + ((x, y, heat),),
                        )
                    )
                else:
                    # print(dx, dy)
                    queue.put(
                        (
                            heat + int(lines[y + dy][x + dx]),
                            x + dx,
                            y + dy,
                            1,
                            dx,
                            dy,
                            path + ((x, y, heat),),
                        )
                    )


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=17)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         answer = partA(example.input_data)
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
