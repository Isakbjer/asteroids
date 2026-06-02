import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT 
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    
    while running:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        screen.fill("black")

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
