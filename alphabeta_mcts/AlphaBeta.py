def evaluation_function(state):
    return state.evaluate()


# alpha beta pruning with min max
def alpha_beta_search(state, depth, player_id):
    alpha = float("-inf")
    beta = float("inf")

    # Inner function for min
    def min_value(state, alpha, beta, depth, player_id):
        if state.is_terminal_state():
            return state.utility_ab(player_id)

        if depth <= 0:
            return evaluation_function(state)

        val = float("inf")
        for action in state.actions:
            val = min(val, max_value(state.take_action(action), alpha, beta, depth-1, player_id))
            if val <= alpha:
                return val
            beta = min(beta, val)
        return val

    # Inner function for max
    def max_value(state, alpha, beta, depth, player_id):
        if state.is_terminal_state():
            return state.utility_ab(player_id)
        if depth <= 0:
            return evaluation_function(state)
        value = float("-inf")
        for action in state.actions:
            value = max(value, min_value(state.take_action(action), alpha, beta, depth-1, player_id))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value
    return max(state.actions, key=lambda x: min_value(state.take_action(x), alpha, beta, depth-1, player_id))


def get_action(state, player_id, depth=6):
    return alpha_beta_search(state, depth, player_id)
