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
# from Dealer import Dealer

# dlr = Dealer()
# dlr.create_hand()
# dlr.hit()
# total = dlr.count_hand()
# dlr.hand.print()
# print(total)


# while True:
#   ui = player.collectinput()

#   if ui in 'Yy':
#     phand.addCard()
#     phand.print()
#   elif ui in 'Nn':
#     exit()
#   else:
#     print("no.")




from Game import Game
def rules():
  print("=====================================================================================================")
  print("1) Blackjacks primary goal is to beat the dealers hand while keeping your hand under a total value of 21")
  print("2) Choosing hit will have you draw another card and add it to your total hands value")
  print("3) Choosing stand will lock your hand in and compare it to the dealers")
  print("=====================================================================================================")

def main():
  rules()
  game = Game()
  game.next()



main()