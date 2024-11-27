import unittest
from board import Board

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



    def testMovePossible(self):
        self.assertFalse(self.board1.move_possible(-1))
        self.assertTrue(self.board1.move_possible(0))
        self.assertTrue(self.board2.move_possible(0))
        self.assertFalse(self.board2.move_possible(6))
        self.assertTrue(self.board2.move_possible(2))


    def testhasCoin(self):
        self.assertFalse(self.board1.has_coin(0, 0))
        self.assertTrue(self.board2.has_coin(5, 6))
        self.assertTrue(self.board2.has_coin(5, 0))

    def testAddCoin(self):
        board3 = Board([[0, 0, 0, 0, 0, 0, 2],
                        [0, 0, 1, 0, 0, 0, 1],
                        [1, 0, 2, 0, 0, 0, 2],
                        [1, 0, 2, 0, 0, 0, 1],
                        [1, 0, 2, 0, 0, 0, 2],
                        [1, 0, 1, 0, 0, 0, 1]])
        board3.add_coin(0, 1)
        self.assertTrue(board3.has_coin(1, 0))
        board3.add_coin(0, 1)
        self.assertTrue(board3.has_coin(0, 0))

    def testCheckVertical(self):
        self.assertFalse(self.board1.check_vertical())
        self.assertTrue(self.board2.check_vertical())
        self.assertFalse(self.board4.check_vertical())

    def testCheckHorizontak(self):
        self.assertFalse(self.board1.check_horizontal())
        self.assertTrue(self.board2.check_horizontal())
        self.assertTrue(self.board4.check_horizontal())

    def testCheckDiagonal(self):
        self.assertFalse(self.board1.check_diagonal())
        self.assertFalse(self.board2.check_diagonal())
        self.assertTrue(self.board5.check_diagonal())
        self.assertTrue(self.board6.check_diagonal())
        self.assertTrue(self.board7.check_diagonal())
        self.assertTrue(self.board8.check_diagonal())

    def testGenerateNextStates(self):
        board_new = Board()
        new_states = board_new.generate_next_states(2)
        self.assertTrue(new_states, 
            [
                Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0]]),
                Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0, 0]]),
                Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 2, 0, 0, 0, 0]]),
                Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0]]),
                Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 2, 0, 0]]),
                Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 2, 0]]),
                Board([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 2]])])
        
        set_two = self.board5.generate_next_states(1)
        self.assertTrue(set_two, [
                Board([[0, 0, 0, 0, 0, 0, 2],
                    [1, 0, 1, 0, 0, 0, 1],
                    [1, 0, 2, 2, 0, 0, 2],
                    [2, 0, 2, 2, 0, 0, 1],
                    [1, 2, 2, 2, 2, 2, 2],
                    [2, 2, 1, 1, 2, 2, 1]]),
            Board([[0, 0, 0, 0, 0, 0, 2],
                    [0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 2, 2, 0, 0, 2],
                    [2, 1, 2, 2, 0, 0, 1],
                    [1, 2, 2, 2, 2, 2, 2],
                    [2, 2, 1, 1, 2, 2, 1]]),
            Board([[0, 0, 1, 0, 0, 0, 2],
                    [0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 2, 2, 0, 0, 2],
                    [2, 0, 2, 2, 0, 0, 1],
                    [1, 2, 2, 2, 2, 2, 2],
                    [2, 2, 1, 1, 2, 2, 1]]),
                    Board([[0, 0, 0, 0, 0, 0, 2],
                    [0, 0, 1, 1, 0, 0, 1],
                    [1, 0, 2, 2, 0, 0, 2],
                    [2, 0, 2, 2, 0, 0, 1],
                    [1, 2, 2, 2, 2, 2, 2],
                    [2, 2, 1, 1, 2, 2, 1]]),
                    Board([[0, 0, 0, 0, 0, 0, 2],
                    [0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 2, 2, 0, 0, 2],
                    [2, 0, 2, 2, 1, 0, 1],
                    [1, 2, 2, 2, 2, 2, 2],
                    [2, 2, 1, 1, 2, 2, 1]]),
                    Board([[0, 0, 0, 0, 0, 0, 2],
                    [0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 2, 2, 0, 0, 2],
                    [2, 0, 2, 2, 0, 1, 1],
                    [1, 2, 2, 2, 2, 2, 2],
                    [2, 2, 1, 1, 2, 2, 1]])
        ])






def main():
    unittest.main()

if __name__ == "__main__":
    main()
