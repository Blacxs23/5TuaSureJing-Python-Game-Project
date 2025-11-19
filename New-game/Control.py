import pygame
from Character import Fighter
pygame.init()

def control(screen):
    #setting game window
    screen_w = 1024
    screen_h = 576
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("DTI Fighter - Control")

    #Set framerate
    clock = pygame.time.Clock()
    FPS = 60

    #import background image
    bg_image = pygame.image.load("New-game/asset/bg/control.png")
    # screen.blit(bg_start,(0,0))

    #import music
    pygame.mixer.music.load("New-game/asset/sound/musiclobby.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0, 5000)

    #function for drawing background
    def draw_bg():
        scaled_bg = pygame.transform.scale(bg_image, (screen_w, screen_h))
        screen.blit(scaled_bg, (0,0))

    #update display
    pygame.display.update()

    run = True
    while run: #all running game code must in this while loop

        #add clock tick to limit player movement
        clock.tick(FPS)

        #draw bg
        draw_bg()

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