import pygame

pygame.init()

# Screen dimensions
screen_w = 1024
screen_h = 576
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("Tug of War")

# background 1
bg_start = pygame.image.load("pygame_app/bg/tow_bg1.jpg")
screen.blit(bg_start,(0,0))

# logo
logo = pygame.image.load("pygame_app/logo/tow_logo.png")
logo = pygame.transform.scale(logo,(502,278))
logo_rect = logo.get_rect()
logo_rect.centerx = screen_w // 2
logo_rect.centery = 150
screen.blit(logo,logo_rect)

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