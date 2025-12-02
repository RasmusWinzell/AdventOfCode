# Advent of Code 2024 Day 15, https://adventofcode.com/2024/day/15
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day15.py
# This is the cleaned solution
from collections import deque

from aocd.models import Puzzle

MOVEMAP = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


class Box:

    def __init__(self, x, y, size=1):
        self.x, self.y, self.size = x, y, size

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def coords(self):
        for i in range(self.size):
            yield self.x + i, self.y


def print_grid(walls, boxes, rx, ry, w, h):
    grid = [["." for _ in range(w)] for _ in range(h)]
    for x, y in walls:
        grid[y][x] = "#"
    for x, y in boxes:
        grid[y][x] = "O"
    grid[ry][rx] = "@"
    print("\n".join("".join(row) for row in grid))


def parse(input, box_size=1):
    grid, moves = input.split("\n\n")
    w, h = grid.index("\n") * box_size, grid.count("\n") + 1
    walls, boxes = set(), set()
    for y, line in enumerate(grid.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                for i in range(box_size):
                    walls.add((x * box_size + i, y))
            elif c == "O":
                boxes.add(Box(x * box_size, y, box_size))
            elif c == "@":
                robot = (x * box_size, y)
    moves = moves.replace("\n", "")
    return walls, boxes, robot, w, h, moves


def solve(input, box_size=1):
    walls, boxes, (x, y), w, h, moves = parse(input, box_size)
    box_coords = {coord: box for box in boxes for coord in box.coords()}

    for move in moves:
        dx, dy = MOVEMAP[move]
        boxes_to_move = set()
        q = deque([(x + dx, y + dy)])
        while q:
            nx, ny = q.popleft()
            if (nx, ny) in walls:
                break
            if (box := box_coords.get((nx, ny))) and box not in boxes_to_move:
                boxes_to_move.add(box)
                q.extend((bx + dx, by + dy) for bx, by in box.coords())
        else:
            x, y = x + dx, y + dy
            for box in boxes_to_move:
                box.move(dx, dy)
            box_coords = {coord: box for box in boxes for coord in box.coords()}

    print_grid(walls, box_coords, x, y, w, h)
    return sum(box.x + box.y * 100 for box in boxes)


# Solved in 0:28:02
def partA(input):
    return solve(input)


# Solved in 1:53:16
def partB(input):
    return solve(input, 2)


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=15)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
