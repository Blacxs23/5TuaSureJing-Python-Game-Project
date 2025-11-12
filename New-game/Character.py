import pygame

# create class to import to main
class Fighter():
    
    # auto this def
    def __init__(self,player ,x, y, flip, data, sprite_sheet, animation_steps):
        self.player = player
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet,animation_steps)
        self.action = 0 #0:idel #1:run #2:jump #3:attack #4:take hit #5:death
        self.frame_index = 0
        self.image =self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x,y, 80,180))
        self.vel_y = 0
        self.running = False
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        self.alive = True

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
                temp_img = pygame.transform.scale(temp_img, (200, 280))  # หรือขนาดที่ต้องการ
                temp_img_list.append(temp_img)
            animation_list.append(temp_img_list)

        return animation_list


    # move function
    def move(self,screen_width,screen_height,surface,target):
        speed = 10
        gravity = 2
        dx = 0
        dy = 0
        self.running = False
        self.attack_type = 0

        #get keypresses
        key = pygame.key.get_pressed()

        if self.attacking == False:
            #check player 1 controls
            if self.player == 1:
                #movement
                if key[pygame.K_a]:
                    dx = -speed
                    self.running = True
                if key[pygame.K_d]:
                    dx = speed
                    self.running = True
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

                #check player 2 controls
            if self.player == 2:
                #movement
                if key[pygame.K_LEFT]:
                    dx = -speed
                    self.running = True
                if key[pygame.K_RIGHT]:
                    dx = speed
                    self.running = True
                #jump
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                #attack
                if key[pygame.K_KP1] or key[pygame.K_KP2]:
                    self.attack(target)
                #determine which attack type was used
                if key[pygame.K_KP1]:
                    self.attack_type = 1
                if key[pygame.K_KP2]:
                    self.attack_type = 2

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

    # handle animation updates
    def update(self):
        #check what action the player is performing
        if self.running == True:
            self.action = 1
        else:
            self.action = 0

        animation_cooldown = 50

        frame_count = len(self.animation_list[self.action])
        if frame_count > 0:
            self.image = self.animation_list[self.action][self.frame_index % frame_count]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
          self.frame_index += 1
          self.update_time = pygame.time.get_ticks()
          #check if the animation has finished
        if self.frame_index >= len(self.animation_list[self.action]):
        #if the player is dead then end the animation
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                #check if an attack was executed
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = 20
                #check if damage was taken
                if self.action == 5:
                    self.hit = False
                    #if the player was in the middle of an attack, then the attack is stopped
                    self.attacking = False
                    self.attack_cooldown = 20

    def attack(self, surface):
      attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y,2*self.rect.width, self.rect.height)
      pygame.draw.rect(surface, (0, 255, 0), attacking_rect)    

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(self.image,(self.rect.x - (self.offset[0]*self.image_scale),self.rect.y - (self.offset[1]*self.image_scale)))