import math
import unittest
from board import Board
import numpy as np

class BoardTests(unittest.TestCase):
    board1 = Board()
    board2 = Board([[0, 0, 0, 0, 0, 0, 2],
                    [0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 2, 0, 0, 0, 2],
                    [1, 0, 2, 0, 0, 0, 1],
                    [1, 0, 2, 0, 0, 0, 2],
                    [1, 1, 1, 1, 0, 0, 1]])

    board4 = Board([[0, 0, 0, 0, 0, 0, 2],
                    [0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 2, 0, 0, 0, 2],
                    [2, 0, 2, 0, 0, 0, 1],
                    [1, 2, 2, 2, 2, 2, 2],
                    [1, 2, 1, 1, 2, 2, 1]])

    board5 = Board([[0, 0, 0, 0, 0, 0, 2],
                    [0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 2, 2, 0, 0, 2],
                    [2, 0, 2, 2, 0, 0, 1],
                    [1, 2, 2, 2, 2, 2, 2],
                    [2, 2, 1, 1, 2, 2, 1]])

    board6 = Board([[0, 0, 0, 0, 0, 0, 2],
                    [0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 2, 2, 0, 1, 2],
                    [2, 0, 2, 2, 1, 0, 1],
                    [1, 0, 2, 1, 2, 2, 2],
                    [2, 0, 1, 1, 2, 2, 1]])

    board7 = Board([[0, 0, 0, 1, 0, 0, 2],
                    [0, 0, 1, 0, 1, 0, 1],
                    [1, 0, 2, 2, 0, 1, 2],
                    [2, 0, 2, 2, 0, 0, 1],
                    [1, 0, 2, 1, 2, 2, 2],
                    [2, 0, 1, 1, 2, 2, 1]])

    board8 = Board([[0, 0, 0, 1, 0, 0, 2],
                    [0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 2, 0, 0, 0, 2],
                    [2, 1, 2, 2, 1, 0, 1],
                    [1, 2, 1, 0, 0, 2, 2],
                    [2, 2, 1, 1, 2, 2, 1]])
    
    board9 = Board([[0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 2, 2, 2, 0],
                    [1, 1, 0, 1, 1, 2, 0],
                    [2, 1, 2, 2, 1, 0, 2],
                    [1, 2, 1, 0, 0, 2, 2],
                    [2, 2, 1, 1, 2, 2, 2]])
    
    board10 = Board([[0, 0, 0, 0, 0, 0, 2],
                    [0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 2, 0, 0, 0, 2],
                    [1, 0, 2, 0, 0, 0, 1],
                    [1, 0, 2, 0, 0, 0, 2],
                    [1, 0, 1, 1, 0, 0, 1]])
    
    board11 = Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [2, 0, 2, 0, 2, 0, 1]])
    
    board12 =Board([[1, 2, 2, 1, 1, 2, 1],
                    [2, 1, 2, 2, 2, 2, 2],
                    [1, 1, 1, 1, 1, 2, 1],
                    [2, 1, 2, 2, 1, 2, 2],
                    [1, 2, 1, 2, 1, 2, 2],
                    [2, 2, 1, 1, 2, 2, 2]])


    def testMovePossible(self):
        self.assertFalse(self.board1.move_possible(-1))
        self.assertTrue(self.board1.move_possible(0))
        self.assertTrue(self.board2.move_possible(0))
        self.assertFalse(self.board2.move_possible(6))
        self.assertTrue(self.board2.move_possible(2))


    def testhasCoin(self):
        self.assertFalse(self.board1.has_any_coin(0, 0))
        self.assertTrue(self.board2.has_any_coin(5, 6))
        self.assertTrue(self.board2.has_any_coin(5, 0))
        self.assertFalse(self.board1.has_specific_coin(0, 0, 1))
        self.assertTrue(self.board2.has_specific_coin(5, 6, 1))
        self.assertTrue(self.board2.has_specific_coin(5, 0, 1))
        self.assertFalse(self.board2.has_specific_coin(5, 0, 2))


    def testAddCoin(self):
        board3 = Board([[0, 0, 0, 0, 0, 0, 2],
                        [0, 0, 1, 0, 0, 0, 1],
                        [1, 0, 2, 0, 0, 0, 2],
                        [1, 0, 2, 0, 0, 0, 1],
                        [1, 0, 2, 0, 0, 0, 2],
                        [1, 0, 1, 0, 0, 0, 1]])
        board3.add_coin(0, 1)
        self.assertTrue(board3.has_specific_coin(1, 0, 1))
        board3.print_board()
        board3.add_coin(0, 1)
        self.assertTrue(board3.has_specific_coin(0, 0, 1))

    def testCheckVertical(self):
        self.assertFalse(self.board1.check_vertical(1))
        self.assertTrue(self.board2.check_vertical(1))
        self.assertFalse(self.board4.check_vertical(2))

    def testCheckHorizontal(self):
        self.assertFalse(self.board1.check_horizontal(1))
        self.assertTrue(self.board2.check_horizontal(1))
        self.assertTrue(self.board4.check_horizontal(2))

    def testCheckDiagonal(self):
        self.assertFalse(self.board1.check_diagonal(2))
        self.assertFalse(self.board2.check_diagonal(1))
        self.assertTrue(self.board5.check_diagonal(2))
        self.assertTrue(self.board6.check_diagonal(2))
        self.assertTrue(self.board7.check_diagonal(2))
        self.assertTrue(self.board8.check_diagonal(1))

    def testHasWon(self):
        this_board6 = Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 1, 1, 1, 0]])
        self.assertFalse(this_board6.check_won(2))

    def testGenerateNextStates(self):
        board_new = Board()
        new_states = board_new.generate_possible_moves()
        self.assertTrue(new_states, 
            [0, 1, 2 ,3, 4, 5, 6])
        
        set_two = self.board5.generate_possible_moves()
        self.assertTrue(set_two, [0, 1, 2,3 ,4 ,5])
        


    def testIsBoardFull(self):
        self.assertFalse(self.board1.is_board_full())
        self.assertFalse(self.board9.is_board_full())
        self.assertFalse(self.board10.is_board_full())
        self.assertTrue(self.board12.is_board_full())

    def testIsTerminal(self):
        self.assertTrue(self.board12.terminal_state())
        self.assertTrue(self.board2.terminal_state())
        self.assertTrue(self.board7.terminal_state())
        self.assertFalse(self.board1.terminal_state())
        self.assertFalse(self.board11.terminal_state())

    def testEvalFunc(self):
        this_board = Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 2, 0]])
        self.assertEqual(this_board.eval_function(2), 4)
        this_board2 = Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 2, 1, 2, 0]])
        self.assertEqual(this_board2.eval_function(2), 19)

        this_board3 = Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 2, 1, 2, 0]])
        self.assertEqual(this_board3.eval_function(2), 42)

        this_board4 = Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 0, 0, 1, 1, 0, 0]])
        self.assertEqual(this_board4.in_a_row_horizontal(1, 2), 2)
        self.assertEqual(this_board4.eval_function(2), 64)
        this_board5 = Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 0, 0, 1, 1, 2, 0]])
        self.assertEqual(this_board5.in_a_row_horizontal(1, 2), 1)

        print("eval func board 5")
        print(this_board5.eval_function(2))
        self.assertEqual(this_board5.eval_function(2), 35)
        this_board6 = Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 1, 1, 1, 0]])
        self.assertEqual(this_board6.eval_function(2), -86)
        #self.assertEqual(this_board6.minimax(3, -math.inf, math.inf, True), 4)

    def testInARowHorizontal(self):
        self.assertEqual(self.board10.in_a_row_horizontal( 1, 2), 2)
        self.assertEqual(self.board11.in_a_row_horizontal( 2, 2), 2)
        self.assertEqual(self.board10.in_a_row_horizontal( 1, 3), 2)
        self.assertEqual(self.board10.in_a_row_horizontal( 1, 2), 2)
        self.assertEqual(self.board10.in_a_row_horizontal( 2, 2), 0)
        self.assertEqual(self.board5.in_a_row_horizontal( 2, 2), 4)
        self.assertEqual(self.board9.in_a_row_horizontal(1, 3), 1)
        self.assertEqual(self.board9.in_a_row_horizontal( 2, 3), 2)
            

    def testInARowVertical(self):
        self.assertEqual(self.board9.in_a_row_vertical( 2,2), 4)
        self.assertEqual(self.board9.in_a_row_vertical(1 ,2), 2)
        self.assertEqual(self.board9.in_a_row_vertical( 2, 3), 1)

    def testInARowDiagonal(self):
       # self.assertEqual(self.board4.in_a_row_diagonal(2,3), 2)
        self.assertEqual(self.board4.in_a_row_diagonal(1,3), 0)
       # self.assertEqual(self.board4.in_a_row_diagonal(2,2), 3)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
