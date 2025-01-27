import pygame, sys, time
from settings import *
from level import Level

# Settings (you can define these in a separate settings.py file or keep them here)
WIDTH, HEIGHT = 800, 600  # Screen dimensions
FPS = 60  # Frames per second

class Game:
    def __init__(self):
        # General setup
        pygame.init()  # Initialize Pygame
        self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up the display surface
        pygame.display.set_caption('Fractured Heart')  # Window title
        self.clock = pygame.time.Clock()  # Clock to control the frame rate

    def run(self):
        while True:
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Handle quit event
                    pygame.quit()
                    sys.exit()

            # Fill the screen with black
            self.display_surface.fill('black')

            # Update the display
            pygame.display.update()

            # Control the frame rate
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()  # Create a Game instance
    game.run()  # Run the game loop
