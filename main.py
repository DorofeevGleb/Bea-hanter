import sys
import pygame


'https://disk.yandex.ru/d/wNupctkyKBAODw' # ссылка на диск со спрайтами


COLORS = [pygame.Color('black'), pygame.Color('DarkGrey'),  pygame.Color('SaddleBrown'), pygame.Color(0, 128, 0), pygame.Color('red'), pygame.Color('Gainsboro')]
SPRITES = [pygame.image.load('test2.png'), pygame.image.load('test4.png'), pygame.image.load('wall.png'), pygame.image.load('grass.png'), pygame.image.load('bee_on_grass.png')]


class Board:
    def __init__(self, level):
        self.bee_pos = (0, 0)
        self.flag = True
        # self.board = [[0] * width for _ in range(height)]
        self.board = ''
        self.new_board = []
        self.board_with_bee = []
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.width = 0
        self.height = 0
        self.sides = (0, 0)
        self.choose_level(level)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def choose_level(self, level):
        if level == 1:
            self.sides = self.height, self.width = 5, 5
            self.board_with_bee = [[3, 2, 2, 2, 2], [3, 3, 3, 3, 3], [3, 2, 3, 2, 2], [3, 2, 3, 3, 3], [2, 2, 2, 2, 4]]
            self.board = str([[3, 2, 2, 2, 2], [3, 3, 3, 3, 3], [3, 2, 3, 2, 2], [3, 2, 3, 3, 3], [2, 2, 2, 2, 3]])
            self.bee_pos = (4, 4)
        elif level == 2:
            self.sides = self.height, self.width = 6, 5
            self.board_with_bee = [[3, 3, 3, 3, 2], [3, 2, 2, 2, 2], [3, 3, 3, 3, 3], [3, 2, 3, 2, 2], [3, 2, 3, 3, 3], [2, 2, 2, 2, 4]]
            self.board = str([[3, 3, 3, 3, 2], [3, 2, 2, 2, 2], [3, 3, 3, 3, 3], [3, 2, 3, 2, 2], [3, 2, 3, 3, 3], [2, 2, 2, 2, 3]])
            self.bee_pos = (5, 4)

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                sun_rect = SPRITES[self.board_with_bee[y][x]].get_rect(topleft=(x * self.cell_size + self.left,
                                                                                y * self.cell_size + self.top))
                screen.blit(SPRITES[self.board_with_bee[y][x]], sun_rect)
        pygame.draw.rect(screen, COLORS[0], (self.left - 2, self.top - 2,
                                             self.left + (self.width - 1) * self.cell_size + 4,
                                             self.height * self.cell_size + 4), 4)

    def bag_fix(self):
        f1, self.new_board = [], []
        for i in self.board[2:-2].split('], ['):
            for j in i.split(', '):
                f1.append(int(j))
            self.new_board.append(f1)
            f1 = []

    def sides_check(self, move):
        if move == 'forward_move':
            new_bee_pos = (self.bee_pos[0] - 1, self.bee_pos[1])
        elif move == 'back_move':
            new_bee_pos = (self.bee_pos[0] + 1, self.bee_pos[1])
        elif move == 'right_move':
            new_bee_pos = (self.bee_pos[0], self.bee_pos[1] + 1)
        elif move == 'left_move':
            new_bee_pos = (self.bee_pos[0], self.bee_pos[1] - 1)
        if (new_bee_pos[0]) >= 0 and new_bee_pos[1] >= 0 and new_bee_pos[0] < self.sides[0] and\
                new_bee_pos[1] < self.sides[1]:
            print(f'{new_bee_pos}2')
            return True
        else:
            return False

    def forward_moving(self):
        self.bag_fix()
        if self.sides_check('forward_move'):
            if self.new_board[(self.bee_pos[0] - 1)][(self.bee_pos[1])] != 2:
                self.bee_pos = (self.bee_pos[0] - 1, self.bee_pos[1])
        self.board_with_bee = self.new_board
        self.board_with_bee[self.bee_pos[0]][self.bee_pos[1]] = 4
        print(self.bee_pos)

    def back_moving(self):
        self.bag_fix()
        if self.sides_check('back_move'):
            if self.new_board[(self.bee_pos[0] + 1)][(self.bee_pos[1])] != 2:
                self.bee_pos = (self.bee_pos[0] + 1, self.bee_pos[1])
        self.board_with_bee = self.new_board
        self.board_with_bee[self.bee_pos[0]][self.bee_pos[1]] = 4
        print(self.bee_pos)

    def right_moving(self):
        self.bag_fix()
        if self.sides_check('right_move'):
            if self.new_board[(self.bee_pos[0])][(self.bee_pos[1] + 1)] != 2:
                self.bee_pos = (self.bee_pos[0], self.bee_pos[1] + 1)
        self.board_with_bee = self.new_board
        self.board_with_bee[self.bee_pos[0]][self.bee_pos[1]] = 4
        print(self.bee_pos)

    def left_moving(self):
        self.bag_fix()
        if self.sides_check('left_move'):
            if self.new_board[(self.bee_pos[0])][(self.bee_pos[1] - 1)] != 2:
                self.bee_pos = (self.bee_pos[0], self.bee_pos[1] - 1)
        self.board_with_bee = self.new_board
        self.board_with_bee[self.bee_pos[0]][self.bee_pos[1]] = 4
        print(self.bee_pos)

    def choosing_a_direction(self, direction):
        if direction == 'forward':
            self.forward_moving()
        if direction == 'back':
            self.back_moving()
        if direction == 'right':
            self.right_moving()
        if direction == 'left':
            self.left_moving()


def main():
    pygame.init()
    pygame.display.set_caption('Bee hunter')
    size = 250, 300
    screen = pygame.display.set_mode(size)
    level = 1
    board = Board(level)
    board.set_view(30, 30, 30)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    board.choosing_a_direction('forward')
                elif event.key == pygame.K_s:
                    board.choosing_a_direction('back')
                elif event.key == pygame.K_a:
                    board.choosing_a_direction('left')
                elif event.key == pygame.K_d:
                    board.choosing_a_direction('right')
        screen.fill(COLORS[5])
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())
