import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT 
from logger import log_state
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0 

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        screen.fill("black")
        dt = clock.tick(60) / 1000.0
        
        
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()




if __name__ == "__main__":
    main()
