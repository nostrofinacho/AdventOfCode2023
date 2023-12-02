# Advent of Code
# The first puzzle of the first day

calibration_sum = 0
with open('Day#1_Puzzle#1_Input.txt') as input_file:
    for calibration_line in input_file:
        calibration_line = calibration_line.rstrip()
        i, j = 0, -1
        while True:
            if calibration_line[i].isdigit():
                calibration_sum += int(calibration_line[i]) * 10
                break
            i += 1
        while True:
            if calibration_line[j].isdigit():
                calibration_sum += int(calibration_line[j])
                break
            j -= 1
print("Sum of all calibration values is", calibration_sum)
