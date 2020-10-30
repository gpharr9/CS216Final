from Hand import Hand
from Player import Player

class Dealer(Player):

  def print_hand(self):
    self.hand.print(True)

  #Used when card value is lower than 17
  def hit(self, player):
    player.hand.addCard()
    print('hit')

  #Used when card value is higher than 17
  def stand(self, player):
    print('stand')

  #Only used by player
  # deprecated for now
  # def split(self):
  #   print('split')
