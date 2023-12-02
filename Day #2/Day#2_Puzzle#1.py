# Advent of Code 2023
# The first puzzle of the second day

# Returns list of hands
def game_to_hands(game: str):
    formatted_hands = []
    hands = game.split(';')
    for hand in hands:
        newhand = [0, 0, 0]
        hand_split = hand.split(',')
        for show in hand_split:
            show_split = show.strip().split(' ')
            if show_split[1] == 'red':
                newhand[0] = int(show_split[0])
            elif show_split[1] == 'green':
                newhand[1] = int(show_split[0])
            elif show_split[1] == 'blue':
                newhand[2] = int(show_split[0])
        formatted_hands.append(newhand)
    return formatted_hands


# Returns a game which consists of hands which are shows in RGB order
def line_to_game(line: str):
    game_split = line.split(':')
    game_id = int(game_split[0].strip().split(' ')[1])
    hands = game_to_hands(game_split[1])
    return game_id, hands


games = {}  # Each game consists of N hands -> each hand is a single bunch of RGB cubes that the elf shows

with open('Day#2_Puzzle#1_Input.txt') as input_file:
    for game_line in input_file:
        game_line = game_line.rstrip()
        game = line_to_game(game_line)
        games[game[0]] = game[1]

# Check if the elf is scamming us
loaded = [12, 13, 14]
sum41 = 0
for game_id in games:
    possible = True
    for hand in games[game_id]:
        if hand[0] > loaded[0] or hand[1] > loaded[1] or hand[2] > loaded[2]:
            possible = False
            break
    if possible:
        sum41 += game_id

print("Sum of IDs of the possible games is", sum41)
