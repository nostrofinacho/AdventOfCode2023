# Advent of Code
# The first puzzle of the eigth day
import math

directions = ""
nodes = {}  # [(AAA, (BBB, CCC))]

with open('Day#8_Puzzle#2_Input.txt') as input_file:
    input_lines = input_file.readlines()
    directions = input_lines[0].rstrip()
    for line in input_lines[2:]:
        banana = line.rstrip().split(' = ')
        nodes[banana[0]] = tuple(banana[1][1:-1].split(', '))

##################################
# Navigate the Haunted Wasteland #
##################################

# Does not work
# Get to the starting position
#current_positions = [node for node in nodes if node[-1] == 'A']
#step_counter = 0
#while [node[-1] for node in current_positions].count('Z') != len(current_positions):
#    for step in directions:
#        current_positions = [nodes[current_position][step == 'R'] for current_position in current_positions]
#    step_counter += 1

current_positions = [node for node in nodes if node[-1] == 'A']
step_counters = []

for current_position in current_positions:
    step_counter = 0
    while current_position[-1] != 'Z':
        for step in directions:
            current_position = nodes[current_position][step == 'R']
            step_counter += 1
    step_counters.append(step_counter)

# Produces 16449085039026865463698093 which is too many
print(str(math.prod(step_counters)) + " steps are required to reach final of the vinyl wasteland.")

# Finding the Least Common Multiple
lcm = 1
for steps in step_counters:
    lcm = math.lcm(lcm, steps)
print(str(lcm) + " steps are required to reach final of the vinyl wasteland.")

