from src.gameEngine.gameObject import GameObject


class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.color("red")
        self.penup()
        self.speed(3)

    @staticmethod
    def get_label():
        return "P"

    def go_up(self):
        next_x = self.xcor()
        next_y = self.ycor() + self.block_size
        if not self.check_wall(next_x, next_y):
            self.goto(next_x, next_y)

    def go_down(self):
        next_x = self.xcor()
        next_y = self.ycor() - self.block_size
        if not self.check_wall(next_x, next_y):
            self.goto(next_x, next_y)

    def go_left(self):
        next_x = self.xcor() - self.block_size
        next_y = self.ycor()
        if not self.check_wall(next_x, next_y):
            self.goto(next_x, next_y)

    def go_right(self):
        next_x = self.xcor() + self.block_size
        next_y = self.ycor()
        if not self.check_wall(next_x, next_y):
            self.goto(next_x, next_y)
