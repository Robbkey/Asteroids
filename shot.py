from circleshape import *
from constants import SHOT_RADIUS


class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)


    def draw(self, screen):
        # draws the shot
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        # updates position of the shot
        self.position += self.velocity * dt