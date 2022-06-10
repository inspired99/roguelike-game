import turtle
from abc import ABC, abstractmethod


class GameObject(turtle.Turtle, ABC):

    # in turtle lib we define init method
    # and set up everything inside it
    @abstractmethod
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.label = None
