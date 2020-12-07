from Hand import Hand
from Player import Player

class Dealer(Player):

  def print_hand(self): # Output of the dealers current hand by using data made in card and hand
    d_arr = self.hand.print(True)
    return d_arr


  def hit(self, player): # Adds a card to the dealers deck based on whether the deck is below 17 or not
    if(player):
      player.hand.add_card()
    else:
      self.hand.add_card()

  #Only used by player
  # deprecated for now
  # def split(self):
  #   print('split')
