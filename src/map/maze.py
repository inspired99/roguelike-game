from random import shuffle, randrange

from src.gameEngine.allyObject import Ally
from src.gameEngine.enemyObject import Enemy
from src.gameEngine.playerObject import Player
from src.gameEngine.tilesObject import Tiles


class Maze:
    def __init__(self):
        self.maze = None
        self.wall_blocks = []
        self.tiles = Tiles()
        self.player = Player()
        self.enemies = []
        self.wizard = None
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

                elif self.is_enemy(symbol):
                    new_enemy = Enemy()
                    new_enemy.set_x_y(x_coord, y_coord)
                    self.enemies.append(new_enemy)

                elif self.is_ally(symbol):
                    ally = Ally()
                    ally.set_x_y(x_coord, y_coord)
                    ally.showturtle()
                    self.wizard = ally

                elif self.is_player(symbol):
                    self.player.showturtle()
                    self.player.goto(x_coord, y_coord)

        for enemy in self.enemies:
            enemy.showturtle()

        self.player.set_walls(self.wall_blocks)

    def is_ally(self, char):
        if char == Ally.get_label():
            return True
        return False

    def is_enemy(self, char):
        if char == Enemy.get_label():
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

    def is_free(self, char):
        if not self.is_enemy(char) and not self.is_wall(char) and not self.is_player(char) and not self.is_ally(char):
            return True
        return False

    def place_random_object(self, symbol):
        obj_pos_y = randrange(0, len(self.maze))
        obj_pos_x = randrange(0, len(self.maze[obj_pos_y]))
        if not self.is_free(self.maze[obj_pos_x][obj_pos_y]):
            self.place_random_object(symbol)
        else:
            self.maze[obj_pos_x] = self.maze[obj_pos_x][:obj_pos_y] + symbol + \
                                   self.maze[obj_pos_x][obj_pos_y + 1:]

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

        enemy_count = 4

        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])

        self.maze = [i for i in s.split("\n") if i]

        for _ in range(enemy_count):
            self.place_random_object(Enemy.get_label())

        self.place_random_object(Player.get_label())
        self.place_random_object(Ally.get_label())

    def check_enemies_collapsed(self):
        for enemy in self.enemies:
            if self.player.is_collision(enemy):
                enemy.disappear()
                self.enemies.remove(enemy)

    def check_wizard_reached(self):
        if self.player.is_collision(self.wizard):
            return True
        return False
