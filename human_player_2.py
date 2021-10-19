from player import Players

class Human_player_2(Players):
    def __init__(self):
        super().__init__()

    def gesture_choice(self):
        player_one_gesture = input("""\nWhat do you want to play player 2? \nRock, Paper, Scissors, Lizard, or Spock: """)
        if player_one_gesture != "Rock" and player_one_gesture != "Paper" and player_one_gesture != "Scissors" and player_one_gesture != "Lizard" and player_one_gesture != "Spock":
            print("\nPlease respond with Rock, Paper, Scissors, Lizard, Spock. (Case sensitive).\n")
            self.gesture_choice()
        else:
            self.gesture = player_one_gesture