import pygame
import Character as fighter  # this imports all fighter-related functions from Character.py

pygame.init()

def main_game(screen):

    # Game setup
    screen_width = 1024
    screen_height = 576
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("DTI Fighter - Main")

    clock = pygame.time.Clock()
    FPS = 60  # lock the game to 60 frames per second for smoother animation

    # setting color
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)

    # HEALTH BAR FUNCTION
    # draws a health bar for each fighter
    def draw_health_bar(health, x, y):
        ratio = health / 100  # convert health to a 0–1 scale
        pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))  # border
        pygame.draw.rect(screen, RED, (x, y, 400, 30))  # background
        pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))  # actual health

    #BACKGROUND SETUP
    bg_image = pygame.image.load("New-game/asset/bg/bg2_boonchoo.png")

    def draw_bg():
        # scale the background to fit the window and draw it
        scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
        screen.blit(scaled_bg, (0, 0))

    # CHARACTER SPRITES

    punya_sheet = pygame.image.load("New-game/asset/character/punya/punya_idel.png").convert_alpha()
    tu_man_sheet = pygame.image.load("New-game/asset/character/tu_man/tu_man_idel.png").convert_alpha()

    # fighter setup data: size, scale, and position offset
    PUNYA_DATA = [160, 4, [15, 0]]
    TU_MAN_DATA = [160, 4, [15, 0]]

    # how many animation frames exist for each action
    PUNYA_ANIMATION_STEPS = [1, 1, 1, 1, 1, 1]
    TU_MAN_ANIMATION_STEPS = [1, 1, 1, 1, 1, 1]

    #CREATE FIGHTER OBJECTS
    fighter_1 = fighter.create_fighter(1, 150, 350, False, PUNYA_DATA, punya_sheet, PUNYA_ANIMATION_STEPS)
    fighter_2 = fighter.create_fighter(2, 900, 350, False, TU_MAN_DATA, tu_man_sheet, TU_MAN_ANIMATION_STEPS)

    #GAME LOOP
    run = True
    while run:
        # keep the game running at the defined frame rate
        clock.tick(FPS)

        # draw the background and health bars
        draw_bg()
        draw_health_bar(fighter_1["health"], 30, 20)
        draw_health_bar(fighter_2["health"], 600, 20)

        #UPDATE PLAYER MOVEMENT & ACTIONS
        # this handles input, gravity, jumping, and attacks
        fighter.move(fighter_1, screen_width, screen_height, screen, fighter_2)
        fighter.move(fighter_2, screen_width, screen_height, screen, fighter_1)

        # UPDATE ANIMATIONS
        # cycles through frames in each fighter's animation
        fighter.update(fighter_1)
        fighter.update(fighter_2)

        #DRAW FIGHTERS
        # displays both fighters on the screen
        fighter.draw(fighter_1, screen)
        fighter.draw(fighter_2, screen)

        # refresh the display each frame
        pygame.display.update()

        # EXIT

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # window close button
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # ESC key
                run = False