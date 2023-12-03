# Advent of Code 2023
# The second puzzle of the third day

EMPTY_CHARACTER = '.'
SCHEMA = []
pins = []   # Part Identification Numbers -> Consist of the (Integer ID, (row_number, column_number_of_last_digit), ID_length)
gears_of_war = {}   # List of all gears -> includes both true gears (adjacent to EXACTLY two part numbers) and faux gears -> {(gear_row, gear_column)=>(pin0, pin1)}


def is_part_number(pin, update_gears=False):
    pin_row = pin[1][0]
    pin_column = pin[1][1]
    pin_length = pin[2]

    parameter_row_indices = [i for i in range(pin_row-1, pin_row+1+1) if 0 <= i < len(SCHEMA)]
    parameter_column_indices = [j for j in range(pin_column-pin_length, pin_column+1+1) if 0 <= j < len(SCHEMA[0])]

    is_gear = False
    adjacent_gears = []
    for i in parameter_row_indices:
        for j in parameter_column_indices:
            if SCHEMA[i][j] == '*':
                adjacent_gears.append((i, j))
            if not (SCHEMA[i][j].isdigit() or SCHEMA[i][j] == EMPTY_CHARACTER):
                is_gear = True

    if update_gears:
        for gear in adjacent_gears:
            if gear in gears_of_war:
                gears_of_war[gear].add(pin)
            else:
                gears_of_war[gear] = {pin}
    return is_gear


with open('Day#3_Puzzle#2_Input.txt') as file_input:
    for line_number, input_line in enumerate(file_input):
        schema_line = input_line.rstrip()
        SCHEMA.append(schema_line)

        current_number = []
        for i in range(len(schema_line)):
            if schema_line[i].isdigit():
                current_number.append(schema_line[i])
            elif len(current_number) != 0:
                pins.append((int(''.join(current_number)), (line_number, i-1), len(current_number)))
                current_number = []

            # Cover the end-of-line case
            if i == len(schema_line) - 1 and len(current_number) != 0:
                pins.append((int(''.join(current_number)), (line_number, i-1), len(current_number)))
                current_number = []

sum41 = 0
# Check for the PINs and update the gearlist
for pin in pins:
    is_part_number(pin, True)

# Calculate gear ratios
for gear in gears_of_war:
    # Faux gear filter (not exactly two PINs adjacent)
    if len(gears_of_war[gear]) != 2:
        continue
    else:
        gear_ratio = 1
        for part in gears_of_war[gear]:
            gear_ratio *= part[0]
        sum41 += gear_ratio
print("Sum of all the gear ratios in the engine schematic is", sum41)
