import turtle
from pathlib import Path

from src.map.maze import Maze


class App:
    def __init__(self):
        self.running = None
        self.resolution = (1024, 980)
        self.length = self.resolution[0]
        self.width = self.resolution[1]
        self.window = turtle.Screen()
        self.maze = Maze()
        self.player = self.maze.get_player()
        self.set_up_window()
        self.set_up_player_control()

    def set_up_window(self):
        self.window.bgpic(str(Path(__file__).resolve().parent.parent) + "/resources/background.gif")
        self.window.title("Roguelike Game")
        self.window.setup(self.length, self.width)
        self.window.listen()
        self.window.onkey(self.turn_off_render, "r")
        self.window.onkey(self.turn_off_render, "R")
        self.window.onkey(self.game_over, "F")
        self.window.onkey(self.game_over, "f")

    def set_up_player_control(self):
        turtle.listen()
        turtle.onkey(self.player.go_left, "Left")
        turtle.onkey(self.player.go_right, "Right")
        turtle.onkey(self.player.go_up, "Up")
        turtle.onkey(self.player.go_down, "Down")

    def turn_off_render(self):
        self.window.tracer(0)

    def game_over(self):
        self.running = False

    def run(self):
        self.running = True
        self.maze.generate_map()
        self.maze.create_maze()

        while self.running:
            self.maze.check_enemies_collapsed()
            if self.maze.check_wizard_reached():
                self.window.ontimer(self.game_over, 1000)

            self.window.update()

        self.window.bye()
