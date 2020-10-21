from Hand import Hand

class Player:

  def create_hand():
    hand = Hand()
    phand = hand.hand
    return phand
  

  def collectinput(self):
    print("Would you like to draw again?")
    ui = input()
    return ui
