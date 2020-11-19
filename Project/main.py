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
def rules(): # Outputs basic rule structure for the game
  print("=====================================================================================================")
  print("1) Blackjacks primary goal is to beat the dealers hand while keeping your hand under a total value of 21")
  print("2) Choosing hit will have you draw another card and add it to your total hands value")
  print("3) Choosing stand will lock your hand in and compare it to the dealers")
  print("=====================================================================================================")


def user_choice(): # Collects user input for use in Player subclass
  print("Do you want to play a round (y/n)")
  state = input()

  if state in "Yy":
    return True
  elif state in "Nn":
    return False
  

def main():
  system('cls') # Clears terminal
  rules() # Outputs rules
  # before start game

  state = user_choice() # Collects input
  
  
  count = 0 # Sets initial turn count to zero
  #game = None # Sets initial game value to None type
  while state == True:
    if(count == 0):
      game = None # Sets initial game value to None type
      game = Game() # Creates game object
    status = game.next() # Progresses the game
    
    count += 1
    if status == 0: # Monitors game state
      print("You win!!!")
      state = user_choice()
      if state == True:
        count = 0
    elif status == 1: # Monitors game state
      print("You lose.")
      state = user_choice()
      if state == True:
        count = 0
    elif status == 2: # Monitors game state
      print("You tied!")
      state = user_choice()
      if state == True:
        count = 0

    


  # game over
  print("Thanks for playing!")

main()