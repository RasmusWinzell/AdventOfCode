# Advent of Code 2023 Day 25, https://adventofcode.com/2023/day/25
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day25.py
# This is the original solution
import re
import sys
from collections import defaultdict
from random import choices, randint

from aocd.models import Puzzle

sys.setrecursionlimit(10000)


def bfs(start, goal, connections):
    queue = [(start, (start,))]
    visited = set()
    while queue:
        node, path = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == goal:
                return path
            queue.extend(
                (c, path + (c,)) for c in connections[node] if c not in visited
            )


# Solved in 1:09:16 (Answer: 569904)
def partA(input):
    connections = defaultdict(list)
    for line in input.splitlines():
        vals = re.findall(r"[a-z]+", line)
        for i in range(1, len(vals)):
            connections[vals[0]].append(vals[i])
            connections[vals[i]].append(vals[0])

    visists = defaultdict(int)
    components = list(connections.keys())
    print(len(components))
    for i in range(10000):
        x1 = randint(0, len(components) - 1)
        x2 = randint(0, len(components) - 1)
        res = bfs(components[x1], components[x2], connections)
        # print(res)
        for rs in zip(res[:-1], res[1:]):
            r1, r2 = sorted(rs)
            visists[(r1, r2)] += 1

    visits = sorted(visists.items(), key=lambda x: x[1], reverse=True)
    remove = set([k for k, v in visits[:3]])
    print(remove)

    queue = [visits[-1][0][0]]
    print(queue)
    visited = set()
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for c in connections[node]:
                if c not in visited:
                    edge = tuple(sorted((node, c)))
                    if edge not in remove:
                        queue.append(c)
    print(sorted(visited))

    l1 = len(visited)
    l2 = len(connections) - l1
    print(l1, l2, l1 * l2)
    return l1 * l2


# Solved in 1:09:16 (Answer: )
def partB(input):
    pass


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=25)

    test_in = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""

    for example in puzzle.examples:
        if example.answer_a:
            answer = partA(test_in)
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
