ACTIONS = {
    'add': 'Add players',
    'players': 'Display players and scores',
    'points': 'Manage points',
    'end': 'End the game'
}

players = {}

while True:
    print("\n*-~ ScoreKeeper V.0.1 ~-*\n")
    for action, description in ACTIONS.items():
        print(f"'{action}' - {description}")

    option = input("\nEnter your option: ")

    if option == "add":
        num_players = int(input("Enter the number of players: "))
        for i in range(num_players):
            player_name = input(f"Enter the name of player {i + 1}: ")
            if player_name in players:
                print(f"Player {player_name} already exists.")
            else:
                players[player_name] = 0
                print(f"Player {player_name} added!")

    elif option == "players":
        print("\nCurrent Scores:\n")
        for player, points in players.items():
            print(f"{player}: {points} points")

    elif option == "points":
        player_name = input("Enter the name of the player who scored: ")
        if player_name not in players:
            print(f"Player {player_name} not found!\nPlease enter a correct player name.")
        else:
            points_scored = int(input(f"How many points did player {player_name} score: "))
            players[player_name] += points_scored

    elif option == "end":
        print("\nThank you for playing! Here's the summary: \n")
        for player, points in players.items():
            print(f"{player}: {points} points")
        best_player = max(players, key=players.get)
        print(f"\nThe player who scored the most points is: {best_player}")
        break

    else:
        print("\nInvalid option. Please try again.")