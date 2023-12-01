# Ryan Arnold - Advent 2023 - Day 1: Trebuchet?!

# Read in the input file and create a list of calibrations
with open('1.txt') as f:
    lines = f.read().splitlines()
    
total = 0
# Calculate the firt and last digit of each line.
for line in lines:
    digits = [d for d in line if d.isdigit()]
    total += int(digits[0] + digits[-1])

# Part 1
print(total)

# Part 2

numbers = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3, 
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7, 
    'eight': 8,
    'nine': 9,
}
