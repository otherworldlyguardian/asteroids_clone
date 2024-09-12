import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rotate_angle = random.uniform(20, 50)
        new_vel_one = self.velocity.rotate(rotate_angle)
        new_vel_two = self.velocity.rotate(-rotate_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        offsring_one = Asteroid(self.position.x, self.position.y, new_radius)
        offsring_two = Asteroid(self.position.x, self.position.y, new_radius)
        offsring_one.velocity = new_vel_one * 1.2
        offsring_two.velocity = new_vel_two