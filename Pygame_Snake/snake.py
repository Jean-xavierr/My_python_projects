import pygame
import random
import sys
import time
from constantes import *

class Snake(object):
    def __init__(self, pos_snake):
        self.pos_snake = pos_snake
        self.body_snake = [pos_snake]
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
        if snake.pos_snake[0] < 6 or snake.pos_snake[0] > SCREEN_RESOLUTION_X - 16 \
            or snake.pos_snake[1] < 6 or snake.pos_snake[1] > SCREEN_RESOLUTION_Y - 16:
                time.sleep(50)
                sys.exit()
        if direction == "UP":
            snake.pos_snake[1] -= 1
        elif direction == "DOWN":
            snake.pos_snake[1] += 1
        elif direction == "RIGHT":
            snake.pos_snake[0] += 1
        elif direction == "LEFT":
            snake.pos_snake[0] -= 1
        if direction == "STOP":
            snake.pos_snake = snake.pos_snake
    
    def eaten_apple(self, apple):
        print(f"print apple pos {apple.pos}")
        print(f"print snake pos {snake.pos_snake}")
        print(f"place apple {apple.place}")
        print(f"score {snake.score}")
        if snake.pos_snake[0] >= apple.pos[0] - 8 and snake.pos_snake[0] <= apple.pos[0] + 8 \
            and snake.pos_snake[1] >= apple.pos[1] - 8 and snake.pos_snake[1] <= apple.pos[1] + 8:
            snake.score += apple.score
            return True
        return False
            

class Game(object):
    def __init__ (self):
        pygame.display.set_caption(GAME_TITLE)
        pygame.display.set_icon(APP_PICTURE)

    def init_window(self, apple):
        window = pygame.display.set_mode((SCREEN_RESOLUTION_X, SCREEN_RESOLUTION_Y))
        window.fill(BLACK_RGB)
        pygame.draw.rect(window, (WHITE_RGB), (0, 0, SCREEN_RESOLUTION_X, SCREEN_RESOLUTION_Y), 10)
        pygame.draw.rect(window, (GREEN_RGB), (snake.pos_snake[0], snake.pos_snake[1], 10, 10))
        window.blit(apple.apple_picture, apple.pos)
        pygame.display.flip()

    def start_game(self, snake):
        start_game = True
        direction = ""
        place = 0
        apple = Apple(place)
        while start_game:
            self.init_window(apple)
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
        return (random.randint(10, SCREEN_RESOLUTION_X - 20), random.randint(10, SCREEN_RESOLUTION_Y - 20))


if __name__ == "__main__":
    pygame.init()
    game = Game()
    snake = Snake([320, 240])
    game.start_game(snake)
    pygame.quit()
