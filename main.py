import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()




    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    # Setup game clock

    clock = pygame.time.Clock()
    dt = 0


    # Game Loop

    while True:

        # Check for Quit

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        updatable.update(dt)
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000






if __name__ == "__main__":
    main()