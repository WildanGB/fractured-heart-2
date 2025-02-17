import pygame, sys
from settings import *
from start_screen import StartScreen  # Assuming you name this file menu.py
from game_over import GameOverScreen
import threading

# Global dictionary for cached assets
assets = {}

def show_loading_screen(screen, message="Loading..."):
    screen.fill((0, 0, 0))  # Black background
    font = pygame.font.Font(UI_FONT, 50)
    loading_text = font.render(message, True, TEXT_COLOR)
    text_rect = loading_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(loading_text, text_rect)
    pygame.display.flip()

def show_transition_screen(screen):
    transition_surface = pygame.Surface((WIDTH, HEIGHT))
    transition_surface.fill((0, 0, 0))
    font = pygame.font.Font(UI_FONT, 40)
    text = font.render("Entering the world...", True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    alpha = 0
    for _ in range(30):  # Smooth fade-in animation
        transition_surface.set_alpha(alpha)
        screen.fill((0, 0, 0))
        screen.blit(transition_surface, (0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()
        alpha += 8
        pygame.time.delay(30)

def load_assets():
    global assets
    # Example: load a floor image and store it in assets.
    assets['floor'] = pygame.image.load('../assets/images/map assets/game map.png').convert_alpha()
    assets['player'] = pygame.image.load('../assets/images/main character/player.png').convert_alpha()
    assets['foliage'] = pygame.image.load('../assets/images/map assets/foliage.png')
    print("Assets loaded.")

def load_assets_thread():
    load_assets()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Fractured-Heart")
    icon = pygame.image.load("../assets/images/enemies/tree/idle/5.png")
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()

    show_loading_screen(screen)

    # Main menu setup
    menu = StartScreen(screen)
    in_menu = True
    game_mode = None  # Will hold "start" or "endless"

    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle menu input
            result = menu.handle_input(event)
            if result in ("start", "endless"):
                game_mode = result
                in_menu = False
            elif result == "quit":
                pygame.quit()
                sys.exit()

        # Update menu display
        menu.display()
        pygame.display.flip()
        clock.tick(FPS)

    if game_mode:
        show_transition_screen(screen)

        # If Endless Mode is selected, adjust module path to load code from "code2"
        if game_mode == "endless":
            sys.path.insert(0, "code2")

        # Sound setup
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

        # Import Level from the appropriate directory (either original or endless mode)
        from level import Level
        level = Level()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        level.toggle_menu()

            # Game loop
            screen.fill(WATER_COLOR)
            level.run()
            pygame.display.update()
            clock.tick(FPS)

            # Game over check
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
                            show_transition_screen(screen)
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
