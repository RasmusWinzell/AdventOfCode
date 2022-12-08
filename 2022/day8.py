# Advent of Code 2022 Day 8
# https://adventofcode.com/2022/day/8
# https://github.com/RasmusWinzell/AdventOfCode

from aocd import data

lines = [list(map(int, line)) for line in data.split("\n")]
size = len(lines)

# Calculate how far one can see from the tree at (x, y) in the dir direction.
def dist(x, y, dir):
    h = lines[y][x]
    for d in range(size):
        x, y = x+dir[0], y+dir[1]
        if 0 <= x < size and 0 <= y < size:
            if lines[y][x] >= h:
                return d+1, False
        else:
            return d, True

# Init values.
visible = [[False]*size for _ in range(size)]
scores = [[1]*size for _ in range(size)]

# Loop through all trees.
for y in range(size):
    for x in range(size):
        # Check distances in all directions.
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            d, sees_edge = dist(x, y, dir)
            if sees_edge:
                visible[y][x] = True
            scores[y][x] *= d

print("Part 1:", sum(map(sum, visible)))
print("Part 2:", max(map(max, scores)))
            