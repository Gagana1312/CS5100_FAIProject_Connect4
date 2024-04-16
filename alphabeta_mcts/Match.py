from GameState import GameState
import AlphaBeta
from MonteCarloTree import MCTSTree

class Match:
    def __init__(self, initial_board, player1, player2, first_player):
        self.player1 = player1
        self.player2 = player2
        self.initial_board = initial_board
        self.intial_state = GameState(initial_board, rows=6, cols=7, current_player_id=first_player)
        self.winner = 0

        functions = {
            'AB': self.alpha_beta,
            'MCTS': self.monte_carlo
        }

        self.player_1_function = functions[self.player1]
        self.player_2_function = functions[self.player2]

        self.run(self.intial_state)

    def alpha_beta(self, state):
        return AlphaBeta.get_action(state, state.current_player_id)

    def monte_carlo(self, state):
        return MCTSTree(state).runMCTS(state.current_player_id, max_t=5)

    def random_play(self, state):
        pass

    def run(self, state):
        while not state.is_terminal_state():
            if state.current_player_id == 1:
                next_action = self.player_1_function(state)
                print(self.player1 + " Player 1: played on " + str(next_action))
            else:
                next_action = self.player_2_function(state)
                print(self.player2 + " Player 2: played on " + str(next_action))
            if next_action not in state.actions:
                print("\n\nIncorrect action")
                continue

            state = state.take_action(next_action)
            state.print_state()

        if state.winner:
            print("Player {} has won".format(state.winner))
            self.winner = state.winner
        else:
            print("Its a draw!")