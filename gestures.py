

class Gestures:
    def __init__(self, name, gesture_loses_to):
        self.name = name
        self.gesture_loses_to = gesture_loses_to
        self.gesture_choices(name, gesture_loses_to)


    def gesture_choices(self, name, gesture_loses_to):
        if self.name == "Rock":
            self.gesture_loses_to = ["Paper", "Spock"]
        elif self.name == "Paper":
            self.gesture_loses_to = ["Scissors", "Lizard"]
        elif self.name == "Scissors":
            self.gesture_loses_to = ["Rock", "Spock"]
        elif self.name == "Lizard":
            self.gesture_loses_to = ["Rock", "Scissors"]
        elif self.name == "Spock":
            self.gesture_loses_to = ["Paper", "Lizard"]

