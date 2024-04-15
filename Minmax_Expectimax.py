# # algorithms.py
from Board import available_moves, execute_move, check_victory

# Board spaces' weights for AI
scoring_grid = [0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 10, 20, 30, 20, 10, 0, 0,
               0, 10, 20, 30, 40, 30, 20, 10, 0,
               0, 20, 30, 40, 50, 40, 30, 20, 0,
               0, 20, 30, 40, 50, 40, 30, 20, 0,
               0, 10, 20, 30, 40, 30, 20, 10, 0,
               0, 0, 10, 20, 30, 20, 10, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0]

# Algorithm.py
from Board import available_moves, execute_move, check_victory

def minimax(board, player, depth):
    decision_funcs = {1: max, -1: min}

    moves = available_moves(board)
    if not moves:
        return 0, -1, -1
    if depth == 0:
        return sum(scoring_grid[m] if board[m] == "O" else -scoring_grid[m] for m in range(11, 61)), -1, -1
    results = []
    for move in moves:
        new_board, pos = execute_move(board, player, move)
        if check_victory(new_board, player, pos):
            return 100000 * player, pos, new_board
        score = minimax(new_board, -player, depth - 1)[0]
        results.append((score, pos, new_board))
    return decision_funcs[player](results)

def expectimax(board, player, depth):
    if depth == 0 or not available_moves(board):
        return evaluate_board(board), -1, board

    best_value = float('-inf') if player == -1 else float('inf')
    best_move = -1
    best_board = None

    for move in available_moves(board):
        new_board, index = execute_move(board, player, move)
        if check_victory(new_board, player, index):
            return (100000 * player, index, new_board) if player == -1 else (-100000 * player, index, new_board)

        score, _, _ = expectimax(new_board, -player, depth - 1)

        if player == -1:  # Maximizing player
            if score > best_value:
                best_value = score
                best_move = index
                best_board = new_board
        else:  # Minimizing player (chance node)
            if score < best_value:
                best_value = score
                best_move = index
                best_board = new_board

    return best_value, best_move, best_board

def evaluate_board(board):
    player_symbols = {1: "O", -1: "x"}
    return sum(scoring_grid[i] if board[i] == player_symbols[1] else -scoring_grid[i] if board[i] == player_symbols[-1] else 0 for i in range(11, 61))
