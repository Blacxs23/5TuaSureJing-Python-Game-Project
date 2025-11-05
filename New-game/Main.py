import pygame
from Character import Fighter
pygame.init()

#setting game window
screen_width = 1024
screen_height = 576
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DTI Fighter")

#Set framerate
clock = pygame.time.Clock()
FPS = 60


#กำหนดสี  #stamp
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#ฟังชั่นวาดหลอดเลือด  #stamp
def draw_health_bar(health, x, y):
    pygame.draw.rect(screen, YELLOW, (x, y, 400, 30))

#create two instances of fighters
fighter_1 = Fighter(150,350)
fighter_2 = Fighter(900,350)

#import background image
bg_image = pygame.image.load("New-game/asset/bg/bg2_boonchoo.png").convert_alpha()

#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
    screen.blit(scaled_bg, (0,0))


#กำหนดสี
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


#game loop
run = True
while run: #all running game code must in this while loop
    
    #add clock tick to limit player movement
    clock.tick(FPS)

    #draw bg
    draw_bg()

    #แสดงหลอดเลือด   #stamp
    draw_health_bar(fighter_1.health, 30, 20)
    draw_health_bar(fighter_2.health, 650, 20)
    
    #move fighter
    fighter_1.move(screen_width)

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #update display
    pygame.display.update()

    #chech if press exit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#exit game
pygame.QUIT()