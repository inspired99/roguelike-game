import turtle
from pathlib import Path

from src.gameEngine.gameObject import GameObject


class Ally(GameObject):
    def __init__(self):
        super().__init__()
        turtle.register_shape(str(Path(__file__).resolve().parent.parent) + "/resources/wizard.gif")
        self.shape(str(Path(__file__).resolve().parent.parent) + "/resources/wizard.gif")
        self.hideturtle()
        self.penup()
        self.speed(3)

    @staticmethod
    def get_label():
        return "A"

    def set_x_y(self, x, y):
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
