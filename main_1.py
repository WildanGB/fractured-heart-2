import pygame, sys
from settings import *
from level import Level
from game_over import GameOverScreen
from main_menu import MainMenuScreen

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        # Game states
        self.state = "main_menu"  # Options: "main_menu", "gameplay", "game_over"

        # Initialize components
        self.level = Level()
        self.main_menu = MainMenuScreen(self.screen)
        self.game_over_screen = GameOverScreen(self.screen, self.level)

        # Sound
        self.main_sound = pygame.mixer.Sound('../audio/main.ogg')
        self.main_sound.set_volume(0.5)
        self.main_sound.play(loops=-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Handle input based on the current state
                if self.state == "main_menu":
                    if self.main_menu.handle_input(event):
                        self.state = "gameplay"

                elif self.state == "gameplay":
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                        self.level.toggle_menu()

                elif self.state == "game_over":
                    result = self.game_over_screen.handle_input(event)
                    if result == "restart":
                        self.level = Level()  # Restart level
                        self.state = "gameplay"
                    elif result == "quit":
                        pygame.quit()
                        sys.exit()

            # Render based on the current state
            self.screen.fill(WATER_COLOR)

            if self.state == "main_menu":
                self.main_menu.display()

            elif self.state == "gameplay":
                self.level.run()
                if self.level.player.health <= 0:  # Example condition for game over
                    self.state = "game_over"

            elif self.state == "game_over":
                self.game_over_screen.display()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()
