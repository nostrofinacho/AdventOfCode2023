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

with open('Day#2_Puzzle#2_Input.txt') as input_file:
    for game_line in input_file:
        game_line = game_line.rstrip()
        game = line_to_game(game_line)
        games[game[0]] = game[1]

transposed_games = {}
for game_id in games:
    game = games[game_id]
    reds = [game[i][0] for i in range(len(game))]
    greens = [game[i][1] for i in range(len(game))]
    blues = [game[i][2] for i in range(len(game))]
    transposed_games[game_id] = [reds, greens, blues]

power_level = 0
for game in transposed_games.values():
    power_level += max(game[0]) * max(game[1]) * max(game[2])

print("Scouter says the power level is", power_level)
