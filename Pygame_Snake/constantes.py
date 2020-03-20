import pygame

# Game Constantes
SCREEN_RESOLUTION_X = 640
SCREEN_RESOLUTION_Y = 480
GAME_TITLE = "Pygame Snake"
APP_PICTURE = pygame.image.load("srcs_pictures/monster_reaper.png")
WINDOW = pygame.display.set_mode((SCREEN_RESOLUTION_X, SCREEN_RESOLUTION_Y))
FPS = 20
SIZE = 10
CELLULE_SIZE = SIZE
CELLULE_NB_X = int(SCREEN_RESOLUTION_X / CELLULE_SIZE)    # Nombre de cellules en abscisse
CELLULE_NB_Y = int(SCREEN_RESOLUTION_Y / CELLULE_SIZE)    # Nombre de cellules en ordonnée
GAME_GRID = True

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