import pygame
from Character import Fighter
pygame.init()

#setting game window
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Araiwa")

#Set framerate
clock = pygame.time.Clock()
FPS = 60

#import background image
bg_image = pygame.image.load("New-game/asset/dirt.jpg").convert_alpha()

#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
    screen.blit(scaled_bg, (0,0))

#create two instances of fighters
fighter_1 = Fighter(150,450)
fighter_2 = Fighter(1000,450)

#game loop
run = True
while run: #all running game code must in this while loop
    
    #add clock tick to limit player movement
    clock.tick(FPS)

    #draw bg
    draw_bg()

    #move fighter
    fighter_1.move(screen_width)

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #chech if press exit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.update()

#exit game
pygame.QUIT()