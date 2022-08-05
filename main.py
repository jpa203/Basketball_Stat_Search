from Player import Player

try:
    bball = open('bball.csv', 'r', encoding='utf-8-sig')
except FileNotFoundError:
    print("Error: File not found")
    exit(1)

file_content = bball.readlines()

bball.close()

my_players = []

for player in range(len(file_content)):
    player_data = file_content[player].split(',')
    my_player = Player(player_data[0], player_data[1], player_data[2],
                       player_data[3], player_data[4])
    my_players.append(my_player)

while True:
    try:
        user_input = input('Enter first and last name: ')
        result = user_input.split()
        first = result[0]
        last = result[1]

        for player in my_players:
            if player.first_name == first and player.last_name == last:
                print(player)
                break
        break
    except Exception:
        print("Player doesn't exist. Make sure name is entered correctly, separated by first and last name.")
