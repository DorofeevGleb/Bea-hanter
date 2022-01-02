import pygame


class DrawableObject():
    def __init__(self, game):
        self.game = game
        self.mask = pygame.rect.Rect(0, 0, 0, 0)

    def move(self, x, y):
        self.mask.x = x
        self.mask.y = y

    def move_center(self, x, y):
        self.mask.centerx = x
        self.mask.centery = y

    def process_event(self, event):
        pass

    def process_logic(self):
        pass

    def process_draw(self):
        pass  # use self.game.screen for drawing, padawan


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, w, h, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (w, h))
        self.rect = self.image.get_rect(center=(x + w // 2, y + h // 2))
