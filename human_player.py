from player import Players

class Human_player(Players):
    def __init__(self):
        super().__init__()

    def gesture_choice(self):
        player_one_gesture = int(input("""What do you want to play? 
        \n1 = Rock
        \n2 = Paper
        \n3 = Scissors
        \n4 = Lizard
        \n5 = Spock"""))
        self.gesture = player_one_gesture
