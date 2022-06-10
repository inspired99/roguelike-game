from random import shuffle, randrange

from src.gameEngine.playerObject import Player
from src.gameEngine.tilesObject import Tiles
from src.gameEngine.treasureObject import Treasure


class Maze:
    def __init__(self):
        self.maze = None
        self.wall_blocks = []
        self.free_blocs = []
        self.tiles = None
        self.player = None
        self.tiles = Tiles()
        self.player = Player()
        self.treasures = []
        self.block_size = self.tiles.block_size
        self.maze_size = int(25 * self.block_size / 2 - self.block_size / 2)

    def get_player(self):
        return self.player

    def get_block_size(self):
        return self.block_size

    def get_walls(self):
        return self.wall_blocks

    def create_maze(self):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                symbol = self.maze[y][x]
                x_coord = -self.maze_size + (x * self.block_size)
                y_coord = self.maze_size - (y * self.block_size)

                if self.is_wall(symbol):
                    self.tiles.goto(x_coord, y_coord)
                    self.tiles.stamp()
                    self.wall_blocks.append((x_coord, y_coord))
                elif self.is_treasure(symbol):
                    new_treasure = Treasure()
                    new_treasure.set_x_y(x_coord, y_coord)
                    new_treasure.showturtle()
                    self.treasures.append(new_treasure)
                elif self.is_player(symbol):
                    self.player.showturtle()
                    self.player.goto(x_coord, y_coord)

                else:
                    self.free_blocs.append((x_coord, y_coord))

        self.player.set_walls(self.wall_blocks)

    def is_treasure(self, char):
        if char == Treasure.get_label():
            return True
        return False

    def is_wall(self, char):
        if char == Tiles.get_label():
            return True
        return False

    def is_player(self, char):
        if char == Player.get_label():
            return True
        return False

    def place_random_treasure(self):
        treasure_pos_y = randrange(0, len(self.maze))
        treasure_pos_x = randrange(0, len(self.maze[treasure_pos_y]))
        if self.is_wall(self.maze[treasure_pos_x][treasure_pos_y]) or self.is_treasure(
                self.maze[treasure_pos_x][treasure_pos_y]):
            self.place_random_treasure()
        else:
            self.maze[treasure_pos_x] = self.maze[treasure_pos_x][:treasure_pos_y] + "T" + \
                                        self.maze[treasure_pos_x][treasure_pos_y + 1:]

    def place_random_player(self):
        player_pos_y = randrange(0, len(self.maze))
        player_pos_x = randrange(0, len(self.maze[player_pos_y]))
        if self.is_wall(self.maze[player_pos_x][player_pos_y]) or self.is_treasure(
                self.maze[player_pos_x][player_pos_y]):
            self.place_random_player()
        else:
            self.maze[player_pos_x] = self.maze[player_pos_x][:player_pos_y] + "P" + \
                                      self.maze[player_pos_x][player_pos_y + 1:]

    def generate_map(self):

        def walk(x, y):
            vis[y][x] = 1

            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]:
                    continue
                if xx == x:
                    hor[max(y, yy)][x] = "W "
                if yy == y:
                    ver[y][max(x, xx)] = "  "
                walk(xx, yy)

        h = w = int(self.block_size / 2)
        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        ver = [["W "] * w + ['W'] for _ in range(h)] + [[]]
        hor = [["WW"] * w + ['W'] for _ in range(h + 1)]

        walk(randrange(w), randrange(h))

        treasures_count = 4

        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])

        self.maze = [i for i in s.split("\n") if i]
        for _ in range(treasures_count):
            self.place_random_treasure()
        self.place_random_player()

    def check_treasures_collected(self):
        for treasure in self.treasures:
            if self.player.is_collision(treasure):
                treasure.collect()
                self.treasures.remove(treasure)
