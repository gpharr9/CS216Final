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
from os import system
def rules():
  print("=====================================================================================================")
  print("1) Blackjacks primary goal is to beat the dealers hand while keeping your hand under a total value of 21")
  print("2) Choosing hit will have you draw another card and add it to your total hands value")
  print("3) Choosing stand will lock your hand in and compare it to the dealers")
  print("=====================================================================================================")


def user_choice():
  print("Do you want to play a round (y/n)")
  state = input()

  if state in "Yy":
    return True
  elif state in "Nn":
    return False
  

def main():
  system('cls')
  rules()
  # before start game

  state = user_choice()
  
  
  count = 0
  game = None
  while state == True:
    if(count == 0):
      # game = None
      game = Game()
    status = game.next()

    if status == 0:
      print("You win!!!")
      state = False
      # state = user_choice()
      # if state == True:
      #   count = 0
    elif status == 1:
      print("You lose.")
      state = False
      # state = user_choice()
      # if state == True:
      #   count = 0
    elif status == 2:
      print("You tied!")
      state = False
      # state = user_choice()
      # if state == True:
      #   count = 0
  

    count += 1


  # game over


main()