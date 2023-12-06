# Advent of Code 2023
# The second puzzle of the fifth day of Christmas


def map_through_puzzle1(input: list, map: list[tuple]):
    output = []
    for input_num in input:
        length = len(output)
        for mapping in map:
            if mapping[1] <= input_num <= mapping[1] + mapping[2]:
                output.append(mapping[0] + input_num - mapping[1])
        if length == len(output):
            output.append(input_num)
    return output


def map_through(input: list, map: list[tuple]):
    print("\nMapping through")
    print(input, map)
    output = []
    for range in input:
        range_output = []
        for mapping in map:


            # If range is a subset of mapping
            if mapping[1] <= range[0] and range[0] + range[1] <= mapping[1] + mapping[2]:
                x = (range[0], range[1])
                range_output.append((mapping[0] - x[0] + mapping[1], x[1]))
            # If range encapsulates mapping
            # range (10, 3) mapping (11,2)
            elif range[0] <= mapping[1] and range[0] + range[1] >= mapping[1] + mapping[2]:
                x = (range[0], mapping[1] - range[0])
                range_output.append((mapping[0] - x[0] + mapping[1], x[1]))

                x = (mapping[1], mapping[2])
                range_output.append((mapping[0] - x[0] + mapping[1], x[1]))

                x = (mapping[1] + mapping[2], range[0] + range[1] - mapping[1] - mapping[2])
                range_output.append((mapping[0] - x[0] + mapping[1], x[1]))

            # If overlap
            # range (97, 3); mapping (50 98 2), (52 50 48)
            elif mapping[1] <= range[0] <= mapping[1] + mapping[2] or mapping[1] <= range[0] + range[1] <= mapping[1] + mapping[2]:
                x = (max(range[0], mapping[1]), min(range[0] + range[1] - range[0], mapping[1] + mapping[2] - range[0]))
                range_output.append((mapping[0] - x[0] + mapping[1], x[1]))


        # If no Matches
        if len(range_output) == 0:
            output.append(range)
        # Cover the lost ranges
        else:
            current_range = range
            for range_out in range_output:
                if current_range[0] < range_out[0]:
                    output.append((current_range[0], range_out[0] - current_range[0]))
                    current_range = (range_out[0] + range_out[1], current_range[1])
        output += range_output

    output = list(dict.fromkeys(output))
    output.sort(key=lambda x:x[0])
    output = [x for x in output if x[1] != 0]
    print("output")
    print(output)
    return output


seeds = []
artefacts = {}
maps = {}
with open('Day#5_Puzzle#2_Input_Example.txt') as input_file:
    map_builder = []
    start_building = False
    map_name = ""
    for input_line in input_file:
        input_line = input_line.rstrip()
        if input_line.startswith("seeds:"):
            seed_num_split = input_line.split(':')[1].split()
            seeds = [(int(seed_num_split[i]), int(seed_num_split[i+1])) for i in range(0, len(seed_num_split), 2)]
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
print(maps)
print("Starting..")
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

print(artefacts)

# Get the puzzle solution
print("Lowest location number that corresponds to initial seed number is", artefacts['location'][0][0])
