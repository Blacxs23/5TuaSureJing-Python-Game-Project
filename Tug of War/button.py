import pygame

# play button
def play_nomal():
    play_default = pygame.image.load("button/play_default.png")
    play_default = pygame.transform.scale(play_default,(225,45))
    play_default_rect = play_default.get_rect()
    play_default_rect.centerx = screen_w // 2
    play_default_rect.centery = 300
    screen.blit(play_default,play_default_rect)


# control button

# credit button