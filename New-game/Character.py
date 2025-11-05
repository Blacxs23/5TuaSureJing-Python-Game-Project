import pygame

# create class to import to main
class Fighter():
    
    # auto this def
    def __init__(self, x, y):
        self.rect = pygame.Rect((x,y, 80,180))
        self.health = 100
        self.attack_type = 0  

    # move function
    def move(self, screen_width):
        speed = 10
        dx = 0
        dy = 0

        #get keypresses
        key = pygame.key.get_pressed()

        #movement
        if key[pygame.K_a]:
            dx = -speed
        if key[pygame.K_d]:
            dx = speed

        #attack
        if key[pygame.K_f] or key[pygame.K_0]:

          #attack type was used
          if key[pygame.K_f]:
              self.attack_type = 1
          if key[pygame.k_0]:
              self.attack_type = 2

        #ensure player stays on screen
        if self.rect.left + dx < 0:
            dx =  -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        #update player position
        self.rect.x += dx
        self.rect.y += dy

def attack(self):
    attack_rect = pygame.Rect(self.rect.centrex, self.rect.y, 2 * self.rect.width, self.rect.height)
    

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)