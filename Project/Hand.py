from Card import Card

options = ["c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "cj", "ca", "cq", "ck", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "dj", "da", "dq", "dk", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "hj", "ha", "hq", "hk", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "sj", "sa", "sq", "sk"]
class Hand:
  def __init__(self):
    self.hand = []
    self.addCard()
    self.addCard()

  def addCard(self):
    card = Card(options)
    options.remove(card.type)

    self.hand.append(card)

  def print(self, dealer):
    length = len(self.hand)
    if(dealer):
      length -= 1
      self.hand[1].print(True)


    for i in range(0, length):
      self.hand[i].print(False)

# 10 jack
# 11 ace
# 12 queen
# 13 kinge