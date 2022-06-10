from src.gameEngine.gameObject import GameObject


class Tiles(GameObject):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.label = "O"
