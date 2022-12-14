# Advent of Code 2022 Day 12
# https://adventofcode.com/2022/day/12
# https://github.com/RasmusWinzell/AdventOfCode

from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=12)
data = puzzle.input_data

from queue import Queue

START, END = "S", "E"
lines = data.split("\n")

# Calculate hights from 0 - 25 (a - z).
heights = [[ord(h.replace(START, "a").replace(END, "z")) - ord("a") for h in line] for line in lines]

# Find indexes for Start (S) and End (E).
sx, sy = [(line.index(START), i) for i, line in enumerate(lines) if line.count(START) > 0][0]
ex, ey = [(line.index(END), i) for i, line in enumerate(lines) if line.count(END) > 0][0]

visited = set()
best = None
Q = Queue()
Q.put((ex, ey, 0))
# Run BFS from End (E) to Start (S). (Finds shortest path to ground on the way).
while not Q.empty():
    x, y, d = Q.get()
    if (x, y) not in visited:
        visited.add((x, y))
        if heights[y][x] == 0 and not best: # First occurance of ground (a), save for part 2.
            best = d
        if (x, y) == (sx, sy): # Start (S) is found, stop searching.
            break
        for x1, y1 in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= x1 < len(heights[0]) and 0 <= y1 < len(heights) and heights[y1][x1] - heights[y][x] >= -1:
                Q.put((x1, y1, d+1))

print("Part 1:", d)
print("Part 2:", best)