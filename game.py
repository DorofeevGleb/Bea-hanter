import pygame
from scenes.game_menu import GameMenu

class Game:
    size = width, height = 550, 700
    SCENE_MENU = 0
    SCENE_GAME = 0
    current_scene_index = SCENE_MENU

    def __init__(self):
        self.score = 0
        self.screen = pygame.display.set_mode(self.size)
        self.scenes = [GameMenu(self)]
        self.game_over = False

    @staticmethod
    def exit_button_pressed(event):
        return event.type == pygame.QUIT

    @staticmethod
    def exit_hotkey_pressed(event):
        return event.type == pygame.KEYDOWN and event.mod & pygame.KMOD_CTRL and event.key == pygame.K_q

    def process_exit_events(self, event):
        if Game.exit_button_pressed(event) or Game.exit_hotkey_pressed(event):
            self.exit_game()

    def process_all_events(self):
        for event in pygame.event.get():
            self.process_exit_events(event)
            self.scenes[self.current_scene_index].process_event(event)

    def set_scene(self, index):
        self.scenes[self.current_scene_index].on_deactivate()
        self.current_scene_index = index
        self.scenes[self.current_scene_index].on_activate()

    def process_all_draw(self):
        self.screen.fill((255, 255, 255))
        self.scenes[self.current_scene_index].process_draw()
        pygame.display.flip()

    def process_all_logic(self):
        self.scenes[self.current_scene_index].process_logic()

    def main_loop(self):
        while not self.game_over:
            if self.current_scene_index == 1:
                pygame.time.delay(5000)
            self.process_all_events()
            self.process_all_logic()
            self.process_all_draw()

    def exit_game(self):
        print('Bye bye')
        self.game_over = True

    def new_game(self):
        self.scenes[1].new_game()
