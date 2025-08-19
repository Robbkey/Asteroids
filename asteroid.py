import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.x = x
        #self.y = y
        #self.pos = (x, y)
        #self.radius = radius



    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        # destroying the asteroid
        self.kill()
        # looking if the asteroid is bigger then min
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # creating a random angle
            angle = random.uniform(20, 50)
            # setting two vectors
            vec1 = self.velocity.rotate(angle)
            vec2 = self.velocity.rotate(-angle)
            # setting the new radius for the new asteroids
            astr_rad = self.radius - ASTEROID_MIN_RADIUS
            #creating the two new asteroids and setting they're velocity
            asteroid1 = Asteroid(self.position.x, self.position.y, astr_rad)
            asteroid1.velocity = vec1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, astr_rad)
            asteroid2.velocity = vec2 * 1.2