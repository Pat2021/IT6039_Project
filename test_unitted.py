import unittest
from BowlingGame import BowlingGame
# Import the BowlingGame class from your code

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
         # Initialize a BowlingGame instance for testing
        self.game = BowlingGame()

    def testGutterGame(self):
        # Test a game where no pins are knocked down (a gutter game)
        for i in range(0, 20): # 0 - 20 rolls with no pins down
            self.game.roll(0)
        
        self.assertEqual(self.game.score(), 0)
    
    def testAllOnes(self):
        # Test a game where one pin is knocked down in each roll
        self.rollMany(1, 20) # 1 - 20 rolls with 1 pin down each time

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)

        self.assertEqual(self.game.score(), 20)

    def testOneSpare(self):
        # Test a game with spares
        self.game.roll(5)
        self.game.roll(5) # Spare
        self.game.roll(3) # Bonus roll
        self.rollMany(0, 17)  # Rolls with no pins down


        self.assertEqual(self.game.score(), 13) # 10 (spare) + 3 (frame 2)

    def testOneStrike(self):
        # Test a game with strikes
        self.game.roll(10) # Strike
        self.game.roll(4)  # Bonus roll 2
        self.game.roll(3)  # Bonus roll 1
        self.rollMany(0, 16) #Rolls with no pins down

        self.assertEqual(self.game.score(),17)

    def testPerfectGame(self):
        # Test a perfect game with all strikes
        self.rollMany(10, 12) # 12 strikes in a row

        self.assertEqual(self.game.score(), 30)

    def testAllFives(self):
        self.rollMany(5, 21) # Roll 5 pins 21 times

        self.assertEqual(self.game.score(), 15)

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)
# Use self.game.roll to simulate rolls
if __name__ == '__main__':
            unittest.main()