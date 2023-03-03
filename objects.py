import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, surface, color, pos_size, x, y):
        self.width = pos_size[0]
        self.heigth = pos_size[1]
        self.x = x
        self.y = y
        
        self.color = color
        self.surface = surface
        super().__init__()
        pygame.draw.rect(self.surface,self.color,
                         (self.width, self.heigth, self.x, self.y))
        
    def move(self, key):
        if key[pygame.K_w]:
            self.heigth -= 3  
        elif key[pygame.K_s]:
            self.heigth += 3
        
    def draw(self):
        pygame.draw.rect(self.surface,self.color, (self.width, self.heigth, self.x, self.y))    



        
        
class Ball(pygame.sprite.Sprite):
    def __init__(self, size, color):
        syper().__init__()
        self.size = (10, 10)    
        self.color = WHITE