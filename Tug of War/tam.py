import pygame


#เรียกใช้โมดูล
pygame.init()

#หน้าจอ
screen_w = 1024
screen_h = 576
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("Tug of War")

#พื้นหลัง
background = pygame.image.load ("Tug of War/bg/tow_bg2.png")   
background = pygame.transform.scale(background, (screen_w, screen_h))

#round
round_img = pygame.image.load ("Tug of War/asset/round/round_1.png")
round_img = pygame.transform.scale(round_img, (500, 100))  
round_rect = round_img.get_rect(center=(screen_w / 2, screen_h / 2))

#ตัวจับเวลา
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
fade_duration = 3000  #3วิ

#ลูปหลัก
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
#คำนวนเวลา
    elapsed_time = pygame.time.get_ticks() - start_time
    alpha = max(255 - int((elapsed_time / fade_duration) * 255), 0)

    #ทำสำเนา
    round_img_fade = round_img.copy()
    round_img_fade.set_alpha(alpha) #ตั้งค่าความทึบของ

    #วาดภาพ(Blit)ลงหน้าจอและอัปเดตหน้าจอ
    screen.blit(background, (0, 0))
    if alpha > 0:
        screen.blit(round_img_fade, round_rect)
    pygame.display.flip()

#คุมเฟรมเรท
    clock.tick(60)


pygame.quit()
sys.exit()