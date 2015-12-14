from BowlingGame import BowlingGame
import unittest

class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self._game = BowlingGame()

    def rollMany(self, n, pincount):
        for i in range(n):
            self._game.roll(pincount)

# First test
    def testGutterGame(self):
            self.rollMany(20,0)
            assert self._game.getScore() == 0

# Second test
    def testAllOnes(self):
            self.rollMany(20,1)
            assert self._game.getScore() == 20

    def testRollSpare(self):
        self._game.roll(5)
        self._game.roll(5)
        self._game.roll(3)
        self.rollMany(17,0)
        assert self._game.getScore() == 16