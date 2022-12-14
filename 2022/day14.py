# Advent of Code 2022 Day 14
# https://adventofcode.com/2022/day/14
# https://github.com/RasmusWinzell/AdventOfCode

from aocd import data

lines = [[list(map(int, seg.split(","))) for seg in line.split(" -> ")] for line in data.split("\n")]
blocked, sands = set(), set()

# Block out all lines.
for line in lines:
    for i in range(1, len(line)):
        x1, y1, x2, y2 = *line[i-1], *line[i]
        yr = list(range(min(y1, y2), max(y1, y2)+1))
        xr = list(range(min(x1, x2), max(x1, x2)+1))
        for j in range(max(len(yr), len(xr))):
            blocked.add((xr[j%len(xr)], yr[j%len(yr)]))

# Recursively put sand.
def put_sand(x, y):
    if (x,y) in blocked or (x,y) in sands:
        return 0
    if y == y_max:
        return limit_ret
    for xn, yn in [(x, y+1), (x-1, y+1), (x+1, y+1)]:
        put = put_sand(xn, yn)
        if put != 0:
            return put
    sands.add((x, y))
    return 1

spawn = (500, 0)
y_max = max([block[1] for block in blocked])
limit_ret = -1

print("Part 1:", sum(1 for _ in iter(lambda: put_sand(*spawn)==1, False)))

# Change y_max and set it as floor.
y_max, limit_ret, sands = y_max + 2, 0, set()
print("Part 2", sum(1 for _ in iter(lambda: put_sand(*spawn)==1, False)))
