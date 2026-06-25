import random
import pygame
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity *dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        tilt = random.uniform(20,50)
        first = self.velocity.rotate(tilt)
        second = self.velocity.rotate(-tilt)
        radius = self.radius - ASTEROID_MIN_RADIUS
        f = Asteroid(self.position.x, self.position.y, radius)
        s = Asteroid(self.position.x, self.position.y, radius)
        f.velocity = first* 1.2
        s.velocity = second * 1.2


