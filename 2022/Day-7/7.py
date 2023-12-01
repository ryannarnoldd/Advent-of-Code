# Ryan Arnold - Advent 2022 - Day 7: No Space Left On Device

# Read in the input file into a list of commands.
with open('7.txt') as f:
    commands = f.read().splitlines()

# Removes the 'ls' and 'dir' commands and removes the '$ ' from the commands.
commands = [command.replace('$ ', '') for command in commands 
    if not command == '$ ls' and not command.startswith('dir')]

files = []
sizes = {}

# Loops through the lines and using a dictonary for file sizes, adds the size of the file to the parent directory.
for index, command in enumerate(commands):

    # If the command is 'cd ..' then pop the last directory from the list.
    if command.startswith('cd'):

        # If the command is 'cd ..' then pop the last directory from the list.
        if command.endswith('..'):
            files.pop()
        # If the command is 'cd <directory>' then append the directory to the list.
        else:
            files.append(index)        
            sizes[index] = 0  

    # Else, set the size of the file and compute the size of the parent directory.  
    else:    
        size = int(command.split(" ")[0])        
        for s in files:            
            sizes[s] += size
    
# Part 1
# Find sum of all files less than 100000 bytes.
part1_results = sum([sizes[s] for s in sizes if sizes[s] <= 100000])
print(part1_results)

# Part 2
# Find the smallest file that is greater than the entire directory minus 40000000 bytes.
target_size = sizes[0] - 40000000
part2_answer = min([sizes[i] for i in sizes if sizes[i] >= target_size])
print(part2_answer)