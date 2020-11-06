from Hand import Hand
from os import system

class Player:

  def __init__(self):
    self.hand = None


  def create_hand(self):
    self.hand = Hand()
    return self.hand

  
  def print_hand(self):
    self.hand.print(False)
  

  def collect_input(self):
    ui = "not empty"
    while(ui not in "Hh" and ui not in "Ss"):
      print("Hit, or Stand (H / S): ")
      ui = input()
      # system('cls')

    return ui

  def count_hand(self):
    x = [str(sub.type[1:]) for sub in self.hand.hand]
    total = 0

    for i in range(0, len(x)):
      if(x[i] == 'j'):
        x[i] = 10
      elif (x[i] == 'a'):
        x[i] = 1
      elif(x[i] == 'q'):
        x[i] = 10
      elif(x[i] == 'k'):
        x[i] = 10

      total += int(x[i])
   
    return total