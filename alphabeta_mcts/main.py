from Match import Match

def create_normal_board():
    board = [[0] * 7 for _ in range(6)]
    return board

def create_one_step_already_taken():
    """
       0 0 0 0 0 0 0
       0 0 0 0 0 0 0
       0 0 0 0 0 0 0
       0 0 0 0 0 0 0
       0 0 0 0 0 0 0
       2 0 0 0 0 0 0
    """
    board = [[0] * 7 for _ in range(6)]
    board[5][0] = 2
    return board

def create_board_biased_for_player_2():
    """
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 2 2 2 0 0
        0 0 1 2 1 0 0
        0 1 2 1 1 0 0
    """
    board = [[0] * 7 for _ in range(6)]
    board[5][1] = 1
    board[5][2] = 2
    board[5][3] = 1
    board[5][4] = 1
    board[4][2] = 1
    board[4][3] = 2
    board[4][4] = 1
    board[3][2] = 2
    board[3][3] = 2
    board[3][4] = 2
    return board


if __name__ == "__main__":
    players = ['AB', 'MCTS', 'EXPECTIMAX', 'MINIMAX']

    player_combinations = []

    for i in players:
        for j in players:
            if i != j:
                player_combinations.append([i, j])
                player_combinations.append([j, i])

    iterations = 3

    all_results = []

    for iter in range(iterations):
        results = []
        for combination in player_combinations:
            board = create_normal_board()
            player1 = combination[0]
            player2 = combination[1]
            match = Match(board, player1, player2, first_player=1)
            normal_winner = match.winner

            board = create_one_step_already_taken()
            player1 = combination[0]
            player2 = combination[1]
            match = Match(board, player1, player2, first_player=1)
            one_step_already_taken_winner = match.winner

            board = create_board_biased_for_player_2()
            player1 = combination[0]
            player2 = combination[1]
            match = Match(board, player1, player2, first_player=1)
            biased_for_player_2_winner = match.winner

            item = {
                'player_1': player1,
                'player_2': player2,
                'winner': normal_winner,
                'one_step_winner': one_step_already_taken_winner,
                'biased_winner': biased_for_player_2_winner
            }

            results.append(item)
        all_results.append(results)

    print(all_results)
