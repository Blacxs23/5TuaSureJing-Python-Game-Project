import pygame

pygame.init()

# Screen dimensions
screen_w = 1024
screen_h = 576
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("Tug of War")

# background 1
bg_start = pygame.image.load("pygame_app/bg/tow_bg2.png")
screen.blit(bg_start,(0,0))

#player1
player_left = pygame.image.load("")

#player2
player_left = pygame.image.load("")


run = True

fps = 60
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
