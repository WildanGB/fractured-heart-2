import pygame, sys
from settings import *
from level import Level
from menu import MainMenuScreen  # Assuming you name this file menu.py

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Fractured-Heart")
    clock = pygame.time.Clock()

    # sound
    main_sound = pygame.mixer.Sound('../audio/main.ogg')
    main_sound.set_volume(0.5)
    main_sound.play(loops=-1)


    # Create and display the main menu
    menu = MainMenuScreen(screen)
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

        screen.fill(WATER_COLOR)
        level.run()
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
