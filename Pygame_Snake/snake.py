import pygame
import random
import sys
import time
import inspect
from constants import *

class Apple(object):
    def __init__(self, place):
        self.id_apple = random.randint(0, 3)
        self.place = place
        self.picture = self.apple_picture()
        self.pos = self.get_apple_pos()

    def apple_picture(self):
        if self.id_apple == 0:
            self.score = 1
            return RED_APPLE
        elif self.id_apple == 1:
            self.score = 2
            return GREEN_APPLE
        elif self.id_apple == 2:
            self.score = 3
            return GOLDEN_APPLE
        elif self.id_apple == 3:
            self.score = -1
            return BLUE_APPLE

    def get_apple_pos(self):
        return (random.randrange(GAME_WINDOW_POSX, GAME_WINDOW_POSX_MAX, CELL_SIZE),\
             random.randrange(GAME_WINDOW_POSY, GAME_WINDOW_POSY_MAX, CELL_SIZE))


class Snake(object):
    def __init__(self, pos_snake):
        self.pos_snake = pos_snake
        self.direction_x = 0
        self.direction_y = 0
        self.body_snake = []
        self.body_size = SIZE
        self.grow_up = 1
        self.score = 0
        self.life = True

    def debug_snake(self, apple):
        print("-----------------------------------")
        print(inspect.cleandoc(f"""{LIGHT_BLUE_COLOR}Snake position:{WHITE_COLOR} {self.pos_snake}
        {LIGHT_BLUE_COLOR}Apple position:{WHITE_COLOR} {apple.pos}
        {LIGHT_BLUE_COLOR}Apple place:{WHITE_COLOR} {apple.place}
        {LIGHT_BLUE_COLOR}Apple score:{WHITE_COLOR} {apple.score}
        {LIGHT_BLUE_COLOR}Snake score:{WHITE_COLOR} {self.score}
        {LIGHT_BLUE_COLOR}Snake body:{WHITE_COLOR} {self.body_snake}"""))
        print("\n\n")

    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                snake.life = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    snake.life = False

                elif event.key == pygame.K_UP:
                    self.direction_x = 0
                    self.direction_y = -CELL_SIZE

                elif event.key == pygame.K_DOWN:
                    self.direction_x = 0
                    self.direction_y = CELL_SIZE

                elif event.key == pygame.K_RIGHT:
                    self.direction_x = CELL_SIZE
                    self.direction_y = 0

                elif event.key == pygame.K_LEFT:
                    self.direction_x = -CELL_SIZE
                    self.direction_y = 0

                elif event.key == pygame.K_SPACE:
                    self.direction_x = 0
                    self.direction_y = 0

    def move(self):
        if self.pos_snake[0] < GAME_WINDOW_POSX or self.pos_snake[0] > GAME_WINDOW_POSX_MAX - 2\
            or self.pos_snake[1] < GAME_WINDOW_POSY or self.pos_snake[1] > GAME_WINDOW_POSY_MAX - 4:
                sys.exit()
        else:
            self.pos_snake = [int(self.pos_snake[0] + self.direction_x), int(self.pos_snake[1] + self.direction_y)]
        self.body_snake.append(self.pos_snake)
        if len(self.body_snake) > self.grow_up:
            self.body_snake.pop(0)

    def snake_bites_tail(self):
        for body_snake in self.body_snake[:-1]:
            if body_snake == self.body_snake[-1]:
                self.life = False

    def eaten_apple(self, apple):
        if self.pos_snake[0] == apple.pos[0] and self.pos_snake[1] == apple.pos[1]:
            self.score += apple.score
            self.grow_up += 1
            return True
        return False

