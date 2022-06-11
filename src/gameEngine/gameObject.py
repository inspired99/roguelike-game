import math
import turtle
from abc import ABC, abstractmethod


class GameObject(turtle.Turtle, ABC):
    """
    Abstract class because in turtle
    lib we define init method
    and set up everything inside it for objects
    """

    @abstractmethod
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.block_size = 24
        self.label = None
        self.walls_blocks = None
        self.x = None
        self.y = None

    @staticmethod
    @abstractmethod
    def get_label():
        return ""

    def set_walls(self, walls):
        self.walls_blocks = walls

    def check_wall(self, x, y):
        if not self.walls_blocks:
            return False
        if (x, y) in self.walls_blocks:
            return True
        return False

    def is_collision(self, obj):
        x = self.xcor() - obj.xcor()
        y = self.ycor() - obj.ycor()
        dist = math.sqrt((x ** 2) + (y ** 2))

        if dist < 5:
            return True
        return False
