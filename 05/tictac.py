import logging


class TicTac:
    def __init__(self):
        print("Welcome to TicTacGame!")
        self.status = ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3")
        print(
            "%s |%s |%s \n---+---+---\n%s |%s |%s \n---+---+---\n%s |%s |%s "
            % self.status
        )

        self.positions = {
            "a1": " ",
            "a2": " ",
            "a3": " ",
            "b1": " ",
            "b2": " ",
            "b3": " ",
            "c1": " ",
            "c2": " ",
            "c3": " ",
        }

        self.positions_value = {
            "a1": 0,
            "a2": 0,
            "a3": 0,
            "b1": 0,
            "b2": 0,
            "b3": 0,
            "c1": 0,
            "c2": 0,
            "c3": 0,
        }

    def show_board(self):
        self.status = self.positions.values()
        return (
            " %s | %s | %s \n---+---+---\n %s | %s | %s \n---+---+---\n %s | %s | %s "
            % tuple(self.status)
        )

    def input_pos(self, player_num):
        return input(f"Player{player_num}: ").lower()

    def validate_input(self, player_num):
        while True:
            move = self.input_pos(player_num)
            try:
                if self.positions[move] == " ":
                    if player_num == 1:
                        self.positions[move] = "X"
                        self.positions_value[move] = 1
                    else:
                        self.positions[move] = "O"
                        self.positions_value[move] = -1
                    print(self.show_board())
                    return self.positions_value[move]
                else:
                    logging.getLogger(__name__).exception(
                        "This position is filled. Please, put another position.",
                        exc_info=False,
                    )
            except:
                logging.getLogger(__name__).exception(
                    "You put the wrong position. Please, put another position.",
                    exc_info=False,
                )

    def start_game(self):
        print("Player1 : X     Player2 : O\nWrite a position!")
        i = 1
        while 0 in self.check_winner() and i != 10 and (3 or -3):
            if 3 in self.check_winner():
                print("Player1 WIN!")
                return 1
            elif -3 in self.check_winner():
                print("Player2 WIN!")
                return 2
            else:
                if i % 2 == 0:
                    self.validate_input(2)
                else:
                    self.validate_input(1)
            i += 1
        if 3 not in self.check_winner():
            print("The game ended in a tie.")
            return 0
        else:
            print("Player1 WIN!")
            return 1

    def check_winner(self):
        pos = list(self.positions_value.values())
        r_match = [pos[i] + pos[i + 1] + pos[i + 2] for i in [0, 3, 6]]
        c_match = [pos[i] + pos[i + 3] + pos[i + 6] for i in [0, 1, 2]]
        d_match = [
            pos[0] + pos[4] + pos[8],
            pos[2] + pos[4] + pos[6],
        ]
        result = r_match + c_match + d_match
        return result


if __name__ == "__main__":
    game = TicTac()
    game.start_game()
