import pygame
from Character import Fighter
pygame.init()

def main_game(screen):
    #setting game window
    screen_width = 1024
    screen_height = 576
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("DTI Fighter - Main")

    #Set framerate
    clock = pygame.time.Clock()
    FPS = 60

    #กำหนดสี  #stamp
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)

    #ฟังชั่นวาดหลอดเลือด  #stamp
    def draw_health_bar(health, x, y):
        ratio = health / 100
        pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
        pygame.draw.rect(screen, RED, (x, y, 400, 30))
        pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

    # define fighter variables
    PUNYA_SIZE = 80
    PUNYA_SCALE = 2
    PUNYA_OFFSET = [30,0]
    PUNYA_DATA = [PUNYA_SIZE,PUNYA_SCALE,PUNYA_OFFSET]
    TU_MAN_SIZE = 80
    TU_MAN_SCALE = 2
    TU_MAN_OFFSET = [30,0]
    TU_MAN_DATA = [TU_MAN_SIZE,TU_MAN_SCALE,TU_MAN_OFFSET]

    #import background image
    bg_image = pygame.image.load("New-game/asset/bg/bg2_boonchoo.png")

    #function for drawing background
    def draw_bg():
        scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
        screen.blit(scaled_bg, (0,0))

    # load spritesheets
    punya_sheet = pygame.image.load("New-game/asset/character/punya/punya_idel.png").convert_alpha()
    tu_man_sheet = pygame.image.load("New-game/asset/character/punya/punya_idel.png").convert_alpha()

    #define number of steps in each animation
    PUNYA_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
    TU_MAN_ANIMATION_SETPS = [8, 8, 1, 8, 8, 3, 7]

    #create two instances of fighters
    fighter_1 = Fighter(150,350,PUNYA_DATA, punya_sheet, PUNYA_ANIMATION_STEPS)
    fighter_2 = Fighter(900,350,TU_MAN_DATA,tu_man_sheet ,TU_MAN_ANIMATION_SETPS)

    #กำหนดสี
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)

    run = True
    while run: #all running game code must in this while loop
        
        #add clock tick to limit player movement
        clock.tick(FPS)

        #draw bg
        draw_bg()

        #แสดงหลอดเลือด   #stamp
        draw_health_bar(fighter_1.health, 30, 20)
        draw_health_bar(fighter_2.health, 600, 20)
        
        #move fighter
        fighter_1.move(screen_width, screen_height, screen)

        #draw fighters
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        #update display
        pygame.display.update()

        #chech if press exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

    return