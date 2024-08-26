# this allows us to use code from
# the open-source pygame library
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player1.draw(screen)
        pygame.display.flip()
        

        dt = clock.tick(60) / 1000
        player1.update(dt)




if __name__ == "__main__":
    main()
