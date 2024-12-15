# Advent of Code 2024 Day 15, https://adventofcode.com/2024/day/15
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day15.py
# This is the original solution
from aocd.models import Puzzle

MOVEMAP = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


def print_grid(walls, boxes, robot, w, h):
    grid = [["." for _ in range(w)] for _ in range(h)]
    for x, y in walls:
        grid[y][x] = "#"
    for x, y in boxes:
        grid[y][x] = "O"
    x, y = robot
    grid[y][x] = "@"
    print("\n".join("".join(row) for row in grid))


# Solved in 0:28:02
def partA(input):
    walls = set()
    boxes = set()
    for y, line in enumerate(input.splitlines()):
        if not line:
            h = y
            break
        w = len(line)
        for x, c in enumerate(line):
            if c == "#":
                walls.add((x, y))
            elif c == "O":
                boxes.add((x, y))
            elif c == "@":
                robot = (x, y)

    moves = "".join(input.splitlines()[y + 1 :])
    print_grid(walls, boxes, robot, w, h)

    x, y = robot

    for move in moves:
        dx, dy = MOVEMAP[move]
        can_move = True
        push_boxes = []
        i = 0
        while True:
            i += 1
            nx, ny = x + i * dx, y + i * dy
            if (nx, ny) in walls:
                can_move = False
                break
            elif (nx, ny) in boxes:
                push_boxes.append((nx, ny))
            else:
                for box in push_boxes[::-1]:
                    bx, by = box
                    boxes.remove(box)
                    boxes.add((bx + dx, by + dy))
                break
        if can_move:
            x, y = x + dx, y + dy
        print_grid(walls, boxes, (x, y), w, h)

    res = sum(x + y * 100 for x, y in boxes)
    print(res)
    return res


def rec_push(boxes, walls, pos, dx, dy, push_boxes):
    if pos in walls:
        return False
    if pos in boxes:
        bx, by = pos
        bx2, by2 = boxes[pos]
        can_push = True
        if bx + dx != bx2 or by + dy != by2:
            can_push = can_push and rec_push(
                boxes, walls, (bx + dx, by + dy), dx, dy, push_boxes
            )
        if bx2 + dx != bx or by2 + dy != by:
            can_push = can_push and rec_push(
                boxes, walls, (bx2 + dx, by2 + dy), dx, dy, push_boxes
            )
        if can_push:
            push_boxes.append((bx2, by2))
            push_boxes.append((bx, by))
        return can_push
    return True


# Solved in 1:53:16
def partB(input):
    walls = set()
    boxes = {}
    for y, line in enumerate(input.splitlines()):
        if not line:
            h = y
            break
        w = len(line) * 2
        for x, c in enumerate(line):
            if c == "#":
                walls.add((x * 2, y))
                walls.add((x * 2 + 1, y))
            elif c == "O":
                boxes[(x * 2, y)] = (x * 2 + 1, y)
                boxes[(x * 2 + 1, y)] = (x * 2, y)
            elif c == "@":
                robot = (x * 2, y)

    moves = "".join(input.splitlines()[y + 1 :])
    print(w, h)
    print_grid(walls, boxes, robot, w, h)

    x, y = robot

    for move in moves:
        print(move)
        dx, dy = MOVEMAP[move]
        can_move = True
        push_boxes = []
        can_move = rec_push(boxes, walls, (x + dx, y + dy), dx, dy, push_boxes)
        if can_move:
            l0 = len(boxes)
            moved = set()
            for bx, by in push_boxes:
                if (bx, by) in moved:
                    continue
                moved.add((bx, by))
                bx2, by2 = boxes[(bx, by)]
                boxes[(bx + dx, by + dy)] = (bx2 + dx, by2 + dy)
                del boxes[(bx, by)]
            x, y = x + dx, y + dy
            if l0 != len(boxes):
                print_grid(walls, boxes, (x, y), w, h)
                print("ERROR")
                break
        print_grid(walls, boxes, (x, y), w, h)

    res = 0
    while boxes:
        box, box2 = boxes.popitem()
        del boxes[box2]
        x, y = min(box, box2)
        res += x + y * 100
    print(res)
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=15)
    #     for example in puzzle.examples:
    #         if example.answer_a:
    #             inp = """########
    # #..O.O.#
    # ##@.O..#
    # #...O..#
    # #.#.O..#
    # #...O..#
    # #......#
    # ########

    # <^^>>>vv<v>>v<<"""
    #             answer = partA(inp)
    #             assert (
    #                 str(answer) == example.answer_a
    #             ), f"Part A: Expected {example.answer_a}, got {answer}"

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
