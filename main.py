import pygame, sys
from settings import *
from level import Level
from start_screen import StartScreen # Assuming you name this file menu.py
from game_over import GameOverScreen
import pygame, sys, threading
from settings import *  # Make sure your constants are available

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
    # Make sure to use .convert() or .convert_alpha() for optimization.
    assets['floor'] = pygame.image.load('../assets/images/map assets/game map.png').convert_alpha()
    # You can load other assets here. For example:
    assets['player'] = pygame.image.load('../assets/images/main character/player.png').convert_alpha()
    assets['foliage']=pygame.image.load('../assets/images/map assets/foliage.png')
    # Load enemy animations, particles, etc.
    # Simulate heavy loading with a delay (for testing only):
    # import time; time.sleep(2)
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

    show_transition_screen(screen)

    # Sound setup
    main_sound = pygame.mixer.Sound('../audio/main.ogg')
    main_sound.set_volume(0.5)
    main_sound.play(loops=-1)

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
