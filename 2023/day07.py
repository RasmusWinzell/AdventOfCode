# Advent of Code 2023 Day 7, https://adventofcode.com/2023/day/7
# https://github.com/RasmusWinzell/AdventOfCode/blob/master/2023/2023/day07.py
# This is the cleaned solution
from collections import Counter

from aocd.models import Puzzle

card_map_a = {ord(k): i for i, k in enumerate("23456789TJQKA")}
card_map_b = {ord(k): i for i, k in enumerate("J23456789TQKA")}
hands = [(-5,), (-4,), (-3, -2), (-3,), (-2, -2), (-2,), (-1,)]


# Solved in 0:27:23 (Answer: 250058342)
def partA(input: str):
    bids = {k: int(v) for k, v in map(str.split, input.split("\n"))}
    card_res = []
    for card in bids.keys():
        counts = sorted(Counter(card).values(), reverse=True)
        valid = [sum(sum(zip(counts, hand), ())) for hand in hands]
        card_res.append((-valid.index(0), card))
    card_res = sorted(card_res, key=lambda c: (c[0], c[1].translate(card_map_a)))
    res = sum(bids[k[1]] * i for i, k in enumerate(card_res, 1))
    return res


# Solved in 1:04:23 (Answer: 250506580)
def partB(input: str):
    bids = {k: int(v) for k, v in map(str.split, input.split("\n"))}
    card_res = []
    for card in bids.keys():
        js = card.count("J")
        counts = sorted(Counter(card.replace("J", "")).values(), reverse=True) + [0]
        valid = [sum(sum(zip(counts, hand), (js,))) for hand in hands]
        card_res.append((-valid.index(0), card))
    card_res = sorted(card_res, key=lambda c: (c[0], c[1].translate(card_map_b)))
    res = sum(bids[k[1]] * i for i, k in enumerate(card_res, 1))
    return res


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=7)

    puzzle_input = puzzle.input_data

    answer_a = partA(puzzle_input)
    answer_b = partB(puzzle_input)

    print(f"Answer A: {answer_a}, Answer B: {answer_b}")