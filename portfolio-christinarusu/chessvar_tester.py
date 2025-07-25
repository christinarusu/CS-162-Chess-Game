# Author: Christina Rusu
# GitHub username: christinarusu
# Date: 12/8/2024
# Description: a program that uses unittests to test the ChessVar class

import unittest
from ChessVar import ChessVar


class TestChessVar(unittest.TestCase):
    """Contains Unittests for ChessVar class"""

    def test_pawn(self):
        """tests the make_move method for moving a pawn"""
        game = ChessVar()
        self.assertTrue(game.make_move('a2', 'a4'))
        self.assertTrue(game.make_move('b7', 'b5'))
        self.assertTrue(game.make_move('h2', 'h3'))
        self.assertTrue(game.make_move('b5', 'a4'))
        self.assertFalse(game.make_move('a4', 'a3'))

    def test_rook(self):
        """tests the make_move method for moving a rook"""
        game = ChessVar()
        self.assertTrue(game.make_move('a2', 'a4'))
        self.assertTrue(game.make_move('h7', 'h5'))
        self.assertFalse(game.make_move('a1', 'a5'))
        self.assertTrue(game.make_move('a1', 'a3'))
        self.assertFalse(game.make_move('h8', 'f6'))
        self.assertFalse(game.make_move('h8', 'h9'))
        self.assertTrue(game.make_move('h8', 'h6'))
        self.assertTrue(game.make_move('a3', 'e3'))
        self.assertTrue(game.make_move('h6', 'h7'))

    def test_bishop(self):
        game = ChessVar()
        self.assertTrue(game.make_move('d2', 'd4'))
        self.assertTrue(game.make_move('e7', 'e5'))
        self.assertTrue(game.make_move('c2', 'c4'))
        self.assertTrue(game.make_move('a7', 'a5'))
        self.assertFalse(game.make_move('c1', 'c3'))
        self.assertTrue(game.make_move('c1', 'g5'))

    def test_queen(self):
        """tests the make_move method for moving a queen"""
        game = ChessVar()
        self.assertTrue(game.make_move('d2', 'd4'))
        self.assertTrue(game.make_move('e7', 'e5'))
        self.assertTrue(game.make_move('c1', 'g5'))
        self.assertFalse(game.make_move('d8', 'b8'))
        self.assertTrue(game.make_move('d8', 'g5'))

    def test_get_game_state(self):
        """tests the get_game_state method"""
        game = ChessVar()
        self.assertTrue(game.make_move('d2', 'd4'))
        self.assertTrue(game.make_move('g7', 'g5'))
        self.assertTrue(game.make_move('c1', 'g5'))
        self.assertTrue(game.make_move('e7', 'e6'))
        self.assertTrue(game.make_move('h2', 'h4'))
        self.assertTrue(game.make_move('e8', 'e7'))
        self.assertTrue(game.make_move('g5', 'e7'))
        self.assertEqual(game.get_game_state(), 'WHITE_WON')
        self.assertFalse(game.make_move('d4', 'd5'))

    def test_get_board(self):
        """tests the get_board method along with the get_capture_pieces method"""
        game = ChessVar()
        self.assertTrue(game.make_move('d2', 'd4'))
        self.assertTrue(game.make_move('e7', 'e5'))
        self.assertTrue(game.make_move('c1', 'g5'))
        self.assertEqual(game.get_board('audience'), [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                                                      ['p', 'p', 'p', 'p', ' ', 'p', 'p', 'p'],
                                                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                      [' ', ' ', ' ', ' ', 'p', ' ', 'B', ' '],
                                                      [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],
                                                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                      ['P', 'P', 'P', ' ', 'P', 'P', 'P', 'P'],
                                                      ['R', 'N', ' ', 'Q', 'K', 'B', 'N', 'R']])
        self.assertEqual(game.get_board('white'), [['*', '*', '*', 'q', '*', '*', '*', '*'],
                                                   ['*', '*', '*', '*', ' ', '*', '*', '*'],
                                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                   [' ', ' ', ' ', ' ', 'p', ' ', 'B', ' '],
                                                   [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],
                                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                   ['P', 'P', 'P', ' ', 'P', 'P', 'P', 'P'],
                                                   ['R', 'N', ' ', 'Q', 'K', 'B', 'N', 'R']])
        self.assertEqual(game.get_board('black'), [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                                                   ['p', 'p', 'p', 'p', ' ', 'p', 'p', 'p'],
                                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                   [' ', ' ', ' ', ' ', 'p', ' ', 'B', ' '],
                                                   [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],
                                                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                   ['*', '*', '*', ' ', '*', '*', '*', '*'],
                                                   ['*', '*', ' ', '*', '*', '*', '*', '*']])
