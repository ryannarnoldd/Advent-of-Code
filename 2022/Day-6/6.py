# Ryan Arnold - Advent 2022 - Day 6: Tuning Trouble
from collections import Counter

# Read in the input file into signal, a string.
with open('6.txt') as f:
    signal = f.read()

# Checks to see if the string has all unique characters using a Counter.
def isUnique(string):
    return all(value == 1 for value in Counter(string).values())

# Part 1
marker = -1

# Loops through the signal and checks if the next 4 characters are unique.
for index in range(len(signal)):
    if isUnique(signal[index: index+4]):
        marker = index + 4
        break

print(marker) # 1909

# Part 2
marker = -1

# Loops through the signal and checks if the next 4 characters are unique.
for index in range(len(signal)):
    if isUnique(signal[index: index+14]):
        marker = index + 14
        break

print(marker) # 3380