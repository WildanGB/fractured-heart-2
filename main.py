import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Fractured Heart')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

    icon = pygame.image.load("../assets/images/enemies/tree/idle/5.png")
    pygame.display.set_icon(icon)

if __name__ == '__main__':
    game = Game()
    game.run()
