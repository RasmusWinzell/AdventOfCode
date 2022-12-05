# Advent of Code 2022 Day 5
# https://github.com/RasmusWinzell/AdventOfCode

def parse_input(data):
    lines = data.split("\n")

    h = 8 # Hight of tallest stack
    w = 9 # Number of stacks

    stacks = []
    for j in range(w):
        stacks.append([])
    for i in range(h):
        for j in range(w):
            if lines[i][1+j*4] != " ":
                stacks[j].append(lines[i][1+j*4])
    
    return stacks, lines[h+2:]

def part1(stacks, instructions):
    for line in instructions:
        m, f, t = map(int, line.split(" ")[1::2])
        for i in range(m):
            stacks[t-1].insert(0, stacks[f-1][0])
            del stacks[f-1][0]

def part2(stacks, instructions):
    for line in instructions:
        m, f, t = map(int, line.split(" ")[1::2])
        vals = stacks[f-1][0:m]
        for val in reversed(vals):
            stacks[t-1].insert(0, val)
        del stacks[f-1][0:m]


from aocd import data
stacks, instructions = parse_input(data)
#part1(stacks, instructions)
part2(stacks, instructions)
answer = "".join([stack[0] for stack in stacks])
print(answer)
