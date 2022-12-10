# Advent of Code 2022 Day 10
# https://adventofcode.com/2022/day/10
# https://github.com/RasmusWinzell/AdventOfCode

from aocd import data

instructions = data.split("\n")

x_vals = [1] + [0] * 6 * 40
instr, bussy_until = 0, 0
for cycle in range(1, len(x_vals)):
    #Calculate X for cycle.
    x_vals[cycle] += x_vals[cycle-1]

    if cycle >= bussy_until and instr < len(instructions):
        # Run instruction.
        args = instructions[instr].split(" ")
        bussy_until = cycle + len(args)
        if len(args) == 2:
            x_vals[cycle + 2] = int(args[1])
        instr += 1      

print("Part 1:", sum([x*i for i, x in list(enumerate(x_vals))[20:len(x_vals):40]]))

pixels = ["#" if abs(i%40-x) <=1 else "." for  i, x in enumerate(x_vals[1:])]
print("Part 2:\n" + "\n".join("".join(pixels[row:row+40]) for row in range(0, 6*40, 40)))


