import pygame, sys
from settings import *
from start_screen import StartScreen  # Assuming you name this file menu.py
from game_over import GameOverScreen
import threading
from settings import *  # Make sure your constants are available

# Global dictionary for cached assets
assets = {}

screen = pygame.display.set_mode((WIDTH, HEIGHT))


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

    # Sound setup
    main_sound = pygame.mixer.Sound('../audio/main.ogg')
    main_sound.set_volume(0.5)
    main_sound.play(loops=-1)

    # Main menu setup
    menu = StartScreen(screen)
    in_menu = True
    game_mode = None  # Will be set to "story" or "endless"

    # Update start menu options to include story mode.
    # (Ensure that your StartScreen menu_items list in start_screen.py is updated accordingly.)
    # For example:
    # self.menu_items = [
    #     {"text": "Start Game in Story Mode", "action": "story"},
    #     {"text": "Start Game in Endless Mode", "action": "endless"},
    #     {"text": "How to Play", "action": "howto"},
    #     {"text": "Credits", "action": "credits"},
    #     {"text": "Quit", "action": "quit"}
    # ]

    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            result = menu.handle_input(event)
            if result in ("story", "endless"):
                game_mode = result
                in_menu = False
            elif result == "quit":
                pygame.quit()
                sys.exit()

        menu.display()
        pygame.display.flip()
        clock.tick(FPS)

    if game_mode:
        show_transition_screen(screen)

        # If story mode is selected, run main_story.py
        if game_mode == "story":
            import main_story
            main_story.main()  # Launch the story map without loading/start screens
            sys.exit()
        else:
            # Endless mode: load the regular game as before.
            from level import Level as LevelClassic
            level = LevelClassic()


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        level.toggle_menu()

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
                            if game_mode == "endless":
                                from level import Level as LevelClassic
                                level = LevelClassic()
                            else:
                                import main_story
                                level = main_story.Level()  # Assuming main_story.py defines Level as well
                            in_game_over = False
                        elif result == "quit":
                            pygame.quit()
                            sys.exit()
                    game_over.display()
                    pygame.display.flip()
                    clock.tick(FPS)

if __name__ == "__main__":
    main()
