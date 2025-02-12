import pygame
from settings import *
from level import Level

class GameOverScreen:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        self.game_over_text_pos = -100
        self.button_spacing = 50
        self.restart_button = None
        self.quit_button = None
        self.create_buttons()

    def create_buttons(self):
        # Set up fonts using the declared UI_FONT from settings.py
        button_font = pygame.font.Font(UI_FONT, 50)
        restart_text = button_font.render("Restart", True, "black")
        quit_text = button_font.render("Quit", True, "black")

        # Calculate the width of the text to adjust button size
        restart_width = restart_text.get_width() + 20  # Adding padding
        quit_width = quit_text.get_width() + 20  # Adding padding

        # Set button dimensions
        button_height = 60

        # Create button rectangles
        self.restart_button = pygame.Rect(
            (WIDTH // 2) - (restart_width + self.button_spacing // 2),
            HEIGHT // 2 + 100,
            restart_width,
            button_height
        )
        self.quit_button = pygame.Rect(
            (WIDTH // 2) + (self.button_spacing // 2),
            HEIGHT // 2 + 100,
            quit_width,
            button_height
        )

        # Store text and their rectangles
        self.restart_text = restart_text
        self.quit_text = quit_text
        self.restart_rect = self.restart_text.get_rect(center=self.restart_button.center)
        self.quit_rect = self.quit_text.get_rect(center=self.quit_button.center)

    def display(self):
        self.level.visible_sprites.custom_draw(self.level.player)
        font = pygame.font.Font(UI_FONT, 100)
        game_over_text = font.render("GAME OVER", True, "red")
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, self.game_over_text_pos))
        self.screen.blit(game_over_text, text_rect)

        if self.game_over_text_pos < HEIGHT // 2:
            self.game_over_text_pos += 5
        else:
            pygame.draw.rect(self.screen, "green", self.restart_button)
            pygame.draw.rect(self.screen, "red", self.quit_button)
            self.screen.blit(self.restart_text, self.restart_rect)
            self.screen.blit(self.quit_text, self.quit_rect)

    def handle_input(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.restart_button.collidepoint(mouse_pos):
                return "restart"
            elif self.quit_button.collidepoint(mouse_pos):
                return "quit"
        return None
