"""
Snake Game | constants.py
Made with PyGame
by : https://github.com/Jean-xavierr
"""

import pygame

# Game Constants | Window Constants
FPS = 5
DEBUG = True
SCREEN_RESOLUTION_X = 640
SCREEN_RESOLUTION_Y = 480
GAME_TITLE = "Pygame Snake"
APP_PICTURE = pygame.image.load("srcs_pictures/icone_snake00.png")
BACKGROUND = pygame.image.load("srcs_pictures/green_gradient_middle.jpg")
WINDOW = pygame.display.set_mode((SCREEN_RESOLUTION_X, SCREEN_RESOLUTION_Y))
SIZE = 20                                           # Body size of the snake
CELL_SIZE = SIZE                                    # CELL size = Body size of the snake
CELL_NB_X = int(SCREEN_RESOLUTION_X / CELL_SIZE)    # Number of cells in horizontal
CELL_NB_Y = int(SCREEN_RESOLUTION_Y / CELL_SIZE)    # Number of cells in vertical

# Game Window Constants
GAME_WINDOW_LENGHT_X = (CELL_NB_X - 4) * CELL_SIZE              # Width of the playing area
GAME_WINDOW_LENGHT_Y = (CELL_NB_Y - 6) * CELL_SIZE              # Height of the playing area
GAME_WINDOW_POSX = CELL_SIZE * 2                                # Starting position in X of the playing area
GAME_WINDOW_POSY = CELL_SIZE * 4                                # Starting position in Y of the playing area
GAME_WINDOW_POSX_MAX = GAME_WINDOW_LENGHT_X + GAME_WINDOW_POSX  # Last position in X of the playing area
GAME_WINDOW_POSY_MAX = GAME_WINDOW_LENGHT_Y + GAME_WINDOW_POSY  # Last position in Y of the playing area
GAME_GRID = True                                                # Activation of the game grid

# Menu button

BUTTON_START = pygame.image.load("srcs_pictures/button_start.png")
BUTTON_STATS = pygame.image.load("srcs_pictures/button_stats.png")
BUTTON_QUIT = pygame.image.load("srcs_pictures/button_quit.png")
BUTTON_1P = pygame.image.load("srcs_pictures/button_1p.png")
BUTTON_2P = pygame.image.load("srcs_pictures/button_2p.png")
BUTTON_INFO = pygame.image.load("srcs_pictures/powerup_box.png")
BUTTON_BACK = pygame.image.load("srcs_pictures/button_back.png")

# Menu pictures

GAME_TOY = pygame.image.load("srcs_pictures/game_toy_console.png")

# Color RGB Constants
BLACK_RGB = pygame.Color(0, 0, 0)
WHITE_RGB = pygame.Color(255, 255, 255)
BLUE_RGB = pygame.Color(0, 190, 255)
GREEN_RGB = pygame.Color(0, 255, 0)
YELLOW_RGB = pygame.Color(255, 255, 51)
# MINT_GREEN_RGB = pygame.Color(152, 251, 152)
SALTE_GREY_RGB = pygame.Color(112,128,144)

# Color Terminal ConstatsRED_COLOR = "\33[31m"
RED_COLOR = "\31[32m"
GREEN_COLOR = "\33[32m"
YELLOW_COLOR = "\33[33m"
BLUE_COLOR = "\33[34m"
PURPLE_COLOR = "\33[35m"
LIGHT_BLUE_COLOR = "\33[36m"
WHITE_COLOR = "\33[37m"

# Apple_pictures
PATH_APPLE_PICTURES = "srcs_pictures/apple_pictures/"
RED_APPLE = pygame.image.load(PATH_APPLE_PICTURES + "red_apple.png")
GOLDEN_APPLE = pygame.image.load(PATH_APPLE_PICTURES + "golden_apple.png")
GREEN_APPLE = pygame.image.load(PATH_APPLE_PICTURES + "green_apple.png")
BLUE_APPLE = pygame.image.load(PATH_APPLE_PICTURES + "blue_apple.png")