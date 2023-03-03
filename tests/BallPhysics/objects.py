import pygame
import math
class Ball(pygame.sprite.Sprite):
    def __init__(self, surface, position):
        super().__init__()
        self.surface = surface
        self.x = position[0]
        self.y = position [1]
        self.angle = 0
        self.x_vel = 5       
        self.y_vel = 0      
        self.rect_size = 10
        self.color = (255,255,255)
        self.hitbox = pygame.draw.rect(self.surface, self.color, 
                         (self.x-self.rect_size/2, self.y-self.rect_size/2, self.rect_size,self.rect_size))
                 
    def draw(self):     
        self.hitbox = pygame.draw.rect(self.surface, self.color, 
                         (self.x-self.rect_size/2, self.y-self.rect_size/2, self.rect_size,self.rect_size))
        
        
        
    def collisions(self,borders):
        if pygame.Rect.colliderect(self.hitbox, borders):
            self.x_vel *= -1
            self.x += self.x_vel
            self.y_vel *= -1
        else:
            self.x += self.x_vel
            self.y += self.y_vel   