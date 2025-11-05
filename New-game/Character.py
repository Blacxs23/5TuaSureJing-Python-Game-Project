import pygame

# create class to import to main
class Fighter():
    
    # auto this def
    def __init__(self, x, y):
        self.rect = pygame.Rect((x,y, 80,180))
        self.vel_y = 0
        self.jump = False
        self.health = 100
        self.attack_type = 0  

    # move function
    def move(self, screen_width,screen_height):
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
        attack_rect = pygame.Rect(self.rect.centrex, self.rect.y, 2 * self.rect.width, self.rect.height)
        pygame.draw.rect(surface, (0, 255, 0), self.rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)