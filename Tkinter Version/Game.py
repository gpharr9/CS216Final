from Player import Player
from Dealer import Dealer
from Computer import Computer
from os import system

class Game:
    def __init__(self): # Creation of Dealer and Player objects
                        # and their respective hands
        self.player_instance = Player() # Player Object
        self.player_instance.create_hand() # Player Hand

        self.dealer_instance = Dealer() # Dealer Object
        self.dealer_instance.create_hand() # Dealer Hand
        # self.computer_instance = Computer()
        self.step = 0


#    def next(self): # Primary game controller, allows everything to progress
#        # first step, show deal and player hand
#        player, dealer = self.print()
#        # second step, prompt the user to what they want to do
#        #self.ui = self.player_instance.collect_input()

#        if(d_state == 0 and p_state == 1): # Determines if the game is a tie of 21
#            return 2

#        if d_state == 0 or d_state == 1: # Determines if the game has a winner or not
#            return d_state
#        if p_state == 0 or p_state == 1: # Determines if the game has a winner or not
#            return p_state
        
        # system("cls")

#        self.print() # Prints out hands
        
        
    def get_count(self):
        self.p_count = self.player_instance.count_hand() # Checks total value of the Player hand
        
        self.d_count = self.dealer_instance.count_hand() # Checks total value of the Dealer hand

        return self.p_count, self.d_count


    def make_stand(self):
        self.p_count = self.player_instance.count_hand() # Checks total value of the Player hand
        self.d_count = self.dealer_instance.count_hand() # Checks total value of the Dealer hand

        # print("Player Count: " + str(pCount))
        # print("Dealer Count: " + str(dCount))

        if(self.p_count > self.d_count): # Player wins
            return 0
        elif(self.p_count < self.d_count): # Dealer wins
            return 1
        elif(self.p_count == self.d_count): # Tie game
            return 2
    
    
    def condition(self):
        #print("Player Hand:") 
        p_arr = self.player_instance.print_hand() # Outputs the card layout based on player hand to the terminal

        #print("Dealer Hand:")
        d_arr = self.dealer_instance.print_hand() # Outputs the card layout based on dealer hand to the terminal

        return p_arr, d_arr

    

    def p_hit(self):
        self.dealer_instance.hit(self.player_instance)
        self.p_count = self.player_instance.count_hand()
        if(self.p_count > 21): # Determines if the player has busted
            return 1
        elif(self.p_count == 21): # Determines if the player has won
            return 0


    def p_stand(self):
        state = self.make_stand()
        return state


#    def validate_player(self): # Function to monitor player hand and ensure it follows game restrictions
#        # check player count
#        if(self.ui in 'Hh'): # Uses user input gathered in Player subclass to find if hitting or standing
#            print('player hitting')
#            self.dealer_instance.hit(self.player_instance) # Sends data to dealer in order to hit
#            p_count = self.player_instance.count_hand() # Determines hands total value
#            print("Player Count: " + str(p_count)) # Used for validating that code is working

#          if(p_count > 21): # Determines if the player has busted
#                return 1
#            elif(p_count == 21): # Determines if the player has won
#                return 0
#        elif(self.ui in 'Ss'): # Prepares the players hand to end game
#            print('player makin a stand')
#            state = self.make_stand()
#            return state

    def validate_dealer(self): # Function to monitor dealer hand and ensure if follows game restrictions
        # check dealer count
        self.d_count = self.dealer_instance.count_hand() # Gathers dealers hand total value for the logic
#        print("Dealer Count: " +str(d_count)) # Used for code validation
        if(self.d_count > 21): # Determines if the dealer has busted
            return 0
        elif(self.d_count == 21): # Determines if the dealer has won
            return 1
        if(self.d_count < 17): # Basic logic to determine dealer action
            #print('dealer hitting')
            self.dealer_instance.hit(None)
        elif(self.d_count > 17): # Basic logic to determine dealer action
            #print('dealer makin a stand')
            state = self.make_stand()
            return state
