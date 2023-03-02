import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, surface, color, pos_size, x, y):
        self.width = pos_size[0]
        self.heigth = pos_size[1]
        self.x = x
        self.y = y
        
        self.color = color
        self.surface = surface
        pygame.sprite.Sprite.__init__(self)
        pygame.draw.rect(self.surface,self.color,
                         (self.width, self.heigth, self.x, self.y))

        
    def move(self, key):
        if key[pygame.K_w]:
            self.y -= 10  
        
        elif key[pygame.K_s]:
            self.y += 10
        
class Ball(pygame.sprite.Sprite):
    def __init__(self, size, color):
        pgame.sprite.Sprite.__init__(self)
        self.size = (10, 10)    
        self.color = color