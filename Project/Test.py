from Hand import Hand

tempHand = Hand()
print(tempHand.hand)

while True:
  print("Would you like to draw again? (Y/N)")
  ui = input(); ui.lower()

  if ui in 'y':
    tempHand.addCard()
    print()
    print(tempHand.hand)
  elif ui in 'n':
    exit()
  else:
    print("no.")