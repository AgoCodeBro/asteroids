from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        trajectories = [self.velocity.rotate(angle), self.velocity.rotate(-angle)]

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        for trajectory in trajectories:
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = trajectory * 1.2

