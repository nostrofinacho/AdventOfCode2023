# Advent of Code 2023
# The first puzzle of the fourth day

def calculate_points():
    for card_id in deck:
        points = 0
        card = deck[card_id]
        winning = card[0]
        gotten = card[1]
        for num in gotten:
            if num in winning:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        deck[card_id] = (winning, gotten, points)

deck = {}
with open('Day#4_Puzzle#1_Input.txt') as input_file:
    for input_line in input_file:
        card_line = input_line.rstrip()
        header_split = card_line.split(':')
        card_id = int(header_split[0].split()[1])
        winning_nums, gotten_nums = [[int(i) for i in n.strip().split()] for n in header_split[1].strip().split('|')]
        deck[card_id] = (winning_nums, gotten_nums)

calculate_points()
sum41 = 0
for card in deck.values():
    sum41 += card[2]

print("Total points:", sum41)
