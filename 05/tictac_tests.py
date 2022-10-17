import unittest
from unittest import mock
from tictac import TicTac


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTac()

    def test_init(self):
        self.assertEqual(
            self.game.status, ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3")
        )
        self.assertEqual(
            self.game.positions,
            {
                "a1": " ",
                "a2": " ",
                "a3": " ",
                "b1": " ",
                "b2": " ",
                "b3": " ",
                "c1": " ",
                "c2": " ",
                "c3": " ",
            },
        )
        self.assertEqual(
            self.game.positions_value,
            {
                "a1": 0,
                "a2": 0,
                "a3": 0,
                "b1": 0,
                "b2": 0,
                "b3": 0,
                "c1": 0,
                "c2": 0,
                "c3": 0,
            },
        )

    def test_show_board(self):
        with mock.patch("tictac.TicTac.__init__") as check:
            check.return_value = (
                "   |   |   \n---+---+---\n   |   |   \n---+---+---\n   |   |   "
            )
            result = self.game.show_board()
            self.assertEqual(result, check.return_value)

    def test_input_pos(self):
        with mock.patch("tictac.TicTac.input_pos") as check:
            res = TicTac.input_pos(self.game, 1)
            self.assertEqual(res, check.return_value)

    def test_validate_input(self):
        def check_input():
            for i in range(cnt_good_cases):
                if i % 2 == 0:
                    res = TicTac.validate_input(self.game, 1)
                    self.assertEqual(res, 1)
                else:
                    res = TicTac.validate_input(self.game, 2)
                    self.assertEqual(res, -1)

        with mock.patch("tictac.TicTac.input_pos") as check:
            good_cases = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
            bad_cases = ["a1de", "a1", ""]
            check.side_effect = good_cases + bad_cases
            cnt_good_cases = len(good_cases)
            check_input()
            with self.assertRaises(Exception):
                res = TicTac.validate_input(self.game, 2)
                self.assertIsNone(res)

    def test_check_winner(self):
        with mock.patch("tictac.TicTac.check_winner") as check:
            options_1 = [
                [3, -1, -1, 1, -1, 1, 1, -1],
                [-2, 3, 0, 1, 0, 0, 1, 0],
                [0, -2, 3, 1, 0, 0, 0, 0],
                [1, 0, 0, 3, -2, 0, 0, 0],
                [0, 2, -1, -1, 3, -1, -1, 0],
                [1, 0, 0, -2, 0, 3, 1, 0],
                [-1, 1, 1, 1, 0, 0, 3, 0],
                [1, -1, 1, 1, 0, 0, 2, 3],
            ]
            for i in options_1:
                check.return_value = i
                res = TicTac.start_game(self.game)
                self.assertEqual(res, 1)

        with mock.patch("tictac.TicTac.check_winner") as check:
            options_2 = [
                [-1, 1, 0, -3, 2, 1, 1, -1],
                [1, 0, -1, 2, -3, 1, 0, 0],
                [1, -1, 0, 2, 1, -3, 0, 0],
                [-1, 1, 0, -3, 1, 2, 0, 1],
                [1, -1, 0, 2, -3, 1, 1, 0],
                [1, 0, -1, 2, 1, -3, 0, -1],
                [1, 0, -1, -1, 0, 1, -3, 0],
                [1, 0, -1, 1, 0, -1, 0, -3],
            ]
            for i in options_2:
                check.return_value = i
                res = TicTac.start_game(self.game)
                self.assertEqual(res, 2)

        with mock.patch("tictac.TicTac.check_winner") as check:
            check.return_value = [1, -1, 1, 1, -1, 1, -1, 1]
            res = TicTac.start_game(self.game)
            self.assertEqual(res, 0)
            check.return_value = [-1, 1, 1, -1, 1, 1, 1, 1]
            res = TicTac.start_game(self.game)
            self.assertEqual(res, 0)
