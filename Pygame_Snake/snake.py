import pygame
import random
import sys
import time
import inspect
from constants import *

class Snake(object):
    def __init__(self, pos_snake):
        self.pos_snake = pos_snake
        self.body_snake = [pos_snake]
        self.body_size = SIZE
        self.life = True
        self.score = 0

    def debug_snake(self, apple):
        print(inspect.cleandoc(f"""DEBUG MODE [{GREEN_COLOR}ACTIVE{WHITE_COLOR}]
        {LIGHT_BLUE_COLOR}Snake position:{WHITE_COLOR} {snake.pos_snake}
        {LIGHT_BLUE_COLOR}Apple position:{WHITE_COLOR} {apple.pos}
        {LIGHT_BLUE_COLOR}Apple place:{WHITE_COLOR} {apple.place}
        {LIGHT_BLUE_COLOR}Apple score:{WHITE_COLOR} {snake.score}
        {LIGHT_BLUE_COLOR}Snake body:{WHITE_COLOR} {snake.body_snake}"""))


    def get_event(self, direction):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    direction = False
                elif event.key == pygame.K_UP:
                    direction = "UP"
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"
                elif event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    direction = "LEFT"
                elif event.key == pygame.K_SPACE:
                    direction = "STOP"
                return direction
        return direction

    def move(self, direction):
        if snake.pos_snake[0] < GAME_WINDOW_POSX or snake.pos_snake[0] > GAME_WINDOW_POSX_MAX - 2\
            or snake.pos_snake[1] < GAME_WINDOW_POSY or snake.pos_snake[1] > GAME_WINDOW_POSY_MAX - 4:
                time.sleep(3)
                sys.exit()
        if direction == "UP":
            snake.pos_snake[1] -= CELL_SIZE
        elif direction == "DOWN":
            snake.pos_snake[1] += CELL_SIZE
        elif direction == "RIGHT":
            snake.pos_snake[0] += CELL_SIZE
        elif direction == "LEFT":
            snake.pos_snake[0] -= CELL_SIZE
        if direction == "STOP":
            snake.pos_snake = snake.pos_snake
    
    def eaten_apple(self, apple, direction):
        if snake.pos_snake[0] >= apple.pos[0] and snake.pos_snake[0] <= apple.pos[0] \
            and snake.pos_snake[1] >= apple.pos[1] and snake.pos_snake[1] <= apple.pos[1]:
            snake.score += apple.score
            self.grow_up_snake(direction)
            return True
        return False
    
    def grow_up_snake(self, direction):
        if direction == "UP":
            snake.body_snake.extend([[snake.pos_snake[0], snake.pos_snake[1] + 1]])
        elif direction == "DOWN":
            snake.body_snake.extend([[snake.pos_snake[0], snake.pos_snake[1] - 1]])
        elif direction == "RIGHT":
            snake.body_snake.extend([[snake.pos_snake[0] - 1, snake.pos_snake[1]]])
        elif direction == "LEFT":
            snake.body_snake.extend([[snake.pos_snake[0] + 1, snake.pos_snake[1]]])

class Game(object):
    def __init__ (self):
        pygame.display.set_caption(GAME_TITLE)
        pygame.display.set_icon(APP_PICTURE)
        self.fps = pygame.time.Clock()

    def debug_window(self):
        print(inspect.cleandoc(f"""DEBUG MODE [{GREEN_COLOR}ACTIVE{WHITE_COLOR}]
        {LIGHT_BLUE_COLOR}Resolution:{WHITE_COLOR} {SCREEN_RESOLUTION_X}:{SCREEN_RESOLUTION_Y}
        {LIGHT_BLUE_COLOR}Game_Grid:{WHITE_COLOR} {GAME_GRID}"""))

    def init_WINDOW(self, apple):
        WINDOW.fill(BLACK_RGB)
        if GAME_GRID:
            self.draw_game_grid()
        if DEBUG:
            snake.debug_snake(apple)
        self.draw_game(apple)
        pygame.display.flip()
        
    def draw_game_grid(self):
        for x in range(GAME_WINDOW_POSX, (GAME_WINDOW_LENGHT_X + GAME_WINDOW_POSX), CELL_SIZE):
            pygame.draw.line(WINDOW, (SALTE_GREY_RGB), (x, GAME_WINDOW_POSY), [x, GAME_WINDOW_POSY_MAX])
        for y in range(GAME_WINDOW_POSY, (GAME_WINDOW_LENGHT_Y + GAME_WINDOW_POSY), CELL_SIZE):
            pygame.draw.line(WINDOW, (SALTE_GREY_RGB), (GAME_WINDOW_POSX, y), [GAME_WINDOW_POSX_MAX, y])

    def draw_game(sefl, apple):
        pygame.draw.rect(WINDOW, (WHITE_RGB), (GAME_WINDOW_POSX, GAME_WINDOW_POSY, GAME_WINDOW_LENGHT_X, GAME_WINDOW_LENGHT_Y), 2)
        for i in range(0, apple.place + 1):
            # print(i)
            # print(snake.body_snake)
            pygame.draw.rect(WINDOW, (GREEN_RGB), (snake.body_snake[i][0], snake.body_snake[i][1], snake.body_size, snake.body_size))
        WINDOW.blit(apple.apple_picture, apple.pos)

    def start_game(self, snake):
        start_game = True
        direction = ""
        place = 0
        apple = Apple(place)
        while start_game:
            self.fps.tick(FPS)
            self.init_WINDOW(apple)
            direction = snake.get_event(direction)
            if snake.eaten_apple(apple, direction) == True:
                place += 1
                apple = Apple(place)
            if direction == False:
                start_game = False
            snake.move(direction)

class Apple(object):
    def __init__(self, place):
        self.id_apple = random.randint(0, 3)
        self.place = place
        self.apple_picture = self.apple_picture()
        self.pos = self.get_apple_pos()
        # self.apple_picture.get_rect(center=(self.pos))

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


if __name__ == "__main__":
    # if SCREEN_RESOLUTION_X % SIZE != 0 or SCREEN_RESOLUTION_Y % SIZE != 0:
    #     print("Error: Size CELL_SIZE")
    #     sys.exit()
    pygame.init()
    game = Game()
    if DEBUG:
        game.debug_window()
    snake = Snake([320, 240])
    game.start_game(snake)
    pygame.quit()
