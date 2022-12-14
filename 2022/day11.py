# Advent of Code 2022 Day 11
# https://adventofcode.com/2022/day/11
# https://github.com/RasmusWinzell/AdventOfCode

from aocd import get_data

import operator, re, math, copy
op = {"+": operator.add, "*": operator.mul}

data = get_data(day=11, year=2022)
# Find all numbers and operators in each line.
linevals = [re.findall("[0-9]+|[+*]", line) for line in data.split("\n")]

items = [list(map(int, line)) for line in linevals[1::7]]
# Make lambda functions for the operations.
ops = [lambda old, o=vals[0], v=vals[-1]: op[o](old, int(v) if v!=o else old) for vals in linevals[2::7]]
# Extract values from single-value lines.
div, go_true, go_false = [[int(vals[0]) for vals in linevals[i::7]] for i in (3,4,5)]

def monkey_business(items, rounds, manage):
    inspected = [0] * len(items)
    for _ in range(1, rounds+1):
        for monkey in range(len(items)):
            for worry in items[monkey]:
                worry = manage(ops[monkey](worry)) # Calculate new worry level.
                to = go_true[monkey] if worry%div[monkey]==0 else go_false[monkey] # Decide who to throw to.
                items[to].append(worry)
            inspected[monkey] += len(items[monkey])
            items[monkey].clear()
    return math.prod(sorted(inspected)[-2:]) # Multiply two largest number of inspections.

# Call with number of rounds and a method to decrease the worry level.
print("Part 1:", monkey_business(copy.deepcopy(items), 20, lambda x: x//3))
print("Part 2:", monkey_business(items, 10000, lambda x: x%math.prod(div)))
