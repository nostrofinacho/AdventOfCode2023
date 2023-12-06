# Advent of Code
# The first puzzle of the sixth day
import math

with open('Day#6_Puzzle#2_Input.txt') as input_file:
    input_lines = input_file.readlines()
    time = int(input_lines[0].split(':')[1].rstrip().replace(' ', ''))
    distance = int(input_lines[1].split(':')[1].rstrip().replace(' ', ''))
print("Time:", time)
print("Distance:", distance)

# Formula for minimal button holding to win the race
# b + d/b <= t
# b*b + d - tb <= 0
# b*b -t*b + d <= 0


def get_minimal_button(t, d):
    f = -t
    a = (-f-math.sqrt((f*f)-(4*d)))/2
    b = (-f+math.sqrt((f*f)-(4*d)))/2

    if get_distance(a, t) == d:
        a += 0.0000000001
    if get_distance(b, t) == d:
        b -= 0.0000000001
    return math.ceil(a), math.floor(b)


def get_distance(b, t):
    return b*0 + (t-b)*b


button_time = get_minimal_button(time, distance)
print("There is totally " + str(button_time[1]-button_time[0]+1) + " number of ways to beat the record in this tiresome race.")
