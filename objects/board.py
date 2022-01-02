import pygame
from pygame.locals import *
from objects.base import DrawableObject
from objects.player import *
import random

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WALLCOLOR = (0, 0, 225)

class Board(DrawableObject):
    def __init__(self, game, maze, blocksize, x, y):
        super().__init__(game)
        self.maze = maze
        self.x = x
        self.y = y
        self.blocksize = blocksize
        self.gameover = False
        self.status = "playing"
        self.objects = [[DrawableObject(game) for _ in range(len(maze[0]))] for _ in range(len(maze))]
        self.player = Bee(game, blocksize, x, y, "images/bee.png")
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                pos_x = x + (blocksize * (2 * j + 1)) / 2
                pos_y = y + (blocksize * (2 * i + 1)) / 2

                if maze[i][j] in [21, 22, 23]:
                    self.objects[i][j] = Flower(self.game, int(blocksize * 0.6), int(blocksize * 0.6), pos_x, pos_y, maze[i][j] % 10)
                elif maze[i][j] == 1:
                    self.objects[i][j] = ImageObject(self.game, blocksize, blocksize, pos_x, pos_y, "images/tree.png")
                elif maze[i][j] == 3:
                    self.objects[i][j] = Home(self.game, int(blocksize * 0.9), int(blocksize * 0.7), pos_x, pos_y, "images/home.png", 5)

    # def on_deactivate(self):
    #     # self.player.moveRight = False
    #     # self.player.moveUp = False
    #     # self.player.moveDown = False
    #     # self.player.moveLeft = False
    # pass

    def process_draw(self):
        surf = pygame.Surface((self.blocksize * len(self.maze[0]), self.blocksize * len(self.maze)))
        surf.fill((13, 175, 106))
        self.game.screen.blit(surf, (self.x, self.y))

        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                self.objects[i][j].process_draw()
        self.player.update()

    def process_event(self, event):
        self.player.process_event(event, self.maze)