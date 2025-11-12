import pygame

# create class to import to main
class Fighter():
    
    # auto this def
    def __init__(self, x, y, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = False
        self.animation_list = self.load_images(sprite_sheet,animation_steps)
        self.action = 0 #0:idel #1:run #2:jump #3:attack #4:take hit #5:death
        self.frame_index = 0
        self.image =self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect((x,y, 80,180))
        self.vel_y = 0
        self.jump = False
        self.attack_type = 0
        self.health = 100

    # zetta 12/11/25
    def load_images(self, sprite_sheet, animation_steps):
        animation_list = []
        sheet_width, sheet_height = sprite_sheet.get_size()

        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                rect_x = x * self.size
                rect_y = y * self.size

                # ตรวจไม่ให้ rectangle เกินขนาดภาพ
                if rect_x + self.size > sheet_width or rect_y + self.size > sheet_height:
                    print(f"!! Skip frame ({x}, {y}) — outside sheet area")
                    continue

                temp_img = sprite_sheet.subsurface(rect_x, rect_y, self.size, self.size)
                temp_img = pygame.transform.scale(temp_img, (80, 180))  # หรือขนาดที่ต้องการ
                temp_img_list.append(temp_img)
            animation_list.append(temp_img_list)

        return animation_list


    # move function
    def move(self, screen_width,screen_height, surface):
        speed = 10
        gravity = 2
        dx = 0
        dy = 0

        #get keypresses
        key = pygame.key.get_pressed()

        #movement
        if key[pygame.K_a]:
            dx = -speed
        if key[pygame.K_d]:
            dx = speed
        #jump
        if key[pygame.K_w] and self.jump == False:
            self.vel_y = -30
            self.jump = True
            
        #attack
        if key[pygame.K_r]:
            self.attack(surface)

            #determine which attack was uesd
            if key[pygame.K_r]:
                self.attack_type = 1 

        #apply gravity
        self.vel_y += gravity

        dy += self.vel_y

        #ensure player stays on screen
        if self.rect.left + dx < 0:
            dx =  -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height -50 :
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 50 - self.rect.bottom

        #update player position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface):
      attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y,2*self.rect.width, self.rect.height)
      pygame.draw.rect(surface, (0, 255, 0), attacking_rect)    

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(self.image,(self.rect.x - (self.offset[0]*self.image_scale),self.rect.y - (self.offset[1]*self.image_scale)))