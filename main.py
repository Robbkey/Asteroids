import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # adding groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # filling groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )


    # i für unser while loop
    i = 0
    # initiate pygame
    pygame.init()

    asteroidfield = AsteroidField()
    # DEBUGGING
    #print(f"AsteroidField created, containers: {AsteroidField.containers}")
    #print(f"Asteroids group size: {len(asteroids)}")

    # initiating our player at a posion
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # saving a pygame clock objekt
    clock = pygame.time.Clock()
    # ouer delta time
    dt = 0
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    # setting the screen settings and saving them in screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    # infinit loop
    while i<1:

        # the block with for and if is so that the x to close a window works
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill the screen objekt we created black
        screen.fill((0, 0, 0))

        # update player position
        updatable.update(dt)

        for astr in asteroids:
            col = astr.collision(player)
            if col == True:
                raise SystemExit("Game over!")
        # DEBUGGING
        #print(f"Asteroids in group: {len(asteroids)}, Drawable objects: {len(drawable)}")

        # draw the player on the screen
        for obj in drawable:
            obj.draw(screen)

        # refresh the display
        pygame.display.flip()

        # frame limiter
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
