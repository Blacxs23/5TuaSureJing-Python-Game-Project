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
        self.attack_cooldown = 0
        self.hit = False
        self.health = 100
        self.alive = True
        self.actions = {"idel": 0,"run": 1,"jump": 2,"Attack1": 3,"Attack2": 4,"RunAttack": 5,"hit": 6,"death": 7}#เกี่ยวกับอนิเมชั่น
        self.update_action(self.actions["RunAttack"])#เกี่ยวกับอนิเมชั่น

        
        
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


    def load_animations(self, base_path, animation_steps):
        for action, frame_count in animation_steps.items():
            temp_list = []
            path = f"{base_path}/{action}"
            for i in range(frame_count):
                img = pygame.image.load(f"{path}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width() * self.image_scale,
                                                   img.get_height() * self.image_scale))
                temp_list.append(img)
            self.animation_list.append(temp_list)


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
                if key[pygame.K_e]:
                    self.attack(target)
                    #which attack was uesd
                    if key[pygame.K_e]:
                        self.attack_type = 1 

            #check player 2 controls
            if self.player == 2:
                #movement
                if key[pygame.K_j]:
                    dx = -speed
                    self.running = True
                if key[pygame.K_l]:
                    dx = speed
                    self.running = True
                #jump
                if key[pygame.K_i] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                #attack
                if key[pygame.K_u]:
                    self.attack(target)
                    # which attack type was used
                    if key[pygame.K_u]:
                        self.attack_type = 1

        #apply gravity
        self.vel_y += gravity
        dy += self.vel_y

        #make player stays on screen
        if self.rect.left + dx < 0:
            dx =  -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height -50 :
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 50 - self.rect.bottom

        #make players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        #apply attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        #update player position
        self.rect.x += dx
        self.rect.y += dy

    # handle animation updates
    def update(self):
        #check what action the player is performing
        if self.health <= 0:
          self.health = 0
          self.alive = False
          self.update_action(6)#6:death
        elif self.hit == True:
            self.update_action(5)#5:hit
        elif self.attacking == True:
          if self.running:#เกี่ยวกับอนิเมชั่น
             self.update_action(self.actions["RunAttack"])#เกี่ยวกับอนิเมชั่น
          elif self.attack_type == 1:#เกี่ยวกับอนิเมชั่น
             self.update_action(self.actions["Attack1"])#เกี่ยวกับอนิเมชั่น
          elif self.attack_type == 2:#เกี่ยวกับอนิเมชั่น
              self.update_action(self.actions["Attack2"])#เกี่ยวกับอนิเมชั่น
        elif self.jump == True:
            self.update_action(2)#2:jump
        elif self.running == True:
            self.update_action(1)#1:run
        else:
            self.update_action(0)#0:idle

        animation_cooldown = 50

        #update image
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

    def attack(self, target):
        if self.attack_cooldown == 0:
            #execute attack
            self.attacking = True
            if  self.flip:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            else:
                attacking_rect = pygame.Rect(self.rect.right, self.rect.y, self.rect.width, self.rect.height)
            if attacking_rect.colliderect(target.rect):
                target.health -= 10
                target.hit = True 

    # zetta
    def update_action(self, new_action):
        #check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)#เกี่ยวกับอนิเมชั่น
        surface.blit(img, (self.rect.x - (self.offset[0]*self.image_scale),#เกี่ยวกับอนิเมชั่น
                   self.rect.y - (self.offset[1]*self.image_scale)))#เกี่ยวกับอนิเมชั่น