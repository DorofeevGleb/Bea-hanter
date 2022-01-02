from .base import BaseScene
from objects.board import *


class GameMenu(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.objects = [
            Board(game, [[3, 23, 0, 1], [22, 0, 0, 0], [22, 0, 0, 0], [22, 0, 0, 0]], 75, 50, 50)
        ]