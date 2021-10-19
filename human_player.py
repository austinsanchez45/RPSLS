from player import Players

class Human_player(Players):
    def __init__(self):
        self.tie_counter = 0
        super().__init__()

    def gesture_choice(self):
        player_one_gesture = input("""\nWhat do you want to play player 1? \nRock, Paper, Scissors, Lizard, or Spock: """)
        if player_one_gesture != "Rock" and player_one_gesture != "Paper" and player_one_gesture != "Scissors" and player_one_gesture != "Lizard" and player_one_gesture != "Spock":
            print("\nPlease respond with Rock, Paper, Scissors, Lizard, Spock. (Case sensitive).\n")
            self.gesture_choice()
        else:
            self.gesture = player_one_gesture
