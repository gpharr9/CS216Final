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
from GUI import GUI




  

def main():
  system('cls') # Clears terminal
  #Outputs rules
  #before start game
  gui = GUI()
  state = gui.set_up()

  
  
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
      state = gui.set_up()
      if state == True:
        count = 0
    elif status == 1: # Monitors game state
      print("You lose.")
      state = gui.set_up()
      if state == True:
        count = 0
    elif status == 2: # Monitors game state
      print("You tied!")
      state = gui.set_up()
      if state == True:
        count = 0

    


  # game over
  print("Thanks for playing!")

main()
