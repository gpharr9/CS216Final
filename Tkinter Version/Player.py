from Hand import Hand
from os import system

class Player:

  def __init__(self): # Creates player hand with a None type
    self.hand = None


  def create_hand(self): # Assigns player hand to Hand object
    self.hand = Hand()
    return self.hand

  
  def print_hand(self): # Prints out intial player hand
    p_arr = self.hand.print(False)
    return p_arr

  

  def collect_input(self): # Gathers unit from user
    ui = "not empty"
    while(ui not in "Hh" and ui not in "Ss"): 
      print("Hit, or Stand (H / S): ") # Determines whether or not the player is going to hit or stand
      ui = input()
      # system('cls')

    return ui

  def count_hand(self): # Iterates through the hand to collect the value of all cards
    x = [str(sub.type[1:]) for sub in self.hand.hand] # Assigns x to determine and pull out the suit of the cards
    total = 0

    for i in range(0, len(x)): #Determines what the cards value will be if the nonsuit is a face card
      if(x[i] == 'j'):
        x[i] = 10
      elif (x[i] == 'a'):
        x[i] = 1
      elif(x[i] == 'q'):
        x[i] = 10
      elif(x[i] == 'k'):
        x[i] = 10

      total += int(x[i]) # Adds all the cards together to get total value
   
    return total
