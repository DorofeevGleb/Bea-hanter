import pygame
from objects.base import DrawableObject
from pygame.locals import *



class Flower(DrawableObject):
    def __init__(self, game, w, h, x, y, flower_type):
        self.game = game
        self.flower_type = flower_type
        self.images = pygame.transform.scale(pygame.image.load(f"images\\flower_{flower_type}.png"),
                                             (w, h))
        self.rect = self.images.get_rect()
        self.rect.center = (x, y)
        self.exist = True

    def process_draw(self):
        self.game.screen.blit(self.images, self.rect)



class ImageObject(DrawableObject):
    def __init__(self, game, w, h, x, y, image):
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load(image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def process_draw(self):
        self.game.screen.blit(self.image, self.rect)


class Home(ImageObject):
    def __init__(self, game, w, h, x, y, image, designed_cnt):
        super().__init__(game, w, h, x, y, image)
        self.current_cnt = 0
        self.designed_cnt = designed_cnt


class Bee(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    explosion = False
    game_over = False

    def __init__(self, game, blocksize, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load(filename), (blocksize, blocksize))  # просто пакмэн без действий
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.playerX = 0
        self.playerY = 0
        self.blocksize = blocksize
        self.rect.center = (
            self.x + self.playerX,
            self.y + self.playerY
        )
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        self.moveLeft = False


    def update(self):
        self.rect.center = (
            self.x + (2 * self.playerX + 1) * self.blocksize / 2,
            self.y + (2 * self.playerY + 1) * self.blocksize / 2
        )

        self.game.screen.blit(self.image, self.rect)



    def process_logic(self, maze):
        if self.moveDown and maze[self.playerY + 1][self.playerX] != 1:
            self.playerY += 1
            if self.playerY == len(maze) - 1:
                self.playerY = 0
        elif self.moveUp and maze[self.playerY - 1][self.playerX] != 1:
            self.playerY -= 1
            if self.playerY == -1:
                self.playerY = len(maze)
        elif self.moveLeft and maze[self.playerY][self.playerX - 1] != 1:
            self.playerX -= 1
            if self.playerX == -1:
                self.playerX = len(maze[0]) - 1
        elif self.moveRight and maze[self.playerY][self.playerX + 1] != 1:
            self.playerX += 1
            if self.playerX == len(maze[0]):
                self.playerX = 0

    def process_event(self, event, maze):
        if event.type == KEYDOWN or event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                self.moveRight = False
                self.moveUp = False
                self.moveDown = False
                self.moveLeft = True
                self.process_logic(maze)
            elif event.key == K_RIGHT or event.key == K_d:
                self.moveRight = True
                self.moveUp = False
                self.moveDown = False
                self.moveLeft = False
                self.process_logic(maze)
            elif event.key == K_UP or event.key == K_w:
                self.moveRight = False
                self.moveUp = True
                self.moveDown = False
                self.moveLeft = False
                self.process_logic(maze)
            elif event.key == K_DOWN or event.key == K_s:
                self.moveRight = False
                self.moveUp = False
                self.moveDown = True
                self.moveLeft = False
                self.process_logic(maze)
            pygame.time.delay(1000)