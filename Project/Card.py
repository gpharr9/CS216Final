from random import randrange

class Card:
  def __init__(self, _options): # Preparation of type variable passed in Hand options
    self.type = _options[randrange(len(_options))]

  def print(self, blank): # Assigning of suit visuals
                          # Break up logic and output to allow unit testing
    suit = self.type[0]
    if(suit == 'c'):   suit = '♣' 
    elif(suit == 'd'): suit = '♦'
    elif(suit == 'h'): suit = '♥'
    elif(suit == 's'): suit = '♠'
    else:              suit = '%'
    num  = self.type[1:].upper()

    if(blank): # Allows the hidden card on the dealer by having a no suit, no number card
      num = suit = " "
    card_layout = """ 
┌────────────┐   
│ {}          │
│            │
│            │
│     {}      │
│            │
│            │
│          {} │
└────────────┘""".format(num,suit,num) # Basic card layout, which has the various suit options plugged in
    #cardLayout = cardLayout.join("\n")
    print(card_layout)

    