from GameState import GameState
import AlphaBeta
from MonteCarloTree import MCTSTree
import Minmax_Expectimax
import sys
import random

class Match:
    def __init__(self, initial_board, player1, player2, first_player, difficulty=None):
        self.player1 = player1
        self.player2 = player2
        self.initial_board = initial_board
        self.intial_state = GameState(initial_board, rows=6, cols=7, current_player_id=first_player)
        self.winner = 0
        self.difficulty = difficulty

        functions = {
            'AB': self.alpha_beta,
            'MCTS': self.monte_carlo,
            'MINIMAX': self.minimax,
            'EXPECTIMAX': self.expectimax,
            'HUMAN': self.human
        }

        if player1 != 'HUMAN' and player2 != 'HUMAN':
            self.difficulty = None

        self.player_1_function = functions[self.player1]
        self.player_2_function = functions[self.player2]

        print("Game difficulty is {}".format(self.difficulty))

        if self.difficulty is not None:
            # Easy difficulty
            if self.difficulty == 1:
                self.diff_possible_decisions = [1, 2]
                self.diff_probability = [0.25, 0.75]
            # Medium difficulty
            elif self.difficulty == 2:
                self.diff_possible_decisions = [1, 2]
                self.diff_probability = [0.125, 0.875]
            # Hard difficulty
            else:
                self.diff_possible_decisions = [2]
                self.diff_probability = [1]

        self.run(self.intial_state)

    def generate_difficulty_based_choice(self):
        if self.difficulty is not None:
            val = random.choices(self.diff_possible_decisions, weights=self.diff_probability, k=1)
            return val[0]
        else:
            return 2

    def alpha_beta(self, state):
        choose = self.generate_difficulty_based_choice()
        if choose == 1:
            print("******Now making a bad decision******")
            return random.choice(state.actions)
        return AlphaBeta.get_action(state, state.current_player_id)

    def monte_carlo(self, state):
        choose = self.generate_difficulty_based_choice()
        if choose == 1:
            print("******Now making a bad decision******")
            return random.choice(state.actions)
        return MCTSTree(state).runMCTS(state.current_player_id, max_t=5)

    def random_play(self, state):
        return random.choice(state.actions)

    def minimax(self, state):
        choose = self.generate_difficulty_based_choice()
        if choose == 1:
            print("******Now making a bad decision******")
            return random.choice(state.actions)
        col, _ = Minmax_Expectimax.minimax(state.board, 4, True)
        return col + 1

    def expectimax(self, state):
        choose = self.generate_difficulty_based_choice()
        if choose == 1:
            print("******Now making a bad decision******")
            return random.choice(state.actions)
        col, _ = Minmax_Expectimax.expectimax(state.board, 4, True)
        return col + 1

    def human(self, state):
        int_input = False
        action = None
        while not int_input:
            try:
                action = int(input("Play your turn. It has to be between 1 and 7. Enter 0 to stop!"))
                if action == 0:
                    print("\nHuman gave up!")
                    sys.exit()
                int_input = True
            except ValueError:
                print("Please enter a number between 1 and 7.")
                continue
            return action

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