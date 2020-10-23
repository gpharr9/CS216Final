 ## Hand Test

# from Hand import Hand

# tempHand = Hand()
# print(tempHand.hand)

# while True:
#   print("Would you like to draw again? (Y/N)")
#   ui = input();

#   if ui in 'Yy':
#     tempHand.addCard()
#     print()
#     print(tempHand.hand)
#   elif ui in 'Nn':
#     exit()
#   else:
#     print("no.")

    
 ## Player Test
# from Player import Player
from Computer import Computer

player = Computer()
phand = player.create_hand()
phand.print()

while True:
  ui = player.collectinput()

  if ui in 'Yy':
    phand.addCard()
    phand.print()
  elif ui in 'Nn':
    exit()
  else:
    print("no.")