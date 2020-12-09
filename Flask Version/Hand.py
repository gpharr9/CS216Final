from Card import Card

class Hand:
  def __init__(self): # Prepares hand object, as well as adds two cards to it
    self.hand = []
    self.options = ["c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "cj", "ca", "cq", "ck", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "dj", "da", "dq", "dk", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "hj", "ha", "hq", "hk", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "sj", "sa", "sq", "sk"]

    self.add_card()
    self.add_card()

  def add_card(self): # Adds additional cards to the hand from the remaining options
    card = Card(self.options)
    self.options.remove(card.type)

    self.hand.append(card)

    
  def print(self, dealer): # Prints out the hand, with different parameters
                           # depending on whether dealer object or player object
    length = len(self.hand)
    c_arr = []
    s = 0
    if(dealer):
      s += 1
      c_arr.append(self.hand[0].get_card(True))


    for i in range(s, length):
      c_arr.append(self.hand[i].get_card(False))
    return c_arr
# 10 jack
# 11 ace
# 12 queen
# 13 kinge
