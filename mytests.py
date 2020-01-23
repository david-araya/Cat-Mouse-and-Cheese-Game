import unittest
import board

class boardTest(unittest.TestCase):
    
    def test_boardSize(self):
        self.assertEquals(board.buildBoard, 144)

    def test_possibleMovesCat(self):
        self.assertEquals(board.possibleMovesCat, 8)

    def test_possibleMovesMouse(self):
        self.assertEquals(board.possibleMovesMouse, 8)

    def test_bestMoveMouse(self):
        self.assertEquals(board.bestMoveMouse, 1)

    def test_bestMoveCat(self):
        self.assertEquals(board.bestMoveCat, 1)
    
#Run directly with python3 mytests.py
if __name__ == '__main__':
    unittest.main()
