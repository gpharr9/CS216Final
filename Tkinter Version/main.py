# Sources: https://github.com/wtran29/Blackjack-Tkinter
# This program runs a blackjack game using Tkinter as well as several different imports

from Game import *
from os import system
import tkinter
from tkinter import *

class Root():
    
  def create_window(self):
    # create a GUI window 
    self.root = tkinter.Tk() 

    # configuring the window
    self.root.title("Black Jack Game")
    self.root.configure(bg = 'sea green')
    # set the size
    height = self.root.winfo_screenheight()
    width = self.root.winfo_screenwidth()
    self.root.geometry(str(height) + "x" + str(width))


   # add display labels
    self.display1 = tkinter.Label(self.root, text = "=====================================================================================================", 
                                                  font = ('Helvetica', 12),) 
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
    
    self.display1.configure(fg = 'light cyan', bg = 'sea green')
    self.display2.configure(fg = 'light cyan', bg = 'sea green')
    self.display3.configure(fg = 'light cyan', bg = 'sea green')
    self.display4.configure(fg = 'light cyan', bg = 'sea green')
    self.display5.configure(fg = 'light cyan', bg = 'sea green')
    # Create buttons for user control
    self.prompt1 = Button(self.root, text = "Play Game", command = self.start_game, bg = 'red', fg = 'white')
    self.prompt2 = Button(self.root, text = "Exit Game", command = self.root.destroy, bg = 'red', fg = 'white')
    self.prompt1.pack()
    self.prompt2.pack()

    return self.root


  def update_output(self, player, dealer):
    p_count = self.g.get_p_count() # getting the total value of the player hand from Game.py

    self.display1.configure(text = "Dealer Hand")
    self.display2.configure(text = dealer) # Outputting dealers cards
    self.display3.configure(text = "Player Count: " + str(p_count)) # Telling the player their current hand value
    self.display4.configure(text = player) # Outputting players cards


  def hit(self):
    self.g.validate_dealer() # Allowing dealer to hit or stand
    self.g.p_hit() # Allowing player to add a card to their deck
    
    # Getting the total value of the dealer and player hands from Game.py
    p_count = self.g.get_p_count()
    d_count = self.g.get_d_count()

    if p_count > 21: # Testing if player has busted
      self.lose() # Running losing parameters
    elif d_count > 21: # Testing is the dealer has busted
      self.win() # Running winning parameters
    else: # If both counts are valid
      player, dealer = self.g.condition() # Getting the hands
      self.update_output(player, dealer) # Outputting hands to Tkinter


  def stand(self):
    self.g.validate_dealer() # Allowing dealer to hit or stand
    self.g.p_stand() # Allowing player to set final card value
    
    # Getting the total value of the dealer and player hands from Game.py
    p_count = self.g.get_p_count()
    d_count = self.g.get_d_count()
  
    if p_count > 21: # Testing if player has busted
      self.lose() # Running losing parameters
    elif d_count > 21: # Testing is the dealer has busted
      self.win() # Running winning parameters
    elif p_count == d_count: # Testing if there is a tie
      self.tie() # Running tie parameters
    else: # If both counts are valid
      self.end_game() # Ending game with final test parameters


  def start_game(self):
    # Initializing displays for game
    self.display1.configure(text = "Dealer Hand") 
    self.display2.configure(text = "")
    self.display3.configure(text = "Player Hand")
    self.display4.configure(text = "")
    self.display5.configure(text = "")

    # Updating buttons for game
    self.prompt1.configure(text = "Hit", command = self.hit)
    self.prompt2.configure(text = "Stand", command = self.stand)

    self.g = None # Sets initial game value to None type
    self.g = Game() # Creates new game object
    player, dealer = self.g.condition() # Gets initial dealer and player hands
    self.update_output(player, dealer) # Outputs initial dealer and player hands


  def win(self):

    # Getting the total value of the dealer and player hands from Game.py
    p_count = self.g.get_p_count()
    d_count = self.g.get_d_count()

    # Outputting win parameters
    self.display1.configure(text = "Congratulations!")
    self.display2.configure(text = "You win!")
    self.display3.configure(text = "Player Count: " + str(p_count))
    self.display4.configure(text = "Dealer Count: " + str(d_count))
    self.display5.configure(text = "Would you like to play again?")
    # Updating buttons to have user decide to play again or not
    self.prompt1.configure(text = "Yes", command = self.start_game)
    self.prompt2.configure(text = "No", command = self.root.destroy)


  def lose(self):

    # Getting the total value of the dealer and player hands from Game.py
    p_count = self.g.get_p_count()
    d_count = self.g.get_d_count()

    # Outputting losing parameters
    self.display1.configure(text = ":(")
    self.display2.configure(text = "You lose!")
    self.display3.configure(text = "Player Count: " + str(p_count))
    self.display4.configure(text = "Dealer Count: " + str(d_count))
    self.display5.configure(text = "Would you like to play again?")
    # Updating buttons to have user decide to play again or not
    self.prompt1.configure(text = "Yes", command = self.start_game)
    self.prompt2.configure(text = "No", command = self.root.destroy)


  def end_game(self):

    # Getting the total value of the dealer and player hands from Game.py
    p_count = self.g.get_p_count()
    d_count = self.g.get_d_count()

    # Testing for winner
    if p_count > d_count:
      self.win()
    elif p_count < d_count:
      self.lose()
    elif p_count == d_count:
      self.tie()


  def tie(self):
    
    # Getting the total value of the dealer and player hands from Game.py
    p_count = self.g.get_p_count()
    d_count = self.g.get_d_count()

    # Outputting tie game parameters
    self.display1.configure(text = "Tie game!")
    self.display3.configure(text = "Player Count: " + str(p_count))
    self.display4.configure(text = "Dealer Count: " + str(d_count))
    self.display4.configure(text = "")
    self.display5.configure(text = "Would you like to play again?")
    # Updating buttons to have user decide to play again or not
    self.prompt1.configure(text = "Yes", command = self.start_game)
    self.prompt2.configure(text = "No", command = self.root.destroy)


def main():
  system('cls') # Clears terminal
  win = Root() # Creates Root object
  root = win.create_window() # Creates initial window
  root.mainloop() # Starts the windows mainloop


main()
