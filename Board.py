# Board.py

def display_board(board):
    print("\n".join([board[start:start+7] for start in range(10, 63, 9)]))

def initialize_board():
    return "?" * 8 + "??......." * 6 + "?" * 10

def available_moves(board):
    valid_columns = []
    for col in range(10, 17):
        if board[col] == ".":
            valid_columns.append(col)
    return valid_columns

def execute_move(board, player, column):
    player_symbols = {1: "O", -1: "x"}
    position = column
    while board[position + 9] == ".":
        position += 9
    new_board = board[:position] + player_symbols[player] + board[position+1:]
    return new_board, position

def check_victory(board, player, position):
    player_symbols = {1: "O", -1: "x"}
    directions = [1, 8, 9, 10]
    for direction in directions:
        count = 1
        check_pos = position
        move_dir = direction
        for _ in range(4):  # Only need to check 4 additional places
            check_pos += move_dir
            if board[check_pos] == player_symbols[player]:
                count += 1
            else:
                if move_dir > 0:
                    move_dir = -direction
                    check_pos = position
                else:
                    break
        if count >= 4:
            return True
    return False
