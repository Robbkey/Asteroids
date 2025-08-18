# importing need variabel and classes
from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # creating the shap for the player
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def rotate(self, dt):
        # saving the rotation of the player
        self.rotation = self.rotation + PLAYER_TURN_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()

        # using a key to rotate counter clockwise
        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        # using d key to rotate clockwise
        if keys[pygame.K_d]:
            self.rotate(dt)

        # using w key to move forward
        if keys[pygame.K_w]:
            self.move(dt)

        # using s key to move backwards
        if keys[pygame.K_s]:
            self.move(-dt)



    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
            