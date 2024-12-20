# Advent of Code 2024 Day 20, https://adventofcode.com/2024/day/20
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day20.py
# This is the original solution
from collections import Counter, deque

from aocd.models import Puzzle


def print_map(m, visited):
    for y, r in enumerate(m):
        for x, c in enumerate(r):
            if (x, y) in visited:
                print("o", end="")
            else:
                print(c, end="")
        print()


# Solved in 1:00:09
def partA(input):
    print(input)
    m = input.splitlines()
    S = [(x, y) for y, r in enumerate(m) for x, c in enumerate(r) if c == "S"][0]
    E = [(x, y) for y, r in enumerate(m) for x, c in enumerate(r) if c == "E"][0]

    visited = {}
    best = float("inf")
    cheats = []

    q = deque([(0, 0, S)])
    while q:
        d, c, p = q.popleft()
        if d > best:
            break
        if p == E:
            best = d
        if d > visited.get((c, p), float("inf")):
            continue
        visited[(c, p)] = d
        x, y = p

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(m[0]) and 0 <= ny < len(m):
                if m[ny][nx] == "#" and c > 0:
                    q.append((d + 1, c - 1, (nx, ny)))
                if m[ny][nx] != "#":
                    q.append((d + 1, c, (nx, ny)))

    print(best)

    # visited = set()
    visited2 = set()
    q = deque([(0, 1, S)])
    while q:
        d, c, p = q.popleft()
        if d > best:
            break
        visited2.add(p)
        # print_map(m, visited2)
        # print()
        if (c, p) in visited:
            if (cheat := visited[(c, p)] - d) >= 100:
                cheats.append(cheat)
            continue
        visited[(c, p)] = d
        x, y = p
        pass

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(m[0]) and 0 <= ny < len(m):
                if m[ny][nx] == "#" and c > 0:
                    q.append((d + 1, c - 1, (nx, ny)))
                if m[ny][nx] != "#":
                    q.append((d + 1, c, (nx, ny)))

    # cheats = sorted(Counter(cheats).items())
    res = len(cheats)
    print(res)
    return res

    # print("No path found")


# Solved in 2:44:35
def partB(input):
    print(input)
    m = input.splitlines()
    S = [(x, y) for y, r in enumerate(m) for x, c in enumerate(r) if c == "S"][0]
    E = [(x, y) for y, r in enumerate(m) for x, c in enumerate(r) if c == "E"][0]

    visited = {}
    best = float("inf")

    q = deque([(0, S)])
    while q:
        d, p = q.popleft()
        if d > best:
            break
        if p == E:
            best = d
        if d > visited.get(p, float("inf")):
            continue
        visited[p] = d
        x, y = p

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(m[0]) and 0 <= ny < len(m):
                if m[ny][nx] != "#":
                    q.append((d + 1, (nx, ny)))

    print(best)

    cheats = []

    for i, p0 in enumerate(visited.keys()):
        print(f"{i}/{len(visited)}")
        visited2 = set()
        q = deque([(visited[p0], 20, p0)])
        while q:
            d, c, p = q.popleft()

            if d > best:
                break

            if p in visited2:
                continue

            visited2.add(p)
            # print_map(m, visited2)
            # print()
            x, y = p
            if m[y][x] != "#" and p != p0:
                cheat = visited[p] - d
                if cheat >= 100:
                    cheats.append(cheat)

            if c == 0:
                continue

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(m[0]) and 0 <= ny < len(m):
                    q.append((d + 1, c - 1, (nx, ny)))
        # exit()

    print(sorted(Counter(cheats).items()))
    res = len(cheats)
    print(res)
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=20)
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
