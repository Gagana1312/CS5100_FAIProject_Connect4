
from Board import is_valid_location,get_next_open_row,drop_piece
import random

def evaluate_window(window, piece):
    opp_piece = 1 if piece == 2 else 2
    score = 0
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 51
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2
    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 4
    return score

def score_position(board, piece):
    score = 0
    # Center column preference
    center_array = [int(i) for i in list(zip(*board))[3]]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Horizontal
    for r in range(6):
        row_array = [int(i) for i in board[r]]
        for c in range(4):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

    # Vertical
    for c in range(7):
        col_array = [int(i) for i in list(zip(*board))[c]]
        for r in range(3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)

    # Positive diagonal
    for r in range(3, 6):
        for c in range(4):
            window = [board[r-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Negative diagonal
    for r in range(3):
        for c in range(4):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score



def winning_move(board, piece):
    for c in range(7 - 3):
        for r in range(6):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    for c in range(7):
        for r in range(6 - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    for c in range(7 - 3):
        for r in range(6 - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    for c in range(7 - 3):
        for r in range(3, 6):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
    return False

def minimax(board, depth, maximizingPlayer):
    valid_locations = [c for c in range(7) if is_valid_location(board, c)]
    is_terminal = winning_move(board, 1) or winning_move(board, 2) or len(valid_locations) == 0
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, 2):
                return (None, 1000000)
            elif winning_move(board, 1):
                return (None, -1000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, score_position(board, 2))
    if maximizingPlayer:
        value = float('-inf')
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = [r[:] for r in board]
            drop_piece(b_copy, row, col, 2)
            new_score = minimax(b_copy, depth - 1, False)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value
    else:  # Minimizing player
        value = float('inf')
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = [r[:] for r in board]
            drop_piece(b_copy, row, col, 1)
            new_score = minimax(b_copy, depth - 1, True)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value

def expectimax(board, depth, maximizingPlayer):
    valid_locations = [c for c in range(7) if is_valid_location(board, c)]
    is_terminal = winning_move(board, 1) or winning_move(board, 2) or len(valid_locations) == 0
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, 2):
                return (None, float('inf'))
            elif winning_move(board, 1):
                return (None, float('-inf'))
            else:
                return (None, 0)
        else:
            return (None, score_position(board, 2))
    if maximizingPlayer:
        value = float('-inf')
        column = valid_locations[0]
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = [row[:] for row in board]
            drop_piece(b_copy, row, col, 2)
            new_score = expectimax(b_copy, depth-1, False)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value
    else:
        avg_value = 0
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = [row[:] for row in board]
            drop_piece(b_copy, row, col, 1)
            new_score = expectimax(b_copy, depth-1, True)[1]
            avg_value += new_score / len(valid_locations)
        return None, avg_value
    
def print_board(board):
    for row in board:
        print(row)