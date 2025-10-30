import pygame
pygame.init()

screen_width = 1280
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tug of War")
running = True

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
screen.fill(WHITE)
pygame.draw.circle(screen, BLUE, (400, 300), 75, 5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.QUIT