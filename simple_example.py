from alpha_beta import alpha_beta

class TestGame:
    def __init__(self, state="s"):
        self.game_state = state
        self.move_dict = {
            "s": ("sl", "sr"),
            "sl": ("sll", "slr"),
            "sr": ("srl", "srr"),
            "sll": (20, 5),
            "slr": (16, 10),
            "srl": (3, 17),
            "srr": (7, 50),
        }
        
    def score(self):
        if self.is_terminal():
            return self.game_state
        else:
            return 0

    def is_terminal(self):
        return isinstance(self.game_state, int)

    def get_available_moves(self):
        return self.move_dict[self.game_state]
    
    def make_move(self, m):
        self.game_state = m
        return self
    
if __name__ == '__main__':
    game = TestGame()
    answer = alpha_beta(game, 5, float('-inf'), float('inf'), True)
    print(answer)