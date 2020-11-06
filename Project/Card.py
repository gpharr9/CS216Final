from random import randrange

class Card:
  def __init__(self, _options):
    self.type = _options[randrange(len(_options))]

  def print(self, blank):
    suit = self.type[0]
    if(suit == 'c'):   suit = '♣'
    elif(suit == 'd'): suit = '♦'
    elif(suit == 'h'): suit = '♥'
    elif(suit == 's'): suit = '♠'
    else:              suit = '%'
    num  = self.type[1:].upper()

    if(blank):
      num = suit = " "
    cardLayout = """
┌────────────┐
│ {}          │
│            │
│            │
│     {}      │
│            │
│            │
│          {} │
└────────────┘""".format(num,suit,num)
    #cardLayout = cardLayout.join("\n")
    print(cardLayout)