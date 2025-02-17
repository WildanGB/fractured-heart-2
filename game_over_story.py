import pygame
from settings_story import WIDTH, HEIGHT, UI_FONT  # Use proper constants from settings
from level_story import Level


class GameOverScreen:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        self.game_over_text_pos = -100
        self.button_width = 250
        self.button_height = 80
        self.button_spacing = 50
        # Define the buttons
        self.restart_button = pygame.Rect(
            (WIDTH // 2) - (self.button_width + self.button_spacing // 2),
            HEIGHT // 2 + 100,
            self.button_width,
            self.button_height
        )
        self.quit_button = pygame.Rect(
            (WIDTH // 2) + (self.button_spacing // 2),
            HEIGHT // 2 + 100,
            self.button_width,
            self.button_height
        )
        # Keyboard navigation
        self.selected_button = 0  # 0 for "Restart", 1 for "Quit"
        self.last_key_time = 0
        self.key_cooldown = 300  # milliseconds

    def display(self):
        # Draw the background using the level's current view
        self.level.visible_sprites.custom_draw(self.level.player)

        # Draw the "GAME OVER" text
        font = pygame.font.Font(UI_FONT, 100)
        game_over_text = font.render("GAME OVER", True, "red")
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, self.game_over_text_pos))
        self.screen.blit(game_over_text, text_rect)

        # Animate the game over text until it reaches the vertical center
        if self.game_over_text_pos < HEIGHT // 2:
            self.game_over_text_pos += 5
        else:

             # Render button text
            button_font = pygame.font.Font(UI_FONT, 40)  # Reduced font size
            restart_text = button_font.render("Restart", True, "black")
            quit_text = button_font.render("Quit", True, "black")

            # # Draw the buttons; highlight the selected button
            # restart_color = "white" if self.selected_button == 0 else "green"
            # quit_color = "white" if self.selected_button == 1 else "red"
            # pygame.draw.rect(self.screen, restart_color, self.restart_button)
            # pygame.draw.rect(self.screen, quit_color, self.quit_button)

            if self.selected_button == 0:
                pygame.draw.rect(self.screen, "white", self.restart_button)
                pygame.draw.rect(self.screen, "black", self.restart_button, 5)
                restart_text = button_font.render("Restart", True, "black")
            else:
                pygame.draw.rect(self.screen, "black", self.restart_button)
                restart_text = button_font.render("Restart", True, "white")


            if self.selected_button == 1: 
                pygame.draw.rect(self.screen, "white", self.quit_button)
                pygame.draw.rect(self.screen, "black", self.quit_button, 5)
                quit_text = button_font.render("Quit", True, "black")
            else: 
                pygame.draw.rect(self.screen, "black", self.quit_button)
                quit_text = button_font.render("Quit", True, "white")


            # Properly center text within buttons
            restart_rect = restart_text.get_rect(center=self.restart_button.center)
            quit_rect = quit_text.get_rect(center=self.quit_button.center)

            self.screen.blit(restart_text, restart_rect)
            self.screen.blit(quit_text, quit_rect)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            current_time = pygame.time.get_ticks()
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                if current_time - self.last_key_time > self.key_cooldown:
                    self.selected_button = 1 - self.selected_button
                    self.last_key_time = current_time
            elif event.key == pygame.K_RETURN:
                return "restart" if self.selected_button == 0 else "quit"
        return None
