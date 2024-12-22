# Advent of Code 2024 Day 21, https://adventofcode.com/2024/day/21
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day21.py
# This is the original solution
from collections import deque
from functools import cache

from aocd.models import Puzzle

DIRS = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
DIRS_INV = {(0, -1): "^", (0, 1): "v", (-1, 0): "<", (1, 0): ">"}

numpad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]
dirpad = [["#", "^", "A"], ["<", "v", ">"]]

pad_list = [numpad, dirpad]

PRIORITY = {"<": 0, "v": 1, "^": 2, ">": 3}
NUM_PRIORITY = {"^": 0, ">": 1, "<": 2, "v": 3}
DIR_PRIORITY = {"v": 0, ">": 1, "<": 2, "^": 3}

numstart = (2, 3)
dirstart = (2, 0)

num_invalid = (0, 3)
dir_invalid = (0, 0)


def find_key(numpad, key):
    for y, row in enumerate(numpad):
        for x, k in enumerate(row):
            if k == key:
                return x, y
    return None


@cache
def gen_move(sx, sy, ex, ey, invalid=dir_invalid):
    dx, dy = ex - sx, ey - sy
    moves = ""
    for x in range(abs(dx)):
        moves += ">" if dx > 0 else "<"
    for y in range(abs(dy)):
        moves += "v" if dy > 0 else "^"
    moves = sorted(moves, key=lambda x: PRIORITY[x])
    x, y = sx, sy
    for move in moves:
        dx, dy = DIRS[move]
        x, y = x + dx, y + dy
        if (x, y) == invalid:
            moves.reverse()
            break
    return "".join(moves) + "A"


@cache
def move_cost(moves, num_pads):
    if moves == "A":
        return 1
    if num_pads == 0:
        return len(moves)

    x, y = dirstart

    count = 0
    for move in moves:
        ex, ey = find_key(dirpad, move)
        next_move = gen_move(x, y, ex, ey)
        cost = move_cost(next_move, num_pads - 1)
        count += cost
        x, y = ex, ey
    return count


def press2(positions, idx):
    if idx == 0:
        return False, True
    elif idx == 1:
        if positions[idx] == (2, 0):
            return False, True
        p0, p = positions[idx - 1 : idx + 1]
        k = dirpad[p[1]][p[0]]
        dx, dy = DIRS[k]
        nx, ny = p0[0] + dx, p0[1] + dy
        positions[idx - 1] = (nx, ny)
        if 0 <= nx < 3 and 0 <= ny < 4 and numpad[ny][nx] != "#":
            return True, False
    elif positions[idx] == (2, 0):
        return press2(positions, idx - 1)
    else:
        p0, p = positions[idx - 1 : idx + 1]
        k = dirpad[p[1]][p[0]]
        dx, dy = DIRS[k]
        nx, ny = p0[0] + dx, p0[1] + dy
        positions[idx - 1] = (nx, ny)
        if 0 <= nx < 3 and 0 <= ny < 2 and dirpad[ny][nx] != "#":
            return True, False
    return False, False


# Solved in 0:49:39
def partA(input):
    print(input)
    codes = input.splitlines()

    res = 0
    for code in codes:

        start_state = (0, numstart, dirstart, dirstart, "")

        visited = set()
        q = deque([start_state])
        min_presses = None
        while q:
            state = q.popleft()
            presses, p1, p2, p3, partial_code = state

            if state in visited:
                continue
            visited.add(state)

            if partial_code == code:
                print("Found code", presses)
                min_presses = presses
                break

            # Moves using arrowkeys
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = p3
                nx, ny = x + dx, y + dy
                if 0 <= nx < 3 and 0 <= ny < 2 and dirpad[ny][nx] != "#":
                    q.append((presses + 1, p1, p2, (nx, ny), partial_code))

            # Press by pressing A
            if p3 == (2, 0):
                if p2 == (2, 0):
                    new_partial = partial_code + numpad[p1[1]][p1[0]]
                    if code.startswith(new_partial):
                        q.append((presses + 1, p1, p2, p2, new_partial))
                else:
                    k2 = dirpad[p2[1]][p2[0]]
                    dx, dy = DIRS[k2]
                    nx, ny = p1[0] + dx, p1[1] + dy
                    if 0 <= nx < 3 and 0 <= ny < 4 and numpad[ny][nx] != "#":
                        q.append((presses + 1, (nx, ny), p2, p3, partial_code))
            else:
                k3 = dirpad[p3[1]][p3[0]]
                dx, dy = DIRS[k3]
                nx, ny = p2[0] + dx, p2[1] + dy
                if 0 <= nx < 3 and 0 <= ny < 2 and dirpad[ny][nx] != "#":
                    q.append((presses + 1, p1, (nx, ny), p3, partial_code))

        res += min_presses * int(code[:3])
    print(res)
    return res


# 3 -> 8 (-1, -2)
# 2^ 1< 1A

# 0 -> 4 (-1, -2)
# 2^ 1< 1A


def sim_press(keys, pads):
    positions = [numstart] + [dirstart] * (len(pads) - 1)
    control_pad = pads[-1]
    w, h = len(control_pad[0]), len(control_pad)

    code = ""
    print("start")
    # print(positions)
    for i, key in enumerate(keys):
        if key == "A":
            valid, press_last = press2(positions, len(pads) - 1)
            # print(positions)
            if press_last:
                code += numpad[positions[0][1]][positions[0][0]]
                print(i + 1, code)
            elif not valid:
                print("Invalid press")
        else:
            dx, dy = DIRS[key]
            x, y = positions[-1]
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h:
                positions[-1] = (nx, ny)
            # print(positions)
    print(code)


# <AAv<AA>>^A
# v<<AA>^AA>A

# v<<A>>^AAv<A<A>>^AAvAA<^A>A
# <vA<AA>>^AAvA<^A>AAvA^A


# Solved in 1 day, 0:00:00
def partB(input):
    print(input)
    #     input = """029A
    # 980A
    # 179A
    # 456A
    # 379A"""
    # input = "179A"
    codes = input.splitlines()
    res = 0
    for code in codes:
        curr_c = "A"
        tot_count = 0
        for c in code:
            sx, sy = find_key(numpad, curr_c)
            ex, ey = find_key(numpad, c)
            move = gen_move(sx, sy, ex, ey, num_invalid)
            cost = move_cost(move, 25)
            tot_count += cost
            curr_c = c
        print(code, tot_count)
        res += tot_count * int(code[:3])

    print(res)
    return res


# v<<A>>^AvA^Av<<A>>^AAv<A<A>>^AAvAA<^A>Av<A>^AA<A>Av<A<A>>^AAAvA<^A>A
# <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
# v<<A>>^AvA^Av<<AA>A>^AA<A>vA^AAvA^Av<A>^AA<A>Av<<A>A>^AAA<A>vA^A

if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=21)
    #     for example in puzzle.examples:
    #         if example.answer_a:
    #             inp = """029A
    # 980A
    # 179A
    # 456A
    # 379A"""
    #             answer = partA(inp)
    #             assert (
    #                 str(answer) == example.answer_a
    #             ), f"Part A: Expected {example.answer_a}, got {answer}"

    #     if puzzle.answered_a:
    #         answer = partA(puzzle.input_data)
    #         assert (
    #             str(answer) == puzzle.answer_a
    #         ), f"Part A: Expected {puzzle.answer_a}, got {answer}"
    #     else:
    #         puzzle.answer_a = partA(puzzle.input_data)
    #         assert puzzle.answered_a, "Answer A not correct"

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
