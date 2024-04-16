import time
from MonteCarloNode import MCTSNode


class MCTSTree:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.root_node = MCTSNode(self.initial_state, children=[], parent=None)

    def best_move(self):
        children = self.root_node.children
        best_node = max(children, key=lambda child: child.total_value / child.node_visits)
        max_index = children.index(best_node)
        return self.initial_state.actions[max_index]

    def runMCTS(self, player_id, max_t):
        current_time = time.time()
        while time.time() - current_time < max_t:
            current_node = self.root_node
            while not current_node.state.is_terminal_state():
                if not current_node.children:
                    current_node = current_node.expand()
                    break
                else:
                    current_node = current_node.select()
            value = current_node.rollout(player_id)
            current_node.backpropagate(value)
        return self.best_move()
