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
    
    p_count, d_count = self.g.get_count()

    if p_count > 21:
      self.lose()
    elif d_count > 21:
      self.win()
    else:
      player, dealer = self.g.condition()
      self.update_output(player, dealer)


  def stand(self):
    self.g.validate_dealer()
    self.g.p_stand()
    
    
    p_count, d_count = self.g.get_count()
    if p_count > 21:
      self.lose()
    elif d_count > 21:
      self.win()
    elif p_count == d_count:
      self.tie()
    else:
      player, dealer = self.g.condition()
      self.update_output(player, dealer)

  def start_game(self):
    self.display1.configure(text = "Dealer Hand")
    self.display2.configure(text = "")
    self.display3.configure(text = "Player Hand")
    self.display4.configure(text = "")
    self.display5.configure(text = "")
    self.prompt1.configure(text = "Hit", command = self.hit)
    self.prompt2.configure(text = "Stand", command = self.stand)

    self.g = None # Sets initial game value to None type
    self.g = Game()


  def win(self):
    p_count, d_count = self.g.get_count()
    
    self.display1.configure(text = "Congratulations!")
    self.display2.configure(text = "You win!")
    self.display3.configure(text = "Player Count: " + str(p_count))
    self.display4.configure(text = "Dealer Count: " + str(d_count))
    self.display5.configure(text = "Would you like to play again?")

    self.prompt1.configure(text = "Yes", command = self.start_game)
    self.prompt2.configure(text = "No", command = self.root.destroy)


  def lose(self):
    p_count, d_count = self.g.get_count()
    
    self.display1.configure(text = ":(")
    self.display2.configure(text = "You lose!")
    self.display3.configure(text = "Player Count: " + str(p_count))
    self.display4.configure(text = "Dealer Count: " + str(d_count))
    self.display5.configure(text = "Would you like to play again?")

    self.prompt1.configure(text = "Yes", command = self.start_game)
    self.prompt2.configure(text = "No", command = self.root.destroy)


  def tie(self):
    p_count, d_count = self.g.get_count()


    self.display1.configure(text = "Tie game!")
    self.display3.configure(text = "Player Count: " + str(p_count))
    self.display4.configure(text = "Dealer Count: " + str(d_count))
    self.display4.configure(text = "")
    self.display5.configure(text = "Would you like to play again?")

    self.prompt1.configure(text = "Yes", command = self.start_game)
    self.prompt2.configure(text = "No", command = self.root.destroy)


def main():
  system('cls') # Clears terminal
  win = Root()
  root = win.create_window()
  root.mainloop()

  # game over
  print("Thanks for playing!")

main()
