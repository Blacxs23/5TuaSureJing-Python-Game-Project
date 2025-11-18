import pygame
from Character import Fighter
pygame.init()
from pygame import mixer

#inport font pygame module
pygame.font.init()

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
    PUNYA_SIZE = 160
    PUNYA_SCALE = 4
    PUNYA_OFFSET = [15,0]
    PUNYA_DATA = [PUNYA_SIZE,PUNYA_SCALE,PUNYA_OFFSET]
    TU_MAN_SIZE = 160
    TU_MAN_SCALE = 5
    TU_MAN_OFFSET = [15,0]
    TU_MAN_DATA = [TU_MAN_SIZE,TU_MAN_SCALE,TU_MAN_OFFSET]

    #import background image
    bg_image = pygame.image.load("New-game/asset/bg/bg2_boonchoo.png")

    #import sound
    pygame.mixer.music.load("New-game/asset/sound/music1.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0, 5000)

    #function for drawing background
    def draw_bg():
        scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
        screen.blit(scaled_bg, (0,0))

    # load spritesheets
    punya_sheet = pygame.image.load("New-game/asset/character/punya/punya_idel.png").convert_alpha()
    tu_man_sheet = pygame.image.load("New-game/asset/character/tu_man/tu_man_idel.png").convert_alpha()

    #define number of steps in each animation
    PUNYA_ANIMATION_STEPS = [1, 1, 1, 1, 1, 1]
    TU_MAN_ANIMATION_SETPS = [1, 1, 1, 1, 1, 1]

    #create two instances of fighters
    fighter_1 = Fighter(1,150,350,False,PUNYA_DATA, punya_sheet, PUNYA_ANIMATION_STEPS)
    fighter_2 = Fighter(2,900,350,False,TU_MAN_DATA,tu_man_sheet ,TU_MAN_ANIMATION_SETPS)

    clock.tick(60)  # Limit FPS

    pygame.display.update()

    font = pygame.font.Font(None, 60)

    run = True
    while run: #all running game code must in this while loop

        #add clock tick to limit player movement
        clock.tick(FPS)

        #draw bg
        draw_bg()

        #time
        time_now = pygame.time.get_ticks() // 1000  # seconds since start
        countdown = 60 - time_now

        #shi 19/11
        #make clock
        #load font

        text = font.render(str(countdown), True, (255, 255, 255))
        screen.blit(text, (495, 17))

        #แสดงหลอดเลือด   #stamp
        draw_health_bar(fighter_1.health, 30, 20)
        draw_health_bar(fighter_2.health, 600, 20)
        
        #move fighter
        fighter_1.move(screen_width, screen_height, screen, fighter_2)
        fighter_2.move(screen_width, screen_height, screen, fighter_1)

        # zetta
        # update fighter
        fighter_1.update()
        fighter_2.update()

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
        if countdown == 0:
            pygame.quit()

    return