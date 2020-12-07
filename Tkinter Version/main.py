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

# Sources: https://github.com/wtran29/Blackjack-Tkinter


from Game import Game
from os import system
import tkinter
from tkinter import *

class Root():
    
  def create_window(self):
    # create a GUI window 
    self.root = tkinter.Tk() 

    # set the title 
    self.root.title("Black Jack Game")

    # set the size 
    self.root.geometry("500x500") 


   # add instructions label
    self.display1 = tkinter.Label(self.root, text = "=====================================================================================================", 
                                                  font = ('Helvetica', 12)) 
    self.display1.pack()

    self.display2 = tkinter.Label(self.root, text = "1) Blackjacks primary goal is to beat the dealers hand while keeping your hand under a total value of 21", 
                                                  font = ('Helvetica', 12)) 
    self.display2.pack()  

    self.display3 = tkinter.Label(self.root, text = "2) Choosing hit will have you draw another card and add it to your total hands value", 
                                                  font = ('Helvetica', 12)) 
    self.display3.pack()

    self.display4 = tkinter.Label(self.root, text = "3) Choosing stand will lock your hand in and compare it to the dealers", 
                                                  font = ('Helvetica', 12)) 
    self.display4.pack()

    self.display5 = tkinter.Label(self.root, text = "=====================================================================================================", 
                                                  font = ('Helvetica', 12)) 
    self.display5.pack()
    self.prompt1 = Button(self.root, text = "Play Game", command = self.start_game)
    self.prompt2 = Button(self.root, text = "Exit Game", command = self.root.destroy)
    self.prompt1.pack()
    self.prompt2.pack()



    return self.root

  def update_output(self, player, dealer):
    self.display2.configure(text = dealer)
    self.display3.configure(text = player)

  def start_game(self):
    state = True
    self.display1.configure(text = "Game Started")
    self.display2.configure(text = "")
    self.display3.configure(text = "")
    self.display4.configure(text = "")
    self.display5.configure(text = "")

    
    count = 0 # Sets initial turn count to zero
    #game = None # Sets initial game value to None type
    while state == True:
      if(count == 0):
        g = None # Sets initial game value to None type
        g = Game() # Creates game object
      status = g.next() # Progresses the game

      count += 1
      if status == 0: # Monitors game state
        print("You win!!!")
      if state == True:
        count = 0
      elif status == 1: # Monitors game state
        print("You lose.")
      if state == True:
        count = 0
      elif status == 2: # Monitors game state
        print("You tied!")
      if state == True:
        count = 0
    







  

def main():
  system('cls') # Clears terminal
  #Outputs rules
  #before start game
  win = Root()
  root = win.create_window()
  root.mainloop()

  # game over
  print("Thanks for playing!")

main()
