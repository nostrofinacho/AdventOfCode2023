# Advent of Code
# The first puzzle of the sixth day
import math

with open('Day#6_Puzzle#1_Input.txt') as input_file:
    input_lines = input_file.readlines()
    times = [int(t) for t in input_lines[0].split(':')[1].split()]
    distances = [int(d) for d in input_lines[1].split(':')[1].rstrip().split()]
print("Times:", times)
print("Distances:", distances)

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


have_your_way_with_me = 1
for race_index in range(len(times)):
    time = times[race_index]
    distance = distances[race_index]
    button_time = get_minimal_button(time, distance)
    print("Minimal button time for t=" + str(time) + " d=" + str(distance) + " is " + str(button_time))
    have_your_way_with_me *= button_time[1] - button_time[0] + 1
print("There are totally " + str(have_your_way_with_me) + " ways to beat the record in every race.")
