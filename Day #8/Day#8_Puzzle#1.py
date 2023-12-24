# Advent of Code
# The first puzzle of the eigth day


directions = ""
nodes = {}  # [(AAA, (BBB, CCC))]

with open('Day#8_Puzzle#1_Input.txt') as input_file:
    input_lines = input_file.readlines()
    directions = input_lines[0].rstrip()
    for line in input_lines[2:]:
        banana = line.rstrip().split(' = ')
        nodes[banana[0]] = tuple(banana[1][1:-1].split(', '))

##################################
# Navigate the Haunted Wasteland #
##################################

# Get to the starting position
current_position = 'AAA'
step_counter = 0
while current_position != 'ZZZ':
    for step in directions:
        current_position = nodes[current_position][step == 'R']
        step_counter += 1

print(str(step_counter) + " steps are required to reach ZZZ.")
