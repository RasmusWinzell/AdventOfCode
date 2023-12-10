# Advent of Code 2023 Day 10, https://adventofcode.com/2023/day/10
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day10.py
# This is the cleaned solution
from aocd.models import Puzzle

dirs = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
    "S": [(1, 0), (0, 1), (-1, 0), (0, -1)],
}


def parse(input: str):
    grid = [list(line) for line in input.splitlines()]
    start = [(y, row.index("S")) for y, row in enumerate(grid) if row.count("S")][0]
    return grid, start


def follow_pipe(pipe, y, x, dy, dx):
    """Returns the next coordinate and direction of the pipe."""
    if (-dy, -dx) not in dirs[pipe]:
        return None, None
    new_dy, new_dx = dirs[pipe][dirs[pipe].index((-dy, -dx)) - 1]
    return (y + new_dy, x + new_dx), (new_dy, new_dx)


def pipe_at(y, x, grid):
    return grid[y][x]


def mark_pipes(grid, y, x, dy=0, dx=0):
    """Mark the path of the pipe as False."""
    grid[y * 2 + 1][x * 2 + 1] = False
    grid[y * 2 + 1 - dy][x * 2 + 1 - dx] = False


def mark_loop(grid, start_coord):
    """
    Make a scaled up grid so there is always empty space between pipes.
    The path of the pipe loop is marked as False, rest is True.
    """
    double_grid = [[True] * (len(grid[0]) * 2 + 1) for _ in range(len(grid) * 2 + 1)]
    mark_pipes(double_grid, *start_coord)
    for start_dir in dirs["S"]:
        coord, dir = follow_pipe(pipe_at(*start_coord, grid), *start_coord, *start_dir)
        while coord and (pipe := pipe_at(*coord, grid)) not in ".S":
            mark_pipes(double_grid, *coord, *dir)
            coord, dir = follow_pipe(pipe, *coord, *dir)
    return double_grid


def bfs_mark(double_grid):
    """Run a BFS to mark all areas outside the loop as False."""
    queue = [(0, 0)]
    while queue:
        y, x = queue.pop(0)
        if not double_grid[y][x]:
            continue
        double_grid[y][x] = False
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= y + dy < len(double_grid) and 0 <= x + dx < len(double_grid[0]):
                queue.append((y + dy, x + dx))


def count_enclosed(double_grid):
    """Looks at every other cell in the grid and counts number True cells."""
    return sum(sum(row[1::2]) for row in double_grid[1::2])


# Solved in 0:37:16 (Answer: 6842)
def partA(input: str):
    grid, start_coord = parse(input)
    for start_dir in dirs["S"]:
        coord, dir, steps = start_coord, start_dir, 0
        while coord:
            steps += 1
            pipe = pipe_at(*coord, grid)
            coord, dir = follow_pipe(pipe, *coord, *dir)
            if coord == start_coord:
                return steps // 2


# Solved in 1:40:59 (Answer: 393)
def partB(input):
    grid, start_coord = parse(input)
    double_grid = mark_loop(grid, start_coord)
    bfs_mark(double_grid)
    return count_enclosed(double_grid)


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=10)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")
    