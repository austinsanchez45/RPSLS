from human_player import Human_player
from ai_player import Ai_player
from human_player_2 import Human_player_2

class Battlefield:
    def __init__(self):
        self.human_player = Human_player()
        self.ai_player = Ai_player()
        self.human_player_2 = Human_player_2()

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
        user_choice = input("Would you like to face off against another human or an AI (Type Human or AI)? ")
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
            if self.human_player.gesture == "Rock":
                if self.ai_player.gesture == "Paper" or self.ai_player.gesture == "Spock":
                    print("The AI won this round!")
                    self.ai_player.score += 1
                else:
                    print("Player 1 won this round!")
                    self.human_player.score += 1
            elif self.human_player.gesture == "Paper":
                if self.ai_player.gesture == "Scissors" or self.ai_player.gesture == "Lizard":
                    print("The AI won this round!")
                    self.ai_player.score += 1
                else:
                    print("Player 1 won this round!")
                    self.human_player.score += 1
            elif self.human_player.gesture == "Scissors":
                if self.ai_player.gesture == "Rock" or self.ai_player.gesture == "Spock":
                    print("The AI won this round!")
                    self.ai_player.score += 1
                else:
                    print("Player 1 won this round!")
                    self.human_player.score += 1
            elif self.human_player.gesture == "Lizard":
                if self.ai_player.gesture == "Rock" or self.ai_player.gesture == "Scissors":
                    print("The AI won this round!")
                    self.ai_player.score += 1
                else:
                    print("Player 1 won this round!")
                    self.human_player.score += 1
            elif self.human_player.gesture == "Spock":
                if self.ai_player.gesture == "Paper" or self.ai_player.gesture == "Lizard":
                    print("The AI won this round!")
                    self.ai_player.score += 1
                else:
                    print("Player 1 won this round!")
                    self.human_player.score += 1
        self.single_player_game_winner()
            
    def single_player_game_winner(self):
        if self.human_player.score == 2:
            print("Congrats! You won the game! ")
            self.play_again_option()
        else:
            print("The AI won this time!")
            self.play_again_option()

    def play_again_option(self):
        self.ai_player.score = 0
        self.human_player.score = 0
        play_again = input("Do you want to play again? ")
        if play_again == "Yes":
            self.single_player_game()
        else:
            self.thanks_for_playing()

    def multiplayer_game(self):
        while self.human_player.score < 2 and self.human_player_2.score < 2:
            self.human_player.gesture_choice()
            print(self.human_player.gesture)
            self.human_player_2.gesture_choice()
            print(self.human_player_2.gesture)
            if self.human_player.gesture == "Rock":
                if self.human_player_2.gesture == "Paper" or self.human_player_2.gesture == "Spock":
                    print("Player 2 won this round!")
                    self.human_player_2.score += 1
                else:
                    print("Player 1 won this round!")
                    self.human_player.score += 1
            elif self.human_player.gesture == "Paper":
                if self.human_player_2.gesture == "Scissors" or self.human_player_2.gesture == "Lizard":
                    print("Player 2 won this round!")
                    self.human_player_2.score += 1
                else:
                    print("Player 1 won this round!")
                    self.human_player.score += 1
            elif self.human_player.gesture == "Scissors":
                if self.human_player_2.gesture == "Rock" or self.human_player_2.gesture == "Spock":
                    print("Player 2 won this round!")
                    self.human_player_2.score += 1
                else:
                    print("Player 1 won this round!")
                    self.human_player.score += 1
            elif self.human_player.gesture == "Lizard":
                if self.human_player_2.gesture == "Rock" or self.human_player_2.gesture == "Scissors":
                    print("Player 2 won this round!")
                    self.human_player_2.score += 1
                else:
                    print("Player 1 won this round!")
                    self.human_player.score += 1
            elif self.human_player.gesture == "Spock":
                if self.human_player_2.gesture == "Paper" or self.human_player_2.gesture == "Lizard":
                    print("Player 2 won this round!")
                    self.human_player_2.score += 1
                else:
                    print("Player 1 won this round!")
                    self.human_player.score += 1
        self.multiplayer_game_winner()

    def multiplayer_game_winner(self):
        if self.human_player.score == 2:
            print("Congrats! Player 1 won the game! ")
            self.play_again_option_mp()
        else:
            print("Congrats! Player 2 won the game!")
            self.play_again_option_mp()


    def play_again_option_mp(self):
        self.human_player_2.score = 0
        self.human_player.score = 0
        play_again = input("Do you want to play again? ")
        if play_again == "Yes":
            self.multiplayer_game()
        else:
            self.thanks_for_playing()

    def thanks_for_playing(self):
        print("Thanks for playing!")
        exit()
        
# -------------------------------------------------------------------------------------------------------------------------