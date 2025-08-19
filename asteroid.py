from circleshape import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.x = x
        #self.y = y
        self.pos = (x, y)
        #self.radius = radius



    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.pos, self.radius, 2)


    def update(self, dt):
        self.pos = self.pos + (self.velocity * dt)

