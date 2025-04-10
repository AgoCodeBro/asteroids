import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import *
from shot import Shot

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    # Create Groups

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()




    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Assign groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

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

        # Draw screen 

        screen.fill("black")
        
        updatable.update(dt)
        
        for item in drawable:
            item.draw(screen)

        # Collision logic

        for item in asteroids:
            if item.collision_check(player):
                print("Game Over")
                return
            
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.kill()
                    shot.kill()


        pygame.display.flip()

        dt = clock.tick(60)/1000






if __name__ == "__main__":
    main()