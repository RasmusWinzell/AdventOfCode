# Advent of Code 2022 Day 13
# https://adventofcode.com/2022/day/13
# https://github.com/RasmusWinzell/AdventOfCode

import json, math, functools
from aocd import data

packets = [json.loads(line) for line in data.split("\n") if line]

def compare(p1, p2):
    # Not same type, change int to list.
    if type(p1) != type(p2):
        p1 = p1 if isinstance(p1, list) else [p1]
        p2 = p2 if isinstance(p2, list) else [p2]
        return compare(p1, p2)

    # Both are int.
    elif isinstance(p1, int):
        return 1 if p1 < p2 else 0 if p1 == p2 else -1
        
    # Both are list.
    else:
        # Compare all elements.
        for i in range(min(len(p1), len(p2))):
            cmp = compare(p1[i], p2[i])
            if cmp != 0:
                return cmp
        # Elements are same, result depends on list lengths.
        return 0 if len(p1) == len(p2) else 1 if len(p1) < len(p2) else -1

corrects = [i//2+1 for i in range(0, len(packets), 2) if compare(packets[i], packets[i+1]) == 1]
print("Part 1:", sum(corrects))

dividers = [[[2]], [[6]]]
ordered = sorted(packets + dividers, key=functools.cmp_to_key(compare), reverse=True)
print("Part 2:", math.prod([1 + ordered.index(div) for div in dividers]))   