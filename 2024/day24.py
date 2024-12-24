# Advent of Code 2024 Day 24, https://adventofcode.com/2024/day/24
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2024/day24.py
# This is the original solution
from collections import defaultdict
from random import randint

from aocd.models import Puzzle


# Solved in 0:32:51
def partA(input):
    regs = {}
    intsructions = []
    ouput_regs = set()
    for line in input.split("\n"):
        if not line:
            continue
        if ": " in line:
            reg, val = line.split(": ")
            regs[reg] = int(val)
            continue
        r1, op, r2, _, r3 = line.split()
        intsructions.append((r1, op, r2, r3))
        if "z" in r3:
            ouput_regs.add(r3)

    visited = set()
    while regs.keys() & ouput_regs != ouput_regs:
        for r1, op, r2, r3 in intsructions:
            if r1 not in regs or r2 not in regs:
                continue
            if (r1, op, r2, r3) in visited:
                continue
            visited.add((r1, op, r2, r3))
            if op == "AND":
                regs[r3] = regs[r1] & regs[r2]
            elif op == "OR":
                regs[r3] = regs[r1] | regs[r2]
            elif op == "XOR":
                regs[r3] = regs[r1] ^ regs[r2]

    for k, v in sorted(regs.items()):
        print(k, v)

    res = ""
    for k in sorted(regs, reverse=True):
        if "z" in k:
            res += str(regs[k])
    res = int(res, 2)
    print(res)
    return res


# Solved in 5:48:39
def partB(input):
    regs = set()
    naming = {}
    for line in input.split("\n"):
        if not line:
            continue
        if ": " in line:
            continue
        r1, op, r2, _, r3 = line.split()
        naming[(r1, op, r2)] = r3
        naming[(r2, op, r1)] = r3
        regs |= {r1, r2, r3}
    inps = sum(1 for r in regs if "x" in r or "y" in r) // 2
    outs = sum(1 for r in regs if "z" in r)

    # generate adder connections
    def get_inst(key, swaps):
        res = naming[key]
        for s1, s2 in swaps:
            if res == s1:
                return s2
            if res == s2:
                return s1
        return res

    def find_error(remaining, swaps=[]):
        try:
            c = None
            for i in range(inps):
                a = "x" + str(i).zfill(2)
                b = "y" + str(i).zfill(2)
                if i == 0:
                    s = get_inst((a, "XOR", b), swaps)
                    c = get_inst((a, "AND", b), swaps)
                    remaining -= {a, b, s, c}
                else:
                    s1 = get_inst((a, "XOR", b), swaps)
                    s = get_inst((s1, "XOR", c), swaps)
                    c1 = get_inst((s1, "AND", c), swaps)
                    c2 = get_inst((a, "AND", b), swaps)
                    c = get_inst((c1, "OR", c2), swaps)
                    remaining -= {a, b, s1, s, c1, c2, c}
        except KeyError as e:
            r1, op, r2 = e.args[0]
            return r1, r2, remaining
        return None, None, remaining

    def find_swap(swaps=[]):
        r1, r2, remaining = find_error(regs.copy(), swaps)
        if r1 is None:
            return None
        final_swaps = []
        for a in (r1, r2):
            for b in regs:
                r11, r22, rem = find_error(regs.copy(), swaps + [(a, b)])
                if len(rem) < len(remaining):
                    print(a, b)
                    return swaps + [(a, b)]
        raise Exception("No swap found")

    swaps = []
    while True:
        out = find_swap(swaps)
        if out is None:
            break
        swaps = out
    res = ",".join(sorted(r for s in swaps for r in s))
    print(res)
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=24)
    #     for example in puzzle.examples:
    #         if example.answer_a:
    #             inp = """x00: 1
    # x01: 0
    # x02: 1
    # x03: 1
    # x04: 0
    # y00: 1
    # y01: 1
    # y02: 1
    # y03: 1
    # y04: 1

    # ntg XOR fgs -> mjb
    # y02 OR x01 -> tnw
    # kwq OR kpj -> z05
    # x00 OR x03 -> fst
    # tgd XOR rvg -> z01
    # vdt OR tnw -> bfw
    # bfw AND frj -> z10
    # ffh OR nrd -> bqk
    # y00 AND y03 -> djm
    # y03 OR y00 -> psh
    # bqk OR frj -> z08
    # tnw OR fst -> frj
    # gnj AND tgd -> z11
    # bfw XOR mjb -> z00
    # x03 OR x00 -> vdt
    # gnj AND wpb -> z02
    # x04 AND y00 -> kjc
    # djm OR pbm -> qhw
    # nrd AND vdt -> hwm
    # kjc AND fst -> rvg
    # y04 OR y02 -> fgs
    # y01 AND x02 -> pbm
    # ntg OR kjc -> kwq
    # psh XOR fgs -> tgd
    # qhw XOR tgd -> z09
    # pbm OR djm -> kpj
    # x03 XOR y03 -> ffh
    # x00 XOR y04 -> ntg
    # bfw OR bqk -> z06
    # nrd XOR fgs -> wpb
    # frj XOR qhw -> z04
    # bqk OR frj -> z07
    # y03 OR x01 -> nrd
    # hwm AND bqk -> z03
    # tgd XOR rvg -> z12
    # tnw OR pbm -> gnj"""
    #             answer = partA(inp)
    #             assert (
    #                 str(answer) == example.answer_a
    #             ), f"Part A: Expected {example.answer_a}, got {answer}"

    if puzzle.answered_a:
        answer = partA(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_a
        ), f"Part A: Expected {puzzle.answer_a}, got {answer}"
    else:
        puzzle.answer_a = partA(puzzle.input_data)
        assert puzzle.answered_a, "Answer A not correct"

    #     for example in puzzle.examples:
    #         if example.answer_b:
    #             inp = """x00: 0
    # x01: 1
    # x02: 0
    # x03: 1
    # x04: 0
    # x05: 1
    # y00: 0
    # y01: 0
    # y02: 1
    # y03: 1
    # y04: 0
    # y05: 1

    # x00 AND y00 -> z05
    # x01 AND y01 -> z02
    # x02 AND y02 -> z01
    # x03 AND y03 -> z03
    # x04 AND y04 -> z04
    # x05 AND y05 -> z00"""
    #             answer = partB(inp)
    #             assert (
    #                 str(answer) == example.answer_b
    #             ), f"Part B: Expected {example.answer_b}, got {answer}"

    if puzzle.answered_b:
        answer = partB(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_b
        ), f"Part B: Expected {puzzle.answer_b}, got {answer}"
    else:
        puzzle.answer_b = partB(puzzle.input_data)
        assert puzzle.answered_b, "Answer B not correct"
