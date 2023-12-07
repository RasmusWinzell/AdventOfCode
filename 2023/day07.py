# Advent of Code 2023 Day 7, https://adventofcode.com/2023/day/7
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day07.py
# This is the original solution
import math
from collections import Counter

from aocd.models import Puzzle

card_map = {k: chr(ord("a") + i) for i, k in enumerate("23456789TJQKA")}
print(card_map)


# Solved in 0:27:23 (Answer: 250058342)
def partA(input: str):
    bids = [bid.split() for bid in input.split("\n")]
    bids = {k: int(v) for k, v in bids}

    card_res = []
    for card in bids.keys():
        value = card
        for k, v in card_map.items():
            value = value.replace(k, v)
        counts = Counter(card).values()
        if 5 in counts:
            card_res.append((7, value, card))
        elif 4 in counts:
            card_res.append((6, value, card))
        elif 3 in counts and 2 in counts:
            card_res.append((5, value, card))
        elif 3 in counts:
            card_res.append((4, value, card))
        elif 2 in Counter(counts).values():
            card_res.append((3, value, card))
        elif 2 in counts:
            card_res.append((2, value, card))
        else:
            card_res.append((1, value, card))
    card_res = sorted(card_res)
    res = sum(bids[k] * (i + 1) for i, (_, _, k) in enumerate(card_res))
    return res


card_map2 = {k: chr(ord("a") + i) for i, k in enumerate("J23456789TQKA")}


def check_valid(wanted, js, counts):
    counts = list(counts)
    print(wanted, js, counts)
    for val in wanted:
        valid = False
        for used_js in range(js + 1):
            if val - used_js in counts:
                valid = True
                counts.remove(val - used_js)
                break
        if valid:
            js -= used_js
        else:
            return False
    print("Valid")
    return True


# Solved in 1:04:23 (Answer: 250506580)
def partB(input: str):
    bids = [bid.split() for bid in input.split("\n")]
    bids = {k: int(v) for k, v in bids}

    card_res = []
    for card in bids.keys():
        print(card)
        value = card
        for k, v in card_map2.items():
            value = value.replace(k, v)
        counts = Counter(card)
        js = card.count("J")
        counts["J"] = 0
        counts = counts.values()
        if check_valid([5], js, counts):
            card_res.append((7, value, card))
        elif check_valid([4], js, counts):
            card_res.append((6, value, card))
        elif check_valid([3, 2], js, counts):
            card_res.append((5, value, card))
        elif check_valid([3], js, counts):
            card_res.append((4, value, card))
        elif check_valid([2, 2], js, counts):
            card_res.append((3, value, card))
        elif check_valid([2], js, counts):
            card_res.append((2, value, card))
        else:
            card_res.append((1, value, card))
    card_res = sorted(card_res)
    print(card_res)
    res = sum(bids[k] * (i + 1) for i, (_, _, k) in enumerate(card_res))
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=7)
    for example in puzzle.examples:
        if example.answer_a:
            answer = partA(example.input_data)
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
