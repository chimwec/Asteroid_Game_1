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

    # Initialize the joystick subsystem
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joystick in joysticks:
        joystick.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # Assuming button 0 is the fire button
                    player.shoot()

        for updates in updatable:
            if isinstance(updates, Player) and joysticks:
                joystick = joysticks[0]  # Use the first connected joystick
                axis_x = joystick.get_axis(0)  # Left stick horizontal axis
                axis_y = joystick.get_axis(1)  # Left stick vertical axis
                updates.update(dt, axis_x, axis_y)
            else:
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


        # Pass joystick data to the player update method
        if joysticks:
            joystick = joysticks[0]  # Use the first connected joystick
            axis_x = joystick.get_axis(0)  # Left stick horizontal axis
            axis_y = joystick.get_axis(1)  # Left stick vertical axis
            player.update(dt, axis_x, axis_y)
        else:
            player.update(dt, 0, 0)

        pygame.display.flip()

        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
