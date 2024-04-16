import re

class GameState:
    def __init__(self, board, rows, cols, current_player_id):
        self.board = board
        self.current_player_id = current_player_id
        self.num_rows = rows
        self.num_cols = cols
        self.actions = self.possible_moves()
        self.winner = self.winner()

    def print_state(self):
        print("------CONNECT 4------\n")
        for row in self.board:
            print(row)
        if self.winner:
            print("Winner -> {}".format(self.winner))
        print("\n")

    def evaluate(self):
        player_pattern = r"0|2"
        opponent_pattern = r"0|1"

        board_str = "".join("".join(map(str, row)) for row in self.board)

        possible_win_comb = len(re.findall(player_pattern * 4, board_str))
        possible_win_comb_opp = len(re.findall(opponent_pattern * 4, board_str))

        return possible_win_comb - possible_win_comb_opp

    def utility_ab(self, player):
        if not self.winner:
            return 0
        if self.winner == player:
            return float("inf")
        else:
            return float("-inf")

    def utility_mcts(self, player):
        if not self.winner:
            return 0
        if self.winner == player:
            return 1
        else:
            return -1

    def is_terminal_state(self):
        if self.winner:
            return True
        if not self.has_actions():
            return True
        return False

    def has_actions(self):
        if len(self.actions) > 0:
            return True
        else:
            return False

    def take_action(self, action):
        if self.is_terminal_state():
            return None

        new_board = [row[:] for row in self.board]
        column_indx = (action - 1)
        row_indx = 0

        for row in range(len(new_board) - 1, -1, -1):
            if new_board[row][column_indx] == 0:
                row_indx = row
                break

        if row_indx is not None:
            new_board[row_indx][column_indx] = self.current_player_id

        next_player = self.next_player()
        return GameState(new_board, self.num_rows, self.num_cols, next_player)

    def next_player(self):
        if self.current_player_id == 1:
            return 2
        else:
            return 1

    def possible_moves(self):
        actions = []

        for col in range(self.num_cols):
            for row in range(self.num_rows - 1, -1, -1):
                if self.board[row][col] == 0:
                    actions.append(col + 1)
                    break

        return actions

    def winner(self):
        pattern_cols = [[1] * 4, [2] * 4]
        pattern_rows = [[1] * 4, [2] * 4]
        pattern_diag1 = [[1] * 4, [2] * 4]
        pattern_diag2 = [[1] * 4, [2] * 4]

        for pattern in pattern_cols + pattern_rows + pattern_diag1 + pattern_diag2:
            if self.has_pattern(pattern):
                return pattern[0]

        return 0

    def has_pattern(self, pattern):
        rows = len(self.board)
        cols = len(self.board[0])

        for i in range(rows):
            for j in range(cols - len(pattern) + 1):
                if self.board[i][j:j + len(pattern)] == pattern:
                    return True

        for j in range(cols):
            for i in range(rows - len(pattern) + 1):
                if [self.board[x][j] for x in range(i, i + len(pattern))] == pattern:
                    return True

        for i in range(rows - len(pattern) + 1):
            for j in range(cols - len(pattern) + 1):
                if [self.board[i + x][j + x] for x in range(len(pattern))] == pattern:
                    return True

        for i in range(rows - len(pattern) + 1):
            for j in range(len(pattern) - 1, cols):
                if [self.board[i + x][j - x] for x in range(len(pattern))] == pattern:
                    return True

        return False

