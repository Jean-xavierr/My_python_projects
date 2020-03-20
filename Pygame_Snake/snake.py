import pygame
import random
import sys
import time
from constantes import *

class Snake(object):
    def __init__(self, pos_snake):
        self.pos_snake = pos_snake
        self.body_snake = [pos_snake]
        self.body_size = SIZE
        self.life = True
        self.score = 0

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
        if snake.pos_snake[0] < 10 or snake.pos_snake[0] > SCREEN_RESOLUTION_X - 20 \
            or snake.pos_snake[1] < 10 or snake.pos_snake[1] > SCREEN_RESOLUTION_Y - 20:
                time.sleep(50)
                sys.exit()
        if direction == "UP":
            snake.pos_snake[1] -= CELLULE_SIZE
        elif direction == "DOWN":
            snake.pos_snake[1] += CELLULE_SIZE
        elif direction == "RIGHT":
            snake.pos_snake[0] += CELLULE_SIZE
        elif direction == "LEFT":
            snake.pos_snake[0] -= CELLULE_SIZE
        if direction == "STOP":
            snake.pos_snake = snake.pos_snake
    
    def eaten_apple(self, apple):
        print(f"print apple pos {apple.pos}")
        print(f"print snake pos {snake.pos_snake}")
        print(f"place apple {apple.place}")
        print(f"score {snake.score}")
        if snake.pos_snake[0] >= apple.pos[0] - 10 and snake.pos_snake[0] <= apple.pos[0] + 10 \
            and snake.pos_snake[1] >= apple.pos[1] - 10 and snake.pos_snake[1] <= apple.pos[1] + 10:
            snake.score += apple.score
            return True
        return False
            

class Game(object):
    def __init__ (self):
        pygame.display.set_caption(GAME_TITLE)
        pygame.display.set_icon(APP_PICTURE)

    def init_WINDOW(self, apple):
        WINDOW.fill(BLACK_RGB)
        if GAME_GRID:
            self.game_grid()
        self.draw_snake_apple(apple)
        pygame.display.flip()
    
    def game_grid(self):
        for x in range(CELLULE_SIZE, (SCREEN_RESOLUTION_X), CELLULE_SIZE):
            pygame.draw.line(WINDOW, (112,128,144), (x, CELLULE_SIZE), [x, SCREEN_RESOLUTION_Y - 6])
        for y in range(CELLULE_SIZE, (SCREEN_RESOLUTION_Y), CELLULE_SIZE):
            pygame.draw.line(WINDOW, (112,128,144), (CELLULE_SIZE, y), [SCREEN_RESOLUTION_X - 6, y])

    def draw_snake_apple(sefl, apple):
        pygame.draw.rect(WINDOW, (WHITE_RGB), (0, 0, SCREEN_RESOLUTION_X, SCREEN_RESOLUTION_Y), 18)
        pygame.draw.rect(WINDOW, (GREEN_RGB), (snake.pos_snake[0], snake.pos_snake[1], snake.body_size, snake.body_size))
        WINDOW.blit(apple.apple_picture, apple.pos)

    def start_game(self, snake):
        fps = pygame.time.Clock()
        start_game = True
        direction = ""
        place = 0
        apple = Apple(place)
        while start_game:
            fps.tick(FPS)
            self.init_WINDOW(apple)
            direction = snake.get_event(direction)
            if snake.eaten_apple(apple) == True:
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
        return (random.randrange(10, SCREEN_RESOLUTION_X - 20, 10), random.randrange(10, SCREEN_RESOLUTION_Y - 20, 10))


if __name__ == "__main__":
    # if SCREEN_RESOLUTION_X % SIZE != 0 or SCREEN_RESOLUTION_Y % SIZE != 0:
    #     print("Error: Size CELLULE")
    #     sys.exit()
    print(CELLULE_NB_X)
    print(CELLULE_NB_Y)
    # pygame.init()
    # game = Game()
    # snake = Snake([320, 240])
    # game.start_game(snake)
    # pygame.quit()
