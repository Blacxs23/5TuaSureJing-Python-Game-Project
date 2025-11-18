import pygame
import sys
from Main import main_game

pygame.init()

# Screen dimensions
screen_w = 1024
screen_h = 576
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("DTI Fighter - Menu")

# background 1
bg_start = pygame.image.load("New-game/asset/bg/bg1_dome.png")
# screen.blit(bg_start,(0,0))

# logo
logo = pygame.image.load("New-game/asset/logo/dti_fighter_logo.png")
logo = pygame.transform.scale(logo,(502,278))
logo_rect = logo.get_rect()
logo_rect.centerx = screen_w // 2
logo_rect.centery = 175
# screen.blit(logo,logo_rect)

# ------play button------

# play default
play_default = pygame.image.load("New-game/asset/button/play_default.png")
play_default = pygame.transform.scale(play_default,(225,45))
play_default_rect = play_default.get_rect()
play_default_rect.centerx = screen_w // 2
play_default_rect.centery = 310
# screen.blit(play_default,play_default_rect)

#  play click
play_click = pygame.image.load("New-game/asset/button/play_click.png")
play_click = pygame.transform.scale(play_click,(225,45))
play_click_rect = play_click.get_rect()
play_click_rect.centerx = screen_w // 2
play_click_rect.centery = 310
# screen.blit(play_click,play_click_rect)

# ------control button------

# control_default
control_default = pygame.image.load("New-game/asset/button/control_default.png")
control_default = pygame.transform.scale(control_default,(225,45))
control_default_rect = control_default.get_rect()
control_default_rect.centerx = screen_w // 2
control_default_rect.centery = 360
# screen.blit(control_default,control_default_rect)

# control_click
control_click = pygame.image.load("New-game/asset/button/control_click.png")
control_click = pygame.transform.scale(control_click,(225,45))
control_click_rect = control_click.get_rect()
control_click_rect.centerx = screen_w // 2
control_click_rect.centery = 360
# screen.blit(control_click,control_click_rect)

# -----credit button-----

# credit_default
credit_default = pygame.image.load("New-game/asset/button/credit_default.png")
credit_default = pygame.transform.scale(credit_default,(160,32))
credit_default_rect = credit_default.get_rect()
credit_default_rect.centerx = screen_w // 2
credit_default_rect.centery = 410
# screen.blit(credit_default,credit_default_rect)

# credit_click
credit_click = pygame.image.load("New-game/asset/button/credit_click.png")
credit_click = pygame.transform.scale(credit_click,(160,32))
credit_click_rect = credit_click.get_rect()
credit_click_rect.centerx = screen_w // 2
credit_click_rect.centery = 410
# screen.blit(credit_click,credit_click_rect)

current_play = "play"
current_control = "control"
current_credit = "credit"

clock = pygame.time.Clock()
FPS = 60

def menu():
    run = True
    while run:

        clock.tick(FPS)

        screen.blit(bg_start,(0,0))
        screen.blit(logo,logo_rect)
  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if current_play == "play":
                    if play_default_rect.collidepoint(mouse_pos):
                        main_game(screen)
                        print("play!")

                if current_control == "control":
                    if control_default_rect.collidepoint(mouse_pos):
                        print("control!")
                    
                if current_credit == "credit":
                    if credit_default_rect.collidepoint(mouse_pos):
                        print("credit!")

        current_mouse_pos = pygame.mouse.get_pos()
        hovering_play_button = False
        hovering_control_button = False
        hovering_credit_button = False

        if current_play == "play":
            if play_default_rect.collidepoint(current_mouse_pos):
                hovering_play_button = True

            if hovering_play_button:
                screen.blit(play_click,play_default_rect)
            else:
                screen.blit(play_default,play_default_rect)

        if current_control == "control":
            if control_default_rect.collidepoint(current_mouse_pos):
                hovering_control_button = True

            if hovering_control_button:
                screen.blit(control_click,control_default_rect)
            else:
                screen.blit(control_default,control_default_rect)

        if current_credit == "credit":
            if credit_default_rect.collidepoint(current_mouse_pos):
                hovering_credit_button = True

            if hovering_credit_button:
                screen.blit(credit_click,credit_default_rect)
            else:
                screen.blit(credit_default,credit_default_rect)

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    menu()