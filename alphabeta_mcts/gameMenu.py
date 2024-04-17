from Match import Match

def display_difficulty_menu():
    print("Please select a difficulty level from the following options:-")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")



def display_menu(player):
    print("Game Menu")
    print("Play Connect 4")
    print(f"Player {player} Options:")
    print("1. Alpha Beta Pruning")
    print("2. Monte Carlo Tree Search")
    print("3. Expectimax")
    print("4. Minimax")
    print("5. Human")
    print("6. Exit")

def get_user_choice(player):
    while True:
        choice = input(f"Player {player}, enter your choice (1-6): ")
        if choice.isdigit() and 1 <= int(choice) <= 6:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def get_difficulty_choice():
    while True:
        choice = input(f"Please enter your choice between 1 to 3: ")
        if choice.isdigit() and 1 <= int(choice) <= 3:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def create_normal_board():
    board = [[0] * 7 for _ in range(6)]
    return board

def main():
    players = [1, 2]
    options = ['AB', 'MCTS', 'EXPECTIMAX', 'MINIMAX', 'HUMAN']
    player_choices = {}
    while True:
        for player in players:
            display_menu(player)
            player_choices[player] = get_user_choice(player)

            if player_choices[player] == 6:
                    print("Exiting the game...")
                    return
        
        print("Player 1 chose option", player_choices[1])
        print("Player 2 chose option", player_choices[2])


        difficulty_level = 1
        if((player_choices[1] != 5 and player_choices[2] == 5) or (player_choices[1] == 5 and player_choices[2] != 5)):
            display_difficulty_menu()
            difficulty_level = get_difficulty_choice()

        board = create_normal_board()
        player1 = options[player_choices[1]]
        player2 = options[player_choices[2]]
        match = Match(board, player1, player2, first_player=1)
        normal_winner = match.winner

        item = {
                    'player_1': player1,
                    'player_2': player2,
                    'winner': normal_winner,
                }

        print(item)

if __name__ == "__main__":
    main()



