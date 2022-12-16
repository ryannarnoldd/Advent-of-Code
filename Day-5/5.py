# Ryan Arnold - Advent 2022 - Day 5: Supply Stacks
import re
from copy import deepcopy

# Read in the input file and splits the input into two, one for the drawing and one for the procedure.
with open('5.txt') as f:
    lines = f.read().split('\n\n')

# Splits the drawing into a list of rows for crates and splits each row into a list of procedures.
drawing = lines[0].split('\n')
procedure = lines[1].splitlines()
crates = {}

# Creates a dictionary of stacks with the key being the index of the stack.
# The value(s) are the crates on the stack.
original_crates = {}
starting_stacks = [re.findall(r".{1,4}", row) for row in drawing[:-1]] # Credit: Github.com/25prabhu10
for row in starting_stacks[::-1]:
    for index, crate in enumerate(row, start=1):
        crate = crate[1].strip()
        if crate:
            if index in original_crates:
                original_crates[index].append(crate)
            else:
                original_crates[index] = [crate]
# Sorts the crates by the key (index of the stack).
original_crates = {key: original_crates[key] for key in sorted(original_crates)}

# Loops through the procedure and finds each value(s) in the instruction.
procedure = [re.findall(r'\d+', instruction) for instruction in procedure]

# Part 1
crates = deepcopy(original_crates) # Creates a deep copy of the original crates.

# Loops through the procedure and moves the crates by popping and appending.
for instruction in procedure:
    amount, source, target = map(int, instruction)
    for _ in range(amount):
        crates[target].append(crates[source].pop())

# Joins the top of each stack into a string.
part1_results = ''.join([crates[key][-1] for key in crates])
print(part1_results) # FWSHSPJWM

# Part 2
crates = deepcopy(original_crates) # Creates a deep copy of the original crates.

# Loops through the procedure and moves the crates by splicing and extending/adding.
for instruction in procedure:
    amount, source, target = map(int, instruction)
    lifted = crates[source][-amount:]
    del(crates[source][-amount:])
    crates[target].extend(lifted)

# Joins the top of each stack into a string.
part2_results = ''.join([crates[key][-1] for key in crates])
print(part2_results) # PWPWHGFZS