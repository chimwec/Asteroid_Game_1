import sys
from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.timer = 0

    def draw(self, screen):
        # Colors
        ship_color = (100, 150, 250)  # Light blue
        accent_color = (50, 100, 200)  # Darker blue
        engine_color = (255, 100, 50)  # Orange

        # Rotate the ship
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = forward.rotate(90)

        # Main body
        points = [
            self.position + forward * self.radius,
            self.position - forward * self.radius * 0.5 + right * self.radius * 0.7,
            self.position - forward * self.radius * 0.8,
            self.position - forward * self.radius * 0.5 - right * self.radius * 0.7,
        ]
        pygame.draw.polygon(screen, ship_color, points)

        # Accent lines
        pygame.draw.line(screen, accent_color, points[0], points[2], 2)
        pygame.draw.line(screen, accent_color, points[1], points[3], 2)

        # Cockpit
        cockpit_pos = self.position + forward * self.radius * 0.3
        pygame.draw.circle(screen, accent_color, (int(cockpit_pos.x), int(cockpit_pos.y)), int(self.radius * 0.2))

        # Engines
        engine_pos1 = self.position - forward * self.radius * 0.6 + right * self.radius * 0.4
        engine_pos2 = self.position - forward * self.radius * 0.6 - right * self.radius * 0.4
        
        # Engine glow effect
        glow_radius = int(self.radius * 0.3)
        glow_color = (255, 200, 100, 100)  # Semi-transparent yellow
        glow_surf = pygame.Surface((glow_radius * 2, glow_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(glow_surf, glow_color, (glow_radius, glow_radius), glow_radius)
        screen.blit(glow_surf, (int(engine_pos1.x - glow_radius), int(engine_pos1.y - glow_radius)), special_flags=pygame.BLEND_ALPHA_SDL2)
        screen.blit(glow_surf, (int(engine_pos2.x - glow_radius), int(engine_pos2.y - glow_radius)), special_flags=pygame.BLEND_ALPHA_SDL2)

        # Engine nozzles
        nozzle_points1 = [
            engine_pos1,
            engine_pos1 - forward * self.radius * 0.2 + right * self.radius * 0.1,
            engine_pos1 - forward * self.radius * 0.2 - right * self.radius * 0.1,
        ]
        nozzle_points2 = [
            engine_pos2,
            engine_pos2 - forward * self.radius * 0.2 + right * self.radius * 0.1,
            engine_pos2 - forward * self.radius * 0.2 - right * self.radius * 0.1,
        ]
        pygame.draw.polygon(screen, engine_color, nozzle_points1)
        pygame.draw.polygon(screen, engine_color, nozzle_points2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def move(self, dt, direction):
        self.position += direction * PLAYER_SPEED * dt
    

    def update(self, dt, axis_x=0, axis_y=0):
        self.timer -= dt

        # Handle keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt, pygame.Vector2(0, -1).rotate(self.rotation))
        if keys[pygame.K_s]:
            self.move(dt, pygame.Vector2(0, 1).rotate(self.rotation))
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Handle controller input
        if abs(axis_x) > 0.1 or abs(axis_y) > 0.1:
            direction = pygame.Vector2(axis_x, axis_y).normalize()
            self.move(dt, direction)
            self.rotation = direction.angle_to(pygame.Vector2(0, -1))

        


    def shoot(self):
        if self.timer > 0:
            return 
        
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN  # Fixed: Changed 'shot' to 'self.timer'
        
       

    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    



    