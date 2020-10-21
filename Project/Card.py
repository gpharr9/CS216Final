from random import randrange

class Card:
  def __init__(self, _options):
    self.type = _options[randrange(len(_options))]

  def print():
      print('stuff')
    # add card designs here (switch case maybe?)