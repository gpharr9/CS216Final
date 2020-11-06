from Player import Player
from Dealer import Dealer
from Computer import Computer
from os import system

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
        self.ui = self.playerInstance.collect_input()
        pState = self.validatePlayer()
        dState = self.validateDealer()

        if dState == 0 or dState == 1:
            return dState
        if pState == 0 or pState == 1:
            return pState
        
        # system("cls")
        self.print()
    
    
    def makeStand(self):
        pCount = self.playerInstance.count_hand()
        dCount = self.dealerInstance.count_hand()

        # print("Player Count: " + str(pCount))
        # print("Dealer Count: " + str(dCount))

        if(pCount > dCount):
            return 0
        elif(pCount < dCount):
            return 1
        elif(pCount == dCount):
            return 2
    
    
    def print(self):
        print("Player Hand:")
        self.playerInstance.print_hand()

        print("Dealer Hand:")
        self.dealerInstance.print_hand()

    
    def validatePlayer(self):
        # check player count
        if(self.ui in 'Hh'):
            print('player hitting')
            self.dealerInstance.hit(self.playerInstance)
            pCount = self.playerInstance.count_hand()
            print("Player Count: " + str(pCount))

            if(pCount > 21):
                return 1
            elif(pCount == 21):
                return 0
        elif(self.ui in 'Ss'):
            print('player makin a stand')
            state = self.makeStand()
            return state

    def validateDealer(self):
        # check dealer count
        dCount = self.dealerInstance.count_hand()
        print("Dealer Count: " +str(dCount))
        if(dCount > 21):
            return 0
        elif(dCount == 21):
            return 1
        if(dCount < 17):
            print('dealer hitting')
            self.dealerInstance.hit(None)
        elif(dCount > 17):
            print('dealer makin a stand')
            state = self.makeStand()
            return state