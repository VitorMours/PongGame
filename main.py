#Import and Initialize pygame
import pygame, sys
import objects
pygame.init()
clock = pygame.time.Clock()
window_size = (720,480)
WHITE = (255,255,255)
BLACK = (0,0,0)


display = pygame.display
screen = display.set_mode(window_size)
display.set_caption("Pong Game")

# Creating Players and Objects



def main():
    #Creating Objects
    player_1 = objects.Player(screen,WHITE, (10, int(window_size[1]/2 - 50)),20,100)
    while True:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        screen.fill(BLACK)
        player_1.draw()
        player_1.move(pygame.key.get_pressed())        
                
        display.flip()


if __name__ == "__main__":
    main()