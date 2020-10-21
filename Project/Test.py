from Hand import *

class Test:
  print(hand)
  print("Would you like to draw again?")
  ui = input()

  if ui in "Yes":
    card = Card()
    hand.append(card.type)
    print(hand)
  else:
    exit()
