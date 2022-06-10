import turtle

from src.map.maze import Maze


class App:
    def __init__(self):
        self.running = None
        self.resolution = (1024, 980)
        self.length = self.resolution[0]
        self.width = self.resolution[1]
        self.window = turtle.Screen()
        self.window.bgcolor("black")
        self.window.title("Roguelike Game")
        self.window.setup(self.length, self.width)
        self.window.listen()
        self.window.onkey(self.turn_off_render, "r")
        self.window.onkey(self.turn_off_render, "R")
        self.window.onkey(self.game_over, "q")
        self.window.onkey(self.game_over, "Q")

    def turn_off_render(self):
        self.window.tracer(0)

    def game_over(self):
        self.running = False

    def run(self):
        self.running = True
        maze = Maze()
        maze.generate_map()
        maze.create_maze()

        while self.running:
            self.window.update()

        self.window.bye()
