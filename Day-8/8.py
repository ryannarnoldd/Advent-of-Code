# Ryan Arnold - Advent 2022 - Day 8: Treetop Tree House

# Read in the input file into a list of directions.
with open('8.txt') as f:
    lines = f.readlines()

# Using a double list comprehension, convert the list of strings into a list of lists of integers.
trees = [[height for height in row.strip()] for row in lines]

# Finds the perimeter of the forest since the edges are always visible.
perimeter = 2*len(trees) + 2*(len(trees[0])-2)

scenic_trees = []

# Loop through each tree, skipping the edges, and check if it is visible.
# Find the max of each row and see if there is a max tree smaller than the current tree.
trees_visible = perimeter
for x in range(1, len(trees)-1):
    for y in range(1, len(trees[x])-1):
        tree_height = trees[x][y]

        # Finds the trees in each direction from the current tree.
        up = [trees[x-i][y] for i in range(1, x+1)]
        down = [trees[x+i][y] for i in range(1, len(trees)-x)]
        left = [trees[x][y-i] for i in range(1, y+1)]
        right = [trees[x][y+i] for i in range(1, len(trees[x])-y)]

        # If the max of any row is smaller than the current tree, it is visible.
        if max(left) < tree_height or max(right) < tree_height or max(up) < tree_height or max(down) < tree_height:
            trees_visible += 1

        # Starting score at one, it checks each row for the number of trees visible from the current tree.
        score = 1
        for check in (up, down, left, right):
            tracker = 0
            for i in range(len(check)):
                tracker += 1

                # If the current tree is taller than the current tree, there is no need to check the rest of the row.
                if check[i] >= tree_height:
                    break
    
            # Multiples the tracker by the number of trees visible from the current tree.
            score *= tracker

        # Adds the score to the list of scores. The max is the highest score possible.
        scenic_trees.append(score)

# Part 1
print(trees_visible)

# Part 2
print(max(scenic_trees))