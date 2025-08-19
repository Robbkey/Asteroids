the following code was made available by boot.dev, because it was not dircetly part of the learning goal:

main.py:
    if __name__ == "__main__":
        main()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return

constants.py:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    ASTEROID_MIN_RADIUS = 20
    ASTEROID_KINDS = 3
    ASTEROID_SPAWN_RATE = 0.8  # seconds
    ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

circleshape.py
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
            # sub-classes must override
            pass

        def update(self, dt):
            # sub-classes must override
            pass

player.py
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # ?
        if keys[pygame.K_d]:
            # ?

    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt

asteroidfield.py
    import pygame
    import random
    from asteroid import Asteroid
    from constants import *


    class AsteroidField(pygame.sprite.Sprite):
        edges = [
            [
                pygame.Vector2(1, 0),
                lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
            ],
            [
                pygame.Vector2(-1, 0),
                lambda y: pygame.Vector2(
                    SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
                ),
            ],
            [
                pygame.Vector2(0, 1),
                lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
            ],
            [
                pygame.Vector2(0, -1),
                lambda x: pygame.Vector2(
                    x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
                ),
            ],
        ]

        def __init__(self):
            pygame.sprite.Sprite.__init__(self, self.containers)
            self.spawn_timer = 0.0

        def spawn(self, radius, position, velocity):
            asteroid = Asteroid(position.x, position.y, radius)
            asteroid.velocity = velocity

        def update(self, dt):
            self.spawn_timer += dt
            if self.spawn_timer > ASTEROID_SPAWN_RATE:
                self.spawn_timer = 0

                # spawn a new asteroid at a random edge
                edge = random.choice(self.edges)
                speed = random.randint(40, 100)
                velocity = edge[0] * speed
                velocity = velocity.rotate(random.randint(-30, 30))
                position = edge[1](random.uniform(0, 1))
                kind = random.randint(1, ASTEROID_KINDS)
                self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
