# algorithms.py

from Board import get_valid_moves, make_move, goal_test

# Board spaces' weights for AI
move_matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 10, 20, 30, 20, 10, 0, 0,
               0, 10, 20, 30, 40, 30, 20, 10, 0,
               0, 20, 30, 40, 50, 40, 30, 20, 0,
               0, 20, 30, 40, 50, 40, 30, 20, 0,
               0, 10, 20, 30, 40, 30, 20, 10, 0,
               0, 0, 10, 20, 30, 20, 10, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0]

funcs = {1: max, -1: min}

def evaluate_board(board):
    score = 0
    for m in range(11, 61):
        if board[m] == "+":
            score += move_matrix[m]
        elif board[m] == "x":
            score -= move_matrix[m]
    return score

def minimax(board, player, depth):
    cols = get_valid_moves(board)
    if len(cols) == 0:
        return 0, -5, -5
    if depth == 0:
        return evaluate_board(board), -5, -5
    moves = []
    for c in cols:
        nm, index = make_move(board, player, c)
        if goal_test(nm, player, index):
            moves.append((100000 * player, index, nm))
        else:
            count = minimax(nm, -player, depth-1)[0]
            moves.append((count, index, nm))
    return funcs[player](moves)

def expectimax(board, player, depth):
    cols = get_valid_moves(board)
    if len(cols) == 0:
        return 0, -5, -5
    if depth == 0:
        return evaluate_board(board), -5, -5
    moves = []
    for c in cols:
        nm, index = make_move(board, player, c)
        if goal_test(nm, player, index):
            moves.append((100000 * player, index, nm))
        else:
            count = expectimax(nm, -player, depth-1)[0]
            if player == -1:
                moves.append((count, index, nm))
            else:
                moves.append((count / len(cols), index, nm))  # Expectimax average for chance nodes
    return funcs[player](moves)
