import pygame

# Game Constantes
SCREEN_RESOLUTION_X = 640
SCREEN_RESOLUTION_Y = 480
GAME_TITLE = "Pygame Snake"
APP_PICTURE = pygame.image.load("srcs_pictures/monster_reaper.png")

# Color RGB Constantes
BLACK_RGB = pygame.Color(0, 0, 0)
WHITE_RGB = pygame.Color(255, 255, 255)
GREEN_RGB = pygame.Color(0, 255, 0)

# Apple_pictures
PATH_APPLE_PICTURES = "srcs_pictures/apple_pictures/"
RED_APPLE = pygame.image.load(PATH_APPLE_PICTURES + "red_apple.png")
GOLDEN_APPLE = pygame.image.load(PATH_APPLE_PICTURES + "golden_apple.png")
GREEN_APPLE = pygame.image.load(PATH_APPLE_PICTURES + "green_apple.png")
BLUE_APPLE = pygame.image.load(PATH_APPLE_PICTURES + "blue_apple.png")