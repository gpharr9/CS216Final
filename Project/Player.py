from Hand import Hand

class Player:

  def create_hand(self):
    hand = Hand()
    return hand
  

  def collectinput(self):
    print("Would you like to draw again?")
    ui = input()
    return ui
