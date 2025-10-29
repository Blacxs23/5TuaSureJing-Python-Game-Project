import pygame

#skill
#player1
keys = pygame.key.get_pressed()
if keys[pygame.K_q]: #Darkness
    print("Prevents the opponent from using skills for about 2 seconds")
if keys[pygame.K_w]: #Freeze
    print("Freeze the opposite side for 0.5 seconds, they can't do anything")
if keys[pygame.K_e]: #Multiply
    print("Multiply the process by 1.2 times the normal for 2 seconds")
if keys[pygame.K_v]: #Steal Process
    print('Steal the process of pressing the opposite side for 1.5 seconds')

#player2
if keys[pygame.K_i]: #Darkness
    print("Prevents the opponent from using skills for about 2 seconds")
if keys[pygame.K_o]: #Freeze
    print("Freeze the opposite side for 0.5 seconds, they can't do anything")       
if keys[pygame.K_p]: #Multiply
    print("Multiply the process by 1.2 times the normal for 2 seconds")
if keys[pygame.K_m]: #Steal Process
    print('Steal the process of pressing the opposite side for 1.5 seconds')
