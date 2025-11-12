import pygame
from Character import Fighter
pygame.init()

def control(screen):
    #setting game window
    screen_width = 1024
    screen_height = 576
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("DTI Fighter - control")

    #Set framerate
    clock = pygame.time.Clock()
    FPS = 60