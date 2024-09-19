import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Draw a more detailed ship shape
        ship_color = (200, 200, 200)  # Light gray
        
        # Main body
        pygame.draw.polygon(screen, ship_color, [
            (self.position.x, self.position.y - self.radius),
            (self.position.x - self.radius, self.position.y + self.radius),
            (self.position.x + self.radius, self.position.y + self.radius)
        ])
        
        # Cockpit
        cockpit_radius = self.radius // 3
        pygame.draw.circle(screen, (100, 100, 100), 
                           (int(self.position.x), int(self.position.y)), cockpit_radius)
        
        # Engines
        engine_width = self.radius // 2
        engine_height = self.radius // 3
        pygame.draw.rect(screen, (150, 0, 0), 
                         (self.position.x - engine_width, 
                          self.position.y + self.radius - engine_height // 2,
                          engine_width // 2, engine_height))
        pygame.draw.rect(screen, (150, 0, 0), 
                         (self.position.x + engine_width // 2, 
                          self.position.y + self.radius - engine_height // 2,
                          engine_width // 2, engine_height))

    def update(self, dt):
        # sub-classes must override
        pass

    def is_collision(self, obj):
        distance = pygame.math.Vector2.distance_to(self.position, obj.position)
        if distance <= self.radius + obj.radius:
            return True
        return False