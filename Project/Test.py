from Hand import Hand

tempHand = Hand()
print(tempHand.hand)

while True:
  print("Would you like to draw again? (Y/N)")
  ui = input();

  if ui in 'Yy':
    tempHand.addCard()
    print()
    print(tempHand.hand)
  elif ui in 'Nn':
    exit()
  else:
    print("no.")
