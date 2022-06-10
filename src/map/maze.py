from random import shuffle, randrange

from src.gameEngine.playerObject import Player
from src.gameEngine.tilesObject import Tiles


class Maze:
    def __init__(self):
        self.block_size = 24
        self.maze_size = 288
        self.maze = None
        self.wall_blocks = []
        self.free_blocs = []
        self.tiles = Tiles()
        self.player = Player()

    def create_maze(self):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                symbol = self.maze[y][x]
                x_coord = -self.maze_size + (x * self.block_size)
                y_coord = self.maze_size - (y * self.block_size)

                if self.is_wall(symbol):
                    self.tiles.goto(x_coord, y_coord)
                    self.tiles.stamp()
                    self.wall_blocks.append((x, y))
                elif self.is_player(symbol):
                    self.player.showturtle()
                    self.player.goto(x_coord, y_coord)
                else:
                    self.free_blocs.append((x, y))

    def is_wall(self, char):
        if char == self.tiles.label:
            return True
        return False

    def is_player(self, char):
        if char == self.player.label:
            return True
        return False

    def generate_map(self):
        def place_random_player():
            player_pos_y = randrange(0, len(self.maze))
            player_pos_x = randrange(0, len(self.maze[player_pos_y]))
            if self.is_wall(self.maze[player_pos_x][player_pos_y]):
                place_random_player()
            else:
                self.maze[player_pos_x] = self.maze[player_pos_x][:player_pos_y] + "P" + \
                                          self.maze[player_pos_x][player_pos_y + 1:]

        def walk(x, y):
            vis[y][x] = 1

            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]:
                    continue
                if xx == x:
                    hor[max(y, yy)][x] = "O "
                if yy == y:
                    ver[y][max(x, xx)] = "  "
                walk(xx, yy)

        h = w = int(self.block_size / 2)
        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        ver = [["O "] * w + ['O'] for _ in range(h)] + [[]]
        hor = [["OO"] * w + ['O'] for _ in range(h + 1)]

        walk(randrange(w), randrange(h))

        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])

        self.maze = [i for i in s.split("\n") if i]
        place_random_player()
