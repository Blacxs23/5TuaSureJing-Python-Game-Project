import pygame
import sys

pygame.init()

screen_w = 1024
screen_h = 576
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("Tug of War")

background = pygame.image.load ("pygame_app/bg/tow_bg2.png")  # 
background = pygame.transform.scale(background, (screen_w, screen_h))


round_img = pygame.image.load("round1.png").convert_alpha()
round_img = pygame.transform.scale(round_img, (600, 200))  # ปรับขนาดถ้าต้องการ
round_rect = round_img.get_rect(center=(screen_w / 2, screen_h / 2))

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
fade_duration = 3000  


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
    elapsed_time = pygame.time.get_ticks() - start_time

    
    alpha = max(255 - int((elapsed_time / fade_duration) * 255), 0)

    
    round_img_fade = round_img.copy()
    round_img_fade.set_alpha(alpha)

    
    screen.blit(background, (0, 0))

    
    if alpha > 0:
        screen.blit(round_img_fade, round_rect)

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()