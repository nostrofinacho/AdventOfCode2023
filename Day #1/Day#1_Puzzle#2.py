# Advent of Code
# The second puzzle of the first day

spelled_digits = ['colazero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
spelled_digits_reversed = ['alocorez', 'eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'nevs', 'thgie', 'enin']   # Where's the reverse? Thanks, now fuck off.
spelled_digits_max_length = len(max(spelled_digits))

calibration_sum = 0
with open('Day#1_Puzzle#2_Input.txt') as input_file:
    for calibration_line in input_file:
        calibration_line = calibration_line.rstrip()
        i = 0
        found = False
        while True:
            if calibration_line[i].isdigit():
                calibration_sum += int(calibration_line[i]) * 10
                break
            else:
                for weight, spelled_digit in enumerate(spelled_digits):
                    potential_spelled_digit = calibration_line[max(0, i - spelled_digits_max_length - 1): i+1]
                    if spelled_digit in potential_spelled_digit:
                        calibration_sum += weight * 10
                        found = True
                        break
                if found:
                    break
            i += 1

        j = -1
        found = False
        while True:
            if calibration_line[j].isdigit():
                calibration_sum += int(calibration_line[j])
                break
            else:
                for weight, spelled_digit in enumerate(spelled_digits):
                    if -j < spelled_digits_max_length:
                        potential_spelled_digit = calibration_line[j:]
                    else:
                        potential_spelled_digit = calibration_line[j:min(-1, j + spelled_digits_max_length + 1)] + calibration_line[min(-1, j + spelled_digits_max_length + 1)]
                    if spelled_digit in potential_spelled_digit:
                        calibration_sum += weight
                        found = True
                        break
                if found:
                    break
            j -= 1
print("Sum of all calibration values is", calibration_sum)
