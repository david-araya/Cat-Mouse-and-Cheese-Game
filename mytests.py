import unittest
import board

class MovementTest(unittest.TestCase):

    def test_add(self):
        self.assertEquals(board.hello_world(), 1)
        
#Run directly with python3 mytests.py
if __name__ == '__main__':
    unittest.main()
