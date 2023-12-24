# Advent of Code
# The first puzzle of the seventh day
card_values = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
hand_size = 5


def hand_strenght(hand):
    # 7-FiveOfAKind, 6-FourOfAKind, 5-FulLHouse, 4-ThreeOfAKind, 3-TwoPairs, 2-SinglePair, 1-HighCard
    card_counts = [hand.count(card_value) for card_value in card_values]

    joker_count = card_counts[-1]
    card_counts = card_counts[:-1]
    card_counts_sorted = sorted(card_counts)

    if card_counts_sorted[-1] + joker_count == 5:
        return 7
    elif card_counts_sorted[-1] + joker_count == 4:
        return 6
    elif card_counts_sorted[-1] + card_counts_sorted[-2] + joker_count == 5:
        return 5
    elif card_counts_sorted[-1] + joker_count == 3:
        return 4
    elif card_counts_sorted[-1] + card_counts_sorted[-2] + joker_count == 4:
        return 3
    elif card_counts_sorted[-1] + joker_count == 2:
        return 2
    elif card_counts_sorted[-1] + joker_count == 1:
        return 1


def compare_hands(left, right):
    # Returns 'l' if the left is stronger, 'r' if the right
    left_strength, right_strength = hand_strenght(left), hand_strenght(right)

    if left_strength > right_strength:
        return 'l'
    elif right_strength > left_strength:
        return 'r'
    else:
        for i in range(hand_size):
            if left[i] == right[i]:
                continue
            if card_values.index(left[i]) < card_values.index(right[i]):
                return 'l'
            else:
                return 'r'


the_whole_thing = []    # [[hand, bid, rank], [hand, bid, rank]]
with open('Day#7_Puzzle#2_Input.txt') as input_file:
    input_lines = input_file.readlines()
    for input_line in input_lines:
        banana = input_line.split()
        the_whole_thing.append([banana[0], int(banana[1]), 0])

print(the_whole_thing)

# Calculate ranks
for i in range(len(the_whole_thing)):
    for j in range(len(the_whole_thing)):

        # Compare yourself only to others!
        if i == j:
            continue

        # Got to the current end of the ranked cards -> stop evaluating
        if the_whole_thing[j][2] == 0:
            if i == 0:
                the_whole_thing[0][2] = 0   # Set the rank for the first hand
            break

        # Hand comparison
        # Bump up the better card, or bump down the worse one
        if compare_hands(the_whole_thing[i][0], the_whole_thing[j][0]) == 'l':
            the_whole_thing[i][2] += 1
        else:
            the_whole_thing[j][2] += 1

    the_whole_thing[i][2] += 1  # Offset from zero

# Solution is saved in the whole thing, print it out
print(the_whole_thing)
print("Total winnings sums up to", sum([hand[1] * hand[2] for hand in the_whole_thing]))
print(sorted(the_whole_thing, key=lambda x: x[2]))
