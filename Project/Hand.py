from Card import *

hand = []
class Hand:
  global hand
  card = Card()

  hand.append(card.type)

## Temp Code
  print(hand)
  print("Would you like to draw again?")
  ui = input()

  if ui in "Yes":
    card = Card()
    hand.append(card.type)
    print(hand)
  else:
    exit()



