import pygame
from constants import *
from player import Player

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    player = Player(x, y)


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
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000






if __name__ == "__main__":
    main()