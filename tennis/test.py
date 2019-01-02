import unittest

from tennis import Tennis


class TestTennis(unittest.TestCase):


    def test_basic_player1(self):
        tennis = Tennis()
        tennis.scoreP1()
        self.assertEqual( tennis.result(), "fifteen - love" )
        tennis.scoreP1()
        self.assertEqual( tennis.result(), "thirty - love" )
        tennis.scoreP1()
        self.assertEqual( tennis.result(), "forty - love" )
        tennis.scoreP1()
        self.assertEqual( tennis.result(), "Player 1 win" )

    def test_basic_player2(self):
        tennis = Tennis()
        tennis.scoreP2()
        self.assertEqual( tennis.result(), "love - fifteen" )
        tennis.scoreP2()
        self.assertEqual( tennis.result(), "love - thirty" )
        tennis.scoreP2()
        self.assertEqual( tennis.result(), "love - forty" )
        tennis.scoreP2()
        self.assertEqual( tennis.result(), "Player 2 win" )

    def test_advanced(self):
        tennis = Tennis()
        tennis.scoreP2()
        tennis.scoreP1()

        self.assertEqual(tennis.result(), "fifteen - fifteen")
        tennis.scoreP1()
        self.assertEqual(tennis.result(), "thirty - fifteen")
        tennis.scoreP2()
        self.assertEqual(tennis.result(), "thirty - thirty")
        tennis.scoreP1()
        self.assertEqual(tennis.result(), "Deuce")
