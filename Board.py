
players = {1: "+", -1: "x"}     # One player is +, other is x

def board(board):
    print(" ".join(board[10:17]) + "\n" +
          " ".join(board[19:26]) + "\n" +
          " ".join(board[28:35]) + "\n" +
          " ".join(board[37:44]) + "\n" +
          " ".join(board[46:53]) + "\n" +
          " ".join(board[55:62]) + "\n")

def start_board():
    return "?" * 8 + "??0000000" * 6 + "?" * 10

def get_valid_moves(board):
    cols = []
    for c in range(10, 17):
        if board[c] == "0":
            cols.append(c)
    return cols

def make_move(board, player, col):
    index = col
    while board[index + 9] == "0":
        index += 9
    return board[:index] + players[player] + board[index + 1:], index

def goal_test(board, player, index):
    dirs = [1, 8, 9, 10]
    for nd in dirs:
        d = nd
        temp = index
        line = 1
        for i in range(5):
            temp += d
            line += 1
            if board[temp] != players[player]:
                line -= 1
                if d > 0:
                    d *= -1
                    temp = index
                else:
                    break
        if line >= 4:
            return True
    return False
