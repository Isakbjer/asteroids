from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_KINDS
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> list["Asteroid"]:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_child_velocity = self.velocity.rotate(angle)
        second_child_velocity = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_child = Asteroid(self.position.x, self.position.y, new_radius)
        second_child = Asteroid(self.position.x, self.position.y, new_radius)

        first_child.velocity = first_child_velocity * 1.2 
        second_child.velocity = second_child_velocity * 1.2
