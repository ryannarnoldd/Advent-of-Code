# Ryan Arnold - Advent 2022 - Day 3: Rucksack Reorganization

priority_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Read in the input file and create a list of items.
with open('3.txt') as f:
    lines = f.readlines()
items = [line.strip() for line in lines]

# Part 1
items_halved = [(item[:len(item)//2], item[len(item)//2:] ) for item in items]

# Calculate the priority of each item and add it to a sum.
priority_sum = 0
for item in items_halved:
    # Find the common character by taking the intersection of the two sets.
    common = set(item[0]) & set(item[1])
    priority_sum += priority_string.index(common.pop()) + 1

print(priority_sum) # 7553

# Part 2

# Combine every 3 items into a list, intersecting the sets to find the common character.
badges = [set.intersection(*map(set, items[i:i+3])) for i in range(0, len(items), 3)]
sum_of_badges = sum(priority_string.index(badge.pop()) + 1 for badge in badges)

print(sum_of_badges) # 2758