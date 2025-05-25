# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()

    game_clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_one = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running = True
    while running:
        ## Create window and let user close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        ## ---> Call player sprite here

        player_one.update(dt)
        player_one.draw(screen)
        pygame.display.flip()

        ## Adjust framerate
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()

