# Advent of Code 2022 Day 6
# https://adventofcode.com/2022/day/7
# https://github.com/RasmusWinzell/AdventOfCode

from aocd import data
from collections import defaultdict

lines = data.split("\n")

current_dir = []
files = {}

# Find all files
for line in lines:
    args = line.split(" ")
    if "$ cd" in line:
        if args[-1] == "/":
            current_dir = [""]
        elif args[-1] == "..":
            del current_dir[-1]
        else:
            current_dir.append(args[-1])
    elif "$ ls" not in line and line[:3] != "dir":
        files["/".join(current_dir + [args[1]])] = int(args[0])

# Calculate size of directories
dir_size = defaultdict(int)
for file in files:
    dirs = file.split("/")
    for i in range(len(dirs)-1):
        dir_size["/".join(dirs[:i+1])] += files[file]

# Part 1
files_to_count = {k: v for k, v in dir_size.items() if v <= 100000}
print(sum(files_to_count.values()))

# Part 2
needed_space = 30000000 - (70000000 - sum(files.values()))
files_to_count = {k: v for k, v in dir_size.items() if v >= needed_space}
print(min(files_to_count.values()))
