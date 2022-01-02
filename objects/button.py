from objects.base import *
import pygame


class Button(DrawableObject):
    def __init__(self, game, text, font_color, font_sise, width, height, x, y, color, hovered_color,
                 function, arg):
        super().__init__(game)
        self.arg = arg
        self.mask = pygame.Rect(x, y, width, height)
        self.color = color
        self.hovered_color = hovered_color
        self.function = function
        self.clicked = False
        self.hovered = False
        self.call_on_release = False
        self.text = text
        self.font = pygame.font.Font(None, font_sise)
        self.font_color = font_color
        self.render_text()

    def render_text(self):
        self.text = self.font.render(self.text, True, self.font_color)

    def process_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.on_release(event)

    def on_release(self, event):
        if self.clicked and self.call_on_release:
            self.function(self.arg)
        self.clicked = False

    def update(self, surface):
        text = self.text
        self.check_hover()
        if self.hovered:
            color = self.hovered_color
        else:
            color = self.color
        self.game.screen.fill(color, self.mask)

        if self.text:
            text_rect = text.get_rect(center=self.mask.center)
            self.game.screen.blit(text, text_rect)


class ImageButton(Button):
    def __init__(self, game, image, image_hover, width, height, x, y, function, arg):
        self.arg = arg
        self.game = game
        self.button = Sprite(image, width, height, x, y)
        self.button_hover = Sprite(image_hover, width, height, x, y)
        self.x = x
        self.y = y
        self.function = function
        self.hovered = False
        self.clicked = False
        self.call_on_release = False

    def on_click(self, event):
        if self.button.rect.collidepoint(pygame.mouse.get_pos()):
            self.clicked = True
            if not self.call_on_release:
                self.function(self.arg)

    def check_hover(self):
        if self.button.rect.collidepoint(pygame.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
        else:
            self.hovered = False

    def process_draw(self):
        self.check_hover()
        if self.hovered:
            button = self.button_hover
        else:
            button = self.button
        self.game.screen.blit(button.image, button.rect)
