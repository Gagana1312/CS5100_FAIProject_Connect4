import math
import copy
import random


def upper_confidence_bound(terminal_val, parent_visits, node_visits):
    if node_visits is None or node_visits == 0:
        return float('inf')
    return terminal_val / node_visits + 2 * math.sqrt(2 * math.log(parent_visits) / node_visits)


class MCTSNode:
    def __init__(self, state, children=[], parent=None):
        self.node_visits = 0
        self.total_value = 0
        self.parent = parent
        self.children = children
        self.state = state

    def rollout(self, player_id):
        state = copy.deepcopy(self.state)
        while True:
            if state.is_terminal_state():
                return state.utility_mcts(player_id)
            state = state.take_action(random.choice(state.actions))

    def backpropagate(self, value):
        self.node_visits += 1
        self.total_value += value
        if self.parent:
            self.parent.backpropagate(value)

    def select(self):
        return max(self.children, key=lambda child: upper_confidence_bound(
            child.total_value, self.node_visits, child.node_visits))

    def expand(self):
        actions = copy.deepcopy(self.state.actions)
        self.children = [self.create_child(a) for a in actions]
        return self.children[0]

    def create_child(self, action):
        return MCTSNode(self.state.take_action(action), [], self)
