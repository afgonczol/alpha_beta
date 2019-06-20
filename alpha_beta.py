def alpha_beta(node, depth, alpha, beta, max_player):
    if depth == 0 or node.is_terminal():
        return node.score()

    if max_player:
        value = float("-inf")
        available_moves = node.get_available_moves()
        for move in available_moves:
            child = node.make_move(move)
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        available_moves = node.get_available_moves()
        for move in available_moves:
            child = node.make_move(move)
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value