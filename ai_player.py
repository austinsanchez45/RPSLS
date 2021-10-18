from player import Players
import random

class Ai_player(Players):
    def __init__(self):
        super().__init__()

    def gesture_choice(self):
        self.gestures_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        ai_choice = random.choice(self.gestures_list)
        self.gesture = ai_choice
