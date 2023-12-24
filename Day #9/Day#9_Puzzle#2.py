# Advent of Code
# The first puzzle of the ninth day

def difference_sequence(input_sequence):
    dif_seq = []
    for i in range(len(input_sequence)-1):
        dif_seq.append(input_sequence[i+1] - input_sequence[i])
    return dif_seq


def print_histria():
    for history in histria:
        for space_num, seq in enumerate(history):
            print(space_num * 2 * ' ', seq)
        print()
    print("\n" + '-' * 30 + "\n")


#########
# INPUT #
#########
histria = []
with open('Day#9_Puzzle#2_Input_Example.txt') as input_file:
    input_lines = input_file.readlines()
    for line in input_lines:
        histria.append([[int(num) for num in line.rstrip().split()]])
print_histria()


#####################################
# Calculate and display differences #
#####################################
for history in histria:
    sequence = history[0]
    while sequence.count(0) != len(sequence):
        history.append(difference_sequence(sequence))
        sequence = history[-1]
print_histria()


###############
# Extrapolate #
###############
for history in histria:
    # Sneak up from behind
    history[-1].insert(0, 0)

    for i in range(len(history)-2, -1, -1):
        sequence = history[i]
        sequence.insert(0, sequence[0] - history[i+1][0])
print_histria()


###########################################
# Sum the Xtrapolated values for solution #
###########################################
print("Sum of the back-in-time Xtrapolated values is", sum([history[0][0] for history in histria]))
