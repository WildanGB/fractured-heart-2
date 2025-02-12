import pygame, sys
from settings import *
from level import Level
from start_screen import StartScreen # Assuming you name this file menu.py
from game_over import GameOverScreen
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Fractured-Heart")
    clock = pygame.time.Clock()

    # Sound setup
    main_sound = pygame.mixer.Sound('../audio/main.ogg')
    main_sound.set_volume(0.5)
    main_sound.play(loops=-1)

    # Create and display the main menu
    menu = StartScreen(screen)
    in_menu = True
    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if menu.handle_input(event):
                in_menu = False

        menu.display()
        pygame.display.flip()
        clock.tick(FPS)

    # After exiting the menu, start the game
    level = Level()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    level.toggle_menu()

        screen.fill('black')
        level.run()
        pygame.display.update()
        clock.tick(FPS)


        # Check for game over condition (e.g., player health <= 0)
        if level.player.health <= 0:
            game_over = GameOverScreen(screen, level)
            in_game_over = True
            while in_game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    result = game_over.handle_input(event)
                    if result == "restart":
                        # Restart the game by reinitializing the level
                        level = Level()
                        in_game_over = False
                    elif result == "quit":
                        pygame.quit()
                        sys.exit()
                game_over.display()
                pygame.display.flip()
                clock.tick(FPS)

if __name__ == "__main__":
    main()
