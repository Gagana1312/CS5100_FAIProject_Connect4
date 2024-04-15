from Minmax_Expectimax import minimax, expectimax
from Board import initialize_board, display_board, available_moves, execute_move, check_victory
import random

def game(opponent, algorithm):
    board = initialize_board()
    print("1234567")
    display_board(board)
    print()
    while True:
        if not available_moves(board):
            print("No winner!")
            break

        if opponent in ["RANDOM", "PLAYER"]:
            if opponent == "RANDOM":
                col = random.choice(available_moves(board))
            else:
                col = int(input("Which column (1 - 7)? ")) + 9  # Offset to match internal representation
            board, index = execute_move(board, 1, col)
            player_action = "Random" if opponent == "RANDOM" else "You"
            print(f"{player_action} chose column {index % 9}")
            display_board(board)
            if check_victory(board, 1, index):
                print(f"{player_action} Wins!")
                break

        if algorithm == "MINIMAX":
            _, index, board = minimax(board, -1, 5)
        elif algorithm == "EXPECTIMAX":
            _, index, board = expectimax(board, -1, 5)

        print(f"AI chose column {index % 9}")
        display_board(board)
        if check_victory(board, -1, index):
            print("AI Wins!")
            break
        
def game_ai_vs_ai(algorithm1, algorithm2):
    board = initialize_board()
    print("Starting AI vs AI match:")
    display_board(board)
    print()
    current_player = 1  # Start with AI using algorithm1
    while True:
        if not available_moves(board):
            print("No winner!")
            break

        if current_player == 1:
            _, index, board = algorithm1(board, current_player, 5)
            print("AI1 (using algorithm1) chose column", (index % 9) + 1)
        else:
            _, index, board = algorithm2(board, current_player, 5)
            print("AI2 (using algorithm2) chose column", (index % 9) + 1)

        display_board(board)
        print()

        if check_victory(board, current_player, index):
            print("AI" + ("1 Wins!" if current_player == 1 else "2 Wins!"))
            break

        current_player *= -1  # Switch players

# Mapping string inputs to actual function references
algorithm_map = {
    "MINIMAX": minimax,
    "EXPECTIMAX": expectimax
}

if __name__ == "__main__":
    while True:
        print("Game Menu:"+"\n1: Random value vs AI (Minimax)\n2: Challenge AI (Minimax)\n3: Random value vs AI (Expectimax)\n4: Challenge AI (Expectimax)")
        print("5: AI vs AI battle (Minimax or Expectimax)")
        print("6. Exit")
        game_selection = input("Choose your option (1-6): ")
        if game_selection == "1":
            game("RANDOM", "MINIMAX")
        elif game_selection == "2":
            game("PLAYER", "MINIMAX")
        elif game_selection == "3":
            game("RANDOM", "EXPECTIMAX")
        elif game_selection == "4":
            game("PLAYER", "EXPECTIMAX")
        elif game_selection == "5":
            ai_mode = input("Choose AI mode (Minimax or Expectimax): ").upper()
            if ai_mode not in algorithm_map:
                print("Invalid mode, returning to menu.")
                continue
            selected_algorithm = algorithm_map[ai_mode]
            game_ai_vs_ai(selected_algorithm, selected_algorithm)
        elif game_selection == "6":
            exit()
        else:
            print("Invalid selection, returning to menu.")
        