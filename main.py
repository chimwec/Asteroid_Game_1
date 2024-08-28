# this allows us to use code from
# the open-source pygame library
import sys
import os
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot




def main():
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    back_ground = pygame.image.load('darkshot.jpg')
    back_ground = pygame.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))
    back_ground.set_colorkey((255, 0, 0))
    score = 0
    score_increment = 10
    
   

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    


    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    font = pygame.font.Font(None, 40)


    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for updates in updatable:
            updates.update(dt)


        for obj in asteroids:
            if obj.is_collision(player):
                print("Game Over!")
                sys.exit() 

            for shot in shots:
                if obj.is_collision(shot):
                    score += score_increment
                    shot.kill()
                    obj.split()

            screen.fill(('black'))
            screen.blit(back_ground, (0, 0))
            score_text = font.render(f'Score: {score}', True, (255, 255, 255), 'blue')
            screen.blit(score_text, (10, 10))

        for obj in drawable:
            obj.draw(screen)


       
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
