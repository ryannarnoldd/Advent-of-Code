# Ryan Arnold - Advent 2022 - Day 10: Cathode-Ray Tube

# Read in the input file and split the lines into a list of instructions.
with open("10.txt") as f:
    circuit = [line.strip() for line in f]

x = 1
cycle = 0
signal_strength = 0
x_register = {}
circuit_times = [20, 60, 100, 140, 180, 220]

# Everytime the cycle is updated, add the x value to the x register.
for instruct in circuit:
    
    # Increment the cycle and add the signal strength if the cycle is in the list.
    if instruct == 'noop':
        cycle += 1
        x_register[cycle] = x
        if cycle in circuit_times: 
            signal_strength += cycle * x

    # Increment the cycle (by one, then another one
    #   and add the signal strength if the cycle is in the list.
    else:
        cycle += 1
        x_register[cycle] = x
        if cycle in circuit_times:
            signal_strength += cycle * x

        cycle += 1
        x_register[cycle] = x
        if cycle in circuit_times:
            signal_strength += cycle * x
            x_register[cycle] = x
        
        # Increment the x value by the V.
        x += int(instruct.split(" ")[1])

# Part 1
print(signal_strength) # 14420

# Part 2
CRT_WIDTH = 40
CRT_HEIGHT = 6
cycle = 1

# Print the CRT. Go through every pixel and check if it is in the range of the x value.
for row in range(CRT_HEIGHT):
    for pixel_pos in range(CRT_WIDTH):

        # If the pixel is in the range of the x value, print a block.
        if x_register[cycle] - 1 <= pixel_pos <= x_register[cycle] + 1:
            pixel = '▓'
        else: pixel = '░'

        # Print the pixel and increment the cycle.
        print(pixel, end='')
        cycle += 1

    print() # RGLRBZAU
