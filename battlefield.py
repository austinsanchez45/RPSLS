from human_player import Human_player
from ai_player import Ai_player
from gestures import Gestures

class Battlefield:
    def __init__(self):
        self.human_player = Human_player()
        self.ai_player = Ai_player()
        self.player_1 = Human_player()
        self.player_2 = Human_player()

    def run_game(self):
        self.display_welcome()

    def display_rules(self):
	    print("""\nHere are the rules to the game:\nRock crushes Scissors\nScissors cuts Paper\nPaper Covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock""")

    def display_welcome(self):
        need_rules = input("\nWelcome to RPSLS! Do you need to go over the rules? ")
        if need_rules == "yes" or need_rules == "Yes":
            self.display_rules()
            self.human_or_ai()
        elif need_rules == "no" or need_rules == "No":
            self.human_or_ai()
        else: 
            print("Please respond with 'yes' or 'no' ")
            self.display_welcome()

    def human_or_ai(self):
        user_choice = input("\nWould you like to face off against another human or an AI (Type Human or AI)? ")
        if user_choice == "Human" or user_choice == "human":
            self.multiplayer_game()
        if user_choice == "AI" or user_choice == "ai":
            self.single_player_game()
        else:
            print("\nThat's not what I asked you to type! Respond with Human or AI.")
            self.human_or_ai()

    def single_player_game(self):
        while self.human_player.score < 2 and self.ai_player.score < 2:
            self.human_player.gesture_choice()
            print(self.human_player.gesture)
            self.ai_player.gesture_choice()
            print(self.ai_player.gesture)
            if self.human_player.gesture == self.ai_player.gesture:
                print("\nIt's a tie")
                self.human_player.tie_counter += 1
            elif self.human_player.gesture == "Rock":
                if self.ai_player.gesture == "Paper" or self.ai_player.gesture == "Spock":
                    print("\nThe AI won this round!")
                    self.ai_player.score += 1
                else:
                    print("\nPlayer 1 won this round!")
                    self.human_player.score += 1
            elif self.human_player.gesture == "Paper":
                if self.ai_player.gesture == "Scissors" or self.ai_player.gesture == "Lizard":
                    print("\nThe AI won this round!")
                    self.ai_player.score += 1
                else:
                    print("\nPlayer 1 won this round!")
                    self.human_player.score += 1
            elif self.human_player.gesture == "Scissors":
                if self.ai_player.gesture == "Rock" or self.ai_player.gesture == "Spock":
                    print("\nThe AI won this round!")
                    self.ai_player.score += 1
                else:
                    print("\nPlayer 1 won this round!")
                    self.human_player.score += 1
            elif self.human_player.gesture == "Lizard":
                if self.ai_player.gesture == "Rock" or self.ai_player.gesture == "Scissors":
                    print("\nThe AI won this round!")
                    self.ai_player.score += 1
                else:
                    print("\nPlayer 1 won this round!")
                    self.human_player.score += 1
            elif self.human_player.gesture == "Spock":
                if self.ai_player.gesture == "Paper" or self.ai_player.gesture == "Lizard":
                    print("\nThe AI won this round!")
                    self.ai_player.score += 1
                else:
                    print("\nPlayer 1 won this round!")
                    self.human_player.score += 1
        self.single_player_game_winner()

    def single_player_game_winner(self):
        if self.human_player.score == 2:
            print("\nCongrats! You won the game! ")
            self.play_again_option()
        else:
            print("\nThe AI won this time!")
            self.play_again_option()

    def play_again_option(self):
        self.ai_player.score = 0
        self.human_player.score = 0
        self.human_player.tie_counter = 0
        play_again = input("\nDo you want to play again? ")
        if play_again == "Yes" or play_again == "yes" or play_again == "y" or play_again == "Y":
            self.single_player_game()
        else:
            self.thanks_for_playing()

    def multiplayer_game(self):
        while self.player_1.score < 2 and self.player_2.score < 2:
            self.player_1.gesture_choice()
            print(self.player_1.gesture)
            self.player_2.gesture_choice()
            print(self.player_2.gesture)
            if self.player_1.gesture == self.player_2.gesture:
                print("\nIt's a tie")
                self.player_1.tie_counter += 1
            elif self.player_1.gesture == "Rock":
                if self.player_2.gesture == "Paper" or self.player_2.gesture == "Spock":
                    print("\nPlayer 2 won this round!")
                    self.player_2.score += 1
                else:
                    print("\nPlayer 1 won this round!")
                    self.player_1.score += 1
            elif self.player_1.gesture == "Paper":
                if self.player_2.gesture == "Scissors" or self.player_2.gesture == "Lizard":
                    print("\nPlayer 2 won this round!")
                    self.player_2.score += 1
                else:
                    print("\nPlayer 1 won this round!")
                    self.player_1.score += 1
            elif self.player_1.gesture == "Scissors":
                if self.player_2.gesture == "Rock" or self.player_2.gesture == "Spock":
                    print("\nPlayer 2 won this round!")
                    self.player_2.score += 1
                else:
                    print("\nPlayer 1 won this round!")
                    self.player_1.score += 1
            elif self.player_1.gesture == "Lizard":
                if self.player_2.gesture == "Rock" or self.player_2.gesture == "Scissors":
                    print("\nPlayer 2 won this round!")
                    self.player_2.score += 1
                else:
                    print("\nPlayer 1 won this round!")
                    self.player_1.score += 1
            elif self.player_1.gesture == "Spock":
                if self.player_2.gesture == "Paper" or self.player_2.gesture == "Lizard":
                    print("\nPlayer 2 won this round!")
                    self.player_2.score += 1
                else:
                    print("\nPlayer 1 won this round!")
                    self.player_1.score += 1
        self.multiplayer_game_winner()

    def multiplayer_game_winner(self):
        if self.player_1.score == 2:
            print("\nCongrats! Player 1 won the game! ")
            self.play_again_option_mp()
        else:
            print("\nCongrats! Player 2 won the game!")
            self.play_again_option_mp()


    def play_again_option_mp(self):
        self.player_2.score = 0
        self.player_1.score = 0
        self.human_player.tie_counter = 0
        play_again = input("\nDo you want to play again? ")
        if play_again == "Yes" or play_again == "yes" or play_again == "Y" or play_again == "y":
            self.multiplayer_game()
        else:
            self.thanks_for_playing()

    def thanks_for_playing(self):
        print("\nThanks for playing!")
        exit()

# -------------------------------------------------------------------------------------------------------------------------