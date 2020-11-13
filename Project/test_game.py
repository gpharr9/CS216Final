import unittest
from Card import *
from Hand import *

# class TestGame(unittest.TestCase):

#     def setUp(self):
#         pass

#     def test_constructor(self):
#         game = Game()
#         print(game.player_instance)

class TestCard(unittest.TestCase):
    def setUp(self):
        pass

    def test_constructor(self):
        card = Card(['a','b','c'])
        self.assertTrue(card.type == 'a' or card.type == 'b' or card.type == 'c', "Card type does not match any of the valid options...")

class TestHand(unittest.TestCase):
    def setUp(self):
        pass

    def test_constructor(self):
        hand = Hand()
        self.assertTrue(len(hand.hand) == 2, "Hand is the improper size, we should have 2 cards in the hand at this point...")
        self.assertTrue(str(type(hand.hand[0])) == "<class 'Card.Card'>" and str(type(hand.hand[1])) == "<class 'Card.Card'>", "One of the indeces is not a card!")

    def test_add_card(self):
        hand = Hand()
        hand.add_card()
        self.assertTrue(len(hand.hand) == 3, "Hand is the improper size, we should have 3 cards in the hand at this point...")

if __name__ == '__main__':
    unittest.main(exit=False)