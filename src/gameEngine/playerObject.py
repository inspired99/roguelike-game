from src.gameEngine.gameObject import GameObject


class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.color("red")
        self.penup()
        self.speed(3)
        self.label = "P"
