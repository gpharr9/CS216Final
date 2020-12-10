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



        self.step = 0


    def get_p_count(self):
        p_count = self.player_instance.count_hand() # Checks total value of the Player hand

        return p_count


    def get_d_count(self):
        d_count = self.dealer_instance.count_hand() # Checks total value of the Dealer hand

        return d_count

    def make_stand(self):
        p_count = self.player_instance.count_hand() # Checks total value of the Player hand
        d_count = self.dealer_instance.count_hand() # Checks total value of the Dealer hand


        if(p_count > d_count): # Player wins
            return 0
        elif(p_count < d_count): # Dealer wins
            return 1
        elif(p_count == d_count): # Tie game
            return 2


    def condition(self):
        #print("Player Hand:") 
        p_arr = self.player_instance.print_hand() # Outputs the card layout based on player hand to the terminal

        #print("Dealer Hand:")
        d_arr = self.dealer_instance.print_hand() # Outputs the card layout based on dealer hand to the terminal

        return p_arr, d_arr

    

    def p_hit(self):
        self.dealer_instance.hit(self.player_instance)
        p_count = self.player_instance.count_hand()
        if(p_count > 21): # Determines if the player has busted
            return 1
        elif(p_count == 21): # Determines if the player has won
            return 0


    def p_stand(self):
        state = self.make_stand()
        return state


    def validate_dealer(self): # Function to monitor dealer hand and ensure if follows game restrictions
        # check dealer count
        d_count = self.dealer_instance.count_hand() # Gathers dealers hand total value for the logic
        if(d_count > 21): # Determines if the dealer has busted
            return 0
        elif(d_count == 21): # Determines if the dealer has won
            return 1
        if(d_count < 17): # Basic logic to determine dealer action
            self.dealer_instance.hit(None)
        elif(d_count > 17): # Basic logic to determine dealer action
            state = self.make_stand()
            return state
