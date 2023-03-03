import pygame, sys
import objects
# Game Varibles
BLACK = (0,0,0)
WHITE = (255,255,255)
WINDOW_SIZE = (720,480)
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480
RED = (255,0,0)


# Inicializing game and settings
pygame.init()
timer = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)



ball = objects.Ball(screen, (WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2))

def main():
    while True:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(BLACK)
        
        #border = pygame.draw.rect(screen, RED, (700, 0, WINDOW_WIDTH, WINDOW_HEIGHT), 2)        
                
        ball.draw()
        ball.collisions()

        pygame.display.flip()
if __name__ == "__main__":
    main()

