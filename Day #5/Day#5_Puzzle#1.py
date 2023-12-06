# Advent of Code 2023
# The first puzzle of the fifth day of Christmas

def map_through(input: list, map: list[tuple]):
    output = []
    for input_num in input:
        length = len(output)
        for mapping in map:
            if mapping[1] <= input_num <= mapping[1] + mapping[2]:
                output.append(mapping[0] + input_num - mapping[1])
        if length == len(output):
            output.append(input_num)
    return output


seeds = []
artefacts = {}
maps = {}
with open('Day#5_Puzzle#1_Input.txt') as input_file:
    map_builder = []
    start_building = False
    map_name = ""
    for input_line in input_file:
        input_line = input_line.rstrip()
        if input_line.startswith("seeds:"):
            seeds = [int(seed) for seed in input_line.split(':')[1].split()]
            artefacts['seed'] = seeds
        elif len(input_line) == 0:
            map_builder = []
            start_building = True
        elif start_building:
            start_building = False
            map_name = input_line.split()[0]
            maps[map_name] = []
            artefacts[map_name.split('-')[2]] = []
        else:
            maps[map_name].append(tuple([int(num) for num in input_line.split()]))
print(artefacts)


for artefact in artefacts:
    # Pick a map to transform further
    picked_map = [map_name for map_name in maps.keys() if map_name.split('-')[0] == artefact]

    # If futher mapping does not exist -> stop
    if len(picked_map) == 0:
        break
    picked_map = picked_map[0]
    map_name_split = picked_map.split('-')
    artefact_from, artefact_to = map_name_split[0], map_name_split[2]

    # Map
    artefacts[artefact_to] = (map_through(artefacts[artefact_from], maps[picked_map]))

print(artefacts)

# Get the puzzle solution
print("Lowest location number that corresponds to initial seed number is", min(artefacts['location']))
