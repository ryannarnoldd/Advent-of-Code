# Ryan Arnold - Advent 2022 - Day 9: Rope Bridge
import numpy as np

# Read in the input file and split the lines into a list of tuples (direction, number).
with open("9.txt") as f:
    motions = [tuple(line.strip().split(" ")) for line in f]

# Convert the number to an integer.
motions = [(motion[0], int(motion[1])) for motion in motions]

# Update the tail position based on the difference between the head and tail.
def update_tail(head, tail):
    difference = head - tail
    change = {
        (2, 1):(1, 1), (1, 2):(1, 1), (2, 0):(1, 0), (2, -1):(1, -1),
        (1, -2):(1, -1), (0, -2):(0, -1), (-1, -2):(-1,-1), (-2, -1):(-1, -1),
        (-2, 0):(-1, 0), (-2, 1):(-1, 1), (-1, 2):(-1, 1), (0, 2):(0, 1), 
        (2, 2):(1, 1), (-2, -2):(-1, -1), (-2, 2):(-1, 1), (2, -2):(1, -1)
    }

    # The new tail position is the old tail position plus the change for the tail.
    new_tail = tail + np.array(change.get(tuple(difference), (0,0)))
    return new_tail

# Update the head position based on the direction, just by adding or subtracting 1.
def update_head(head, direction):
    if direction == 'U':
        head[0] += 1
    elif direction == 'D':
        head[0] -= 1
    elif direction == 'L':
        head[1] -= 1
    elif direction == 'R':
        head[1] += 1
    return head

# Simulate the motion of the rope and return the number of visited positions.
# n is the number of knots in the rope.
def simulate_motion(n):
    rope = [np.array([0,0]) for _ in range(n)]
    visited = set([tuple(rope[-1])])

    # For each motion, update the head and tail positions, for each distance in the motion.
    for motion in motions:
        direction = motion[0]
        distance = motion[1]
        while distance > 0:
            rope[0] = update_head(rope[0], direction)
            distance -= 1

            # Go through each knot in the rope and update the tail position.
            for i in range(1, len(rope)):
                rope[i] = update_tail(rope[i-1], rope[i])
            visited.add(tuple(rope[-1]))
    return len(visited)

# Part 1
print(simulate_motion(2))

# Part 2
print(simulate_motion(10))


