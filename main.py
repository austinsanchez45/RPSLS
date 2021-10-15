class Battlefield:
    def __init__(self):
	    pass

    def run_battle(self):
        game_start = self.display_welcome()
	game_rules = self.display_rules()
        if game_start:
            play_again = "Yes"
            while play_again == "Yes":
                self.display_winners(self.battle())
                play_again = input("\nDo you want to play again(Yes or No)? ")
                

    def display_welcome(self):
        game_start = int(input("""
        \nRock Paper Scissors Lizard Spock!
        \nPress 1 to play!
        \n"""))
        if  game_start == 1:
            return True
        else:
            return False

    def display_rules(self):
	    print("""
	    \nHere are the rules to the game:
	    \nRock crushes Scissors
	    \nScissors cuts Paper
	    \nPaper Covers Rock
	    \nRock crushes Lizard
	    \nLizard poisons Spock
	    \nSpock smashes Scissors
	    \nScissors decapitates Lizard
	    \nLizard eats Paper
	    \nPaper disproves Spock
	    \nSpock vaporizes Rock""")