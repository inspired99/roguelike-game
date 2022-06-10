from src.gameEngine.gameObject import GameObject


class Treasure(GameObject):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed(3)
        self.x = None
        self.y = None

    @staticmethod
    def get_label():
        return "T"

    def set_x_y(self, x, y):
        self.x = x
        self.y = y
        self.showturtle()
        self.goto(self.x, self.y)

    def collect(self):
        self.hideturtle()