class Game(object):
    def __init__ (self):
        pygame.display.set_caption(GAME_TITLE)
        pygame.display.set_icon(APP_PICTURE)
        self.menu = True
        self.in_progress = False
        self.button = 0
        self.fps = pygame.time.Clock()
        self.place = 0
        self.apple = Apple(self.place)

    def debug_game(self):
        print(inspect.cleandoc(f"""DEBUG MODE [{GREEN_COLOR}ACTIVE{WHITE_COLOR}]
        {YELLOW_COLOR}Window resolution:      {WHITE_COLOR}[{SCREEN_RESOLUTION_X}:{SCREEN_RESOLUTION_Y}]
        {LIGHT_BLUE_COLOR}GAME Window resolution: {WHITE_COLOR}[{GAME_WINDOW_LENGHT_X}:{GAME_WINDOW_LENGHT_Y}]"""))
        if GAME_GRID:
            print(inspect.cleandoc(f"{LIGHT_BLUE_COLOR}Game Grid :             {WHITE_COLOR}[{GREEN_COLOR}ACTIVE{WHITE_COLOR}]"))
        else:
            print(inspect.cleandoc(f"{LIGHT_BLUE_COLOR}Game Grid :             {WHITE_COLOR}[{RED_COLOR}NO ACTIVE{WHITE_COLOR}]"))
        print(inspect.cleandoc(f"""{LIGHT_BLUE_COLOR}Number cells in X:{WHITE_COLOR}      {CELL_NB_X}
        {LIGHT_BLUE_COLOR}Number cells in Y:{WHITE_COLOR}      {CELL_NB_Y}"""))
        snake.debug_snake(self.apple)

    def draw_window(self):
        # WINDOW = pygame.display.set_mode((SCREEN_RESOLUTION_X, SCREEN_RESOLUTION_Y))
        WINDOW.fill(BLACK_RGB)
        pygame.draw.rect(WINDOW, (WHITE_RGB), (GAME_WINDOW_POSX, GAME_WINDOW_POSY, GAME_WINDOW_LENGHT_X, GAME_WINDOW_LENGHT_Y), 2)
        if GAME_GRID:
            self.draw_game_grid()
        for body_snake in snake.body_snake:
            pygame.draw.rect(WINDOW, (GREEN_RGB), (body_snake[0], body_snake[1], snake.body_size ,snake.body_size))
        WINDOW.blit(self.apple.picture, self.apple.pos)
        self.draw_score(snake)
        pygame.display.flip()

    def draw_game_grid(self):
        for x in range(GAME_WINDOW_POSX, (GAME_WINDOW_LENGHT_X + GAME_WINDOW_POSX), CELL_SIZE):
            pygame.draw.line(WINDOW, (SALTE_GREY_RGB), (x, GAME_WINDOW_POSY), [x, GAME_WINDOW_POSY_MAX])
        for y in range(GAME_WINDOW_POSY, (GAME_WINDOW_LENGHT_Y + GAME_WINDOW_POSY), CELL_SIZE):
            pygame.draw.line(WINDOW, (SALTE_GREY_RGB), (GAME_WINDOW_POSX, y), [GAME_WINDOW_POSX_MAX, y])
        
    def draw_score(self, snake):
        score_message = self.font_message(CELL_SIZE * 1.2, f"Score : {snake.score}", BLUE_RGB)
        WINDOW.blit(score_message, (GAME_WINDOW_POSX, GAME_WINDOW_POSY / 2, CELL_SIZE, CELL_SIZE))

    def font_message(self, size_police, text, color):
        font = pygame.font.SysFont('Arial', int(size_police), True)
        return (font.render(text, True, color))

    def get_event_menu(self, game_menu):
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                elif event.key == pygame.K_RETURN:
                    self.menu = False
                    if game_menu:
                        if self.button == 3:
                            sys.exit()
                        elif self.button == 1 or self.button == 2:
                            self.in_progress = True
                    else:
                        if self.button == 0:
                            self.menu = True
                            self.in_progress = False
                elif event.key == pygame.K_UP:
                    if self.button > 0:
                        self.button -= 1
                elif event.key == pygame.K_DOWN:
                    if game_menu:
                        if self.button < 4:
                            self.button += 1
                    else:
                        if self.button == 0:
                            self.button += 1
        
    def index_button_menu(self):
        if self.button == 0:
            pygame.draw.rect(WINDOW, (YELLOW_RGB), (SCREEN_RESOLUTION_X / 2 - 152, SCREEN_RESOLUTION_Y / 3 - 2, 305, 35), 1)
        if self.button == 1:
            pygame.draw.rect(WINDOW, (YELLOW_RGB), (SCREEN_RESOLUTION_X / 2 - 152, SCREEN_RESOLUTION_Y / 3 + 50 -2, 305, 35), 1)
        if self.button == 2:
            pygame.draw.rect(WINDOW, (YELLOW_RGB), (SCREEN_RESOLUTION_X / 2 - 77, SCREEN_RESOLUTION_Y / 3 + 100 - 2, 155, 35), 1)
        if self.button == 3:
            pygame.draw.rect(WINDOW, (YELLOW_RGB), (SCREEN_RESOLUTION_X / 2 - 152, SCREEN_RESOLUTION_Y / 3 + 150 -2, 305, 35), 1)
        if self.button == 4:
            pygame.draw.rect(WINDOW, (YELLOW_RGB), (SCREEN_RESOLUTION_X - 62, SCREEN_RESOLUTION_Y - 52, 35, 35), 1)

    def index_button_in_progress(self):
        if self.button == 0:
            pygame.draw.rect(WINDOW, (YELLOW_RGB), (SCREEN_RESOLUTION_X / 2 - 152, SCREEN_RESOLUTION_Y / 2 + 50 - 2, 305, 35), 1)
        if self.button == 1:
            pygame.draw.rect(WINDOW, (YELLOW_RGB), (SCREEN_RESOLUTION_X / 2 - 17, SCREEN_RESOLUTION_Y / 2 + 98, 35, 35), 1)

    def draw_game_menu(self):
        WINDOW.blit(BACKGROUND, (0, 0, SCREEN_RESOLUTION_X, SCREEN_RESOLUTION_Y))
        menu_message = self.font_message(CELL_SIZE * 2, f"Snake Game", GREEN_RGB)
        WINDOW.blit(menu_message, (GAME_WINDOW_POSX, GAME_WINDOW_POSY / 4))
        WINDOW.blit(BUTTON_1P, (SCREEN_RESOLUTION_X / 2 - 150, SCREEN_RESOLUTION_Y / 3))
        WINDOW.blit(BUTTON_2P, (SCREEN_RESOLUTION_X / 2 - 150, SCREEN_RESOLUTION_Y / 3 + 50))
        WINDOW.blit(BUTTON_STATS, (SCREEN_RESOLUTION_X / 2 - 75, SCREEN_RESOLUTION_Y / 3 + 100))
        WINDOW.blit(BUTTON_QUIT, (SCREEN_RESOLUTION_X / 2 - 150, SCREEN_RESOLUTION_Y / 3 + 150))
        WINDOW.blit(BUTTON_INFO, (SCREEN_RESOLUTION_X - 60, SCREEN_RESOLUTION_Y - 50))

    def draw_game_in_progress(self):
        in_progress_window = pygame.display.set_mode((SCREEN_RESOLUTION_X, SCREEN_RESOLUTION_Y))
        in_progress_window.blit(BACKGROUND, (0, 0, SCREEN_RESOLUTION_X, SCREEN_RESOLUTION_Y))
        in_progress_message = self.font_message(CELL_SIZE, "This feature is in production, coming soon.", YELLOW_RGB)
        in_progress_window.blit(GAME_TOY, (SCREEN_RESOLUTION_X / 2 - 50 , SCREEN_RESOLUTION_Y / 4))
        in_progress_window.blit(in_progress_message, (SCREEN_RESOLUTION_X / 2 - 200, SCREEN_RESOLUTION_Y / 2))
        in_progress_window.blit(BUTTON_BACK, (SCREEN_RESOLUTION_X / 2 - 150 , SCREEN_RESOLUTION_Y / 2 + 50))
        in_progress_window.blit(BUTTON_INFO, (SCREEN_RESOLUTION_X / 2 - 15, SCREEN_RESOLUTION_Y / 2 + 100))

    def start_game(self, snake):
        while self.menu:
            pygame.time.Clock().tick(5)
            self.get_event_menu(True)
            self.draw_game_menu()
            self.index_button_menu()
            pygame.display.flip()
            if not self.menu:
                self.button = 0

        while self.in_progress:
            pygame.time.Clock().tick(5)
            self.get_event_menu(False)
            self.draw_game_in_progress()
            self.index_button_in_progress()
            pygame.display.flip()
            if not self.in_progress:
                return


        while snake.life:
            self.fps.tick(FPS)
            snake.get_event()
            snake.move()
            snake.snake_bites_tail()
            if DEBUG:
                self.debug_game()
            if snake.eaten_apple(self.apple):
                self.place += 1
                self.apple = Apple(self.place)
            self.draw_window()

if __name__ == "__main__":
    pygame.init()
    snake = Snake([SCREEN_RESOLUTION_X / 2, SCREEN_RESOLUTION_Y / 2])
    game = Game()
    game.start_game(snake)
    while game.menu:
        game.start_game(snake)
    print("FIN")
    pygame.quit()