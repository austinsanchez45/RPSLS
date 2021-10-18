from human_player import Human_player
from ai_player import Ai_player
import random

class Battlefield:
    def __init__(self):
        self.human_player = Human_player()
        self.ai_player = Ai_player()

    def run_game(self):
        self.display_welcome()


    def display_rules(self):
	    print("""
        \nHere are the rules to the game:\nRock crushes Scissors\nScissors cuts Paper\nPaper Covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock""")

    def display_welcome(self):
        need_rules = input("Welcome to RPSLS! Do you need to go over the rules?")
        if need_rules == "yes":
            self.display_rules()
        elif need_rules == "no":
            print("THIS IS A TEST FILLER. GAME SHOULD START FROM HERE.")
            # PLAYER 1 START!!!!!!
        else: 
            print("Please respond with 'yes' or 'no'")
            self.display_welcome()






    # def player_choice(self):
    #     player_gesture = int(input("""What do you want to play? 
    #     \n1 = Rock
    #     \n2 = Paper
    #     \n3 = Scissors
    #     \n4 = Lizard
    #     \n5 = Spock"""))
    #     gesture = player_gesture

    # def ai_choice(self):
    #     gestures =  ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    #     ai_choice = random.choice(gestures)
    #     print(ai_choice)
    #     self.gesture = ai_choice
