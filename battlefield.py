from human_player import Human_player
from ai_player import Ai_player

class Battlefield:
    def __init__(self):
        self.human_player = Human_player()
        self.ai_player = Ai_player()

    def run_game(self):
        self.display_welcome()


    def display_rules(self):
	    print("""\nHere are the rules to the game:\nRock crushes Scissors\nScissors cuts Paper\nPaper Covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock""")

    def display_welcome(self):
        need_rules = input("Welcome to RPSLS! Do you need to go over the rules?")
        if need_rules == "yes":
            self.display_rules()
            self.human_or_ai()
        elif need_rules == "no":
            self.human_or_ai()

            # PLAYER 1 START!!!!!!
        else: 
            print("Please respond with 'yes' or 'no'")
            self.display_welcome()



    def single_player_game(self):
        print("Player 1 goes first!")

    def multiplayer_game(self):
        pass


    def human_or_ai(self):
        user_choice = input("Would you like to face off against another human or an ai(Type Human or AI)? ")
        if user_choice == "Human":
            self.single_player_game()
        if user_choice == "AI":
            self.multiplayer_game()
        else:
            print("That's not what I asked you to type!")
            self.human_or_ai()



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
