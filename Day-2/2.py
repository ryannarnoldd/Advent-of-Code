# Ryan Arnold - Advent 2022 - Day 2: Rock Paper Scissors

# Create a dictionary of the shape scores and a dictionary of the results.
shape_scores = {'X': 1, 'Y': 2, 'Z': 3}

# Read in the input file and create a list of play moves, in the form of a tuple.
with open('2.txt') as f:
    lines = f.readlines()
strategy_guide = [tuple(line.strip().split(' '))  for line in lines]

# Part 1
part1_results = {
    ('A', 'Z'): 0, ('B', 'X'): 0, ('C', 'Y'): 0, # Lose
    ('A', 'X'): 3, ('B', 'Y'): 3, ('C', 'Z'): 3, # Draw
    ('A', 'Y'): 6, ('B', 'Z'): 6, ('C', 'X'): 6  # Win
}

# Calculate the scores for each round.
scores = [part1_results[round] + shape_scores[round[1]] for round in strategy_guide]

print(sum(scores)) # 12794

# Part 2
part2_results = {
    ('A', 'X'): 'Z', ('B', 'X'): 'X', ('C', 'X'): 'Y', # Lose
    ('A', 'Y'): 'X', ('B', 'Y'): 'Y', ('C', 'Y'): 'Z', # Draw
    ('A', 'Z'): 'Y', ('B', 'Z'): 'Z', ('C', 'Z'): 'X'  # Win
}

# Calculate the scores for each round.
total_score = 0
for round in strategy_guide:
    shape_chosen = part2_results[round]
    if round[1] == 'X':
        total_score += 0 + shape_scores[shape_chosen] # Lose
    elif round[1] == 'Y':
        total_score += 3 + shape_scores[shape_chosen] # Draw
    else:
        total_score += 6 + shape_scores[shape_chosen] # Win
    
print(total_score) # 14979


