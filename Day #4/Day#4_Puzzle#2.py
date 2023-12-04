# Advent of Code 2023
# The first puzzle of the fourth day

def evaluate_deck():
    for card_id in range(1, len(deck)+1):
        card = deck[card_id]
        matches = set(card[0]) & set(card[1])
        for id in range(card_id+1, card_id+len(matches)+1, 1):
            deck[id] = (deck[id][0], deck[id][1], deck[id][2]+card[2])

deck = {}
with open('Day#4_Puzzle#2_Input.txt') as input_file:
    for input_line in input_file:
        card_line = input_line.rstrip()
        header_split = card_line.split(':')
        card_id = int(header_split[0].split()[1])
        winning_nums, gotten_nums = [[int(i) for i in n.strip().split()] for n in header_split[1].strip().split('|')]
        deck[card_id] = (winning_nums, gotten_nums, 1)

evaluate_deck()

sum41 = 0
for card in deck.values():
    sum41 += card[2]

print("Ended up with " + str(sum41) + " scratchcards.")
