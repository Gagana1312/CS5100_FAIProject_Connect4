

from Board import create_normal_board, is_valid_location, drop_piece, get_next_open_row
from Minmax_Expectimax import winning_move, minimax, expectimax, evaluate_window,print_board

def play_game(ai_depth, game_mode):
    board = create_normal_board()
    game_over = False
    turn = 0  # 0 for player, 1 for AI
    print_board(board)
    while not game_over:
        if turn == 0:
            valid_choice = False
            while not valid_choice:
                try:
                    col = int(input("Player 1 Make your Selection (1-7): ")) - 1
                    if 0 <= col <= 6 and is_valid_location(board, col):
                        valid_choice = True
                    else:
                        print("Invalid selection. Please choose a number between 1 and 7.")
                except ValueError:
                    print("Invalid selection.")
                    break
            
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("Player 1 wins!")
                game_over = True
            print_board(board)

        else:
            if game_mode == 'minimax':
                print("AI (Minimax) chance...")
                col, minimax_score = minimax(board, ai_depth, -float('inf'), float('inf'), True)
            elif game_mode == 'expectimax':
                print("AI (Expectimax) chance...")
                col, expectimax_score = expectimax(board, ai_depth, True)

            if col is not None and is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
                print(f"AI has dropped a piece in column {col+1}")

                if winning_move(board, 2):
                    print(f"Player 2 (AI using {game_mode}) wins!")
                    game_over = True
            else:
                print("No valid moves for AI. It's a draw.")
            print_board(board)

        turn += 1
        turn = turn % 2

play_game(ai_depth=4, game_mode='minimax')  
#play_game(ai_depth=4, game_mode='expectimax') 
