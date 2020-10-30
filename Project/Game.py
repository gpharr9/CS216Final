from Player import Player
from Dealer import Dealer
from Computer import Computer

class Game:
    def __init__(self):
        self.playerInstance = Player()
        self.playerInstance.create_hand()

        self.dealerInstance = Dealer()
        self.dealerInstance.create_hand()
        # self.computerInstance = Computer()
        self.step = 0


    def next(self):
        # first step, show deal and player hand
        self.print()

        # second step, prompt the user to what they want to do
        ui = self.playerInstance.collect_input()
        if(ui in 'Hh'):
            self.dealerInstance.hit(self.playerInstance)
            pCount = self.playerInstance.count_hand()

            if(pCount > 21):
                print("You lost, bye.")

        elif(ui in 'Ss'):
            self.makeStand()

        
            
        #self.print()
    
    
    def makeStand(self):
        pCount = self.playerInstance.count_hand()
        dCount = self.dealerInstance.count_hand()

        # print("Player Count: " + str(pCount))
        # print("Dealer Count: " + str(dCount))

        if(pCount > dCount):
            print("Player wins")
        elif(pCount < dCount):
            print("Dealer wins")
        elif(pCount == dCount):
            print("Tie!")
    
    
    def print(self):
        print("Player Hand:")
        self.playerInstance.print_hand()

        print("Dealer Hand:")
        self.dealerInstance.print_hand()

    
    def validateState(self):
        print('validate')


    def verifyUser(self):
        print('verify')