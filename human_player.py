from player import Players

class Human_player(Players):
    def __init__(self):
        super().__init__()

    def gesture_choice(self):
        player_one_gesture = input("""What do you want to play? \nRock, Paper, Scissors, Lizard, or Spock """)
        self.gesture = player_one_gesture
