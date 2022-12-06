# Advent of Code 2022 Day 6
# https://github.com/RasmusWinzell/AdventOfCode

from aocd import data

# Part 1
#packet_size = 4

# Part 2
packet_size = 14

x = []
for i in range(len(data)):
    if len(x) == packet_size:
        del x[0]
    x.append(data[i])
    if len(set(x)) == packet_size:
        print(i+1, x)
        break