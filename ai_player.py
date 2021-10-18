from player import Players

class Ai_player:
    def __init__(self):
        self.ai_gesture = None
        super().__init__()

    def gesture_choice(self):
        gestures =  ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        ai_choice = random.choice(gestures)
        print(ai_choice)
        self.gesture = ai_choice
