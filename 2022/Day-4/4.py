# Ryan Arnold - Advent 2022 - Day 4: Camp Cleanup
from collections import Counter

# Read in the input file and create a tuples of the sections.
with open('4.txt') as f:
    lines = f.readlines()
sections = [tuple(line.strip().split(',')) for line in lines]

# Part 1
# Function to check if first is contained in second or vice versa.
def fully_contained(pair):
    # Split the pairs into tuples of ints. Then checks if the intervals are fully contained by comparing start and end points.
    first = tuple(map(int, pair[0].split('-')))
    second = tuple(map(int, pair[1].split('-')))
    return (first[0] >= second[0] and first[1] <= second[1]) or (first[0] <= second[0] and first[1] >= second[1])

# Finds the sum of conditions that are True (contained).
fully_contained = sum(1 for pair in sections if fully_contained(pair))

print(fully_contained) # 509

# Part 2
# Function to check if first overlaps the second or vice versa.
def overlapped(pair):
    # Split the pairs into tuples of ints. Then checks if the intervals overlap by comparing max and min.
    first = tuple(map(int, pair[0].split('-')))
    second = tuple(map(int, pair[1].split('-')))
    return max(first[0], second[0]) <= min(first[1], second[1])

# Finds the sum of conditions that are True (overlapped).
overlapped = sum(1 for pair in sections if overlapped(pair))

print(overlapped) # 870