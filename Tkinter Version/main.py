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


from Game import *
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
    height = self.root.winfo_screenheight()
    width = self.root.winfo_screenwidth()
    self.root.geometry(str(height) + "x" + str(width))


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
    p_count, d_count = self.g.get_count()
    
    self.display1.configure(text = "Dealer Count: " + str(d_count))
    self.display2.configure(text = dealer)
    self.display3.configure(text = "Player Count: " + str(p_count))
    
    self.display4.configure(text = player)



  def hit(self):
    self.g.validate_dealer()
    self.g.p_hit()
    player, dealer = self.g.condition()

    self.update_output(player, dealer)


  def stand(self):
    self.g.validate_dealer()
    self.g.p_stand()
    player, dealer = self.g.condition()

    self.update_output(player, dealer)

  def start_game(self):
    self.display1.configure(text = "Dealer Hand")
    self.display2.configure(text = "")
    self.display3.configure(text = "Player Hand")
    self.display4.configure(text = "")
    self.display5.configure(text = "")

    #self.display1.place(relx = 0.5, rely = 0.5)
    #self.display2.place(relx = 125, rely = 125)
    #self.display3.place(relx = 250, rely = 250)
    #self.display4.place(relx = 375, rely = 375)
    #self.prompt1.place(relx = 125, rely = 500)
    #self.prompt1.place(relx = 375, rely = 500)

    self.prompt1.configure(text = "Hit", command = self.hit)
    self.prompt2.configure(text = "Stand", command = self.stand)
    self.count = 0 # Sets initial turn count to zero
    self.state = True
    self.status = None
    #game = None # Sets initial game value to None type

    self.next()
    


  def win(self):
    self.display1.configure(text = "Congratulations!")
    self.display2.configure(text = "You win!")
    self.display3.configure(text = "")
    self.display4.configure(text = "")
    self.display5.configure(text = "Would you like to play again?")

    self.prompt1.configure(text = "Yes", command = self.start_game)
    self.prompt2.configure(text = "No", command = self.root.destroy)


  def lose(self):
    self.display1.configure(text = ":(")
    self.display2.configure(text = "You lose!")
    self.display3.configure(text = "")
    self.display4.configure(text = "")
    self.display5.configure(text = "Would you like to play again?")

    self.prompt1.configure(text = "Yes", command = self.start_game)
    self.prompt2.configure(text = "No", command = self.root.destroy)


  def tie(self):
    self.display1.configure(text = "Tie game!")
    self.display2.configure(text = "")
    self.display3.configure(text = "")
    self.display4.configure(text = "")
    self.display5.configure(text = "Would you like to play again?")

    self.prompt1.configure(text = "Yes", command = self.start_game)
    self.prompt2.configure(text = "No", command = self.root.destroy)
  


  def next(self):
    while self.state == True:
      if(self.count == 0):
        self.g = None # Sets initial game value to None type
        self.g = Game() # Creates game object
      #status = self.g.next() # Progresses the game

      player, dealer = self.g.condition()
      self.count += 1
      self.update_output(player, dealer)

      if self.status == 0: # Monitors game state
        self.win()
      elif self.status == 1: # Monitors game state
        self.lose()
      elif self.status == 2: # Monitors game state
        self.tie()


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
