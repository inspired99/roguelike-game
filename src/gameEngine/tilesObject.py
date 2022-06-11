import turtle
from pathlib import Path

from src.gameEngine.gameObject import GameObject


class Tiles(GameObject):
    def __init__(self):
        super().__init__()
        turtle.register_shape(str(Path(__file__).resolve().parent.parent) + "/resources/tree.gif")
        self.shape(str(Path(__file__).resolve().parent.parent) + "/resources/tree.gif")
        self.penup()
        self.speed(0)

    @staticmethod
    def get_label():
        return "W"
