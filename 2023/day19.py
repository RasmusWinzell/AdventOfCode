# Advent of Code 2023 Day 19, https://adventofcode.com/2023/day/19
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day19.py
# This is the original solution
from aocd.models import Puzzle


def run_flow(part, flow_name, flows):
    if flow_name == "R":
        return False
    if flow_name == "A":
        return True
    flow = flows[flow_name]
    rules = flow.split(",")
    for rule in rules:
        if ":" not in rule:
            return run_flow(part, rule, flows)
        var = rule[0]
        op = rule[1]
        val = int(rule[2:].split(":")[0])
        next_flow = rule[2:].split(":")[1]
        if op == "<":
            if part[var] < val:
                return run_flow(part, next_flow, flows)
        elif op == ">":
            if part[var] > val:
                return run_flow(part, next_flow, flows)
    return False


# Solved in 0:21:48 (Answer: 449531)
def partA(input):
    flows = input.split("\n\n")[0].split("\n")
    flows = {f.split("{")[0]: f.split("{")[1][:-1] for f in flows}
    parts = input.split("\n\n")[1].split("\n")
    parts = [
        {v.split("=")[0]: int(v.split("=")[1]) for v in p[1:-1].split(",")}
        for p in parts
    ]
    print(flows)
    print(parts)

    score = 0
    for part in parts:
        res = run_flow(part, "in", flows)
        if res is True:
            score += sum(part.values())
    print(score)
    return score


def copy_lims(lims):
    return {k: lim.copy() for k, lim in lims.items()}


def run_flowB(part_lims, flow_name, flows):
    if flow_name == "R":
        return []
    if flow_name == "A":
        return [part_lims]
    flow = flows[flow_name]
    rules = flow.split(",")
    res = []
    for rule in rules:
        if ":" not in rule:
            res += run_flowB(copy_lims(part_lims), rule, flows)
        else:
            var = rule[0]
            op = rule[1]
            val = int(rule[2:].split(":")[0])
            next_flow = rule[2:].split(":")[1]
            if op == "<":
                new_lims = copy_lims(part_lims)
                new_lims[var][1] = min(new_lims[var][1], val - 1)
                res += run_flowB(new_lims, next_flow, flows)
                part_lims[var][0] = max(part_lims[var][0], val)
            elif op == ">":
                new_lims = copy_lims(part_lims)
                new_lims[var][0] = max(new_lims[var][0], val + 1)
                res += run_flowB(new_lims, next_flow, flows)
                part_lims[var][1] = min(part_lims[var][1], val)
    return res


import math
from collections import defaultdict


# Solved in 3:16:11 (Answer: 122756210763577)
def partB(input):
    flows = input.split("\n\n")[0].split("\n")
    flows = {f.split("{")[0]: f.split("{")[1][:-1] for f in flows}

    part_lims = {k: [1, 4000] for k in "xmas"}
    res = run_flowB(part_lims, "in", flows)

    count = 0
    for r in res:
        count += math.prod([r[k][1] - r[k][0] + 1 for k in "xmas"])
    print(count)
    return count


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=19)
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
