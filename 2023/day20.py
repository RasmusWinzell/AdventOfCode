# Advent of Code 2023 Day 20, https://adventofcode.com/2023/day/20
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day20.py
# This is the original solution
import math
from collections import defaultdict

from aocd.models import Puzzle


# Solved in 0:59:59 (Answer: 1020211150)
def partA(input):
    lines = input.splitlines()
    connections = {}
    for line in lines:
        module, other = line.split(" -> ")
        if module[0] in "%&":
            module_type = module[0]
            module_id = module[1:]
        else:
            module_type = None
            module_id = module
        dests = other.split(", ")
        connections[module_id] = (module_type, dests)

    flip_flops = defaultdict(bool)
    conjunctions = defaultdict(dict)
    for module_id, (module_type, dests) in connections.items():
        if module_type == "&":
            for module_id2, (module_type2, dests2) in connections.items():
                if module_id in dests2:
                    conjunctions[module_id][module_id2] = False
    print(conjunctions)
    pulses = []
    for _ in range(1000):
        print()

        queue = [("broadcaster", False, "button")]
        while queue:
            module_id, pulse, src = queue.pop(0)
            pulses.append(pulse)
            print(src, "-", pulse, "->", module_id)
            if module_id == "output" or module_id not in connections:
                # print(f"Output {module_id}: {output}")
                continue

            module_type, dests = connections[module_id]
            output = pulse
            if module_type == "%":
                if not pulse:
                    flip_flops[module_id] = not flip_flops[module_id]
                    output = flip_flops[module_id]
                else:
                    output = None
            elif module_type == "&":
                conjunctions[module_id][src] = pulse
                output = not all(conjunctions[module_id].values())

            if output is not None:
                for dest in dests:
                    queue.append((dest, output, module_id))

    lows = pulses.count(False)
    highs = pulses.count(True)
    print(lows, highs, lows * highs)
    return lows * highs


# Solved in 2:48:45 (Answer: 238815727638557)
def partB(input):
    lines = input.splitlines()
    connections = {}
    for line in lines:
        module, other = line.split(" -> ")
        if module[0] in "%&":
            module_type = module[0]
            module_id = module[1:]
        else:
            module_type = None
            module_id = module
        dests = other.split(", ")
        connections[module_id] = (module_type, dests)

    flip_flops = defaultdict(bool)
    conjunctions = defaultdict(dict)
    sends_to_rx = None
    for module_id, (module_type, dests) in connections.items():
        if "rx" in dests:
            sends_to_rx = module_id
        if module_type == "&":
            for module_id2, (module_type2, dests2) in connections.items():
                if module_id in dests2:
                    conjunctions[module_id][module_id2] = False

    print(conjunctions)
    cycles = {k: None for k, _ in conjunctions[sends_to_rx].items()}
    pulses = []
    for i in range(1000000000):
        # print()
        pulse_count = defaultdict(int)
        queue = [("broadcaster", False, "button")]
        while queue:
            module_id, pulse, src = queue.pop(0)
            pulses.append(pulse)
            # print(src, "-", pulse, "->", module_id)
            if module_id == sends_to_rx and pulse:
                print("pulse", src, i + 1)
                pulse_count[src] += 1
            if module_id == "output" or module_id not in connections:
                # print(f"Output {module_id}: {output}")
                continue

            module_type, dests = connections[module_id]
            output = pulse
            if module_type == "%":
                if not pulse:
                    flip_flops[module_id] = not flip_flops[module_id]
                    output = flip_flops[module_id]
                else:
                    output = None
            elif module_type == "&":
                conjunctions[module_id][src] = pulse
                output = not all(conjunctions[module_id].values())

            if output is not None:
                for dest in dests:
                    queue.append((dest, output, module_id))

        for k, v in cycles.items():
            val = pulse_count[k]
            if val and v is None:
                print("found", k, i + 1)
                cycles[k] = i + 1
        if all(cycles.values()):
            print(cycles)
            button_presses = math.lcm(*cycles.values())
            print(button_presses)
            return button_presses


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=20)

    #     partA(
    #         """broadcaster -> a
    # %a -> inv, con
    # &inv -> b
    # %b -> con
    # &con -> output"""
    #     )
    #     exit()
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         answer = partA(example.input_data)
    #         assert (
    #             str(answer) == example.answer_a
    #         ), f"Part A: Expected {example.answer_a}, got {answer}"

    if puzzle.answered_a:
        answer = partA(puzzle.input_data)
        assert (
            str(answer) == puzzle.answer_a
        ), f"Part A: Expected {puzzle.answer_a}, got {answer}"
    else:
        puzzle.answer_a = partA(puzzle.input_data)
        assert puzzle.answered_a, "Answer A not correct"

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
