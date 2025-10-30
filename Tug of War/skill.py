import pygame

pygame.init()

# Screen dimensions
screen_w = 1024
screen_h = 576
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("Tug of War")

# background 1
bg_start = pygame.image.load("Tug of War/bg/tow_bg2.png")
screen.blit(bg_start,(0,0))

#player1
player_left = pygame.image.load("Tug of War/asset/player/player_1.png")
player_left = pygame.transform.scale(player_left,(150,180))
player_left_rect = player_left.get_rect()
player_left_rect = (100,250)
screen.blit(player_left,player_left_rect)

#player2
player_right = pygame.image.load("Tug of War/asset/player/player_2.png")
player_right = pygame.transform.scale(player_right,(150,180))
player_right_rect = player_left.get_rect()
player_right_rect = (775,250)
screen.blit(player_right,player_right_rect)



run = True

fps = 60
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            #botton_skill_player1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]: #Darkness
                print("Prevents the opponent from using skills for about 2 seconds")
            if keys[pygame.K_w]: #Freeze
                print("Freeze the opposite side for 0.5 seconds, they can't do anything")
            if keys[pygame.K_e]: #Multiply
                print("Multiply the process by 1.2 times the normal for 2 seconds")
            if keys[pygame.K_v]: #Steal Process
                print('Steal the process of pressing the opposite side for 1.5 seconds')

            #botton_skill_player2
            if keys[pygame.K_i]: #Darkness
                print("Prevents the opponent from using skills for about 2 seconds")
            if keys[pygame.K_o]: #Freeze
                print("Freeze the opposite side for 0.5 seconds, they can't do anything")   
            if keys[pygame.K_p]: #Multiply
                print("Multiply the process by 1.2 times the normal for 2 seconds")
            if keys[pygame.K_m]: #Steal Process
                print('Steal the process of pressing the opposite side for 1.5 seconds')
            
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
