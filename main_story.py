import pygame, sys
from settings import *
from level_story import Level  # Import the story version of Level
from game_over import GameOverScreen

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Fractured-Heart Story Mode")
    icon = pygame.image.load("../assets/images/enemies/tree/idle/5.png")
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()

    # Initialize the story mode level
    level = Level()

    # Sound setup
    main_sound = pygame.mixer.Sound('../audio/main.ogg')
    main_sound.set_volume(0.5)
    main_sound.play(loops=-1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Allow toggling the upgrade menu (or pause menu) with U
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    level.toggle_menu()

        screen.fill(WATER_COLOR)
        level.run()
        pygame.display.update()
        clock.tick(FPS)

        # Game over handling
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
