# Ryan Arnold - Advent 2022 - Day 11: Monkey in the Middle
from math import floor
from copy import deepcopy

# Read in the input file and split the lines into a list of monkeys.
with open("11.txt") as f:
    data = f.read().split('\n\n')

# Split the monkeys into a list of monkeys with a dictionary of their info.
monkeys_info = [line.split('\n') for line in data]
monkeys_info =  [[info.strip() for info in monkey] for monkey in monkeys_info]
divided = True
first_monkeys = {}
mod = 1

# Create a dictionary for each monkey with their info.
for index, line in enumerate(monkeys_info):
    first_monkeys[index] = {
        'items': [int(x) for x in line[1].split(': ')[1].split(', ')],
        'operation': line[2].split('= ')[1],
        'test': int(line[3].split('by ')[1]),
        'true': int(line[4].split('monkey ')[1]),
        'false': int(line[5].split('monkey ')[1]),
        'inspected': 0
    }

    # Get the mod value for part 2.
    mod *= int(first_monkeys[index]['test'])

# Copy the first monkeys to the second monkeys.
second_monkeys = deepcopy(first_monkeys)

# Function to run the monkey business, return the number of items inspected of top TWO.
def monkey_business(monkeys, rounds=20, divided=True):
    for rounds in range(rounds):
        for _, monkey in monkeys.items():
            for _ in range(len(monkey['items'])):   
                monkey['inspected'] += 1
                old = monkey['items'][0]

                # If first round, divide by 3, else mod by the mod value.
                if divided:
                    new = floor(eval(monkey['operation'])/3) 
                else: 
                    new = eval(monkey['operation']) % mod

                monkey['items'][0] = new

                # Check if the new item is divisible by the test value and give it to the correct monkey.
                if new % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(new)
                    monkey['items'].pop(0)
                else:
                    monkeys[monkey['false']]['items'].append(new)
                    monkey['items'].pop(0)
    
    # Sort the list by ['inspected'] and return the product of the top two.
    sorted_monkeys = list(sorted(monkeys.items(), key=lambda m: m[1]['inspected'], reverse=True))
    monkey_business = sorted_monkeys[0][1]['inspected'] * sorted_monkeys[1][1]['inspected']
    return monkey_business

# Part 1
print(monkey_business(first_monkeys)) # 78960

# Part 2
print(monkey_business(second_monkeys, rounds=10000, divided=False)) # 14561971968