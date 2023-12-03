# Advent of Code 2023
# The first puzzle of the third day

EMPTY_CHARACTER = '.'
SCHEMA = []
pins = []   # Part Identification Numbers -> Consist of the (Integer ID, (row_number, column_number_of_last_digit), ID_length)


def is_part_number(pin):
    pin_row = pin[1][0]
    pin_column = pin[1][1]
    pin_length = pin[2]

    parameter_row_indices = [i for i in range(pin_row-1, pin_row+1+1) if 0 <= i < len(SCHEMA)]
    parameter_column_indices = [j for j in range(pin_column-pin_length, pin_column+1+1) if 0 <= j < len(SCHEMA[0])]

    for i in parameter_row_indices:
        for j in parameter_column_indices:
            if not (SCHEMA[i][j].isdigit() or SCHEMA[i][j] == EMPTY_CHARACTER):
                return True
    return False


with open('Day#3_Puzzle#1_Input.txt') as file_input:
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
for pin in pins:
    if is_part_number(pin):
        sum41 += pin[0]
print("Sum of all of the part numbers in the engine schematic is", sum41)
