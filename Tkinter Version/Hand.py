from Card import Card

options = ["c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "cj", "ca", "cq", "ck", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "dj", "da", "dq", "dk", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "hj", "ha", "hq", "hk", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "sj", "sa", "sq", "sk"]
class Hand:
  def __init__(self): # Prepares hand object, as well as adds two cards to it
    self.hand = []
    self.add_card()
    self.add_card()

  def add_card(self): # Adds additional cards to the hand from the remaining options
    card = Card(options)
    options.remove(card.type)

    self.hand.append(card)

    
  def print(self, dealer): # Prints out the hand, with different parameters
                           # depending on whether dealer object or player object
    length = len(self.hand)
    if(dealer):
      length -= 1
      print(self.hand[1].get_card(True))


    for i in range(0, length):
      print(self.hand[i].get_card(False))

# 10 jack
# 11 ace
# 12 queen
# 13 kinge
