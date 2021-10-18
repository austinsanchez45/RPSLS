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
        need_rules = input("Welcome to RPSLS! Do you need to go over the rules? ")
        if need_rules == "yes":
            self.display_rules()
            self.human_or_ai()
        elif need_rules == "no":
            self.human_or_ai()

            # PLAYER 1 START!!!!!!
        else: 
            print("Please respond with 'yes' or 'no' ")
            self.display_welcome()




    def human_or_ai(self):
        user_choice = input("Would you like to face off against another human or an ai(Type Human or AI)? ")
        if user_choice == "Human":
            self.multiplayer_game()
        if user_choice == "AI":
            self.single_player_game()
        else:
            print("That's not what I asked you to type!")
            self.human_or_ai()

    def single_player_game(self):
        while self.human_player.score < 2 and self.ai_player.score < 2:
            self.human_player.gesture_choice()
            print(self.human_player.gesture)
            self.ai_player.gesture_choice()
            print(self.ai_player.gesture)
            if (self.human_player.gesture == "Rock" and self.ai_player.gesture == "Paper") or (self.human_player.gesture == "Rock" and self.ai_player.gesture == "Spock"):
                self.ai_player.score += 1
                print(f"The AI won this round! It's score is now {self.ai_player.score}")


    def multiplayer_game(self):
        pass



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
