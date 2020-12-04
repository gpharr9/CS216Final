import unittest
from Card import *
from Hand import *
from Player import *

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

    def test_get_card(self):
        card = Card(['h7'])
        suit = '♥'
        num = '7'
        
        card_data = card.get_card(False)
        check = """ 
┌────────────┐   
│ {}          │
│            │
│            │
│     {}      │
│            │
│            │
│          {} │
└────────────┘""".format(num,suit,num)
        self.assertTrue(card_data == check, "The card data does not match...")

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

class TestPlayer(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_hand(self):
        player = Player()
        testHand = player.create_hand()
        self.assertTrue(type(testHand) is Hand, "The player did not create a hand object...")


    def test_count_hand(self):
        player = Player()
        testHand = Hand()
        testHand.hand = []
        testHand.hand.append(Card(['c3']))
        testHand.hand.append(Card(['h3']))
        testHand.hand.append(Card(['d6']))
        player.hand = testHand
        self.assertTrue(player.count_hand() == 12, "Count hand did not properly add the hand total...")

if __name__ == '__main__':
    unittest.main(exit=False)
