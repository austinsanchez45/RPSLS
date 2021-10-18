from player import Players
import random

class Ai_player:
    def __init__(self):
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        super().__init__()

    def gesture_choice(self):
        print("""Here are the gestures you can choose from: 
        \n1 = Rock
        \n2 = Paper
        \n3 = Scissors
        \n4 = Lizard
        \n5 = Spock""")
        # ai_choice = random.choice(self.gestures)
        # print(ai_choice)
        # self.gesture = ai_choice
