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


def inverse_map(input, map):
    for mapping in map:
        if mapping[0] <= input < mapping[0] + mapping[2]:
            return mapping[1] - mapping[0] + input

    return input


seeds = []
artefacts = {}
maps = {}
with open('Day#5_Puzzle#2_Input.txt') as input_file:
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

location = 0
seed_found = False
while True:
    humidity = inverse_map(location, maps['humidity-to-location'])
    temperature = inverse_map(humidity, maps['temperature-to-humidity'])
    light = inverse_map(temperature, maps['light-to-temperature'])
    water = inverse_map(light, maps['water-to-light'])
    fertilizer = inverse_map(water, maps['fertilizer-to-water'])
    soil = inverse_map(fertilizer, maps['soil-to-fertilizer'])
    seed_faux = inverse_map(soil, maps['seed-to-soil'])

    # Check if seed exists
    for seed_range in seeds:
        if seed_range[0] <= seed_faux < seed_range[0] + seed_range[1]:
            print("Found the seed " + str(seed_faux) + " for location " + str(location))
            seed_found = True
    if seed_found:
        break
    else:
        location += 1
if not seed_found:
    print("Did not find a solution")
# Solution save Found the seed 1055427336 for location 99751240
