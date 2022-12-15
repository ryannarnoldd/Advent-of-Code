# Ryan Arnold - Advent 2022 - Day 1: Calorie Counting

# Read in the input file and create a list of calories
with open('1.txt') as f:
    lines = f.readlines()
carried_food = [int(line) if line != "\n" else 0 for line in lines]
    
# Calculate the calories for each elf.
calories = []
current_calories = 0
for food in carried_food:
    if food != 0:
        current_calories += food
    else:
        calories.append(current_calories)
        current_calories = 0

# Part 1
print(max(calories)) # 70116

# Part 2
calories.sort(reverse=True)
print(sum(calories[:3])) # 206582