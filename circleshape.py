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

    def collision(self, other):
        dist = pygame.math.Vector2.distance_to(self.position, other.position)
        # DEBUGGING
        #print(f"distanz between player and asteroid {dist}")
        #print(f"positon asteroid: {self.position}, position ship: {other.position}")
        #print(f"is {dist} smaller then {self.radius + other.radius}")
        if dist <= self.radius + other.radius:
            #DEBUGGING
            #print("HIT!!!!")
            return True
        else:
            #DEBUGGING
            #print ("not Hit")
            return False
