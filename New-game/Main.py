import pygame
from class_fighter import Fighter
pygame.init()

#setting game window
screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Araiwa")

#import background image
bg_image = pygame.image.load("asset"/"background.jpg").convert_alpha()

#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
    screen.blit(scaled_bg, (0,0))


#create two instances of fighters
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

#draw fighters
fighter_1.draw(screen)
fighter_2.draw(screen)

#game loop
run = True
while run: #all running game code must in this while loop
    
    draw_bg()

    for event in pygame.event.get(): #chech if press exit button
        if event.type == pygame.QUIT:
            run = False


    #update display
    pygame.display.update()

#exit game
pygame.QUIT()
