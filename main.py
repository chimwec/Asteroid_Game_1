# this allows us to use code from
# the open-source pygame library
import pygame
from constants import * 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()
        

if __name__ == "__main__":
    main()


     This repo is for a game that i want to practice develop, i have done few but this will be more advanced one yet. 
 I want it to demonstrate my versitility
